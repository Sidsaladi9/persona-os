# Tools

Scripts the OS actually asks you to run. Plain Python 3, no dependencies.

| Command | When |
|---|---|
| `python3 tests/relevance_report.py` | Which artifacts you never opened again. `/tune-up` runs it. |
| `python3 tests/score_skill.py skills/<name>/SKILL.md` | After writing a skill with `skill-creator`. Ship at 100. |
| `python3 tests/run_all.py` | Score every skill you have, including your own. |
| `python3 tests/check_artifact.py --skill <name> <file>` | Does a produced artifact match what the skill promised? |
| `python3 tests/index_workspace.py` | Regenerate `workspace/INDEX.md`. |

The full suite — including the CI gates and the worked-example checks — lives in [the repo](https://github.com/Sidsaladi9/persona-os/tree/main/plugins/product-manager-os/tests).
