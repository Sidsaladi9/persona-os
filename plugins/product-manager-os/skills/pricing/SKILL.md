---
name: pricing
description: Designs pricing and packaging using value-metric selection, Van Westendorp willingness-to-pay analysis, and good-better-best tiering. Picks the metric you charge on, chooses the model (per-seat, usage, tiered), sets three tiers with anchoring, and stress-tests for money left on the table. Use when you say "how should we price this," "what should our tiers be," "are we underpriced," "per-seat vs usage," or "package our plans."
---

# Pricing

Good pricing is a packaging decision before it's a number. This skill picks the **value metric** (what you charge on), chooses a **model**, sets **good-better-best** tiers, and pressure-tests willingness-to-pay with **Van Westendorp** before you commit to a price.

**Grounded in:** *Monetizing Innovation* — Madhavan Ramanujam: design around willingness-to-pay and the value metric before building.
**Go deeper (The Product Channel):** [The Art of Pricing](https://sidsaladi.substack.com/p/week-41-the-art-of-pricing-11-essential)

## When to use this
- Launching a new product or paid tier and need to set prices from scratch.
- Suspect you're underpriced or leaving money on the table at the top end.
- Deciding between per-seat, usage-based, or flat tiered pricing.
- Repackaging existing plans because customers cluster on one tier or churn at upgrade.
- Building a pricing page and need three tiers with a clear anchor and a "most popular" pick.

## Before you start (gather these)
- **Value metric candidates** — what scales with the value the customer gets (seats, projects, API calls, GB, transactions, contacts).
- **Cost-to-serve** per unit of that metric (to set a price floor and protect margin on usage plans).
- **Willingness-to-pay signal** — at minimum a few customer quotes or a Van Westendorp survey (the four price questions below); failing that, competitor price points.
- **Segments** — who buys (solo / team / enterprise) and the job each segment hires the product for.
- **Current numbers if repricing** — plan distribution, ARPA, upgrade/churn points.

If 2+ of these are missing or vague, ASK 2-4 sharp questions before proceeding, e.g.: "What single thing grows as a customer gets more value from this?" / "Do you have any WTP data, or should I anchor off competitors?" / "Which segments are you packaging for?" / "What's your cost to serve one unit?" If the data is provided, proceed and state assumptions inline (e.g., "Assuming cost-to-serve is negligible for seats; flag if not").

## Process
1. **Pick the value metric.** Score 3-4 candidates against: does it grow as the customer gets more value? is it easy to understand and predict? hard to game? cheap to meter? Choose the one that aligns *your* revenue with *their* success. A good metric makes price feel fair because the customer only pays more when they're getting more.
2. **Choose the model.** Per-seat when value scales with people (collaboration tools). Usage when value scales with consumption and is spiky (infra, API). Flat tiered when value is bundled and you want predictable revenue + simple buying. Hybrid (platform fee + usage) when you need a floor plus upside. Default to tiered unless usage clearly tracks value better.

   **If per-seat, choose the billable unit explicitly: provisioned seats (every seat purchased) vs. active seats (only seats that logged in / used the product in the period).** This choice materially changes churn: provisioned billing maximizes near-term revenue but inflates the bill with unused seats, which surfaces at renewal as "we're paying for 200 and using 60" and drives downgrades or churn. Active-seat billing lowers headline ARPA but ties the invoice to realized value, so renewals defend themselves. State which unit you're billing and why.
3. **Estimate willingness-to-pay with Van Westendorp — per segment.** Ask (survey or proxy from interviews) the four questions: at what price is it *too cheap* (quality doubt), *a bargain*, *getting expensive*, *too expensive*. Plot the cumulative curves and read off the canonical intersections:
   - **Point of Marginal Cheapness (PMC)** = "too cheap" × "expensive" — the lower bound of the acceptable range.
   - **Point of Marginal Expensiveness (PME)** = "bargain" × "too expensive" — the upper bound.
   - **Acceptable range** runs PMC → PME.
   - **Optimal Price Point (OPP)** = "too cheap" × "too expensive" — the price with the fewest people rejecting on either side.
   - **Indifference Price Point (IPP)** = "bargain" × "expensive" — where as many call it cheap as call it expensive (often the median/competitor anchor).

   Run the four questions **separately for each segment** (solo / team / enterprise) — willingness-to-pay diverges sharply across them, and one blended curve hides the spread that justifies your tiers. Use the range, not a single number.
4. **Set good-better-best tiers.** Build three tiers around the WTP range. **Good** = lands the core job for the price-sensitive segment (the anchor's floor). **Better** = the target plan most buyers should pick; load it with the features the median segment values and mark it "most popular." **Best** = a deliberately premium anchor that makes Better look reasonable and captures high-WTP buyers. Differentiate tiers by the value metric + a small number of meaningful features, not a long checklist.
5. **Anchor intentionally.** Order tiers high-to-low or put the anchor (Best, or an Enterprise "Contact us") at the top so Better reads as the sensible middle. The decoy effect is real: a slightly-worse, similarly-priced option pushes buyers to your target tier.
6. **Set the gaps.** Price the jump between tiers so upgrading is an easy yes. The common ~2-3x rule of thumb refers to **total plan price** (Better's monthly bill ≈ 2-3x Good's), *not* per-unit/per-seat price — per-unit rates usually *fall* as tiers rise (volume discount), so don't apply the multiple to the unit rate. It's a defensible starting ratio, not a rule. If everyone clusters on one tier, your fences (the things that force an upgrade) are in the wrong place.
7. **Stress-test for money left on the table.** Check: is Best capped (or "Contact us") so you don't cap your biggest accounts? Is the cheapest tier capturing low-WTP buyers without cannibalizing the middle? Does any single tier hold >70% of customers (sign of bad fences)? Is the value metric something a growing customer will naturally consume more of?
8. **Define expansion.** Name the moment a happy customer outgrows their tier (more seats, more usage, a gated feature they now need). Expansion revenue beats acquisition; the metric should make it automatic.

## Output template

```markdown
# Pricing & Packaging: [Product]

## 1. Value Metric
**Chosen metric:** [e.g., active projects]
**Why:** [grows with value, predictable, hard to game, cheap to meter]

| Candidate metric | Scales w/ value? | Easy to predict? | Hard to game? | Cheap to meter? | Verdict |
|---|---|---|---|---|---|
| [seats]    | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [keep/drop] |
| [projects] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [chosen]    |
| [API calls]| [Y/N] | [Y/N] | [Y/N] | [Y/N] | [drop]      |

## 2. Pricing Model
**Model:** [tiered / per-seat / usage / hybrid]
**Rationale:** [why this fits how value is delivered]
**Price floor:** [cost-to-serve per unit] → never price below [floor]

## 3. Willingness-to-Pay (Van Westendorp — per segment)

Run the four questions separately per segment (median responses):

| Segment | Too cheap | Bargain | Getting expensive | Too expensive |
|---|---|---|---|---|
| Solo | [$X] | [$X] | [$X] | [$X] |
| Team | [$X] | [$X] | [$X] | [$X] |
| Enterprise | [$X] | [$X] | [$X] | [$X] |

Derived points per segment (canonical intersections):

| Segment | PMC (too cheap × expensive) | PME (bargain × too expensive) | Acceptable range (PMC→PME) | OPP (too cheap × too expensive) | IPP (bargain × expensive) |
|---|---|---|---|---|---|
| Solo | [$X] | [$X] | [$low]–[$high] | [$X] | [$X] |
| Team | [$X] | [$X] | [$low]–[$high] | [$X] | [$X] |
| Enterprise | [$X] | [$X] | [$low]–[$high] | [$X] | [$X] |

- **Source:** [n responses per segment / interview proxy / competitor anchor — state confidence]
- **Note:** never blend segments into one curve — the spread across segments is what justifies the tier prices below.

## 4. Good–Better–Best Tiers

| | [Good] | [Better] ★ Most popular | [Best] |
|---|---|---|---|
| **Price** | [$X/mo] | [$Y/mo] | [$Z/mo or "Contact us"] |
| **Value metric** | [up to N units] | [up to M units] | [unlimited / custom] |
| **For** | [segment] | [segment] | [segment] |
| **Key features** | [core job] | [core + 2-3 high-value] | [everything + premium] |
| **Upgrade trigger** | [hits N units / needs X] | [needs SSO / scale] | — |

**Anchor:** [Best / Enterprise] is positioned to make [Better] the obvious choice.
**Target tier:** [Better] — expect [~%] of buyers here.
**Tier gaps:** [Good→Better ~Nx], [Better→Best ~Nx] — *(total plan price, not per-unit rate)*.

### 4b. Usage / Hybrid variant (use instead of the table above if model is usage or hybrid)

| | [Good] | [Better] ★ Most popular | [Best] |
|---|---|---|---|
| **Platform fee** | [$X/mo or $0] | [$Y/mo] | [$Z/mo or "Contact us"] |
| **Included units** | [N units/mo] | [M units/mo] | [custom commit] |
| **Overage rate** | [$/unit above N] | [$/unit above M, lower] | [negotiated $/unit] |
| **Metered on** | [value metric] | [value metric] | [value metric] |
| **Billing basis** | [active not provisioned, if seats] | [active not provisioned] | [committed-use / true-up] |
| **For** | [segment] | [segment] | [segment] |
| **Upgrade trigger** | [consistently over N units] | [needs higher commit / lower rate] | — |

- **Per-unit rate falls as tiers rise** (volume discount) — keep every unit rate ≥ cost-to-serve floor.
- **Floor:** platform fee guarantees minimum revenue; overage captures upside.
- **Metered billing:** if pure pay-as-you-go (no platform fee), set included units to 0 and lead with the per-unit rate; protect margin with the floor on every unit.

## 5. Money-Left-on-the-Table Check
- [ ] Top tier uncapped or "Contact us" (don't cap biggest accounts)
- [ ] No single tier holds >70% of customers (fences are working)
- [ ] Cheapest tier captures low-WTP without cannibalizing [Better]
- [ ] Best tier captures high-WTP buyers (someone should buy it)
- [ ] Price ≥ floor on every tier

## 6. Expansion Path
**Outgrow moment:** [customer crosses N units / needs gated feature]
**Mechanic:** [auto-prompt upgrade / overage / seat add]
**Expected expansion:** [net revenue retention target / direction]

## 7. Open Questions & Next Test
- [biggest assumption to validate]
- [test: e.g., A/B the Better price, or run Van Westendorp on n=50]
```

## Avoid (anti-patterns)
- **Cost-plus pricing.** Marking up your costs ignores what the value is worth — it caps your upside and signals low value. Price to WTP; use cost only as a floor.
- **Charging on a metric that doesn't track value** (e.g., per-seat for a tool one admin runs for the whole org). The customer feels nickel-and-dimed and games it.
- **A single price from Van Westendorp.** It gives a *range*; pick within it based on positioning, don't treat the OPP as gospel.
- **Feature-checklist tiers.** Twenty checkmarks per column hide the actual fence. Differentiate on the value metric plus 2-3 features that genuinely matter.
- **Capping your top tier.** A hard-numbered "Enterprise: $X" leaves your biggest, highest-WTP accounts paying less than they would. Use "Contact us."

## Tips
- The **middle tier should be your hero.** Design Good and Best to sell Better — Good is a little too limited, Best is a little too much, Better is just right.
- **Round numbers signal premium; charm prices signal value.** $99 reads "deal," $100 reads "professional." Match the price ending to the segment.
- **Annual upfront beats monthly for cash and retention.** Offer ~2 months free on annual; it pulls forward cash and cuts churn.
- When repricing, **grandfather existing customers** or migrate them gently — a surprise price hike on loyal users costs more in goodwill and churn than it gains in ARPA.
