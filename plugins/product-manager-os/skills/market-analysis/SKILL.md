---
name: market-analysis
description: Runs a structured environmental scan using SWOT, PESTEL, Porter's Five Forces, and Ansoff growth options, then synthesizes them into 2-3 strategic implications. Use when you need to assess a market before entering it, pressure-test a strategy, prep a board or planning deck, answer "what are the forces shaping this market" or "where should we grow," or turn scattered market notes into a decision.
---

# Market Analysis

A market analysis applies four classic frameworks — SWOT, PESTEL, Porter's Five Forces, and Ansoff — as one connected scan, not four wall posters. The output is not four diagrams; it's 2-3 strategic implications that the four lenses agree on. If your SWOT, your PESTEL, your forces map, and your growth options never reference each other, you've done four exercises and zero strategy.

The discipline here is convergence. PESTEL surfaces the macro shifts. Five Forces explains why the market is (or isn't) attractive. SWOT positions *you* inside that market. Ansoff turns it into where-to-grow choices. The synthesis asks: given all four, what 2-3 things must we believe and do?

**Grounded in:** *Competitive Strategy* — Michael Porter: Porter's Five Forces, synthesized into strategic implications.
**Go deeper (The Product Channel):** [The Ultimate Guide to Product Strategy](https://sidsaladi.substack.com/p/the-ultimate-guide-to-crafting-a)

## When to use this
- Assessing a new market, segment, or geography before committing resources to enter it.
- Pressure-testing an existing strategy against macro shifts (regulation, AI, rates, supply chains).
- Prepping a strategy, board, or annual-planning narrative that needs an external-environment section.
- Deciding *where* to grow next — deeper in the current market, adjacent segments, new products, or diversification.
- Turning a pile of market notes, analyst reports, and competitor intel into a structured point of view.

## Before you start (gather these)
- **The market/decision in scope** — which market, and what decision is this feeding (enter / exit / expand / defend)? "Analyze the market" with no decision behind it sprawls into a textbook.
- **Your position in it** — your product, your buyer, your current share/traction. SWOT and Ansoff are relative to *you*; without this the analysis floats free.
- **Macro and competitive inputs** — known regulatory/tech/economic shifts, the main rivals, substitutes, and who holds pricing power (suppliers, buyers, channels).
- **Time horizon** — are we reasoning about now, or 3 years out? PESTEL trends and Ansoff bets depend on it.

If two or more of these are missing or vague, **ASK 2-4 sharp clarifying questions before analyzing** — e.g. "Which market and what decision is this feeding?", "What's your current position/share?", "What horizon — now or 3 years out?", "Any known regulatory or tech shifts already on your radar?" If the inputs are already provided, proceed and **state your assumptions inline** (e.g. "Assuming mid-market B2B SaaS, 3-year horizon, US-first").

**Non-interactive fallback:** if you cannot ask — a batch, one-shot, eval, or automated context where there's no user to answer — do **not** block or stall on missing inputs. State the gaps as explicit assumptions inline (in the `Assumptions:` header and at the relevant lens) and proceed to a full analysis. A clearly-flagged best-effort analysis beats a refusal to start.

## Process
1. **Frame the decision.** Write the one sentence this analysis exists to answer (e.g. "Should we expand from SMB into mid-market?"). Pin the market boundary and horizon. Every lens below serves this sentence.
2. **PESTEL — scan the macro field.** Walk Political, Economic, Social, Technological, Environmental, Legal. For each, note only forces that *materially move this market* — skip generic trends. If a factor genuinely exerts no material force on this market, write **"No material force"** rather than inventing a weak one to fill the row. Tag each real force as **tailwind**, **headwind**, or **watch**, and mark whether it's **fact** (a passed law, a published rate) or **inference** (your read on direction).
3. **Porter's Five Forces — rate market attractiveness.** Score each force **Low / Medium / High** (force *intensity*, where High = worse for incumbents): competitive rivalry, threat of new entrants, threat of substitutes, buyer power, supplier power. One line of *why* per force, and — same discipline as PESTEL — mark the verdict driver as **fact** (a measured concentration ratio, a public switching cost) or **inference** (your read). Conclude with a verdict: is this market structurally attractive, contested, or a trap?
4. **SWOT — position yourself inside it.** Strengths and Weaknesses are internal and relative to rivals; Opportunities and Threats must trace back to specific PESTEL forces and Porter findings (don't restate generic items). Carry the **fact / inference** tag through here too: a Strength you can measure (NPS, share, a shipped capability) is a fact; a believed Opportunity is an inference — say which, so the crossed SWOT doesn't build moves on hunches dressed as facts. Be honest about weaknesses — a flattering SWOT is useless.
5. **Cross the SWOT (this is where most analyses quit too early).** Build the four pairings: S×O (where to attack), W×O (what to fix to capture upside), S×T (how to defend), W×T (existential risks to de-risk or avoid). These pairings *are* the strategic moves.
6. **Ansoff — frame the growth options.** Lay out the four quadrants for *this* company: Market Penetration (more share, same product/market), Market Development (new segments/geos), Product Development (new products, same market), Diversification (new product + new market). Note the bet, the risk level, and what would have to be true for each. **A single move can sit in one quadrant by mechanism and another by intent** — e.g. launching a feature to defend an existing segment is Product Development by mechanism but Market Penetration by intent. When that happens, **name both** (mechanism quadrant + intent quadrant) rather than forcing one label; the risk profile follows the mechanism, the strategic story follows the intent.
7. **Synthesize into 2-3 implications.** This is the deliverable. Each implication must be supported by **at least two of the four frameworks** (e.g. "PESTEL tailwind + S×O pairing → press product development into segment X"). If an implication rests on only one lens, it's an observation, not a strategy. End each with a concrete next move and what would falsify it.

## Worked example (one implication, end to end)

A condensed trace showing how the lenses connect into a single move — your real output carries 2-3 of these:

- **Decision:** "Should a mid-market B2B SaaS expand from SMB into mid-market over 18 months?"
- **PESTEL (Technological):** Buyers now expect SOC 2 + SSO as table stakes — *tailwind*, *fact* (it's in their RFPs). Environmental: *No material force*.
- **Five Forces:** Buyer power *Medium* (fragmented mid-market buyers, no single whale) — *inference*; verdict: **Contested but enterable**.
- **SWOT S×O pairing:** Strength = a mature SSO/audit-log stack we already ship (*fact*) × Opportunity = the compliance-as-table-stakes tailwind → we can clear the mid-market security bar that SMB-only rivals can't.
- **Ansoff:** This is **Market Development by mechanism** (new segment, same product) and **Market Penetration by intent** (defending our base from upmarket churn) — name both.
- **→ Implication:** "Lead mid-market entry with the compliance story." **Next move:** package SSO + audit logs as a 'Mid-Market Ready' tier; pilot with 5 logos in Q3. **Backed by:** PESTEL Technological tailwind + S×O + Ansoff Market Development. **Falsified if:** mid-market pilots cite price, not compliance, as the blocker.

## Output template

```markdown
# Market Analysis: [Market] — [Decision in scope]
Prepared: [date] · For: [audience/role] · Horizon: [now / 3yr] · Author: [name or role; leave blank if none — don't invent]
Inputs: [live research / user-provided / mixed] · Assumptions: [state any made inline]

## Decision this answers
> [The one sentence. e.g. "Should we expand from SMB into mid-market over the next 18 months?"]

## 1. PESTEL — macro field
| Factor | Force (specific to this market) | Tailwind / Headwind / Watch | Fact / Inference |
|---|---|---|---|
| Political | [e.g. procurement-policy shift] | [Tailwind] | [Fact] |
| Economic | [e.g. rate environment, budget pressure] | [Headwind] | [Inference] |
| Social | [e.g. buyer behavior / norms shift] | [Watch] | [Inference] |
| Technological | [e.g. AI commoditizes feature X] | [Headwind] | [Fact] |
| Environmental | [e.g. ESG reporting mandate] | [Watch] | [Fact] |
| Legal | [e.g. data-residency regulation] | [Headwind] | [Fact] |

**Net macro read:** [2-3 sentences — which 1-2 forces dominate the picture and why.]

## 2. Porter's Five Forces — market attractiveness
| Force | Intensity (Low/Med/High) | Why |
|---|---|---|
| Competitive rivalry | [High] | [fragmented, price wars on…] |
| Threat of new entrants | [Med] | [moderate capital, low switching costs] |
| Threat of substitutes | [High] | [DIY / adjacent tool / status quo] |
| Buyer power | [High] | [concentrated buyers, easy comparison] |
| Supplier power | [Low] | [commoditized inputs] |

**Verdict:** [Attractive / Contested / Trap] — [one-line rationale: where the structural profit pools are, if any.]

## 3. SWOT — our position in this market
| Strengths (internal) | Weaknesses (internal) |
|---|---|
| [Specific, relative to rivals] | [Honest, named] |
| [...] | [...] |

| Opportunities (→ ties to PESTEL/Porter) | Threats (→ ties to PESTEL/Porter) |
|---|---|
| [O1 — from Technological tailwind] | [T1 — from buyer power + substitute] |
| [...] | [...] |

### Crossed SWOT (the moves)
- **S×O (attack):** [Use strength __ to capture opportunity __.]
- **W×O (fix-to-win):** [Weakness __ blocks opportunity __; close it by __.]
- **S×T (defend):** [Use strength __ to blunt threat __.]
- **W×T (de-risk/avoid):** [Weakness __ + threat __ = existential; mitigate or stay out.]

## 4. Ansoff — growth options
| Quadrant | The bet | Risk | What must be true |
|---|---|---|---|
| Market Penetration | [more share, same product/market] | [Low] | [room to grow share; CAC holds] |
| Market Development | [new segment/geo] | [Med] | [segment __ has the same job-to-be-done] |
| Product Development | [new product, same buyers] | [Med] | [we can build __; buyers want it from us] |
| Diversification | [new product + new market] | [High] | [a capability bridges both] |

**Recommended Ansoff focus:** [which quadrant(s), and why — tie back to the forces above.]

## 5. Strategic implications (the deliverable)
> 2-3 implications, each backed by ≥2 frameworks above.

1. **[Implication headline.]**
   - Backed by: [e.g. PESTEL Technological tailwind + SWOT S×O + Ansoff Product Development].
   - So what / next move: [concrete action + owner + rough timeframe].
   - Falsified if: [the signal that would kill this thesis].

2. **[Implication headline.]**
   - Backed by: [Porter verdict + W×T pairing].
   - So what / next move: [...].
   - Falsified if: [...].

3. **[Optional third.]**
   - Backed by: [...].
   - So what / next move: [...].
   - Falsified if: [...].

## Open questions / data to confirm
- [Gap 1 — what we'd want to verify before betting on this.]
- [Gap 2 — ...]
```

## Avoid (anti-patterns)
- **Four disconnected diagrams.** If the SWOT, PESTEL, forces map, and Ansoff grid never reference each other, you failed the assignment — the synthesis is the product, not the frameworks.
- **Generic PESTEL.** "AI is growing," "the economy is uncertain" — true everywhere, useful nowhere. Every factor must be specific enough that it would read differently for a different market.
- **Flattering SWOT.** Listing weaknesses you've already solved and threats you don't fear. Name the real ones; an honest W×T is the most valuable cell in the whole analysis.
- **Skipping the crossed SWOT.** A plain four-box SWOT with no S×O/W×T pairings is a list, not a strategy. The crossings are where moves come from.
- **Recommending all four Ansoff quadrants.** "We'll penetrate, develop, build new products, *and* diversify" is not a strategy — it's an absence of one. Pick.

## Tips
- **Lead with the decision, end with the implications; treat the four frameworks as the middle.** A reader should be able to read only the top and bottom and act.
- **Tag fact vs. inference everywhere, especially in PESTEL.** "A law passed" and "I think regulation is coming" carry very different weight in a board room.
- **Score Five Forces by *intensity*, not goodness.** High rivalry is bad for you; say "High" and let the verdict line interpret it. Don't quietly flip the scale.
- **Force convergence in the synthesis.** Before writing each implication, literally check which frameworks support it. If only one does, demote it to an open question — you've found a hunch, not a conclusion.
