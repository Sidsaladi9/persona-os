# Workspace — where the work lands

Every artifact this OS produces goes in here, at a **predictable path**, instead of scrolling away in a chat window.

This is not filing for its own sake. It is what makes the rest of the OS work:

- **Skills read it.** `write-spec` finds the strategy. `sprint-planning` finds last sprint. `red-team` finds the plan it's attacking. You stop re-pasting context you already gave.
- **The activity log is written from it.** Every artifact written appends a line to `memory/activity-log.md`, which is the input to `/tune-up`. No writing, no learning loop.
- **`decisions/` is the memory the chat can't hold.** Six months later, "why did we kill the CSV export?" has an answer with a date on it.

Each skill declares where it writes in its own frontmatter (`outputs:`). You never have to remember the path.

---

## The folders

| Folder | Holds | Written by |
|---|---|---|
| `projects/<slug>/` | Everything about one named piece of work — spec, stories, prioritization, launch plan, pre-mortem, test scenarios | `write-spec` · `user-stories` · `prioritize` · `launch-plan` · `pre-mortem` · `red-team` · `sprint-planning` · `test-scenarios` · `business-case` |
| `research/` | What you learned about users and the market — interviews, synthesis, personas, journey maps, sizing, competitors | `customer-interview` · `synthesize-research` · `personas` · `journey-map` · `segmentation` · `market-sizing` · `market-analysis` · `competitive-brief` · `feedback-analysis` · `triage-requests` |
| `strategy/` | The durable, slow-changing calls — strategy, positioning, pricing, ICP, roadmap, OKRs, growth loops | `product-strategy` · `positioning` · `pricing` · `icp` · `roadmap` · `okrs` · `business-model` · `growth-loops` |
| `metrics/` | Numbers and what they meant — reviews, cohorts, experiment readouts, saved queries | `metrics-review` · `cohort-analysis` · `experiment-analysis` · `north-star` · `sql-queries` |
| `meetings/` | Notes and retros, by date | `meeting-notes` · `retro` |
| `comms/` | Anything that goes to other humans — updates, release notes, incident comms | `stakeholder-update` · `release-notes` · `incident-comms` |
| `decisions/` | One file per decision that would be expensive to relitigate | any skill, whenever a real call gets made |

`projects/` is the only folder that nests. Everything else is flat, dated files — flat is easier to grep and nothing gets buried.

---

## Naming

- Dates are **absolute and sortable**: `2026-08-18`, never "last Tuesday".
- Slugs are lowercase-hyphenated: `projects/csv-export/`, not `projects/CSV Export/`.
- A file is named for **what it is**, not who asked: `spec.md`, not `spec-for-priya.md`.

## `INDEX.md`

`workspace/INDEX.md` is a generated map of what exists. Regenerate it any time with:

```bash
python3 tests/index_workspace.py
```

## Privacy

The workspace is **local files in your repo**. Nothing syncs anywhere. If your product context is confidential, add `workspace/` to `.gitignore` — the OS works exactly the same either way.
