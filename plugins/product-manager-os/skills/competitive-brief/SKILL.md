---
name: competitive-brief
description: Use when you need a competitive analysis brief or competitor teardown for one or more rivals or a feature area. Triggers include "competitive analysis", "build a battlecard for [competitor]", "how do we compare to X", "where should we differentiate", "competitor teardown", and prepping board or sales materials on the competitive landscape.
---

# Competitive Brief

A competitive brief turns scattered impressions about a rival into a decision. The point is never to list features side by side — it's to answer "where do we win, where do we lose, and what do we do about it?" This skill produces a strategy brief and a sales battlecard, both grounded in dated evidence and ending in a recommendation, not a shrug.

Good competitive work is opinionated and honest. It names where the competitor is genuinely better, distinguishes what you *know* from what you *suspect*, and resists the urge to make your product look good on paper. A brief that flatters you is worse than useless — it loses deals quietly.

## When to use this
- Informing product strategy or prioritization: deciding where to differentiate vs. reach parity.
- Building or refreshing a sales battlecard for the field team.
- Prepping board, investor, or leadership materials on the competitive landscape.
- A competitor just shipped, repriced, or repositioned and you need to assess the impact.
- Entering a new segment and need to map who already owns it.

## Before you start (gather these)
- **Competitor name(s)** — one for a deep teardown, or a set for a landscape.
- **The dimension(s) that matter** — what decision is this feeding? (Pricing? A specific feature gap? Enterprise readiness? GTM motion?) A brief with no decision behind it sprawls.
- **Your own positioning** — your target buyer, your wedge, your current pricing. The brief is relative to *you*; without this, it's just a profile.
- **Evidence sources.** If web search is available, this skill can research pricing pages, docs, changelogs, G2/Capterra reviews, job postings, and press. If it's not available — or for anything non-public (win/loss notes, sales-call intel, contract terms) — ask the user to paste it. Always say which mode you're in.

## Process
1. **Define the comparison frame.** Pin down the decision and pick 5–9 dimensions that actually move it (e.g. core capability, integrations, pricing model, time-to-value, security/compliance, support, ecosystem). Drop vanity dimensions nobody buys on. State the frame before gathering anything.
2. **Gather evidence (web + user-provided).** Pull from the live web where available; otherwise work from pasted material. For each claim, capture the source and the date you observed it. Tag every data point as **fact** (verifiable: a published price, a documented limit) or **inference** (your read: "likely targeting mid-market because…"). Flag gaps explicitly rather than guessing.
   - **If the user's intel is secondhand recall** (remembered from a call, "I think they…", no source pasted), treat the *entire* output as provisional: stamp the verification status accordingly and put a prominent **`⚠️ PROVISIONAL — re-pull before use`** banner at the top of both the brief and the battlecard.
   - **In user-provided / recall mode**, where nearly every competitor claim is inference, don't tag every line. State the default once up front — e.g. "*Unless marked otherwise, all competitor claims below are inference from user recall, not verified.*" — and then tag only the **exceptions** (the few that are verified fact, or the few that are pure guesswork beyond even recall).
3. **Map onto a matrix.** Score us vs. each competitor across the dimensions. Use plain marks (✅ strong / ⚠️ partial / ❌ absent / — unknown), not invented 1–10 scores that imply false precision.
4. **Identify gaps, parity, and differentiation.** Sort every dimension into three buckets: *we lose* (their advantage), *we're at parity* (table stakes, neutralize cheaply), *we win* (our wedge, press it). Be ruthless about the first bucket.
5. **Derive strategic implications.** Translate the map into "so what." Where you lose: is it worth closing, or do you concede and out-position? Where you win: how do you make it un-ignorable? What's the threat trajectory — where are they heading next (read their changelog and job posts)?
6. **Build the battlecard.** Compress the brief into a field-ready card the sales team can use live: their pitch, your counter, traps to set, objection handling, proof points. If sales can't skim it in 30 seconds, it won't get used.

## Output templates

### Template 1 — Competitive Brief

```
# Competitive Brief: [Us] vs [Competitor(s)]
Prepared: [date] · Author: [operator's name/role, or the persona if none given — otherwise leave blank; don't invent one] · Evidence dated as of: [date]
Research mode: [live web search / user-provided only / mixed]

## Overview
- Who they are, stage, size, momentum (funding, headcount, growth signals) — [fact/inference]
- Why they're on our radar / what triggered this brief

## Positioning
- Their stated positioning (their words): "[…]"
- Their real target buyer (our read): [segment] — [fact/inference + why]
- Our positioning by contrast: […]

## Feature comparison matrix
| Capability / dimension | Us | [Competitor] | Gap (who wins, how big) |
|---|---|---|---|
| [Core capability]   | ✅ | ⚠️ | Us — meaningful |
| [Integrations]      | ⚠️ | ✅ | Them — closeable |
| [Pricing model]     | ✅ | ❌ | Us — structural |
| [Security/compliance] | — | ✅ | Them — unknown on our side |
(✅ strong · ⚠️ partial · ❌ absent · — unknown)

## Pricing & packaging
- Their model, tiers, and headline prices [date observed] — [fact]
- Hidden costs / gotchas (overages, seat minimums, add-ons)
- How a real deal compares vs. ours — compute a concrete per-deal dollar figure at a representative seat count, both sides (e.g. "at 40 seats: $X/yr us vs. $Y/yr them, before overages"); state the seat count and any assumptions

## Strengths / Weaknesses
**Their strengths:** […]
**Their weaknesses:** […]

## Where to differentiate (press our advantage)
- [Dimension] — why it's defensible, how to make it the deciding factor

## Where to reach parity (neutralize, don't lead)
- [Dimension] — minimum bar to take it off the table, rough cost/effort

## Threats
- Where they're heading next (from changelog / job posts / funding) — [inference]
- What would hurt us most if they shipped it

## Recommended moves
1. [Action] — owner, rough timing, expected effect
2. […]
3. […]
```

### Template 2 — Sales Battlecard

```
# Battlecard: vs [Competitor]  ·  updated [date]
**Intel as-of:** [date] · **Verification:** [verified live / user-provided / unverified — re-pull before use]

**Their pitch (what reps will hear):** "[…]"

**Our counter (one breath):** "[…]"

**Landmines to set** (questions that expose their weak spots):
- "Ask them about [X]…" → they struggle because […]
- "Have them show you [Y] live…" → […]

**Objection handling**
| They'll say | We say |
|---|---|
| "[Competitor] is cheaper" | "[reframe to TCO / value…]" |
| "They have [feature]" | "[parity claim or out-position…]" |
| "[Competitor] is the market leader" | "[…]" |

**Proof points** (dated, specific, defensible):
- [Metric / customer / benchmark] — [date]
- […]
```

## Quality bar
- [ ] Every claim is **evidence-backed and dated** — no "I think they cost more."
- [ ] **Fact vs. inference** is marked throughout; guesses are labeled as guesses.
- [ ] The frame ties to a **real decision**, not a generic profile.
- [ ] At least one dimension where **the competitor genuinely wins** is named honestly.
- [ ] Marketing copy is treated as a *claim to verify*, not as truth.
- [ ] Unknowns are flagged as unknowns (—), not papered over.
- [ ] It ends with a **recommendation and owners** — not just a comparison table.

## Tips
- **Date every data point.** "Pricing as of [date]" is the difference between a brief that ages gracefully and one that gets someone fired in a deal.
- **Competitors change fast.** A brief is a snapshot, not a monument — note when it should be re-pulled, and re-verify before any high-stakes use (board deck, big deal).
- **Never trust marketing copy as truth.** "Enterprise-grade," "AI-powered," "real-time" are claims to test, not facts to repeat. Prefer docs, changelogs, pricing pages, and actual reviews over the homepage.
- **Reviews are gold, with a grain of salt.** G2/Capterra/Reddit reveal real weaknesses, but skew toward churned or angry users — weight by recency and volume.
- **Read the changelog and the job board.** What they ship and who they hire tells you where they're going better than any press release.
- **Resist symmetry.** You don't owe each competitor equal coverage. Go deep on the one that actually threatens the deal or the roadmap.
- **One competitor, one teardown; many competitors, one landscape.** Don't write five shallow profiles when the decision needs one sharp comparison.
