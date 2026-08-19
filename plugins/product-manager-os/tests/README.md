# Tests

Most skill packs ship a lint that proves the files parse. This scores them.

Every skill gets a number out of 100, the numbers are committed, and CI fails
when a number goes **down** — not just when a file is malformed. That turns
"battle-tested" from a claim in a README into something you can check out and
run yourself.

| Script | What it does |
|---|---|
| [`score_skill.py`](score_skill.py) | Scores one `SKILL.md` — 22 binary checks, 6 dimensions, 0–100 |
| [`run_all.py`](run_all.py) | Scores all 53, writes [`RESULTS.md`](RESULTS.md), enforces four gates |
| [`check_artifact.py`](check_artifact.py) | Checks a produced artifact against the output template its skill promised |
| [`check_all_artifacts.py`](check_all_artifacts.py) | Runs that check across every worked example in `examples/cadence/` |
| [`relevance_report.py`](relevance_report.py) | Checks whether produced artifacts were ever referenced or revisited — the "did this output matter?" signal |
| [`index_workspace.py`](index_workspace.py) | Regenerates `workspace/INDEX.md` |

## Three different questions

**`run_all.py` asks: is the instruction good?** Does the frontmatter tell a PM
whether they can start right now. Is the judgment grounded in a named source.
Does a `guided` skill actually ask before producing, or does it invent the
inputs it should have requested.

**`check_all_artifacts.py` asks: did the instruction produce what it promised?**
A skill can score 100 and still yield a thin artifact. This reads the skill's
declared `## Output template`, extracts the structure, and checks a real output
against it — including a density check that catches the artifact with every
heading present and nothing underneath them.

**`relevance_report.py` asks: was the output worth producing?** The other two run
in CI against fixtures. This one runs against *your* `workspace/` and answers the
question neither can: after an artifact was written, did anyone ever come back to
it? A skill whose outputs are consistently never referenced or revisited is
producing the wrong thing, or producing it at the wrong moment. It's the signal
the activity log structurally cannot give you, and `/tune-up` reads it.

## Gates

`run_all.py --check` fails on any of:

1. **Floor** — a skill below 85.
2. **Regression** — a skill below its recorded score in [`baseline.json`](baseline.json). This is the gate that matters. Gaps are allowed; silent decay is not.
3. **Integrity** — a skill directory with no `SKILL.md`.
4. **Routing** — an `outputs:` path pointing at a folder that doesn't exist.

`check_all_artifacts.py` fails on conformance below 70%, density below 25 words
per required element, or a skill shipping with no worked example. Two skills are
exempt with a stated reason; an exemption without one is just a skipped test.

## Running them

```bash
python3 tests/run_all.py                     # score everything, write the scoreboard
python3 tests/run_all.py --check             # CI mode, no writes
python3 tests/check_all_artifacts.py         # output conformance across all examples
python3 tests/relevance_report.py            # which of YOUR artifacts went dead
python3 tests/score_skill.py skills/write-spec/SKILL.md
python3 tests/check_artifact.py --skill write-spec --template-only
```

`relevance_report.py` is deliberately **not** in CI — it reads your local
workspace, which CI has no business seeing and which is empty on a fresh clone.

After adding or editing a skill:

```bash
python3 tests/run_all.py && python3 tests/check_all_artifacts.py
```

Then commit `RESULTS.md`. If you deliberately raised a score, accept the new
floor with `python3 tests/run_all.py --baseline` and commit `baseline.json` too.

## A note on the scorer

`score_skill.py` is a **loss function**, and it is meant to stay fixed. The
point of a fixed measure is that editing a skill moves the number for a real
reason. If you find yourself wanting to change a check so a skill passes, the
skill is what needs changing — the one exception is a genuine parser bug, and
those get fixed with a test, not a threshold.

New skills ship at **100**, never at the 85 floor. The floor is what a skill is
allowed to decay to, not what it's allowed to arrive at.
