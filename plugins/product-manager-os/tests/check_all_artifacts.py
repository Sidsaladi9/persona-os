#!/usr/bin/env python3
"""
Product Manager OS — run artifact conformance across every worked example.

Each skill ships a real produced artifact in `examples/cadence/<skill>.md`.
This checks every one of them against its own skill's declared Output template.

That closes the loop the other PM skill packs leave open: they verify the
*instruction* exists; this verifies the instruction actually yields the artifact
it promised. If someone edits a skill's output template and forgets the example,
this fails — which is exactly when it should.

  python3 tests/check_all_artifacts.py
  python3 tests/check_all_artifacts.py --check   # CI mode, non-zero exit on failure
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAMPLES = os.path.join(ROOT, "examples", "cadence")
MIN_CONFORMANCE = 70.0
MIN_DENSITY = 25.0

# Skills whose artifact is deliberately not a markdown document in examples/cadence.
# Each needs a reason — an exemption without one is just a skipped test.
EXEMPT = {
    "visualize":     "produces a self-contained HTML file, not a markdown artifact",
    "skill-creator": "produces a SKILL.md; covered by tests/run_all.py instead",
}


def main():
    skills = sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                    if os.path.isfile(os.path.join(ROOT, "skills", d, "SKILL.md")))
    rows, failures, skipped = [], [], []

    for skill in skills:
        if skill in EXEMPT:
            continue
        ex = os.path.join(EXAMPLES, f"{skill}.md")
        if not os.path.isfile(ex):
            skipped.append(skill)
            continue
        r = subprocess.run(
            [sys.executable, os.path.join(HERE, "check_artifact.py"),
             "--skill", skill, ex],
            capture_output=True, text=True)
        out = r.stdout
        pc = re.search(r"conformance:\s*([\d.]+)%\s*\((\d+)/(\d+)", out)
        dn = re.search(r"([\d.]+) words per required element", out)
        wd = re.search(r"\n\s*(\d+) words", out)
        if not pc:
            failures.append(f"{skill}: checker produced no result — {r.stderr.strip()[:120]}")
            continue
        pct, got, tot = float(pc.group(1)), int(pc.group(2)), int(pc.group(3))
        dens = float(dn.group(1)) if dn else 0.0
        words = int(wd.group(1)) if wd else 0
        rows.append((skill, pct, got, tot, words, dens))
        if pct < MIN_CONFORMANCE:
            missing = re.findall(r"❌ \w+\s+(.+)", out)[:4]
            failures.append(f"{skill}: {pct}% conformance — missing {', '.join(missing)}")
        elif dens < MIN_DENSITY:
            failures.append(f"{skill}: shape is right but thin ({dens} words per element)")

    rows.sort(key=lambda r: r[1])
    print(f"\n{'skill':<28}{'conform':>9}{'elements':>10}{'words':>8}{'density':>9}")
    print("─" * 66)
    for skill, pct, got, tot, words, dens in rows:
        flag = "" if pct >= MIN_CONFORMANCE and dens >= MIN_DENSITY else "  ←"
        print(f"{skill:<28}{pct:>8}%{f'{got}/{tot}':>10}{words:>8}{dens:>9}{flag}")
    print("─" * 66)
    if rows:
        mean = round(sum(r[1] for r in rows) / len(rows), 1)
        perfect = sum(1 for r in rows if r[1] == 100.0)
        print(f"{len(rows)} artifacts checked · mean {mean}% · {perfect} at 100%")
    if EXEMPT:
        print(f"\nexempt ({len(EXEMPT)}): " +
              " · ".join(f"{k} — {v}" for k, v in EXEMPT.items()))
    if skipped:
        print(f"\n⚠️  {len(skipped)} skills have no worked example: {', '.join(skipped)}")
        failures.append(f"COVERAGE: {len(skipped)} skills ship without a worked example")
    print()

    if failures:
        print("FAILED:")
        for f in failures:
            print(f"  ✗ {f}")
        print()
        sys.exit(1)
    print("All artifacts conform to their skill's declared output template.\n")


if __name__ == "__main__":
    main()
