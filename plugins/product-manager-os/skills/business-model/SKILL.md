---
name: business-model
description: Fills a complete Lean Canvas (or Business Model Canvas) across every block — problem, customer segments, unique value proposition, solution, channels, revenue, cost, key metrics, and unfair advantage — then flags the single riskiest block to validate first. Use when you say "map our business model," "fill a lean canvas," "what's our UVP," "how do we make money," "where's the riskiest assumption," or "pressure-test this idea before we build."
---

# Business Model

Captures an entire business or product bet on one page using Ash Maurya's Lean Canvas (the startup-oriented variant of Osterwalder's Business Model Canvas), then ranks blocks by risk so you validate the assumption most likely to kill the business — before you spend a quarter building.

**Grounded in:** *Running Lean* — Ash Maurya: the Lean Canvas and finding the riskiest block to validate first.
**Go deeper (The Product Channel):** [Product Led Growth](https://sidsaladi.substack.com/p/product-led-growth)

## When to use this
- A new product, feature line, or 0-to-1 bet needs a one-page model before it goes to leadership or a build team.
- You have a deck full of vision but can't crisply say who pays, for what, and why you instead of an incumbent.
- An existing product's economics feel off and you need to see the whole revenue/cost/segment picture at once.
- You're prepping a stage-gate, investment ask, or kill/continue decision and need the riskiest assumption named explicitly.
- A founder or stakeholder keeps debating the solution before anyone agreed on the problem or the customer.

## Before you start (gather these)
- **Customer segment(s)** — who specifically has the problem, and who's the early adopter (not "everyone").
- **Top 1–3 problems** — the actual pains, and what they do today as a workaround.
- **How money moves** — pricing idea, who pays, and rough cost structure (even ballpark).
- **Why you** — any unfair advantage, traction, or asset a competitor can't copy.

If two or more of these are missing or vague, ASK 2–4 sharp clarifying questions before filling the canvas — e.g. "Who's the single early-adopter segment, not the eventual market?", "What does this person do today instead?", "Who actually pays, and roughly how much?", "What can't a well-funded competitor copy in 6 months?" If the inputs are already provided, proceed and state any assumptions inline as `[ASSUMPTION: ...]` so they're visible and testable.

**Existing-business mode.** If this is a *running business* (has ARR, paying users, or live traffic) rather than a 0-to-1 bet, the problem and segment are already validated by the fact that people pay — don't re-litigate them as interview assumptions. Instead:
- **Pull segment, problem, and unit-economics from data, not interviews.** Read who actually pays and churns from billing/analytics, which problem retains them from usage and support tickets, and CAC/LTV/margin from real revenue and cost numbers. Treat these blocks as measured, not assumed (Uncertainty drops accordingly).
- **Default the risk lens to Solution + Key Metrics** — the assumptions most likely to still be unproven once problem/segment are settled (does the solution actually move the metric that compounds the model?).
- **Look for the unfair advantage in what you already own** — proprietary data, an installed user base, or distribution a new entrant can't buy is usually the real moat for an operating business.

## Process
1. **Lock the segment first.** Fill the customer segment and name an *early adopter* sub-segment. Everything else inherits from who. If the segment is "everyone," it's wrong — narrow it.
2. **Problem before solution.** Write the top 1–3 problems and the *existing alternatives* (what they hack together today). Resist writing solutions here.
3. **Draft the UVP as a single, specific sentence.** "We help [segment] achieve [outcome] without [pain of the old way]." Add a high-level concept ("X for Y") if it sharpens it. Make it a claim, not a feature list.
4. **Map solution to problems 1:1.** Each top problem gets exactly one solution bullet. If a solution doesn't trace to a problem, cut it.
5. **Channels — path to customers.** List how you reach the segment (inbound, outbound, partnerships, communities). Flag which are unproven.
6. **Revenue & cost on the same pass.** Revenue streams + pricing model; cost structure (CAC, COGS, fixed). Do a back-of-envelope unit-economics sanity check — does a customer net positive?
7. **Key metrics — the one number.** Pick the 1–3 numbers that tell you the model works (activation, retention, paid conversion). Name the single "North Star."
8. **Unfair advantage — be honest.** Only list things that *can't be easily copied or bought* (insider info, network effects, community, exclusive partnerships). "Great team" and "first mover" don't count.
9. **Rank risk and pick ONE.** Score **all nine blocks** on the two axes that matter: *Uncertainty* (1–5, how unproven the assumption is) and *Fatal* (1–5, how badly the business dies if it's wrong). **Risk = Uncertainty × Fatal** (range 1–25). Break ties by the higher *Fatal* score. The highest-Risk block is what you validate next — name it and propose the cheapest experiment to test it.

## Output template

```markdown
# Business Model — [Product / Venture Name]
Framework: Lean Canvas · Date: [YYYY-MM-DD] · Owner: [name]

## The Canvas

| Block | Contents |
|---|---|
| **1. Problem** | 1. [top problem] · 2. [problem] · 3. [problem]<br>**Existing alternatives:** [what they do today] |
| **2. Customer Segments** | [target segment]<br>**Early adopter:** [specific beachhead — who feels the pain most] |
| **3. Unique Value Proposition** | "[We help [segment] achieve [outcome] without [old-way pain].]"<br>**High-level concept:** [X for Y] |
| **4. Solution** | P1 → [solution] · P2 → [solution] · P3 → [solution] |
| **5. Channels** | [channel] · [channel] · [channel]  ([proven] / [unproven]) |
| **6. Revenue Streams** | [model: subscription/usage/one-time] · Price: [$] · Who pays: [payer] |
| **7. Cost Structure** | [CAC] · [COGS / unit cost] · [fixed costs]<br>**Unit-economics check:** [LTV vs CAC, gross margin — does a customer net positive?] |
| **8. Key Metrics** | [metric] · [metric]<br>**North Star:** [the one number] |
| **9. Unfair Advantage** | [thing competitors can't copy or buy] |

## Riskiest Block to Validate First

Risk = Uncertainty × Fatal (1–25). Score **all nine blocks**; break ties by the higher Fatal score.

| Block | Uncertainty (1–5) | Fatal if wrong? (1–5) | Risk (U × F) |
|---|---|---|---|
| Problem | [n] | [n] | [n] |
| Customer Segments | [n] | [n] | [n] |
| UVP | [n] | [n] | [n] |
| Solution | [n] | [n] | [n] |
| Channels | [n] | [n] | [n] |
| Revenue Streams | [n] | [n] | [n] |
| Cost Structure | [n] | [n] | [n] |
| Key Metrics | [n] | [n] | [n] |
| Unfair Advantage | [n] | [n] | [n] |

**Riskiest block: [name]** — [one sentence: why this assumption, if false, sinks the model].

**Cheapest test:** [the smallest experiment — e.g. 5 problem interviews, a fake-door landing page, a pre-sale of 10 units, a smoke-test ad] · **Pass/fail signal:** [the specific result that confirms or kills it] · **Timebox:** [days/weeks].

## Open assumptions
- [ASSUMPTION: ...] — [how we'll resolve it]
```

## Avoid (anti-patterns)
- **Solutions hiding in the Problem block.** "They need a dashboard" is a solution; the problem is "they can't see X without manual spreadsheet work." Keep them separate.
- **"Everyone" as a segment.** A canvas with a broad market and no named early adopter can't be validated; it just feels safe.
- **A UVP that's a feature list.** "Fast, secure, AI-powered" is not a value proposition. It must name the outcome and the pain it removes.
- **Fake unfair advantage.** Listing "passion," "first mover," or "great team" — all copyable or buyable. If a competitor with money could replicate it this quarter, it's not unfair.
- **Skipping the risk ranking.** A filled canvas with no riskiest-block call is a poster, not a decision tool. The whole point is choosing what to test first.

## Tips
- Fill the canvas in problem-driven order (segment → problem → UVP → solution), not left-to-right. The right side (revenue, cost) only makes sense once the left side is real.
- Pressure-test revenue against cost on the same pass — a beautiful UVP with LTV < CAC is a charity, not a business.
- For the riskiest block, default to the cheapest test that can return a *no*. You're hunting for disconfirmation, not validation theater.
- Re-run this monthly on live bets. The riskiest block changes as you de-risk; last month's scariest assumption is often this month's known fact.
