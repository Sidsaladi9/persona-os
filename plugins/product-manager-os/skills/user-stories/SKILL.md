---
name: user-stories
description: Breaks an epic, spec, or feature into well-formed user stories with Given/When/Then acceptance criteria, applies INVEST, and splits stories that are too big. Use when a PM says "break this epic into stories", "write user stories", needs "acceptance criteria for X", wants to "split this story", or asks to "turn this PRD into a backlog".
---

# User Stories

Turn a fuzzy epic, spec, or feature into a backlog of small, testable, independently shippable user stories. Each story names a user, a capability, and an outcome, carries acceptance criteria a developer and tester can verify, and is sliced as a thin vertical end-to-end path — never a horizontal technical layer. Where a story is too big, split it with a proven pattern rather than guessing.

## When to use this
- An epic or spec is too large to estimate or build, and needs decomposing.
- You're handed a PRD and need a ready-to-groom backlog out of it.
- A single story keeps growing or hides several decisions and should be split.
- A story exists but its acceptance criteria are vague, missing, or untestable.
- Sprint planning needs stories small enough to fit a sprint with clear "done."

## Before you start (gather these)
- The epic / spec / feature you're decomposing — the scope boundary.
- The user or persona who benefits (and any distinct user types involved).
- The outcome / goal: what changes for them when this ships.
- If pointed at a PRD or doc, read it first and pull the above from it.
- If scope, persona, or outcome is unclear, ask before slicing — don't invent them.

## Principles
- **Story form:** As a [user/persona], I want [capability], so that [outcome]. The "so that" is non-negotiable — it's the user value and the reason to build.
- **INVEST** every story:
  - *Independent* — minimal ordering dependencies on other stories.
  - *Negotiable* — a conversation, not a frozen contract of implementation detail.
  - *Valuable* — delivers observable value to a user or the business.
  - *Estimable* — the team understands it well enough to size it.
  - *Small* — fits comfortably in a sprint; ideally a few days.
  - *Testable* — you can write the acceptance criteria that prove it's done.
- **Acceptance criteria as Given/When/Then** — Given [context], When [action], Then [observable result]. Cover the happy path AND edge cases (empty, invalid, unauthorized, limits, failures).
- **Vertical slices over horizontal** — each story is a thin end-to-end path that delivers value (UI + logic + data for one capability), not a layer ("build the API," "build the schema") that delivers nothing alone. *Exception for quality-bar / model-accuracy work:* a story that proves a probabilistic capability hits its bar against an eval set (detection/scoring verified offline, no UI yet) is a legitimate first vertical slice — the verifiable accuracy *is* the value.
- **Acceptance criteria for probabilistic / ML / quality-bar features** — Given/When/Then is deterministic, but ML behavior is only correct ~85% of the time, so don't write AC as if each case must pass. Instead make the criteria threshold-based and measured against a fixed eval set / golden dataset: define a labeled dataset, set precision/recall (or F1, accuracy) targets, and write AC like "Given the golden eval set of N labeled examples, when the model runs, then precision ≥ 0.90 and recall ≥ 0.80." Specify the dataset, the metric, and the threshold so the AC is still pass/fail — just measured statistically rather than per-instance.

## Splitting patterns (when a story is too big)
- **Workflow steps** — slice along the steps of a process. "Checkout" → enter address → choose shipping → pay → confirm.
- **Business-rule variations** — one story per rule. Discount: percentage off, then BOGO, then loyalty tier.
- **Happy vs. edge path** — ship the happy path first, edges as follow-ups. "Pay with valid card" before "handle declined card."
- **Simple vs. complex** — do the basic case, defer the hard one. "Search by exact name" before "fuzzy + filters search."
- **Data / interface variations** — split by input type, format, or channel. "Upload CSV" before "upload Excel and JSON."
- **CRUD operations** — split create / read / update / delete. "View saved reports" can ship before "edit" and "delete."
- **Defer performance** — make it work, then make it fast. "Generate report (any speed)" before "generate report in <2s."

## Process
1. **Identify the user(s) and the epic's outcome** — who benefits and what changes for them. List distinct personas if more than one.
2. **Slice into vertical stories** — break the outcome into thin end-to-end capabilities, each delivering value on its own. Reach for a splitting pattern when a slice is still chunky.
3. **Write each in story form** — As a / I want / so that. Confirm the "so that" states real value.
4. **Add Given/When/Then acceptance criteria** — at least one happy-path scenario plus the edge cases that matter (invalid, empty, unauthorized, limits, failure).
5. **Check INVEST and bound the slice** — run each story through the six letters; flag and fix anything that fails. State what's explicitly out of scope for the story (deferred work, things handled elsewhere) so the boundary is unambiguous.
6. **Split anything too big** — if a story fails *Small* or *Estimable*, or hides multiple decisions, apply a splitting pattern and re-check.
7. **Sequence** — order by dependency and value; surface the thinnest slice that proves the epic end-to-end first.

## Output template
Copy-paste per story:

```
### [Story title]

As a [user/persona],
I want [capability],
so that [outcome].

**Acceptance criteria**
- Given [context], when [action], then [observable result].
- Given [edge context], when [action], then [result].
- Given [error/limit context], when [action], then [result].

**Notes / edge cases**
- [assumptions, open questions, data or rule details]

**Out of scope**
- [explicitly not in this story — deferred or handled elsewhere]
```

**Suggested build order**
1. [story] — thinnest end-to-end slice; proves the path.
2. [story] — [why next: unblocks X / highest value]
3. [story] — ...

## Avoid (anti-patterns)
- **Horizontal / technical-layer stories** — "build the API," "create the schema," "wire up the service." They deliver no user value alone. Slice vertically. *Exception:* a detection/eval-only story for an ML or quality-bar feature — verified against an eval set with no UI — is not a horizontal layer; the measured accuracy is real, demonstrable value and is a valid first slice.
- **Untestable acceptance criteria** — "works well," "is fast," "is intuitive." If you can't write a pass/fail check, rewrite it as Given/When/Then.
- **Giant stories** — one story hiding a dozen decisions, rules, or screens. If you can't estimate it, split it.
- **Missing the "so that"** — a capability with no stated user value. If there's no outcome, question whether to build it.

## Tips
- One verb per story. "Create and edit and export" is three stories.
- If estimation triggers an argument, the story is too big or too vague — split or clarify.
- Write the edge-case criteria first sometimes; they expose hidden scope fast.
- A story you can demo in one sentence ("watch me pay with a saved card") is the right size.
- Keep acceptance criteria about observable behavior, not implementation.
- Name the persona specifically ("returning shopper," not "user") — it sharpens the slice.
