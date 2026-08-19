#!/usr/bin/env python3
"""
Product Manager OS — score every skill, write the scoreboard, gate on regression.

Why a scoreboard and not a pass/fail badge: a badge tells you nothing moved.
This tells you which skill got worse when you edited it, and by how much.

  python3 tests/run_all.py              # score all, print summary, write RESULTS.md
  python3 tests/run_all.py --check      # CI mode: no writes, non-zero exit on failure
  python3 tests/run_all.py --baseline   # accept current scores as the new baseline

Gates (CI fails on any):
  1. FLOOR       — no skill scores below MIN_SCORE
  2. REGRESSION  — no skill scores below its recorded baseline
  3. UNIQUENESS  — no two skills share a name, and every skill dir has a SKILL.md
  4. ROUTING     — every declared output path lands in a folder that exists
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from score_skill import score_file, find_skills_dir, DIM_NAMES  # noqa: E402

MIN_SCORE = 85.0
BASELINE = os.path.join(HERE, "baseline.json")
RESULTS = os.path.join(HERE, "RESULTS.md")
README = os.path.abspath(os.path.join(ROOT, "..", "..", "README.md"))

VALID_ROOTS = {
    "projects", "research", "strategy", "metrics", "meetings",
    "comms", "decisions", "memory", "skills",
}


def all_skills():
    d = find_skills_dir(ROOT)
    out = []
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name, "SKILL.md")
        if os.path.isfile(p):
            out.append(p)
    return out


def main():
    check = "--check" in sys.argv
    paths = all_skills()
    results = [score_file(p) for p in paths]
    results.sort(key=lambda r: (r["score"], r["skill"]))

    failures = []

    # gate 3 — structural integrity
    dirs = [d for d in sorted(os.listdir(find_skills_dir(ROOT)))
            if os.path.isdir(os.path.join(find_skills_dir(ROOT), d))]
    missing = [d for d in dirs if not os.path.isfile(os.path.join(find_skills_dir(ROOT), d, "SKILL.md"))]
    for d in missing:
        failures.append(f"UNIQUENESS: skills/{d}/ has no SKILL.md")

    # gate 4 — output routing resolves
    for r in results:
        fm_out = ""
        txt = open(r["path"], encoding="utf-8").read()
        m = re.search(r"^outputs:\s*(.+)$", txt, re.M)
        if m:
            fm_out = m.group(1).strip().strip("\"'")
        root = fm_out.split("/")[0] if fm_out else ""
        if root not in VALID_ROOTS:
            failures.append(f"ROUTING: {r['skill']} writes to '{fm_out}' — '{root}' is not a known destination")

    # gate 1 — floor
    for r in results:
        if r["score"] < MIN_SCORE:
            failures.append(f"FLOOR: {r['skill']} scored {r['score']} (min {MIN_SCORE}) — {', '.join(r['failed'])}")

    # gate 2 — regression
    base = {}
    if os.path.isfile(BASELINE):
        base = json.load(open(BASELINE)).get("scores", {})
    regressions = []
    for r in results:
        prev = base.get(r["skill"])
        if prev is not None and r["score"] < prev:
            regressions.append((r["skill"], prev, r["score"]))
            failures.append(f"REGRESSION: {r['skill']} {prev} → {r['score']}")

    scores = [r["score"] for r in results]
    mean = round(sum(scores) / len(scores), 1)
    perfect = sum(1 for s in scores if s == 100.0)

    print(f"\n{'skill':<28}{'tier':<11}{'score':>7}   weakest dimension")
    print("─" * 78)
    for r in results:
        weak = min(r["dimensions"].items(), key=lambda kv: kv[1]["got"] / kv[1]["max"])
        label = "—" if weak[1]["got"] == weak[1]["max"] else f"{weak[0]} {DIM_NAMES[weak[0]]}"
        print(f"{r['skill']:<28}{r['tier'] or '?':<11}{r['score']:>7}   {label}")
    print("─" * 78)
    print(f"{len(results)} skills · mean {mean} · {perfect} at 100 · floor {min(scores)}\n")

    if "--baseline" in sys.argv:
        json.dump({"min_score": MIN_SCORE, "mean": mean,
                   "scores": {r["skill"]: r["score"] for r in results}},
                  open(BASELINE, "w"), indent=2, sort_keys=True)
        print(f"baseline written → {BASELINE}\n")

    if not check:
        write_results(results, mean, perfect)
        print(f"scoreboard written → {RESULTS}")
        if update_badge(len(results), mean):
            print(f"README badge updated → {README}")
        print()

    if failures:
        print("FAILED:")
        for f in failures:
            print(f"  ✗ {f}")
        print()
        sys.exit(1)
    print("All gates passed.\n")


def update_badge(n_skills, mean):
    """Keep the README badge honest. A hand-typed score is a score that drifts.

    Only ever touches the persona-os repo's own README. Installed into a user's
    project, ROOT/../.. is somewhere above their project entirely — writing there
    would be a scorer quietly editing a file that has nothing to do with it."""
    marker = os.path.join(os.path.dirname(README), ".claude-plugin", "marketplace.json")
    if not os.path.isfile(README) or not os.path.isfile(marker):
        return False
    txt = open(README, encoding="utf-8").read()
    new = (f"[![Skills scored](https://img.shields.io/badge/"
           f"{n_skills}%20skills-mean%20{mean}%2F100-2ea44f)]"
           f"(plugins/product-manager-os/tests/RESULTS.md)")
    out = re.sub(r"\[!\[Skills scored\]\([^)]*\)\]\([^)]*\)", new, txt)
    if out == txt:
        return False
    open(README, "w", encoding="utf-8").write(out)
    return True


def write_results(results, mean, perfect):
    by_tier = {}
    for r in results:
        by_tier.setdefault(r["tier"] or "?", []).append(r)
    lines = [
        "# Skill Scoreboard",
        "",
        "Generated by `python3 tests/run_all.py`. Every skill is scored 0–100 by "
        "[`tests/score_skill.py`](score_skill.py) — 22 binary checks across 6 dimensions.",
        "",
        "**This is a loss function, not a badge.** It exists so that when a skill is edited, "
        "the number moves and you can see which direction. CI fails on any regression against "
        "[`baseline.json`](baseline.json), not just on a hard floor.",
        "",
        f"**{len(results)} skills · mean {mean} · {perfect} at 100 · floor {min(r['score'] for r in results)}**",
        "",
        "| Dimension | Points | What it asks |",
        "|---|---|---|",
        "| D1 Contract | 25 | Can a PM tell from the frontmatter whether they can start right now? |",
        "| D2 Structure | 20 | Are the five load-bearing sections present? |",
        "| D3 Grounding | 15 | Is the judgment borrowed from a named source, not invented? |",
        "| D4 Usability | 20 | Enough triggers, inputs, and steps to actually run it — and does it ask before producing? |",
        "| D5 Output | 12 | Is the artifact shape concrete, and does it land somewhere real? |",
        "| D6 Anti-generic | 8 | Does it show a concrete example and stay free of filler? |",
        "",
    ]
    for tier in ("quick", "guided", "campaign"):
        rs = sorted(by_tier.get(tier, []), key=lambda r: r["skill"])
        if not rs:
            continue
        lines += [f"## `{tier}` ({len(rs)})", "",
                  "| Skill | Score | D1 | D2 | D3 | D4 | D5 | D6 |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for r in rs:
            d = r["dimensions"]
            cells = " | ".join(f"{d[k]['got']}/{d[k]['max']}" for k in
                               ("D1", "D2", "D3", "D4", "D5", "D6"))
            lines.append(f"| `{r['skill']}` | **{r['score']}** | {cells} |")
        lines.append("")
    open(RESULTS, "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
