---
name: segmentation
description: Segment a market or user base by needs and behavior — not just demographics — then size, score, and pick a beachhead segment with a defensible rationale. Use when someone says "segment this market", "who should we target first", "find our beachhead", "break our users into segments", "which customers do we prioritize", or "TAM/SAM by segment".
---

# Segmentation

Useful segments group people by what they're trying to get done and how they behave — not by age, company size, or industry. Demographics and firmographics are addressable labels you bolt on *after* you've found a real need-and-behavior cluster; they are how you reach a segment, not what makes it one. This skill finds those clusters, sizes and scores them, and picks the one beachhead worth winning first.

**Grounded in:** *Crossing the Chasm* — Geoffrey Moore: pick a single beachhead segment instead of boiling the ocean.
**Go deeper (The Product Channel):** [How to Create a Customer Persona](https://sidsaladi.substack.com/p/week-21-how-to-create-a-customer)

The test for a real segment: **the people in it share a need or behavior such that one product decision serves all of them and would change if you targeted a different segment.** If a single offering satisfies two "segments" equally, they're one segment.

## When to use this
- You're entering a market and need to decide which slice to attack first instead of building for "everyone."
- Your user base feels heterogeneous and you suspect you're averaging across groups that want different things.
- Sales, marketing, and product each describe "the customer" differently and you need one shared map.
- You're writing a strategy, GTM plan, or board deck that needs a defensible TAM/SAM broken down by segment.
- A feature lands well with some users and flat with others, and you want to know what actually distinguishes them.

## Before you start (gather these)
- **The market or user base** — the full population you're segmenting (a market category, your current users, a funnel stage, a region).
- **Signal on needs and behavior** — interviews, support tickets, usage analytics, win/loss notes, sales call themes, survey data, or job-to-be-done evidence. This is what you cluster on; without it you're guessing.
- **Sizing inputs** — anything that lets you estimate segment size: customer counts, market reports, ARPU/willingness-to-pay, conversion rates, deal sizes.
- **Your strategic constraint** — what "beachhead" means for *you* this cycle: fastest revenue, lowest CAC, strongest reference logos, clearest path to expansion, or defensibility.

If two or more of these are missing or vague, **ASK 2–4 sharp questions before segmenting** — e.g. "What population are we segmenting — the whole market or just current users?", "What needs/behavior data do you have, or are we working from hypotheses?", "What does winning the beachhead need to deliver first: revenue, logos, or learning?", "Do you have any size or willingness-to-pay numbers?" If the data is already provided, proceed and state your assumptions inline (mark sizing guesses and unproven clusters explicitly).

## Process
0. **State the decision and the metric this segmentation must move.** Before anything, write down the concrete decision this segmentation feeds and the single outcome metric it must improve — e.g. "which segment to target first to lift week-2 retention," "where to focus to cut blended CAC," or "which slice expands net revenue retention." Then pick the lens (step 1) that best predicts *variance in that specific outcome*. The right axis isn't "the most interesting cut" — it's the one along which the target metric differs most between groups. If two candidate lenses both look reasonable, prefer the one where you'd expect the outcome metric to swing hardest across its segments.
1. **Pick the segmentation lens first, and name it.** Choose the primary axis that actually predicts different product needs: jobs-to-be-done, the trigger/occasion that brings them to a solution, the workflow or behavior pattern, or the underlying need. Demographics/firmographics are *descriptors*, not the lens. Picking the wrong axis is the most expensive mistake here — segmenting a productivity tool by company size when the real divider is "solo vs. collaborative workflow" produces segments that don't behave differently.
2. **Cluster on needs and behavior.** Group the population by shared job, trigger, pain, and current workaround. Two people in different industries who hire your product for the same job belong in the same segment; two people in the same industry doing different jobs do not.
3. **Pressure-test that the clusters are real.** For each pair of segments ask: "would the product decision differ?" If one offering serves both equally, merge them. If one cluster splits into two different builds, split it. Aim for 3–6 segments — enough to be specific, few enough to act on.
4. **Attach descriptors so each segment is addressable.** Now bolt on the firmographic/demographic/channel labels that let you actually find and reach this cluster. A need-based segment you can't target is an insight, not a segment.
5. **Size each segment.** Estimate population × reachable share × value (ARPU or deal size). Show your math and label every number as `[sourced]` or `[estimate]`. A rough, transparent number beats a precise-looking fabricated one. **When population is an `[estimate]` derived from analogs (a comparable market, a proxy company, a top-down guess), treat the resulting segment value as an *ordinal ranking signal* — "A is bigger than B is bigger than C" — not a bankable TAM you can put in a plan.** Express analog-derived sizes as ranges (e.g. "$1–3M"), never point estimates, and say so in the Basis column. Use these numbers to *rank* segments, not to forecast revenue.
6. **Set the weights *before* you score, then score.** Fix the criterion weights from your strategic constraint first — committing to weights after seeing the scores lets you rationalize a predetermined winner. Worked example: if the constraint is "fastest path to a referenceable win this cycle," you might set Pain intensity 0.30, Reachability 0.25, Ability to win 0.25, Size/value 0.10, Expansion 0.10 — pain and reach dominate because a winnable, urgent segment beats a big, contested one for this goal. Then rate every segment 1–5 on: Size/value, Pain intensity (how badly they need a solution now), Reachability (can you find and sell to them efficiently), Ability to win (do you have a right-to-win vs. incumbents), and Expansion potential (does winning them open adjacent segments). Don't pretend all five matter equally.
   - **Sanity-check the weights by flipping the two heaviest.** Swap the weights on your two most heavily weighted criteria and recompute the totals. If the beachhead is the same segment, the call is robust — note that. If it changes, that's a signal: either your weights encode a real strategic bet you should state explicitly, or the top segments are close enough that the choice hinges on a judgment call you must surface. Explain which it is rather than burying it.
7. **Pick the beachhead and write the rationale.** Choose one segment to win first. The beachhead is usually *not* the biggest — it's the one where intense pain meets reachability and a right-to-win, and that serves as a launchpad to bigger segments. State explicitly which segments you're deferring and why, and what winning the beachhead unlocks next.

## Output template
```markdown
# Segmentation: [market / user base]

**Population segmented:** [the full set, e.g. "current 4,200 active accounts" or "the X market"]
**Primary lens:** [jobs-to-be-done | trigger/occasion | behavior pattern | core need] — chosen because [why this axis predicts different needs]
**Strategic constraint this cycle:** [revenue | logos | CAC | learning | defensibility]
**Data basis:** [what evidence backs the clusters; mark thin areas]

## Segments

### Segment A — [behavior-based name, e.g. "Solo firefighters"]
- **Core job / need:** When [situation], they want to [job], so they can [outcome].
- **Defining behavior:** [how they act today — workflow, frequency, the workaround/competitor they use now]
- **Trigger:** [what brings them to look for a solution]
- **Descriptors (how to reach them):** [firmographic/demographic/channel labels — title, segment size of co., where they hang out]
- **Why they're distinct:** [the product decision that differs for this segment vs. others]

[repeat block for each segment B, C, …]

### Anti-segment (non-job cluster) — *optional, include if one exists*
- **Defining behavior:** [what these people do — often low-intent, mixed-motive, or grab-bag usage that doesn't cohere around one job]
- **Why no single product decision wins them:** [they don't share a job/trigger, so any one build/price/message that serves part of them alienates or misses the rest — they're a residual, not a segment]
- **Recommended action:** [explicitly de-prioritize / don't build for them this cycle / serve passively with the beachhead product / revisit if a real sub-cluster emerges from data]

## Sizing

| Segment | Population | Reachable share | Value (ARPU/deal) | Est. segment value | WTP confidence | Basis |
|---|---|---|---|---|---|---|
| A | [n] | [%] | [$] | [$ or range] | [high/med/low] | [sourced/estimate] |
| B | [n] | [%] | [$] | [$ or range] | [high/med/low] | [sourced/estimate] |
| C | [n] | [%] | [$] | [$ or range] | [high/med/low] | [sourced/estimate] |

> Show the math: segment value = population × reachable share × value. Flag every [estimate].
> **WTP confidence** = how well-grounded the willingness-to-pay / value number is: `high` (sourced from real deals or pricing data), `med` (a few data points or close analog), `low` (assumed from a distant analog). Low-WTP-confidence sizes are ordinal ranking signals only — use ranges, not point estimates.
> When population is an analog-derived `[estimate]`, give a range in "Est. segment value" and rank rather than bank these numbers.

## Scoring (1–5; weights reflect strategic constraint)

| Criterion | Weight | A | B | C |
|---|---|---|---|---|
| Size / value | [w] | [1–5] | | |
| Pain intensity | [w] | | | |
| Reachability | [w] | | | |
| Ability to win | [w] | | | |
| Expansion potential | [w] | | | |
| **Weighted total** | | **[x]** | **[x]** | **[x]** |

## Beachhead decision

**Target first: [Segment X]**

Rationale:
- **Pain:** [why this segment needs a solution now, not someday]
- **Reachability:** [why you can find and sell to them efficiently]
- **Right to win:** [why you beat the incumbent/alternative here specifically]
- **Launchpad:** [the adjacent segment(s) winning X unlocks, and the mechanism — shared workflow, reference logos, data advantage]

**Deliberately deferred:**
- [Segment Y] — [why not now: e.g. bigger but you have no right-to-win yet]
- [Segment Z] — [why not now]

**What would change this call:** [the signal — e.g. "if Segment Y's pain is validated at >X, reprioritize"]. Call out any low-WTP-confidence sizing that the decision leans on: if the beachhead ranks ahead of the next segment only on a `low` WTP-confidence value estimate, name the pricing/willingness-to-pay evidence that would confirm or flip the ranking (e.g. "if Segment A's real WTP comes in below $Y, B overtakes it").
```

## Avoid (anti-patterns)
- **Segmenting by demographics/firmographics as the primary lens.** "Enterprise vs. SMB" or "millennials vs. boomers" feels rigorous but usually splits people who want the same thing and lumps together people who don't. Lead with need/behavior; add the labels after.
- **Segments that don't change a decision.** If your product, pricing, and messaging would be identical across two segments, they're one segment wearing two names. Merge them.
- **Picking the biggest segment as the beachhead by reflex.** The largest segment is often the most contested and the hardest to win from zero. Beachhead = winnable + painful + a launchpad, not just big.
- **Fabricated sizing precision.** A "$2.3B SAM" with no visible math is theater. Show population × reach × value and label estimates — a transparent range beats a fake point estimate.
- **No anti-segment.** If you can't name who you're *not* serving first and why, you haven't actually focused — you've just ranked everyone.

## Tips
- Name segments by behavior, not label — "Weekend power-users" or "Compliance-driven buyers" sticks and encodes the defining trait; "Segment 2" doesn't.
- The beachhead test from Moore/Blank: can you win >50% of this segment, is it big enough to matter but small enough to dominate, and does it give you a beach to land on for the next one? If not, narrow further.
- Sanity-check segments against real usage data before trusting interview-derived clusters — what people say and what they do diverge, and behavior wins.
- Re-run segmentation when the product, market, or data shifts. Segments are a snapshot of how needs cluster *now*; today's beachhead becomes tomorrow's saturated base.
