---
name: north-star
description: Defines a North Star Metric that captures delivered customer value and decomposes it into 3-4 movable input metrics. Use when you need to "pick a North Star metric," "we're optimizing for revenue and it's hurting us," "build an input metric tree," "what should the team actually move," "align the roadmap to one number," or "our metric is a vanity metric."
---

# North Star Metric

Defines a single North Star Metric (NSM) that measures the value customers actually receive, then decomposes it into the 3-4 input metrics teams can directly influence — the North Star + input metric tree framework.

**Grounded in:** *Lean Analytics* — Croll & Yoskovitz: the One Metric That Matters and its input tree.
**Go deeper (The Product Channel):** [How to Develop and Write KPIs](https://sidsaladi.substack.com/p/how-to-develop-and-write-kpis-a-guide)

## When to use this
- The team is optimizing for revenue or signups and it's quietly degrading the product or customer experience.
- Leadership wants "one number" to rally the org but every proposal is a lagging vanity metric.
- A roadmap exists but no one can say how a given feature moves the top-line goal.
- You're setting OKRs or quarterly goals and need a metric tree to cascade them from.
- Multiple teams each chase their own metric and the numbers conflict or cancel out.

## Before you start (gather these)
- **The core value exchange**: what does a customer do in your product that means they got value? (the action, not the purchase)
- **A rough activity dataset or description**: usage counts, active users, key actions per period — pasted numbers or even ballpark ranges are fine.
- **Business model**: subscription, transactional, marketplace, ads, freemium — this shapes whether the NSM should be breadth, depth, or frequency.
- **Current metric(s)** the team reports today and who owns them.

If 2+ of these are missing or vague, ASK 2-4 sharp questions before proceeding, e.g.: "What single action, if a user never did it, would mean they got zero value?" / "Is value driven more by how many people use it, or how often each person does?" / "What's your business model and what's the lag between usage and revenue?" If a dataset is already pasted, proceed and state your assumptions inline (e.g., "assuming 'active' = action in trailing 28 days").

**Non-interactive / one-pass mode:** if the caller wants a single complete deliverable (e.g., "just give me the NSM," a batch/automation context, or no human is available to answer), do NOT block on questions. Proceed end-to-end using the most defensible assumptions, and surface every assumption explicitly in the **Assumptions made** block (and any threshold you couldn't data-validate as a flagged hypothesis) so the caller can correct in one round.

## Process
1. **Locate the value moment.** Identify the single repeated action where the customer realizes the product's promise. Pressure-test it: if a user did *only* this, would they pay / stay / refer? If yes, it's a candidate.
2. **Draft the NSM as value delivered, not value extracted.** Frame it as `[breadth] × [depth/frequency] of [value action]` — e.g., "weekly active teams completing ≥1 workflow," not "MRR." Revenue is the *consequence*; the NSM must *lead* it.
3. **Run the three gates.** A valid NSM must (a) reflect customer value, (b) lead revenue, and (c) be measurable and movable. Reject any candidate that fails one. Vanity metrics (registered users, page views, raw GMV) fail gate (a) or (c).
4. **Decompose into 3-4 inputs.** Break the NSM into a small tree of inputs a team can directly own. First classify the NSM shape, because reconstruction logic differs:
   - **(a) Decomposable NSM** — the NSM is literally a product/sum of quantities (e.g., `rate × rate × volume`, "active accounts × actions per account"). Inputs are the factors and must arithmetically multiply/sum back to the NSM.
   - **(b) Count or funnel NSM** — the NSM is a *count of qualified users/accounts* (e.g., "weekly active accounts completing ≥1 workflow") or a funnel (e.g., **Acquisition × Activation × Retention**). Here the inputs are sequential **conversion factors or survival rates that govern the count**, not factors that multiply to it. The reconstruction is `top-of-funnel volume × conversion₁ × conversion₂ × … = the count` (a flow equation), not "inputs multiply to equal the NSM directly."

   Use a clean structure — typically **Breadth × Frequency × Depth** (decomposable) or **Acquisition × Activation × Retention** (count/funnel). Each input should map to a team and a lever.
5. **Data-validate any numeric threshold in the NSM.** If the NSM contains a cutoff (e.g., "≥3 standups/week," "≥1 workflow"), do NOT guess it. Run an **activation-threshold analysis**: for each candidate threshold, correlate it against the outcome that matters (retention, conversion, or paid-survival) and pick the threshold where the correlation/lift inflects — the "aha" point above which users reliably stick. State the chosen threshold, the data that justified it, and the lift vs. the next candidate. If the data isn't available, mark the threshold as a hypothesis to validate and say so explicitly.
6. **Verify the math — by shape.** Use the reconstruction logic that matches the NSM shape from step 4:
   - **Decomposable:** confirm the inputs *multiply or sum* back to the NSM exactly. If they don't reconstruct it, the tree is decorative — fix it. State the relationship explicitly (× or +).
   - **Count/funnel:** confirm the flow equation closes — `top-of-funnel × conversion₁ × … × retention = the qualified count`. The factors are rates/survival, not co-equal multipliers; checking that they reproduce the count is the valid check. Don't force strict multiply-back of co-equal terms onto a funnel.
7. **Model retention explicitly as a survival lever.** If retention is an input (it usually is for count/funnel NSMs), represent it as a **cross-week survival / cohort-decay rate** — e.g., "fraction of week-N active accounts still active in week N+1," or a cohort retention curve — not a static percentage. In the reconstruction it enters as the survival factor that carries accounts forward across periods: `accounts this week ≈ retained-from-last-week (survival × last week's active) + newly activated`. This keeps retention inside the flow equation without violating the multiply/sum rule, because survival governs carryover rather than acting as a co-equal multiplier of the count.
8. **Assign ownership and a counter-metric.** For each input, name the owning team and a guardrail metric so optimizing one input can't silently wreck quality (e.g., pair "sessions per user" with "support tickets per session").
9. **Set a cadence and baseline.** Define how each is measured, the current value (with an as-of date), and a target with a target date. NSM moves slowly; inputs move weekly — review inputs weekly, NSM monthly.

## Output template

```markdown
# North Star Metric — [Product / Team]

## North Star Metric
**[NSM, stated as value delivered — e.g., "Weekly active accounts completing ≥1 [core action]"]**

- **Current value:** [number] · **Baseline as-of:** [date] · **Target:** [number] **by** [target date]
- **Why this captures value:** [1-2 sentences — what the customer got, not what we charged]
- **How it leads revenue:** [the causal chain: more NSM → __ → revenue, with the typical lag]
- **Measurement:** [exact definition — window, what counts as "active," what counts as the action]

### Three gates (must pass all)
| Gate | Pass? | Evidence |
|---|---|---|
| Reflects customer value | [Y/N] | [why] |
| Leads revenue | [Y/N] | [why] |
| Measurable & movable | [Y/N] | [why] |

## Input metric tree
> NSM shape: **[Decomposable | Count/Funnel]**
> Relationship to NSM: **[Breadth × Frequency × Depth, factors multiply back | Acquisition × Activation × Retention, flow equation governs the count]**

| Input metric | Definition | Owner (team) | Lever (how we move it) | Current → Target | Counter-metric (guardrail) |
|---|---|---|---|---|---|
| **Breadth** — [e.g., new active accounts] | [definition] | [team] | [lever] | [x → y] | [guardrail] |
| **Frequency** — [e.g., sessions per account / week] | [definition] | [team] | [lever] | [x → y] | [guardrail] |
| **Depth** — [e.g., actions completed per session] | [definition] | [team] | [lever] | [x → y] | [guardrail] |
| **[4th input, optional]** — [e.g., **Retention** = week-over-week survival rate, fraction of active accounts still active next week] | [definition — state it as a cross-week survival / cohort-decay rate, not a static %] | [team] | [lever] | [x → y] | [guardrail] |

**Threshold validation:** [If the NSM has a numeric cutoff: state the chosen threshold, the activation-threshold analysis that picked it (correlation/lift vs. retention or conversion), and the next-best candidate. If unvalidated, label it a hypothesis.]

**Reconstruction check (use the form matching the NSM shape):**
- **Decomposable:** [Input A] × [Input B] × [Input C] ≈ NSM → [show the arithmetic with current numbers]
- **Count/Funnel:** [top-of-funnel volume] × [activation rate] × [retention/survival rate] ≈ [qualified count = NSM] → [show the flow arithmetic with current numbers; retention enters as the survival factor carrying accounts across periods, not as a co-equal multiplier]

## Cadence
- **Inputs:** reviewed [weekly] by [owners] — these move fast and are where work happens.
- **NSM:** reviewed [monthly] by [leadership] — slow-moving outcome.

## Assumptions made
- [Any definition, window, or proxy assumed because data was incomplete.]

## What this NSM explicitly is NOT
- [Name the vanity metric(s) rejected and the gate they failed — e.g., "Not total signups (fails value gate — signups ≠ usage)."]
```

## Avoid (anti-patterns)
- **Picking revenue/MRR as the North Star.** Revenue is a lagging consequence; teams can goose it short-term (discounts, dark patterns) while value erodes. The NSM must *lead* revenue.
- **A cumulative or "total ever" metric** (total users, total GMV-to-date) — it only goes up and can't tell you if you're getting better *now*. Use active/per-period.
- **Inputs that don't reconstruct the NSM.** If your tree's inputs don't multiply or sum back to the top number, you've listed related KPIs, not a decomposition.
- **6+ inputs.** A tree no team can hold in their head won't drive behavior. Cap it at 3-4 first-level inputs; nest deeper only if a team owns the sub-branch.
- **No counter-metrics.** Optimizing "frequency" with no quality guardrail breeds engagement-bait and notification spam.

## Tips
- The fastest NSM test: "If this number went up 30% and *nothing else changed*, would customers be better off?" If the honest answer is "not necessarily," it's a vanity metric.
- Prefer **active over total**, **per-account over raw count**, and **completed over started** — each shift moves you closer to measured value.
- Map every input to exactly one owning team. An input no team owns is a wish; an input two teams own is a fight.
- Pick the NSM shape from the business model: marketplaces lean on **frequency × matched value**, SaaS on **active accounts × depth**, content/consumer on **frequency × retention**. Don't borrow another company's NSM — borrow their *structure*.
