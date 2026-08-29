#!/usr/bin/env python3
"""
Relevance report — which artifacts died, and which skills keep producing them.

The activity log tells you a skill *ran*. It cannot tell you the output was worth
producing. This checks the other half: after an artifact was written, did anyone
ever come back to it?

A skill whose artifacts are never revisited is either producing the wrong thing or
producing it at the wrong moment. That's the most useful signal in the OS and the
one nothing else measures — the analogue of tracking what you generated versus what
you actually published.

  python3 tests/relevance_report.py
  python3 tests/relevance_report.py --days 90
  python3 tests/relevance_report.py --json

Signals used (both observable locally, no telemetry):
  referenced — another artifact, a decision, or the activity log mentions the file
  revisited  — the file was modified meaningfully after the session that created it

An artifact is DEAD if neither is true and it's older than the grace window.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_skill import find_skills_dir, require_skills_dir  # noqa: E402
WS = os.path.join(ROOT, "workspace")
MEM = os.path.join(ROOT, "memory")

GRACE_DAYS = 7          # too new to judge
SKIP = {"README.md", "INDEX.md", "TEMPLATE.md"}


def skill_outputs():
    """Map an output-path pattern to the skill that declares it.

    This is the only tool /tune-up runs by itself, and its real job — finding
    artifacts nobody came back to — reads workspace/, not skills/. On a plugin
    install the skills are in the plugin cache and may not be reachable at all.
    Losing the skill attribution is a smaller loss than losing the whole report,
    so this degrades instead of exiting.
    """
    out = {}
    sdir = find_skills_dir(ROOT)
    if not os.path.isdir(sdir):
        return out
    for name in sorted(os.listdir(sdir)):
        f = os.path.join(sdir, name, "SKILL.md")
        if not os.path.isfile(f):
            continue
        m = re.search(r"^outputs:\s*(.+)$", open(f, encoding="utf-8").read(), re.M)
        if m:
            out[name] = m.group(1).strip().strip("\"'")
    return out


def match_skill(rel, mapping):
    """Best-effort: which skill's declared output path does this file look like?"""
    best, best_len = None, -1
    for skill, pat in mapping.items():
        # turn projects/<project>/spec.md into ^projects/[^/]+/spec\.md$
        # note: re.escape does NOT escape < or >, so match them raw
        rx = "^" + re.sub(r"<[^>]*>", "[^/]+", re.escape(pat)) + "$"
        if re.match(rx, rel):
            # prefer the most specific match (most literal, non-placeholder chars)
            lit = len(re.sub(r"<[^>]*>", "", pat))
            if lit > best_len:
                best, best_len = skill, lit
    return best


def collect_corpus():
    """Everything that could reference an artifact: other artifacts + the logs."""
    texts = []
    for base in (WS, MEM):
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for fn in filenames:
                if not fn.endswith((".md", ".sql", ".html")):
                    continue
                p = os.path.join(dirpath, fn)
                try:
                    texts.append((os.path.relpath(p, ROOT),
                                  open(p, encoding="utf-8", errors="ignore").read()))
                except OSError:
                    pass
    return texts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=180)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isdir(WS):
        print("no workspace/ — nothing to report")
        return

    mapping = skill_outputs()
    corpus = collect_corpus()
    now = datetime.now()
    cutoff = now - timedelta(days=a.days)
    grace = now - timedelta(days=GRACE_DAYS)

    rows = []
    for dirpath, dirnames, filenames in os.walk(WS):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.startswith(".") or fn in SKIP:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, WS).replace(os.sep, "/")
            st = os.stat(full)
            created = datetime.fromtimestamp(getattr(st, "st_birthtime", st.st_ctime))
            modified = datetime.fromtimestamp(st.st_mtime)
            if created < cutoff:
                continue

            base = os.path.basename(rel)
            referenced = any(
                (rel in text or base in text)
                for src, text in corpus
                if os.path.relpath(full, ROOT) != src
            )
            revisited = (modified - created).total_seconds() > 3600
            too_new = created > grace
            dead = not referenced and not revisited and not too_new

            rows.append({
                "artifact": rel,
                "skill": match_skill(rel, mapping) or "—",
                "age_days": (now - created).days,
                "referenced": referenced,
                "revisited": revisited,
                "status": "too new" if too_new else ("dead" if dead else "live"),
            })

    if a.json:
        print(json.dumps(rows, indent=2))
        return

    if not rows:
        print("\nNo artifacts in workspace/ yet.")
        print("This report becomes useful after a few weeks of real work — it's how the")
        print("OS finds out which of its outputs you never look at again.\n")
        return

    dead = [r for r in rows if r["status"] == "dead"]
    live = [r for r in rows if r["status"] == "live"]
    new = [r for r in rows if r["status"] == "too new"]

    print(f"\n{'artifact':<46}{'skill':<22}{'age':>5}  ref  rev  status")
    print("─" * 92)
    for r in sorted(rows, key=lambda r: (r["status"] != "dead", r["artifact"])):
        print(f"{r['artifact'][:44]:<46}{r['skill'][:20]:<22}{r['age_days']:>4}d"
              f"{'   ✓' if r['referenced'] else '   ·'}"
              f"{'    ✓' if r['revisited'] else '    ·'}"
              f"  {r['status']}")
    print("─" * 92)
    print(f"{len(rows)} artifacts · {len(live)} live · {len(dead)} dead · {len(new)} too new to judge\n")

    # the part that actually feeds the tune-up
    by_skill = {}
    for r in rows:
        if r["status"] == "too new" or r["skill"] == "—":
            continue
        d, t = by_skill.get(r["skill"], (0, 0))
        by_skill[r["skill"]] = (d + (1 if r["status"] == "dead" else 0), t + 1)

    flagged = [(s, d, t) for s, (d, t) in by_skill.items() if t >= 3 and d / t >= 0.67]
    if flagged:
        print("Skills whose output goes dead (≥3 artifacts, ≥2/3 never revisited):")
        for s, d, t in sorted(flagged, key=lambda x: -x[1] / x[2]):
            print(f"  ⚠️  {s:<24} {d}/{t} dead")
        print("\n  These are producing something you don't come back to. Either the artifact")
        print("  is wrong, or it's being produced at the wrong moment. Worth a tune-up.\n")
    elif by_skill:
        print("No skill is systematically producing dead artifacts.\n")

    never = sorted(set(mapping) - {r["skill"] for r in rows})
    if never and len(rows) >= 10:
        print(f"Never used ({len(never)}): {', '.join(never[:14])}"
              f"{' …' if len(never) > 14 else ''}")
        print("  Not a problem on its own — most PMs use a subset. Worth a look if one of")
        print("  these covers work you've been doing by hand.\n")


if __name__ == "__main__":
    main()
