#!/usr/bin/env python3
"""
Product Manager OS — Artifact Conformance Check

`score_skill.py` grades the *instruction*. This grades the *result*.

A skill can score 100 and still produce a thin artifact. This reads the skill's
declared `## Output template`, extracts the structure it promises, and checks a
real produced artifact against it — so "the output format is right" is a number
you can see instead of a claim you make.

Usage:
  python3 tests/check_artifact.py --skill write-spec workspace/projects/csv-export/spec.md
  python3 tests/check_artifact.py --skill metrics-review --stdin < artifact.md
  python3 tests/check_artifact.py --skill write-spec --template-only   # show what's required
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from score_skill import (split_frontmatter, section, find_skills_dir,  # noqa: E402
                         require_skills_dir)

# Placeholders that mean "the model fills this in" — never required literally.
PLACEHOLDER = re.compile(r"[<\[][^>\]]{0,60}[>\]]")


def required_elements(skill):
    """Pull the promised structure out of a skill's Output template section."""
    path = os.path.join(require_skills_dir(ROOT), skill, "SKILL.md")
    if not os.path.isfile(path):
        sys.exit(f"no such skill: {skill}")
    fm, body = split_frontmatter(open(path, encoding="utf-8").read())
    tpl = section(body, r"Output template")
    if not tpl:
        sys.exit(f"{skill} declares no Output template — nothing to check against")

    # Strip fence markers but keep their contents; the template is often fenced.
    tpl = re.sub(r"^```.*$", "", tpl, flags=re.M)

    headings, labels = [], []
    for line in tpl.split("\n"):
        h = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
        if h:
            t = PLACEHOLDER.sub("", h.group(2)).strip(" -–—:")
            if len(t) >= 3:
                headings.append(t)
            continue
        # ALL-CAPS lines act as section labels in our plain-text templates
        # ("POSITIONING STATEMENT", "KEY RESULTS (outcomes …):"). Strip the
        # placeholders first, then look for a caps label with an optional
        # parenthetical aside and an optional trailing colon.
        bare = PLACEHOLDER.sub("", line).rstrip()
        caps = re.match(
            r"^\s*([A-Z]{3}[A-Z0-9 &/'’,.\-]{0,50}?)(?:\s*\([^)]*\))?\s*:?\s*$",
            bare)
        if caps:
            t = caps.group(1).strip(" -–—:")
            # a divider row is not a heading
            if len(t) >= 4 and not set(t) <= set("- =_|"):
                headings.append(t)
                continue

        # "**Label:**" rows are the other way our templates express required fields
        for lm in re.finditer(r"\*\*([^*]{3,48}?):?\*\*\s*:?", line):
            t = PLACEHOLDER.sub("", lm.group(1)).strip(" -–—:")
            if len(t) >= 3:
                labels.append(t)

    # de-dupe, keep order
    seen, out_h, out_l = set(), [], []
    for t in headings:
        k = t.lower()
        if k not in seen:
            seen.add(k); out_h.append(t)
    for t in labels:
        k = t.lower()
        if k not in seen:
            seen.add(k); out_l.append(t)
    return fm, out_h, out_l


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def present(needle, haystack_norm):
    n = norm(needle)
    if not n:
        return True
    if n in haystack_norm:
        return True
    # tolerate reordering/synonym drift: all significant words present
    words = [w for w in n.split() if len(w) > 3]
    return bool(words) and all(w in haystack_norm for w in words)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", nargs="?")
    ap.add_argument("--skill", required=True)
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--template-only", action="store_true")
    ap.add_argument("--min", type=float, default=70.0,
                    help="minimum conformance %% to pass (default 70)")
    a = ap.parse_args()

    fm, headings, labels = required_elements(a.skill)

    if a.template_only:
        print(f"\n{a.skill} promises this shape "
              f"(tier {fm.get('tier')} → {fm.get('outputs')}):\n")
        for h in headings:
            print(f"  ##  {h}")
        for l in labels:
            print(f"  **  {l}")
        print()
        return

    text = sys.stdin.read() if a.stdin else open(a.artifact, encoding="utf-8").read()
    hay = norm(text)

    checks = [("heading", h) for h in headings] + [("field", l) for l in labels]
    if not checks:
        sys.exit(f"{a.skill}: output template has no checkable structure")

    hits = [(k, t, present(t, hay)) for k, t in checks]
    got = sum(1 for _, _, ok in hits if ok)
    pct = round(100.0 * got / len(hits), 1)

    src = "<stdin>" if a.stdin else a.artifact
    print(f"\n{a.skill} → {src}")
    print(f"conformance: {pct}%  ({got}/{len(hits)} required elements)\n")
    for k, t, ok in hits:
        print(f"  {'✅' if ok else '❌'} {k:<8} {t}")

    # words-per-required-element: catches the artifact that has every heading and
    # nothing underneath them.
    words = len(text.split())
    density = round(words / max(len(hits), 1), 1)
    print(f"\n  {words} words · {density} words per required element", end="")
    thin = density < 25
    print("  ⚠️  thin — headings present but little substance" if thin else "")

    if not a.stdin and fm.get("outputs"):
        want_root = fm["outputs"].split("/")[0]
        got_path = os.path.normpath(a.artifact).replace("\\", "/")
        routed = f"/{want_root}/" in f"/{got_path}" or got_path.startswith(want_root + "/")
        print(f"  {'✅' if routed else '⚠️ '} routing: expected under '{want_root}/'")

    print()
    if pct < a.min or thin:
        sys.exit(1)


if __name__ == "__main__":
    main()
