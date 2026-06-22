---
name: market-sizing
description: Sizes a market with both top-down and bottom-up methods using the TAM/SAM/SOM framework, states every assumption, reconciles the two estimates, and sanity-checks the result. Use when you need to size an opportunity, fill the market section of a PRD or business case, justify a bet to leadership, or pressure-test a number someone handed you ("how big is this really?", "what's the TAM?", "is this market worth entering?").
---

# Market Sizing

A market size is only as good as the assumptions under it. This skill sizes a market two independent ways — **top-down** (start from a published total, narrow down) and **bottom-up** (build up from units × price) — across the **TAM / SAM / SOM** layers, then reconciles them. The goal is a number that survives a skeptical exec or investor, not a single confident-sounding hand-wave.

**Grounded in:** *Disciplined Entrepreneurship* — Bill Aulet: bottom-up TAM from a defined beachhead, cross-checked top-down.
**Go deeper (The Product Channel):** [The Product Channel](https://sidsaladi.substack.com)

The discipline is this: every figure is traceable to a stated assumption, and the two methods are forced to meet. When they diverge wildly, that gap is the finding — it tells you which assumption is doing the heavy lifting.

## When to use this
- Filling the market-opportunity section of a PRD, business case, or strategy doc.
- Justifying (or killing) a new product, segment, or geo-expansion bet to leadership.
- Prepping board, investor, or fundraising materials that need a defensible TAM/SAM/SOM.
- Pressure-testing a number a founder, analyst, or vendor handed you that smells inflated.
- Comparing two opportunities to decide which is worth the next quarter of build time.

## Before you start (gather these)
- **The offering and the buyer** — what exactly is sold, and who pays. "AI note-taking for sales reps" sizes very differently from "meeting software."
- **The geography and segment** — global vs. a region; SMB vs. mid-market vs. enterprise. Scope creep here is the #1 source of fantasy TAMs.
- **A price anchor** — your actual or intended price (ACV, monthly seat, transaction take-rate). Bottom-up is impossible without it. **If you're sizing a new feature, tier, or add-on, capture both the current price and the intended/new price** — the delta between them is usually the load-bearing input (it sets the incremental ARR), so size the uplift explicitly, not just the headline market.
- **At least one population anchor** — a count of potential buyers or units (e.g. "~400K SaaS companies in the US", "~2M sales reps"), or a published market-size figure to narrow from.
- **A realistic share or penetration assumption** — what slice of SAM you can plausibly win in 3–5 years.

If two or more of these are missing or vague, **ask 2–4 sharp clarifying questions before sizing** — e.g. "Global or a specific region?", "What's your price point and unit (per seat, per transaction)?", "Who's the exact buyer?", "What time horizon for SOM?". If the inputs are already provided, proceed and state every assumption inline. If web search is available, you may pull population counts and published market figures live and cite them with a date; otherwise work from pasted/given data and label estimates as assumptions.

## Process
1. **Lock the scope in one sentence.** Write the market definition as "[offering] for [buyer] in [geography/segment]." Everything downstream inherits this. A loose definition produces a loose number — pin it before touching math.
2. **Build TOP-DOWN.** Start from a credible published total (analyst report, industry revenue, census of buyers). The first row is always **TAM = the published total / un-narrowed seats × price, before any geo or segment cut** — so the broadest layer is explicit and traceable. Then narrow with explicit filters: geography → segment → addressable subset → realistically winnable. Each cut is a labeled assumption with a number: `Total $X → ×[filter %] → $Y`. Name the source and its date; if it's an estimate, say so.
3. **Build BOTTOM-UP independently.** Don't peek at the top-down number. State TAM first as **all potential buyers/units × price (no penetration applied)**, then apply penetration to reach SAM. Compute `# of potential buyers × adoption/penetration × annual price (ACV)`. For transactional markets use `volume × frequency × price × take-rate`. The **penetration term here = the share of the population that fits or could buy** (product/segment fit), NOT the share you'll win — win-share belongs only in the SOM step. Show the formula with every variable filled and sourced.
4. **Assign the three layers.** **TAM** = total demand if everyone who could buy did (the whole defined market). **SAM** = the slice you can actually serve given your product, channel, geo, and segment focus. **SOM** = what you can realistically capture in your stated horizon (3–5 yrs) given competition, sales capacity, and GTM — usually a single-digit % of SAM. **State the SOM unit explicitly:** ARR for a subscription business, GMV or transactional revenue for a marketplace/transactional business — and keep the same unit consistent across all three layers. Compute each from *both* methods where possible.
5. **Reconcile the two numbers — and check the convergence is real.** Put top-down and bottom-up side by side. **A tight gap only means something if the two methods rest on genuinely different bases.** If your top-down is just the same buyer count × price dressed up as a published total, the "convergence" is circular and proves nothing. Anchor top-down on an independent basis — sum of competitor ARR, analyst category-spend, industry revenue — separate from the units × price you used bottom-up. **If no independent basis exists, say so: declare the convergence non-independent rather than reporting a misleadingly tight gap.** Then: if they're within ~2× and independent, converge on a range and move on. If they diverge more, **find the assumption driving the gap** (usually penetration %, price, or buyer count) and state which method you trust more and why. Do not average two numbers you don't believe.
6. **Sanity-check against reality.** Test the result against a known anchor: implied market share vs. the current leader's revenue, SOM vs. your realistic sales capacity (can your funnel even close that many?), penetration vs. comparable adoption curves. **Run an implied-CAGR check:** the growth rate required to get from current revenue to the SOM over the stated horizon — is it within plausible category-ramp bounds, or does it imply a growth rate no comparable company has sustained? If SOM implies you'd outsell the incumbent in year two, or grow faster than any analog ever has, the number is wrong — go back.
7. **Flag the load-bearing assumption.** Name the single input the whole estimate hinges on, and show how the number moves if it's off by half or double. This is what a sharp reviewer will attack — get there first.

## Output template

```markdown
# Market Sizing: [Offering] for [Buyer] in [Geography/Segment]
Prepared: [date] · Author: [name/role or leave blank — don't invent] · Data mode: [live web / provided only / mixed]

## Market definition
> [Offering] for [buyer] in [geography/segment], over a [3–5 yr] horizon.

## Headline
| Layer | Top-down | Bottom-up | Converged figure |
|-------|----------|-----------|------------------|
| **TAM** (total demand) | $[X] | $[X] | **$[X]** |
| **SAM** (serviceable) | $[X] | $[X] | **$[X]** |
| **SOM** (obtainable, [N] yrs) | $[X] | $[X] | **$[X]** |

One-line takeaway: [e.g. "A $[SOM] obtainable market in [N] years — worth pursuing / too thin to justify the build, because…"]

## Top-down build
| Step | Figure | Assumption / filter | Source · date | Fact / est. |
|------|--------|---------------------|---------------|-------------|
| Published total | $[X] | [the broad market] | [source] · [date] | [fact/est] |
| = **TAM** (un-narrowed total, before geo/segment) | **$[X]** | [whole defined market] | [source] · [date] | [fact/est] |
| × Geography | $[X] | [%] in [region] | [source] | [est] |
| × Segment | $[X] | [%] are [segment] | [source] | [est] |
| × Addressable | $[X] | [%] fit our product | [reasoning] | [est] |
| = **SAM** | **$[X]** | | | |

## Bottom-up build
**Formula (SAM):** `[# buyers] × [fit/could-buy %] × [annual price] = SAM`
(transactional: `[volume] × [frequency] × [price] × [take-rate]`)
TAM = `[all potential buyers] × [annual price]` with NO penetration applied. The penetration term above is **share of the population that fits / could buy** — win-share is applied later, only in the SOM step.

| Variable | Value | Where it comes from | Fact / est. |
|----------|-------|---------------------|-------------|
| Potential buyers (all) | [N] | [source · date] | [fact/est] |
| Annual price (ACV) | $[X] | [your pricing] | [fact] |
| **= TAM** (no penetration) | **$[X]** | all buyers × price | |
| × Penetration (fit / could-buy %) | [%] | [comparable / assumption] | [est] |
| **= SAM** | **$[X]** | | |

## Reconciliation
- Top-down SAM: $[X] · Bottom-up SAM: $[X] · Gap: [N]×
- Independent basis? [Top-down anchored on [competitor ARR sum / analyst category spend / industry revenue], separate from the units × price used bottom-up. / NON-INDEPENDENT — top-down reuses the same buyer count × price, so this convergence is circular and proves nothing.]
- [Within 2× AND independent → converge on $[range]. / Diverge → the gap is driven by [assumption]; trusting [method] because [reason].]
- Converged SAM: **$[X]** (range $[low]–$[high])

## SOM (obtainable)
- **Unit:** [ARR — subscription / GMV (or transactional revenue) — transactional]
- SAM $[X] × [target win-share %] over [N] yrs = **$[SOM]**
- Justification: [competitive density, sales capacity, GTM motion, comparable ramp]

## Sanity checks
- [ ] Implied market share vs. leader ([leader] does ~$[X]): [pass/fail + note]
- [ ] Implied CAGR — current revenue $[X] → SOM $[X] over [N] yrs requires ~[X]%/yr: [within plausible category-ramp bounds? pass/fail vs. analog]
- [ ] SOM vs. our realistic sales capacity ([N] deals/yr × $[ACV]): [pass/fail]
- [ ] Penetration vs. comparable adoption curve: [pass/fail]
- [ ] Scope discipline — does every number still match the one-sentence definition? [yes/no]

## Load-bearing assumption
- **[The single input the estimate hinges on]** = [value].
- If it's half: SOM ≈ $[X]. If double: SOM ≈ $[X].
- Confidence: [high/med/low] · How to firm it up: [what data would replace the guess]

## What would change this number
- [The 1–2 pieces of real data — a pricing test, a buyer count, a published report — that would move this from estimate to defensible.]
```

## Avoid (anti-patterns)
- **The "1% of a huge number" trap.** "It's a $50B market, we just need 1%" is not sizing — it's a wish. Always build bottom-up; if you can't reach the number with real units × price, it isn't real.
- **Scope drift between layers.** Defining TAM as "global meetings software" then pricing SOM off "US sales teams." Every layer must trace to the same one-sentence definition.
- **Skipping reconciliation.** Reporting only the method that gives the bigger number, or quietly averaging two estimates that disagree by 10×. The divergence is the insight — surface it.
- **Confident decimals on guesses.** "$847.3M SAM" implies precision you don't have. Use rounded figures and ranges; precision should match the quality of the inputs.
- **Ignoring the time horizon on SOM.** A SOM with no "by when" is meaningless — 5% share in year 1 and year 5 are wildly different claims.

## Tips
- **Bottom-up is the truth-teller; top-down is the credibility check.** When they disagree, trust the bottom-up build you can defend line by line — but make the top-down agree before you ship.
- **Size the slice you'll actually attack first, not the dream.** A precise, winnable $20M SAM beats a vague $5B TAM in any real prioritization conversation.
- **Pre-compute the half/double swing on your weakest assumption.** Whoever's reviewing will poke the softest number — show you already stress-tested it and you control the conversation.
- **Anchor SOM to sales capacity, not ambition.** If your funnel can close 200 deals a year at $30K ACV, your year-1 SOM ceiling is $6M no matter how big the TAM is.
