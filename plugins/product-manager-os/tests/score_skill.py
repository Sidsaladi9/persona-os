#!/usr/bin/env python3
"""
Product Manager OS — Skill Scorer (immutable loss function)

Scores one SKILL.md from 0-100 across 6 dimensions. Every check is binary, so a
score is a count of things that are true, not an opinion.

This is deliberately NOT a pass/fail lint. A lint tells you a file is well-formed.
A score tells you whether the skill will actually produce a good artifact for a
real PM, and lets you watch that number move when you edit it.

Usage:
  python3 tests/score_skill.py skills/write-spec/SKILL.md
  python3 tests/score_skill.py skills/write-spec/SKILL.md --json
"""
import json
import glob
import os
import re
import sys

TIERS = {"quick", "guided", "campaign"}


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _has_skills(p):
    try:
        return os.path.isdir(p) and any(
            os.path.isfile(os.path.join(p, d, "SKILL.md")) for d in os.listdir(p))
    except OSError:
        return False


def find_skills_dir(root):
    """Where the skills live, which depends on how the OS was installed.

    The repo and most bundles use <root>/skills. Claude Code's own installer
    puts them in .claude/skills and Cursor in .cursor/rules — so a hard-coded
    'skills' path silently finds nothing in the two commonest file installs.

    And on a `/plugin install` the skills are not in the project AT ALL: they
    live in the plugin cache, and the project only ever gets memory/, workspace/
    and this tests/ folder. Every tool here used to die on an unhandled
    FileNotFoundError there — including relevance_report.py, which /tune-up runs,
    and score_skill.py, which skill-creator tells the user to run. CLAUDE.md
    promises both. CI never saw it because its smoke test installs with
    install.sh, which does copy the skills into the project.
    """
    for cand in ("skills", ".claude/skills", ".cursor/rules"):
        p = os.path.join(root, cand)
        if _has_skills(p):
            return p

    # Installed as a plugin: ask the host where the plugin lives.
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root and _has_skills(os.path.join(plugin_root, "skills")):
        return os.path.join(plugin_root, "skills")

    # Last resort: the plugin cache, newest version first. Running a tool from a
    # plain shell means CLAUDE_PLUGIN_ROOT is unset, which is the normal case for
    # someone following an instruction the OS printed.
    cache = os.path.expanduser("~/.claude/plugins/cache")
    if os.path.isdir(cache):
        cands = glob.glob(os.path.join(cache, "*", "product-manager-os", "*", "skills"))
        cands += glob.glob(os.path.join(cache, "*", "*", "*", "skills"))
        for c in sorted(set(cands), reverse=True):
            if _has_skills(c):
                return c

    return os.path.join(root, "skills")


def require_skills_dir(root):
    """find_skills_dir, but with a human answer instead of a traceback."""
    d = find_skills_dir(root)
    if _has_skills(d):
        return d
    sys.stderr.write(
        "Could not find the skills.\n\n"
        "Looked in ./skills, ./.claude/skills, ./.cursor/rules, "
        "$CLAUDE_PLUGIN_ROOT/skills, and ~/.claude/plugins/cache.\n\n"
        "If you installed Product Manager OS as a plugin, the skills live in the\n"
        "plugin cache rather than in this project — that is normal. Run this from\n"
        "the plugin directory, or set CLAUDE_PLUGIN_ROOT to it:\n\n"
        "  CLAUDE_PLUGIN_ROOT=~/.claude/plugins/cache/persona-os/product-manager-os/<version> \\\n"
        "    python3 tests/" + os.path.basename(sys.argv[0]) + "\n\n"
        "Tools that only read workspace/ (relevance_report.py) work either way.\n")
    sys.exit(2)

WORKSPACE_ROOTS = {
    "projects", "research", "strategy", "metrics",
    "meetings", "comms", "decisions",
}
# outputs may also target these non-workspace destinations
OTHER_ROOTS = {"memory", "skills"}

# Words that signal filler rather than instruction. A skill that reaches for these
# is describing itself instead of telling the model what to do.
BANNED = [
    r"\butilize\b",
    r"\bsynerg",
    r"\bparadigm shift\b",
    r"\bin today's fast[- ]paced\b",
    r"\bbest[- ]in[- ]class\b",
    r"\bworld[- ]class\b",
    r"\bseamlessly\b",
    r"\bunlock the power\b",
]


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            v = km.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[km.group(1)] = v
    return fm, m.group(2)


# The canonical top-level sections. A section ends at the next one of THESE,
# not at the next "##" — because an Output template legitimately contains its own
# "##" headings as part of the template it is showing.
SECTION_NAMES = (
    r"When to use", r"Before you start", r"Process", r"Output template",
    r"Avoid", r"Tips", r"Quality bar", r"Assumptions", r"TL;DR",
    r"Success metrics", r"Worked example", r"What good looks like",
)
_STOP = re.compile(r"^##\s+(?:" + "|".join(SECTION_NAMES) + r")", re.M | re.I)


def _top_level_headings(text):
    """Yield (line_index, char_offset, heading_text) for ## headings that are NOT
    inside a fenced code block. Output templates are fenced and contain their own
    ## headings — those are template content, not section boundaries."""
    offset, in_fence = 0, False
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        elif not in_fence:
            m = re.match(r"^##\s+(.+?)\s*$", line)
            if m:
                yield offset, m.group(1)
        offset += len(line) + 1


def section(body, heading_re):
    """Return the text of the first section whose ## heading matches."""
    heads = list(_top_level_headings(body))
    start = None
    for i, (off, title) in enumerate(heads):
        if re.match(heading_re, title, re.I):
            start = i
            break
    if start is None:
        return None
    begin = heads[start][0]
    begin += body[begin:].find("\n") + 1  # skip the heading line itself
    for off, title in heads[start + 1:]:
        if re.match(r"(?:" + "|".join(SECTION_NAMES) + r")", title, re.I):
            return body[begin:off]
    return body[begin:]


def bullets(txt):
    return re.findall(r"^\s*[-*]\s+\S", txt or "", re.M)


def build_checks(fm, body, slug):
    """Each check: (dimension, name, points, bool)."""
    c = []

    wtu = section(body, r"When to use")
    bys = section(body, r"Before you start")
    proc = section(body, r"Process")
    out = section(body, r"Output template")
    avoid = section(body, r"Avoid")

    # ── D1 CONTRACT (25) — can a PM tell if they can start right now? ──
    c.append(("D1", "name_present_and_matches_dir", 3,
              fm.get("name", "") == slug))
    c.append(("D1", "description_substantial", 3,
              len(fm.get("description", "")) >= 120))
    c.append(("D1", "description_has_triggers", 3,
              bool(re.search(r"use when|\"", fm.get("description", ""), re.I))))
    c.append(("D1", "tier_valid", 4, fm.get("tier") in TIERS))
    c.append(("D1", "time_present", 4, len(fm.get("time", "")) >= 3))
    c.append(("D1", "inputs_specific", 4, len(fm.get("inputs", "")) >= 15))
    c.append(("D1", "outputs_is_path", 4,
              bool(re.match(r"^[a-z][\w./<>-]*\.\w+$|^[a-z][\w./<>-]*/$",
                            fm.get("outputs", "")))))

    # ── D2 STRUCTURE (20) — the five sections every skill owes the reader ──
    for nm, sec in (("when_to_use", wtu), ("before_you_start", bys),
                    ("process", proc), ("output_template", out),
                    ("avoid_anti_patterns", avoid)):
        c.append(("D2", f"has_{nm}", 4, sec is not None))

    # ── D3 GROUNDING (15) — is the judgment borrowed from somewhere real? ──
    g = re.search(r"\*\*Grounded in:\*\*\s*(.+)", body)
    c.append(("D3", "has_grounded_in", 7, g is not None))
    gtxt = g.group(1) if g else ""
    # a real source names a work (*italics*) or a person (Two Capitalised Words)
    c.append(("D3", "grounding_names_a_source", 8,
              bool(re.search(r"\*[^*]{4,}\*", gtxt))
              or bool(re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", gtxt))))

    # ── D4 USABILITY (20) — enough scaffolding to actually run it ──
    c.append(("D4", "when_to_use_has_3_triggers", 5, len(bullets(wtu)) >= 3))
    c.append(("D4", "before_you_start_has_3_inputs", 5, len(bullets(bys)) >= 3))
    c.append(("D4", "process_has_numbered_steps", 5,
              len(re.findall(r"^\s*(?:\d+\.|###\s*\d+)", proc or "", re.M)) >= 3))
    # guided/campaign skills must ask before producing; quick skills are exempt
    tier = fm.get("tier")
    asks = bool(re.search(r"clarifying question|ask 2|ask 3|ask the user|"
                          r"ASK \d|assumptions block|state.{0,20}assumption",
                          body, re.I))
    c.append(("D4", "asks_before_producing", 5, asks if tier in ("guided", "campaign") else True))

    # ── D5 OUTPUT (12) — is the artifact shape concrete and does it land? ──
    c.append(("D5", "output_template_is_concrete", 6,
              bool(out) and len([l for l in out.split("\n") if l.strip()]) >= 5))
    root = (fm.get("outputs", "").split("/") or [""])[0]
    c.append(("D5", "output_path_resolves", 6, root in WORKSPACE_ROOTS | OTHER_ROOTS))

    # ── D6 ANTI-GENERIC (8) — does it show, not just tell? ──
    c.append(("D6", "has_concrete_example", 4,
              bool(re.search(r"\be\.g\.|for example|worked example|\|.*\|", body, re.I))))
    c.append(("D6", "no_filler_language", 4,
              not any(re.search(p, body, re.I) for p in BANNED)))

    return c


DIM_NAMES = {
    "D1": "Contract", "D2": "Structure", "D3": "Grounding",
    "D4": "Usability", "D5": "Output", "D6": "Anti-generic",
}


def score_file(path):
    slug = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(text)
    checks = build_checks(fm, body, slug)

    total = sum(p for _, _, p, ok in checks if ok)
    possible = sum(p for _, _, p, _ in checks)
    dims = {}
    for d, _, p, ok in checks:
        got, cap = dims.get(d, (0, 0))
        dims[d] = (got + (p if ok else 0), cap + p)

    return {
        "skill": slug,
        "path": path,
        "tier": fm.get("tier"),
        "score": round(100.0 * total / possible, 1),
        "dimensions": {d: {"got": g, "max": m} for d, (g, m) in sorted(dims.items())},
        "failed": [n for _, n, _, ok in checks if not ok],
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    target = args[0]
    # Accept a bare skill name as well as a path. On a plugin install the skills
    # are not under the project at all, so "skills/<name>/SKILL.md" — what
    # skill-creator prints — resolves to nothing and the open() below used to
    # raise FileNotFoundError at the user.
    if not os.path.isfile(target):
        name = target
        for suffix in ("/SKILL.md",):
            if name.endswith(suffix):
                name = name[: -len(suffix)]
        name = os.path.basename(name.rstrip("/"))
        cand = os.path.join(find_skills_dir(ROOT), name, "SKILL.md")
        if os.path.isfile(cand):
            target = cand
        else:
            sys.stderr.write(
                f"No skill at '{args[0]}', and no skill named '{name}' in "
                f"{find_skills_dir(ROOT)}.\n"
                "Pass a path to a SKILL.md, or a skill name.\n")
            sys.exit(2)
    res = score_file(target)
    if "--json" in sys.argv:
        print(json.dumps(res, indent=2))
        return
    print(f"\n{res['skill']}  [{res['tier']}]  →  {res['score']}/100\n")
    for d, v in res["dimensions"].items():
        mark = "✅" if v["got"] == v["max"] else "⚠️ "
        print(f"  {mark} {d} {DIM_NAMES[d]:<14} {v['got']:>3}/{v['max']}")
    if res["failed"]:
        print("\n  failed checks:")
        for f in res["failed"]:
            print(f"    ❌ {f}")
    print()


if __name__ == "__main__":
    main()
