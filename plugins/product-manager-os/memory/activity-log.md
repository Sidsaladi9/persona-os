# Activity Log

> The OS appends one line here after each meaningful task. It's the **behavior** layer of memory — what you've been doing — kept separate from the knowledge files (product/team/strategy) so it never pollutes them.
>
> It exists so the OS can spot work you repeat and offer to build or tune a skill for it (see *The self-improving loop* in `CLAUDE.md`). **This file is loop-input only: it is read by the tune-up, never sent anywhere, never pasted into an output. Local-only.** Clear or edit it anytime.

**Line format** (one per task, newest at the bottom):
```
- YYYY-MM-DD · asked: "<short paraphrase>" · skill: <name | none> · correction: <none | "what you changed in-session">
```

- **`skill: none`** means you hand-rolled it — no skill fired. Three of these for the same kind of job → the loop offers to build a skill.
- **`correction`** is what the user asked you to change about your output *during the session* (e.g. "shorter", "changed RICE weights", "wanted more pushback"). `none` = they accepted it as-is. The same correction on the same skill 3× → the loop offers to tune that skill (or house-style).

## Example entries (illustrative — safe to delete)
```
- 2026-06-05 · asked: "draft launch email for beta" · skill: none · correction: none
- 2026-06-12 · asked: "prioritize Q3 backlog" · skill: prioritize · correction: "changed RICE weights to favor retention"
- 2026-06-19 · asked: "draft launch email for v2" · skill: none · correction: none
```

## Log
<!-- real entries go below; the OS appends here, newest at the bottom -->
