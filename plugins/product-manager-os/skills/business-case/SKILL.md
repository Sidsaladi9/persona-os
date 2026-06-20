---
name: business-case
description: Builds an executive business case / ROI model that justifies funding one feature or investment — cost of inaction, options (incl. do-nothing), an expected-value benefit model (reach × adoption × value-per-unit), build+run cost, payback and ROI, sensitivity, and a fund/kill ask. Use when you say "build a business case", "is this worth building", "what's the ROI", "justify this investment", "cost-benefit", "make the case to fund this", or "should we build X or not". Justifies ONE bet against its own cost — it does not rank a backlog (that's prioritize), set a price (that's pricing), or choose direction (that's product-strategy).
---

# Business Case

Turns a proposed investment into the one-page artifact you bring to a funding decision: what it costs to do nothing, the options on the table, an expected-value benefit model, payback and ROI over a stated horizon, the input the verdict hinges on, and a clear fund-or-kill ask. Built for the PM who has to defend a bet to a skeptical exec or finance partner — the model is the argument, not a vibe.

This is the **investment-justification** skill, and it's deliberately narrow. It justifies **one bet against its own cost and the do-nothing line.** It does **not** rank a backlog (that's `prioritize`), set a price (that's `pricing`), or choose product direction (that's `product-strategy`). If you're sequencing five features, you want `prioritize`; if you're deciding whether *this one* clears its cost, you're in the right place.

**Grounded in:** classic cost-benefit analysis (expected value, payback, ROI) + *Monetizing Innovation* — Ramanujam & Tacke: size the value before you authorize the build. (We borrow only the "quantify value first" discipline, not the willingness-to-pay machinery — that's `pricing`.)
**Go deeper (The Product Channel):** [The Product Channel](https://sidsaladi.substack.com)

## When to use this
- Leadership asks "is this worth building?" and you need a defensible yes/no with numbers, not a pitch.
- You're going into planning or a funding review and must justify why this bet earns headcount/budget.
- A big or hard-to-reverse investment (a new product line, a platform rebuild, a major hire) needs a written case before commit.
- Finance or an exec sponsor wants payback, ROI, and the cost of *not* doing it — the do-nothing baseline.
- You suspect a loud-favorite feature won't actually clear its cost, and you want the model to say so before the team burns a quarter on it.

## Before you start (gather these)
- **The investment** — the one feature/bet being justified, in a sentence. One bet per case.
- **The problem & who it hurts** — what's broken today and the evidence it's real (tickets, churn reasons, lost deals, a metric).
- **Reach** — how many users/accounts/events the change can touch per period (a real count, not "lots").
- **Value per unit** — what one successful outcome is worth: incremental ARR, retained revenue, hours saved × loaded cost, support deflection. The conversion from "it worked" to dollars. **Be explicit whether this is per-user or per-account** — mixing the two is the most common silent 10x error in these models.
- **Cost to build + run** — eng/design person-months × loaded cost, plus ongoing infra/support/maintenance per period.
- **The decision context** — who funds it, the budget/horizon, and what it's competing against.

If 2+ of these are missing or vague, **ASK 2-4 sharp questions before modeling** — e.g., "How many accounts does this realistically touch per quarter?", "What's one successful outcome worth in dollars — new revenue, retained revenue, or cost saved, and is that per user or per account?", "Roughly how many eng person-months?", "What does doing nothing cost us if we skip this?" If you already hold the inputs, **proceed and state every estimate as a labeled assumption** so finance can challenge the number, not the narrative.

## Process
1. **State the bet and the ask up front.** One sentence on the investment, one on what you're asking for (fund $X / N person-months, or kill). Lead with the answer; the model is the justification, not the suspense.
2. **Quantify the cost of inaction (the do-nothing baseline).** Every option is measured against *not acting*. Put a number on the status quo: revenue lost to churn, deals slipping, support load, opportunity cost. If doing nothing is genuinely fine, the honest case may be to **not** build — say so.
3. **List the options, including do-nothing.** A business case with one option is an ultimatum. Show 2-4 real alternatives (build full, build a thin v1, buy/partner, do nothing) so the decision is a choice, not a rubber stamp.
4. **Build the benefit model as expected value.** Benefit per period = **Reach × Adoption rate × Value-per-unit**, then apply a **confidence/probability-of-success discount** to turn a best case into an expected case. Keep each factor an explicit, sourced number, and make the arithmetic reproduce: a reviewer should multiply the factors and land on your total. An unhedged top-line is a tell that no one stress-tested it.
5. **Total the cost: build + run.** One-time build (person-months × loaded cost, plus any licensing) **plus** recurring run cost per period (infra, support, maintenance). ROI math that omits run cost is how "profitable" features quietly lose money.
6. **Compute payback and ROI on one stated convention.** **Net benefit/period = expected benefit − run cost** (run is now baked into net). **Payback = build cost ÷ net benefit/period.** **ROI over horizon = (cumulative net benefit − build cost) ÷ build cost** — do **not** re-subtract run cost in the ROI line, or you double-count it. State the horizon explicitly; ROI with no horizon is meaningless.
7. **Run sensitivity on the load-bearing input.** Find the one number the verdict hinges on (usually adoption or value-per-unit) and show conservative / base / optimistic. Name the **break-even threshold**: how low can that input go before the case flips to kill (payback slips past the horizon)?
8. **List risks and assumptions, each with a number attached.** Not "adoption is uncertain" — "if adoption lands at 15% instead of 30%, payback doubles to 14 months." Make the risk move the model.
9. **Make the call.** FUND / FUND A SMALLER VERSION / KILL / REVISIT-WHEN — with the single reason. Then state what evidence would flip it. A business case that can't say "kill" isn't analysis, it's advocacy.

## Output template
Fill in every `[bracket]`. Show the arithmetic — a reviewer should be able to redo your math from the factor tables. Round sensibly and label every estimate. Mark soft estimates with ⚠.

```markdown
# Business Case: [Investment name]

**Author:** [name] · **Date:** [date] · **Decision owner:** [who funds this] · **Horizon:** [e.g. 12 months]

## TL;DR — the ask
**Recommendation: [FUND / FUND A SMALLER VERSION / KILL / REVISIT WHEN ___].**
[1-2 sentences: what we'd build, what it costs, what it returns, and the payback. The exec should be able to decide from this block alone.]
- **Ask:** [$X / N person-months over N weeks]
- **Expected return:** [$Y net benefit / period] · **Payback:** [N months] · **[Horizon] ROI:** [N%]
- **Confidence:** [High / Med / Low] — load-bearing on [the one assumption].

## Problem & cost of inaction
[What's broken, for whom, with evidence. Then the do-nothing baseline as a number.]
- **Evidence:** [churn reason / lost deals / ticket volume / metric]
- **Cost of doing nothing:** [$X/period or trajectory] — [e.g. "we lose ~$Z/quarter to this; it compounds as ___"]

## Options considered
| Option | What it is | One-time cost | Run cost/period | Expected benefit/period | Verdict |
|---|---|---|---|---|---|
| A — Do nothing | accept the status quo | $0 | $0 | −[cost of inaction] | [baseline] |
| B — [thin v1] | [smallest version that tests the value] | [$ / N pm] | [$] | [$] | [recommended?] |
| C — [build full] | [the complete version] | [$ / N pm] | [$] | [$] | [ ] |
| D — [buy / partner] | [vendor or integration instead of build] | [$] | [$] | [$] | [ ] |

**Chosen:** [Option X] — [one line on why it beats the others, including do-nothing].

## Value model (expected value)
**Benefit / period = Reach × Adoption × Value-per-unit, then × confidence discount.**
[State the unit explicitly: per-account or per-user. State whether benefit is new revenue, retained revenue, or cost saved.]

| Factor | Value | Source / basis |
|---|---|---|
| Reach (units/period) | [N] | [real count — analytics, CRM, market data] |
| Adoption rate | [%] | [comparable feature / benchmark / estimate ⚠] |
| → Successful units/period | [N] | = Reach × Adoption |
| Value per successful unit | [$] | [incremental ARR / retained ACV / hours × loaded cost — state per-unit basis] |
| Gross benefit/period | [$] | = successful units × value-per-unit |
| Confidence discount | [×0.X] | [probability the link holds ⚠] |
| **Expected benefit / period** | **[$Y]** | = gross × discount |

## Cost model
| Cost | Amount | Basis |
|---|---|---|
| Build (one-time) | [$ = N pm × loaded cost] | [eng-sized, not PM-guessed] |
| Run (per period) | [$] | [infra + support + maintenance] |
| **Net benefit / period** | **[$Y − run]** | expected benefit − run cost |

## Payback & ROI
- **Payback:** build cost ÷ net benefit/period = [$build] ÷ [$net] = **[N months]**
- **[Horizon] ROI:** (cumulative net benefit − build cost) ÷ build cost = **[N%]**
  *(run cost is already inside net benefit — do not subtract it again here)*
- **Cumulative net at horizon:** [$]

## Sensitivity — what the verdict hinges on
Load-bearing input: **[the one number]**.

| Scenario | [Load-bearing input] | Net benefit/period | Payback | Verdict |
|---|---|---|---|---|
| Conservative | [low] | [$] | [N mo] | [fund/kill] |
| Base | [mid] | [$] | [N mo] | [fund] |
| Optimistic | [high] | [$] | [N mo] | [fund] |

**Break-even:** the case flips to KILL if [input] falls below **[threshold]** (payback past the [horizon]) — [how plausible that is].

## Risks & assumptions (each with a number)
| # | Risk / assumption | If it's wrong | Mitigation / cheapest test |
|---|---|---|---|
| 1 | [assumption, stated as a number] | [quantified impact on payback/ROI] | [the test that de-risks it] |
| 2 | [assumption] | [impact] | [test] |

## Decision ask
**[FUND / FUND SMALLER / KILL / REVISIT WHEN ___].** [The single most important reason.]
**What would change this call:** [the evidence — a test result, a real adoption number — that flips the verdict.]
```

## Avoid (anti-patterns)
- **A value model whose arithmetic doesn't reproduce.** If the factor table multiplies to $2.6K but the "Expected benefit" cell says $24K, the whole case is dead on arrival — every reviewer who multiplies the row catches it. Make Reach × Adoption × Value × discount actually equal your headline number.
- **Per-user value priced as per-account (or vice-versa).** "$4/mo" is a per-*user* number; an account with 6 users is worth ~$288/yr. Stating value-per-unit on the wrong basis is a silent 10x error that flips fund to kill or back. Label the unit.
- **Double-counting run cost in ROI.** If net benefit already subtracts run cost, the ROI line uses *build* cost as the denominator — re-subtracting run there understates ROI and contradicts the payback line. Pick one convention (the template's) and hold it.
- **Top-line benefit with no confidence discount.** "Reach × value = $4M" with 100% adoption baked in is a fantasy. Discount for the probability it lands, and show the factor.
- **Forgetting run cost entirely.** A feature with great build-cost ROI can bleed money on infra and support forever. Always model recurring cost, not just the one-time build.
- **No do-nothing option.** A case with a single option isn't a decision — it's a demand. The status quo is always a real alternative and must be costed.
- **PM-invented effort.** Engineering sizes the build; a PM who guesses person-months rigs the entire ROI. Get the cost from eng or flag it as an estimate.
- **A model that can't say "kill."** If every input is tuned until the answer is "fund," you've written advocacy. A real case has a break-even threshold and is willing to cross it.
- **Doing `prioritize`'s job.** This justifies *one* bet against its own cost and the do-nothing line — it doesn't rank a list. Comparing five features for sequencing is `prioritize`.

## Quality bar
Before delivering, verify every box:
- [ ] A reviewer reading only the TL;DR can make the fund/kill call — it states the ask, return, payback, and confidence.
- [ ] The do-nothing baseline is costed as a number, and "do nothing" is a row in the options table.
- [ ] There are 2-4 real options, not one.
- [ ] **The value-model arithmetic reproduces:** Reach × Adoption × Value-per-unit × discount equals the stated expected benefit. A reviewer can redo it from the table.
- [ ] Value-per-unit states its basis (per-user vs per-account) and its type (new / retained / cost-saved).
- [ ] A confidence/probability discount is applied and shown — no bare best-case top-line.
- [ ] Both build (one-time) and run (recurring) costs are modeled.
- [ ] Payback and ROI use the one stated convention; run cost is not double-counted in ROI; the horizon is explicit.
- [ ] The build cost is eng-sized or flagged as a PM estimate.
- [ ] Sensitivity covers conservative/base/optimistic on the load-bearing input, with a named break-even threshold.
- [ ] Every risk/assumption carries a quantified impact and a cheapest test.
- [ ] The recommendation is one of FUND / FUND SMALLER / KILL / REVISIT-WHEN, with a single reason and a stated flip condition — and the case is genuinely capable of landing on KILL.

## Tips
- **Lead with payback, not ROI.** Execs feel "pays for itself in 7 months" faster than "75% ROI." Payback answers "when do I get my money back?" — the first question a funder asks.
- **Retained revenue counts as much as new revenue.** A feature that stops churn has a real, modelable benefit — don't undersell defensive bets by only counting new ARR.
- **One load-bearing input usually decides everything.** Find it (almost always adoption or value-per-unit), put your homework there, and run sensitivity on it rather than spreading false precision across ten cells.
- **The thin-v1 option is often the winning move.** When the value is uncertain, the strongest case is rarely "build the whole thing" — it's "spend a little to learn whether the big benefit is real," then re-decide. Price the learning, not just the feature.