---
name: sprint-planning
description: Plan a sprint — scope work, estimate realistic capacity, set a goal, and draft a copy-pasteable plan. Use when you say "plan our sprint", "size the backlog", "what fits in this sprint", need a "sprint goal", are deciding "P0 vs stretch", or need to "handle carryover" from last sprint. Works from a pasted backlog or pulls from Linear/Jira if connected.
---

# Sprint Planning

A sprint plan is a bet: this team, this much time, against one outcome that matters. Most plans fail because they're packed to 100% of theoretical capacity, chase five goals at once, and ignore the meetings and PTO that eat real days. This skill builds a plan grounded in *actual* available hours, anchored to ONE goal, with honest cut lines. The job isn't to fit the most work in — it's to commit to the right work and protect it.

## When to use this
- Kicking off a new sprint and need to scope what's realistic.
- Sizing a backlog against who's actually available (PTO, meetings, on-call).
- Deciding what's P0 (must ship) vs. P1 vs. stretch.
- Handling carryover from the last sprint without silently overcommitting.
- Sanity-checking a plan someone else drafted: "does this actually fit?"

## Before you start (gather these)
Ask for anything missing before planning — don't guess capacity.
- **Backlog items** — pasted list with rough sizes, or note: *"I can pull open issues from Linear/Jira if connected."*
- **Sprint length** — e.g., 1 or 2 weeks; working days only.
- **Team + availability** — who's on the sprint, plus PTO, holidays, on-call, part-time splits.
- **Carryover** — unfinished work from last sprint and its remaining estimate.
- **Sprint goal candidate** — the one outcome this sprint is for (if they have one).
- **Recurring overhead** — standing meetings, ceremonies, support rotations per person.

## Process
1. **Compute realistic capacity.** For each person, subtract overhead first, then take the buffer off what's left — the **20% buffer is 20% of the subtotal AFTER subtracting PTO/holidays, meetings, and on-call**, not 20% of raw working days. Formula: `Available = (working days − meetings − PTO/holidays − on-call) × 0.8`. The buffer absorbs interrupts, reviews, and the unknown. Sum each person's Available to a team total. This number, not the calendar, is your budget.
2. **Set ONE sprint goal.** A single sentence stating the outcome and why it matters — not a list of tickets. If you can't name one goal, the sprint isn't scoped yet.
3. **Rank against the goal.** Tag each item **P0** (goal fails without it), **P1** (high value, goal survives without it), or **Stretch** (nice if time remains). Carryover competes on the same ranking — it is not auto-committed.
4. **Fit to capacity.** Fill P0 first, then P1, stopping when committed estimates reach your *buffered* capacity. Draw a visible cut line. Everything below it is stretch or next sprint.
5. **Name an owner per item.** No item ships without exactly one accountable owner. Flag any person loaded past their individual capacity.
6. **Flag dependencies & risks.** External teams, design/research not-yet-done, unknowns needing a spike, single points of failure. Each gets an owner and a "what we'll do about it."
7. **Protect the buffer.** Do not backfill it with stretch work. It absorbs reality; spending it upfront guarantees a miss.

## Output template
```
# Sprint Plan — [Sprint name / dates]

## Sprint Goal
[One sentence: the outcome this sprint delivers and why it matters.]

## Capacity Summary
| Person | Raw | −Meetings | −PTO | −On-call | Subtotal | −Buffer (20%) | Available |
|--------|-----|-----------|------|----------|----------|---------------|-----------|
| [Name] | [N] | [m] | [p] | [o] | [s] | [s×0.2] | [s×0.8] |
| ...    | ... | ... | ... | ... | ... | ... | ... |
| **Team total** | | | | | | | **[N committable days]** |

## Committed (≤ capacity)
**P0 — must ship**
- [ ] [Item] — owner: [Name] — est: [Xd]
**P1 — high value**
- [ ] [Item] — owner: [Name] — est: [Xd]
_Committed total: [Xd] / [capacity Yd]_

## Stretch (only if time remains)
- [ ] [Item] — owner: [Name] — est: [Xd]

## Carryover Handling
- [Item from last sprint] → [re-committed as P0 / deprioritized / dropped / absorbed into [item] (estimate already counted there — not double-counted) + why]

## Dependencies & Risks
- [Dependency/risk] — owner: [Name] — mitigation: [action]

## Definition of Done
- [ ] Merged & deployed to [env]  · [ ] Tested  · [ ] Docs/tracking updated  · [ ] [team's DoD criteria]
```

## Quality bar
- [ ] Capacity subtracts meetings, PTO/holidays, on-call **and** a buffer (~20%).
- [ ] Total committed estimate is **≤ buffered capacity** (verify the math).
- [ ] Exactly **one** crisp sprint goal, written as an outcome.
- [ ] Every committed item has exactly **one** owner; no person is overloaded.
- [ ] Carryover is explicitly re-ranked, not silently rolled in.
- [ ] Dependencies and risks each have an owner and a mitigation.

## Tips
- **Never plan to 100%.** Buffered capacity is the real ceiling — full calendars always overrun.
- **One goal, not five.** If everything is the goal, nothing is. Sub-goals are just P1 items.
- **Protect the goal from scope creep.** Mid-sprint adds displace something — make the trade visible, don't absorb it.
- **Carryover is a smell, not a default.** Chronic carryover means you're overcommitting; cut, don't roll.
- **Estimate in ideal days, plan in available days** — the gap between them is exactly the overhead you must subtract.
- **A spike is a commitment too.** If an item is too unknown to size, the P0 is the spike, not the build.
- **Round to the nearest 0.5 day.** Capacity estimates aren't precise to the decimal — round each Available figure to the nearest half-day and treat the "≤ capacity" fit as approximate. Don't manufacture false precision like 5.2 / 6.4 / 0.6 days; 5.0 ≤ 6.5 with a little room is the honest read.
