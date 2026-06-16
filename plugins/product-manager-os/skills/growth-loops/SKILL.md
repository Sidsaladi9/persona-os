---
name: growth-loops
description: Designs compounding growth loops instead of one-shot funnels, using the Reforge model — classify the loop (viral, content, sales, paid), map inputs → action → output → reinvestment, and locate the compounding step and where it leaks. Use when you say "our funnel is leaking," "growth has plateaued," "how do we make acquisition compound," "what's our viral loop," or "model our content/paid loop."
---

# Growth Loops

Funnels are linear and consume what you pour in; loops are circular and reinvest their own output to fuel the next turn. This skill applies the Reforge-style growth loop model — every durable growth engine is a loop where the output of one cycle becomes the input of the next, and the job is to find the compounding step and stop the leaks around it.

**Grounded in:** *Hooked* — Nir Eyal: build a compounding loop (trigger → action → reward → investment), not a one-shot funnel.
**Go deeper (The Product Channel):** [Network Effects 101](https://sidsaladi.substack.com/p/network-effects-101-the-ultimate)

## When to use this
- Growth has plateaued and paid spend is the only lever still moving the number.
- You can describe your funnel stage by stage but can't say how a new user *creates* the next one.
- You're choosing between investment areas (viral vs. content vs. paid vs. sales) and need to compare their loop economics.
- A loop "works" but barely — you suspect a single step is leaking most of the volume.
- Leadership keeps funding top-of-funnel campaigns instead of fixing the mechanism that should compound.

## Before you start (gather these)
- **The action that produces growth output** — what a user does that can pull in or re-engage another user (shares, publishes content, invites a teammate, generates an indexable artifact).
- **Step-level numbers** — volume and conversion at each stage of one loop turn (e.g., signups → activated → who-shares → invites-sent → invite-accept → new-signup).
- **Cycle time** — how long one turn takes (hours for viral, weeks-to-months for content/SEO).
- **The reinvested output** — what the loop spits out that becomes next-cycle input (new users, content pages, referral credits, revenue redeployed into spend).
- **Loop economics** for paid/sales loops — CAC, payback period, and what fraction of revenue is reinvested.

If two or more of these are missing or vague, you MAY ask 2–4 sharp questions — e.g., "When a user gets value, what's the single action that could bring in another user?", "What are the conversion rates at each step of one turn?", "How long is one cycle?", "For paid: what's CAC and payback, and how much revenue goes back into spend?" But asking is optional, not mandatory: **on a first pass you are explicitly permitted to proceed with reasonable, clearly-stated assumptions rather than stalling on clarifying questions.** Pick defensible placeholder numbers, label them in the Assumptions section, model the loop end-to-end, and let the user correct the inputs — a complete model with stated assumptions is more useful than a question-asking stall. State assumptions inline as you go (e.g., *"Assuming invite-accept ≈ 25% absent data"*).

## Process
1. **Classify the loop.** Pin it to one primary type: **Viral** (users invite/expose other users), **Content** (users or the product generate content that acquires via search/social), **Sales** (revenue funds a sales motion that lands accounts), or **Paid** (revenue funds ads that acquire users). Most companies run 2–3; model the dominant one first.
2. **Write the loop as a sentence.** Force it into "A new user does X, which produces Y, which brings in the next new user." If you can't close the sentence back to a new input, it's a funnel, not a loop — name that honestly.
3. **Map the four nodes: Input → Action → Output → Reinvestment.** Input = what enters the turn. Action = the value-driven behavior that generates output. Output = the asset/signal/revenue created. Reinvestment = how that output re-enters as next-cycle input. Draw it as a closed circle. **Before treating this as a viral acquisition loop, test whether the reinvested input is a genuinely NEW user** — not an existing teammate, a re-activated dormant account, or the same user returning. If the output mostly re-engages people already in the product, it's an expansion/retention mechanism, not acquisition; classify it as such and do NOT compute viral K on it.
4. **Quantify each step with a conversion rate and volume.** Put real numbers on every arrow for one full turn. This is where you find leaks — the step that drops the most volume relative to its potential.
5. **Identify the compounding step.** This is the single node where output exceeds input — the multiplier that makes the loop grow rather than decay. For viral, K is the full chain, not just sent × accept: **K = pct_who_invite × invites_per_inviter × pct_external × accept_rate** — where `pct_who_invite` is the fraction of users who invite *at all*, `invites_per_inviter` is invites sent per inviting user, `pct_external` is the fraction of invites going to genuinely new people (not existing teammates already in the product), and `accept_rate` is the fraction of those that convert to a new user. Omitting `pct_who_invite` or `pct_external` inflates K badly. For content it's pages-published × traffic-per-page × convert-to-creator. Name it explicitly; everything else is plumbing around it.
6. **Find the leak.** The primary leak is the lowest-converting step *adjacent to* the compounding step — fixing a distant step doesn't compound, fixing this one does. Name a **primary leak**, and if a second adjacent step is also clearly draining volume, name a **secondary leak** too (don't force exactly one when two genuinely matter). Distinguish a leak (fixable conversion gap) from a ceiling (structural limit).
7. **Compute the loop coefficient.** Estimate the multiplier per turn (K for viral; output-per-input for others). >1 = compounding, ~1 = flat, <1 = decaying-needs-constant-refueling. State cycle time alongside it — a K of 1.2 every 2 days beats 1.5 every 90 days.
8. **Prescribe one intervention.** Pick the highest-leverage fix at the leak adjacent to the compounding step, with the expected effect on the loop coefficient. One lever, not a laundry list.

## Output template

# Growth Loop: [Product / Motion]

## Loop classification
- **Primary loop type:** [Viral / Content / Sales / Paid]
- **Acquisition loop vs expansion/retention mechanism:** [Acquisition — reinvested output is a genuinely NEW user/account] / [Expansion or retention — reinvested output re-engages an EXISTING user; do NOT compute viral K here]
- **Secondary loops in play:** [list, or "none"]
- **Cycle time:** [e.g., 3 days / 6 weeks / 1 sales quarter]

## The loop in one sentence
A [new user / account] does [action], which produces [output], which brings in [next input] — closing the loop in [cycle time].
> If this sentence can't close, it's a funnel today. Gap: [what's missing to make it a loop].

## Loop map (Input → Action → Output → Reinvestment)

| Node | What it is | Volume (1 turn) | → Conversion to next | Notes |
|------|-----------|-----------------|----------------------|-------|
| Input | [new users / spend / content seeds] | [n] | [%] | |
| Action | [value-driven behavior] | [n] | [%] | activation gate |
| Output | [asset / signal / revenue created] | [n] | [%] | |
| Reinvestment | [how output re-enters as input] | [n] | — | next-turn input |

Closed-circle view:

```
   ┌──────────────────────────────────────┐
   │  INPUT [n] ──▶ ACTION [n] ──▶ OUTPUT  │
   │     ▲                          [n]    │
   │     └──── REINVESTMENT ◀───────┘      │
   └──────────────────────────────────────┘
```

## Compounding step
- **Where output > input:** [the multiplier node]
- **Why it compounds:** [each turn's output seeds more than one next input because …]
- **Current multiplier here:** [for viral, the full K chain — e.g., K = pct_who_invite 30% × invites_per_inviter 2.4 × pct_external 70% × accept_rate 22% = 0.11 new users/user]

## The leak
- **Primary leak (adjacent to compounding step):** [step name]
  - **Current vs. realistic conversion:** [12%] → [target 25%]
  - **Leak or ceiling?** [Leak — fixable] / [Ceiling — structural, don't over-invest]
  - **Volume lost per turn:** [n]
- **Secondary leak (adjacent, optional — only if it genuinely matters):** [step name, or "none"]
  - **Current vs. realistic conversion:** [X%] → [target Y%]
  - **Volume lost per turn:** [n]

## Loop coefficient
- **Multiplier per turn:** [K = 0.X / 1.X]
- **Verdict:** [Compounding >1 / Flat ~1 / Decaying <1 — requires constant refueling]
- **Per cycle time:** [coefficient] every [cycle time]

## The one intervention
- **Fix:** [single highest-leverage change at the leak]
- **Expected effect:** moves [step] from [X%] → [Y%], lifting loop coefficient [0.X] → [0.Y]
- **How to validate:** [the one metric to watch over the next N turns]

## Assumptions
- [Any number estimated rather than measured]

## Avoid (anti-patterns)
- **Drawing a funnel and calling it a loop.** If the last step doesn't feed the first, you have a funnel — say so instead of forcing a circle.
- **Optimizing a step far from the compounding node.** Lifting top-of-funnel signups when the leak is invite-accept just pours more water through the same hole; gains don't compound.
- **Reporting K without cycle time.** A coefficient is meaningless unmoored from how fast the loop turns — a slow strong loop loses to a fast modest one.
- **Modeling three loops at once.** Pick the dominant loop, fix it, then move to the next; blended numbers hide which mechanism actually compounds.
- **Treating a paid loop as compounding when payback is too long.** If reinvested revenue can't refuel spend faster than CAC is incurred, it's a funnel with extra steps — flag the payback constraint.

## Tips
- The fastest diagnostic: ask "what does a new user *make* that brings in the next one?" If the answer is "nothing, marketing does," you don't have a loop yet — that's the finding.
- Compounding steps are usually one of: an artifact that's indexable/shareable, an invite that carries the product's value, or revenue with sub-cycle-time payback. Look there first.
- Separate *leaks* (conversion gaps you can close) from *ceilings* (structural caps like total addressable inviters). Spend on leaks, accept ceilings.
- Loops decay silently — re-quantify each step every quarter. A loop that was >1 drifts below 1 as channels saturate and the compounding step erodes.
