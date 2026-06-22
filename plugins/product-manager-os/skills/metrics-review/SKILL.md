---
name: metrics-review
description: Reviews product metrics with trend analysis and turns raw numbers into a scorecard with actions. Use when the user asks to "review our metrics", "run a weekly/monthly/quarterly metrics review", "why did signups drop", "why did this spike", "build a metrics scorecard", or "compare against target". Works with pasted numbers or a CSV; pulls from Amplitude/Mixpanel/GA if connected.
---

# Metrics Review

Most metrics reviews fail in the same way: a wall of numbers with no baseline, no driver, and no decision. This skill turns whatever the user has — a pasted table, a CSV, a screenshot, or a connected analytics tool — into a tight scorecard that says what moved, why, and what to do about it. The deliverable is a decision, not a dashboard.

**Grounded in:** *Lean Analytics* — Croll & Yoskovitz: compare every metric to a baseline and find the one that moves the business.
**Go deeper (The Product Channel):** [Product Metrics](https://sidsaladi.substack.com/p/week-5-week-in-product-series-product)

You are an opinionated analyst, not a number-reader. Every red gets a hypothesis. Every action gets an owner. Nothing gets reported without a comparison baseline.

## When to use this
- Running a recurring review (weekly business review, monthly metrics, quarterly board prep)
- Investigating a sudden spike or drop ("signups fell 18% this week — why?")
- Checking performance against targets or OKRs before a leadership update
- Turning a raw export or pasted numbers into a shareable scorecard with recommended actions
- Sanity-checking a dashboard someone else built before you forward it up the chain

## Before you start (gather these)
Ask for whatever is missing — don't proceed on one number with no context.

- **Metric values** for the **current period** AND a **prior period** (last week/month/quarter). A number with no baseline is not reviewable.
- **Time grain and window** — what period is "current"? Are these point-in-time snapshots or period totals?
- **Targets / goals** for each metric, if any (OKR target, plan number, last quarter's result).
- **Segments**, if available — by channel, plan tier, platform, geo, cohort, new vs. returning. This is where drivers hide.
- **Known events** — launches, pricing changes, outages, holidays, campaigns, tracking changes. Annotate these; they explain half of all moves.
- **Definitions** — confirm how each metric is calculated (e.g., is "active" DAU, WAU, or logged-in?). Mismatched definitions cause fake trends.

**If Amplitude, Mixpanel, or GA is connected:** offer to pull the numbers directly — name the events/metrics and date ranges you'll query, then fetch. **If nothing is connected:** ask the user to paste the numbers, drop a CSV, or share a screenshot of their dashboard. The skill works fully from pasted data — no account required.

## Process

1. **Build the metric tree (AARRR).** Organize every metric into the funnel so you review the *system*, not a random list:
   - **Acquisition** — traffic, signups, new leads, CAC
   - **Activation** — % reaching the aha/value moment, onboarding completion, first key action
   - **Retention** — DAU/WAU/MAU, D7/D30 retention, churn, resurrected users
   - **Revenue** — MRR/ARR, ARPU, conversion to paid, expansion, NRR
   - **Referral** — invites sent, viral coefficient, NPS, shares
   Note which stages have no data and flag them as blind spots.
   **Escape hatch for retention-led / engagement-core products:** when one funnel stage *is* the core value loop (e.g., retention or an engagement habit is the product's value event, not a downstream stage), organize the review around that loop rather than forcing every metric into a distinct AARRR bucket. Make the value loop the spine, then note where metrics overlap across stages (e.g., the same engagement event drives both activation and retention) instead of double-counting them.

2. **Compute the deltas.** For each metric calculate **Δ vs. prior period** (absolute and %) and **vs. target** (absolute and %). Always show the percentage *and* the absolute — a 50% jump on 4 users is noise; a 2% drop in MRR may be five figures.

3. **Set status.** Assign 🟢 / 🟡 / 🔴 against target (or against prior period if no target exists). Default thresholds, adjust to the metric: 🟢 at or above target / improving as expected; 🟡 within ~5% of target or flat where growth was expected; 🔴 missing target or moving the wrong way. For a metric with **no target**, color it against the prior period: 🔴 if it is moving materially the wrong way (a meaningful decline beyond normal variance, not noise), 🟡 if flat where growth was expected, 🟢 if improving as expected. State the threshold you used.

4. **Segment to find the driver.** For every 🔴 and surprising 🟢, break the metric down (channel, cohort, platform, geo, plan) to localize the move. "Signups −18%" is not an insight; "−18% is entirely paid-search signups after the campaign paused, organic is flat" is. Aim to name the *single biggest contributor* to each material move.

5. **Separate signal from noise.** Before raising an alarm, rule out: small denominators, normal week-to-week variance, seasonality/day-of-week, a tracking or instrumentation change, partial-period data, and one-off events. If a move is within historical noise, label it **noise** and move on — don't manufacture a story.

6. **Derive 2–3 priorities.** Convert the top findings into a *short* list of concrete next steps. "2–3" means 2–3 findings/priorities to act on — not a hard cap on table rows. A single 🔴 can legitimately spawn more than one row (e.g., an investigate-step *and* a build-step both tied to it). Each action ties to a specific red or risk, names an **owner**, and has a **by-when**. Resist sprawling into ten unrelated threads — pick the few findings that matter. If a red has no clear action yet, the action is "investigate X by [date], owner [name]."

## Output template

Fill this in and hand it back as the deliverable. Keep it to one screen where possible.

```markdown
# 📊 Metrics Scorecard — [Product/Team] · [Period, e.g. Wk of Jun 9–15 2026]
**Compared to:** [prior period] · **Targets from:** [OKR/plan/source] · **Prepared:** [date]

| Metric | Stage | Current | Prior | Δ (abs / %) | vs Target | Status |
|---|---|---:|---:|---:|---:|:---:|
| Signups | Acquisition | 1,240 | 1,510 | −270 / −18% | −24% | 🔴 |
| Activation rate | Activation | 41% | 39% | +2pp / +5% | −4pp | 🟡 |
| WAU | Retention | 18.4k | 18.1k | +0.3k / +2% | on plan | 🟢 |
| New MRR | Revenue | $22.1k | $25.0k | −$2.9k / −12% | −15% | 🔴 |
| Invites sent | Referral | 880 | 845 | +35 / +4% | n/a | 🟢 |
<!-- Right-align number columns. Show pp for percentage-point moves. -->

## What moved and why
- 🔴 **Signups −18%** — entirely paid-search; the [campaign] paused Tue. Organic flat. *Hypothesis: spend gap, not demand.*
- 🔴 **New MRR −12%** — downstream of the signup drop + 2 enterprise deals slipped to next period. *Hypothesis: timing, not conversion.*
- 🟢 **Activation +2pp** — new onboarding checklist (shipped Jun 4) landing as expected.

## Watch list (not red yet — monitor)
- D30 retention drifting down 3 weeks running (−1pp/wk); not yet below target.
- Mobile activation 8pp behind web — widening.

## Recommended actions
| # | Action | Tied to | Owner | By when |
|---|---|---|---|---|
| 1 | Resume/replace paused paid-search campaign | Signups 🔴 | @marketing-lead | Jun 17 |
| 2 | Confirm 2 enterprise deals' new close dates | New MRR 🔴 | @ae-name | Jun 16 |
| 3 | Investigate mobile activation gap, propose fix | Watch list | @pm-name | Jun 20 |

**Annotations this period:** paid campaign paused (Tue), onboarding checklist shipped (Jun 4), [holiday/outage if any].
```

## Quality bar
Before you hand off the scorecard, confirm:
- [ ] **No metric without a baseline** — every row has a prior period and/or a target.
- [ ] **Every 🔴 has a hypothesis** — a named, falsifiable reason for the move, ideally pinned to a segment.
- [ ] **Every action has an owner and a by-when** — no orphan tasks.
- [ ] **Absolute and % shown** for each delta — no percentage stands alone.
- [ ] **Signal separated from noise** — small-n and within-variance moves are labeled, not dramatized.
- [ ] **Definitions confirmed** — you know exactly what each metric measures and the date windows match.
- [ ] **Status thresholds stated** — the reader knows what 🟡 vs 🔴 means here.
- [ ] **2–3 priorities, not ten** — the review ends in a decision, not a backlog. (This caps *findings*, not table rows — one red may need both an investigate- and a build-row.)

## Tips
- **Beware vanity metrics.** Total signups, pageviews, and registered users feel good and move nothing. Prefer rates and per-user metrics (activation %, retention %, ARPU, NRR) that are robust to growth and survive scaling.
- **Always compare to a baseline.** A number alone is uninterpretable. Prior period answers "is this changing?"; target answers "is this good?". Show both whenever you can.
- **Annotate launches and events.** The first question on any spike or drop is "what shipped?" Keep a running annotation line (releases, pricing, campaigns, outages, holidays) so you can answer it instantly.
- **Watch the denominator.** Big percentage swings on small bases are almost always noise. State the n.
- **Suspect the instrumentation first on weird moves.** A metric that doubles or vanishes overnight is more often a tracking change than real behavior — verify the pipeline before you write the narrative.
- **Use percentage points for rate changes.** Activation going 39% → 41% is +2pp (and +5% relative); say "pp" to avoid the classic ambiguity.
- **Lead with the decision.** Executives read the actions first. Put what to do where the eye lands; relegate the table to evidence.
- **Be consistent period over period.** Same metrics, same definitions, same order every time — so trends jump out and reviews get faster.

---
*Make it shareable: the `visualize` skill renders this as a KPI scorecard — a self-contained HTML visual you can screenshot into a deck or Slack.*
