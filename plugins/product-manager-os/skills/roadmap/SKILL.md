---
name: roadmap
description: Use when the user wants to update the roadmap, build a Now/Next/Later view, reprioritize after new information, decide what moves to make room for a new initiative, shift timelines after a dependency slip, or figure out where a new initiative fits. Forces explicit trade-offs and keeps the roadmap anchored to outcomes, not a feature wishlist.
---

# Roadmap

A roadmap is a statement of intent, not a delivery contract. Its job is to communicate *what outcomes you're betting on, in what order, and with how much confidence* — not to promise dates for a list of features. This skill helps you update, reprioritize, or build a roadmap in Now / Next / Later format, and it will make you say out loud what moves when you add something new. Most "roadmap updates" go wrong because people quietly inflate scope without admitting the trade-off. Don't let that happen.

## When to use this
- Adding a new initiative and you need to decide what gets bumped to make room.
- Priorities shifted after new information (a competitor move, a data point, a leadership ask).
- A dependency slipped and timelines need to move.
- Building a Now / Next / Later view from scratch.
- A stakeholder is treating the roadmap like a commitment and you need to reframe it as intent.

## Before you start (gather these)
- **Current roadmap** — in whatever form it exists. If there isn't one, say so; this skill can build from scratch.
- **The change** — the new initiative, the new information, or the slipped dependency that triggered this.
- **Capacity** — rough team size / number of parallel bets you can actually run in "Now." Be honest; "Now" is almost always smaller than people want.
- **Strategic themes or goals** — the 2-4 outcomes the product is pursuing this quarter/half. Everything on the roadmap should ladder up to one of these.

If any of these are missing, ask before proceeding — especially the strategic themes and capacity. A roadmap without themes is just a backlog with optimistic dates.

## Process
1. **Anchor to strategic themes first.** List the 2-4 outcomes you're driving toward (e.g. "reduce activation drop-off," "land enterprise-ready security," not "ship SSO"). Every roadmap item must trace to one. If an item traces to none, it's a candidate for the parking lot.
2. **Restate items as outcomes, not features.** "SSO + audit logs" becomes "Unblock enterprise deals stuck on security review." This keeps the conversation on *why* and lets you swap the *how* later without re-litigating priority.
3. **Place items in Now / Next / Later by confidence × value.** **Now** = committed, in-flight or starting, high confidence on both the problem and the approach. **Next** = strong intent, sequenced, but details may shift. **Later** = directional bets; deliberately fuzzy. Resist the urge to overload "Now" — capacity is the constraint, not ambition.
4. **When adding something, force the trade-off.** The number of "Now" slots equals your capacity number — so a full "Now" has no free slots, and adding to it requires removing something. Never add to "Now" without naming what leaves it. State it explicitly: *"To pull X into Now, Y moves to Next."* The trade-off can also be scope-narrowing in place: keep the item in "Now" but shrink it (e.g. full ML detector → rules-based v1) so it fits the same slot. If nothing moves and nothing shrinks, you're either over capacity or the new thing isn't actually a priority. Make the choice visible.
5. **Flag dependencies and risks.** For each Now/Next item note what it's blocked by or what it blocks. When a dependency slips, move the dependent item — don't pretend the date holds.
6. **Keep it outcome-oriented and honest on time.** Use ranges or relative horizons (this quarter / next quarter / later), never false-precision dates. "Later" is allowed to be vague — that's a feature, not a bug.

## Output template

```
# [Product] Roadmap — [Date]

Strategic themes this period:
1. [Theme / outcome]
2. [Theme / outcome]
3. [Theme / outcome]

## Now  (committed, in-flight — high confidence)
- **[Outcome it drives]**
  - Why now: [the bet / what makes this the priority]
  - Confidence: High / Med / Low
  - Dependencies: [blocked by / blocks — or "none"]
  - Owner: [name]

## Next  (sequenced, strong intent — details may shift)
- **[Outcome it drives]**
  - Why now: [...]
  - Confidence: High / Med / Low
  - Dependencies: [...]
  - Owner: [name]

## Later  (directional bets — deliberately fuzzy)
- **[Outcome it drives]** — [one line on the bet; no dates, no owner needed]

## Changes this update
- [What moved and why, e.g. "Pulled X into Now after [signal]; Y moved Now → Next to make room."]
- [Coupled move (one decision): "Pulled X into Now AND pushed Y out to Next — same trade, made together because [signal]."]
- [Scope shrink in place: "Kept X in Now but narrowed it — full ML detector → rules-based v1 — so it fits the same slot."]
- [Dependency slip: "Z slipped from Next to Later — blocked on [dependency]."]

## Parking lot
- [Ideas considered but not scheduled — and the reason: doesn't tie to a theme / below the line / needs validation]
```

## Quality bar
- [ ] Every item ties to a named strategic theme/outcome — no orphan features.
- [ ] Items are phrased as outcomes ("unblock enterprise deals"), not solutions ("ship SSO").
- [ ] "Now" respects capacity — it's not a wishlist.
- [ ] Every add to "Now" has an explicit trade-off in "Changes this update" (what moved out).
- [ ] Dates are ranges or relative horizons, never false-precision day-level commitments.
- [ ] Dependencies are flagged on every Now/Next item.
- [ ] "Later" is allowed to be fuzzy — no fake owners or dates forced onto it.
- [ ] "Changes this update" explains *why* each move happened, not just *what* moved.

## Tips
- **A roadmap is a statement of intent, not a contract.** Say this to stakeholders explicitly. Confidence decreases as you move right; communicate that, don't hide it.
- **Prioritize by outcome, not by who's loudest.** When two items compete, ask which theme each serves and which moves the metric more — not which exec asked.
- **Protect "Now" from churn.** Every mid-stream addition has a switching cost. Default to "that's a strong Next," and make anyone who wants it in Now name what they'll drop.
- **If everything is a priority, nothing is.** A "Now" with eight items is a planning failure, not a productive team.
- **Re-derive, don't just append.** When reprioritizing, re-check every item against the themes — stale items hide in roadmaps that only ever grow.
