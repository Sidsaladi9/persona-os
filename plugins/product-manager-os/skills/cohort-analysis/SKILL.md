---
name: cohort-analysis
description: Builds and interprets a cohort retention table — defines the cohort and return event, reads where and when users drop off, compares cohorts over time, and converts the retention curve into a hypothesis and an action. Use when you say "build a cohort table," "why is retention dropping," "are newer signups sticking better," "where do users churn," or "what happened to the March cohort."
---

# Cohort Analysis

Group users by when they first joined, then track what fraction return in each period after. A cohort retention table turns a flat churn number into a curve you can read: where the cliff is, whether the curve flattens (a sticky core), and whether newer cohorts retain better than older ones.

**Grounded in:** *Lean Analytics* — Croll & Yoskovitz: cohort retention curves read against a benchmark, not zero.
**Go deeper (The Product Channel):** [Product Metrics](https://sidsaladi.substack.com/p/week-5-week-in-product-series-product)

## When to use this
- Retention or churn looks bad but you can't tell if it's getting better or worse over time.
- You shipped an onboarding, activation, or pricing change and want to see if it moved retention for users who joined after.
- You need to know *where* in the lifecycle users drop — day 1, week 1, month 2 — not just that they do.
- Leadership asks "are the users we're acquiring now any good?" and you need cohort-over-cohort evidence.
- You want to find your retention floor (the curve flattening) to size a real, durable user base vs. a leaky bucket.

## Before you start (gather these)
- **The cohort definition**: what groups users (usually signup/first-purchase date) and the grain (daily, weekly, monthly).
- **The return event**: what "retained" means — opened app, completed a core action, paid again. Vanity logins are weak; a value-moment event is strong.
- **The period grid**: how you'll bucket time after joining (Day 0/1/7/30, or Week 0–8, or Month 0–6).
- **The raw data**: either a pre-built cohort table, or per-user rows of (join_date, activity_dates) you can pivot.

If the return event is undefined or the grain is unclear (2+ of these vague or missing), ASK 2–4 sharp questions first: *What single action means a user got value? What's the natural usage frequency — daily, weekly, monthly? When does a user "start" (signup vs. first key action)?* If data is already provided, proceed and state assumptions inline (e.g. "Assuming retained = ≥1 core action that week; cohort = signup week").

## Process
1. **Lock the definition before touching numbers.** One return event, one start moment, one period grain matched to natural usage frequency (don't measure a monthly product daily). Write it as one sentence: "Cohort = [start], retained = [event] within [period]."
2. **Build the table.** Rows = cohorts (oldest at top), columns = periods since join (0, 1, 2…). Cell = % of that cohort's Period-0 size active in that period. Period 0 is always 100% (or define it as activated users). Keep an N column — never read a cohort with tiny N.
3. **Find the cliff (scan EVERY adjacent-period drop).** Don't presume it's P0→P1. Compute the drop between each adjacent pair (P0→P1, P1→P2, P2→P3…) and find the largest fall wherever it lands. Many products have a week-2 (or later) cliff, not a day-1 one. A P0→P1 cliff points at onboarding/activation; a later cliff points at a habit or value-depth problem. Whatever the biggest fall is, that's the cliff — name it by the period pair where it actually occurs.
4. **Read across each row (the curve shape).** Does it keep falling to zero (leaky bucket, no product-market fit) or flatten into a plateau (a retained core — that plateau % is your retention floor)?
5. **Read down each column (cohort-over-cohort).** Hold the period constant and compare cohorts. If newer cohorts show higher Period-1 or Period-3 retention, your recent changes are working. This is the diagonal-free way to see trend.
6. **Find the inflection.** Name the single period where the most users are lost relative to value delivered. That's where one intervention has the most leverage.
7. **Segment if the curve is muddy.** Split by acquisition channel, plan, or first action. Blended curves often hide one great segment and one terrible one.
8. **Form a hypothesis, then an action.** Convert the read into one testable sentence: "Users drop at [period] because [hypothesis]; if we [action], Period-[n] retention rises from [x]% to [target]%."

## Output template

```markdown
# Cohort Retention Analysis — [Product / Segment]

**Date:** [date] · **Analyst:** [name]
**Definition:** Cohort = users by [signup week]. Retained = [≥1 core action] in the period. Grain = [weekly].
**P0 denominator:** P0 = [all signups | activated only] — this choice changes every downstream %.
**Signup→P0 activation rate:** [z]% ([signups] → [activated]). *(Required when P0 = activated only — an activated-P0 table conceals tire-kicker churn that happens before activation. Report this rate or warn it's hidden.)*
**Window:** [cohorts from X to Y] · **Assumptions:** [stated inline]

## Retention table (% of cohort active)
| Cohort (size N) | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| [Wk of date] (N=[ ]) | 100% | [ ]% | [ ]% | [ ]% | [ ]% | [ ]% |
| [Wk of date] (N=[ ]) | 100% | [ ]% | [ ]% | [ ]% | [ ]% | — |
| [Wk of date] (N=[ ]) | 100% | [ ]% | [ ]% | — | — | — |
| **Avg (mature cohorts only)** | 100% | [ ]% | [ ]% | [ ]% | [ ]% | [ ]% |

*Avg row excludes partial/young cohorts (those without complete periods) — blending them in distorts the curve.*

**Benchmark band:** ~[X]% P1 / ~[Y]% floor — typical for [category, e.g. B2B SaaS vs. consumer social]. Read every number against this band, not against zero.

## What the curve says
- **The cliff (P[n]→P[n+1]):** [x]% drop — the largest adjacent fall, found by scanning every period pair (not assumed at P0→P1). [Onboarding/activation read if early; habit/value-depth read if later.]
- **Curve shape:** [Falls to zero ▸ leaky bucket] OR [flattens at ~[y]% by P[n] ▸ that's the retention floor].
- **Retention floor:** ~[y]% — the durable core. [Is that enough to build on?]
- **Cohort-over-cohort (read down a column):** P[n] retention went [x]% → [y]% across cohorts ▸ [improving / flat / decaying]. [Tie to a known ship.]
- **Inflection point:** Most users lost at **P[n]** relative to value delivered.

## Segment cut (if run)
| Segment | P1 | P3 | Floor | Read |
|---|---|---|---|---|
| [Channel / plan A] | [ ]% | [ ]% | [ ]% | [strong/weak] |
| [Channel / plan B] | [ ]% | [ ]% | [ ]% | [strong/weak] |

## Hypothesis → action
- **Hypothesis:** Users drop at **P[n]** because [specific cause].
- **Evidence:** [the cells / comparison that support it].
- **Action:** [one intervention targeting that period].
- **Success metric:** P[n] retention rises from **[x]% → [target]%** for cohorts after [ship date].
- **Re-check:** Re-pull this table in [N periods]; watch the [P n] column down the cohorts.
```

## Avoid (anti-patterns)
- **Reading a single blended retention number** instead of the curve — it hides whether you're improving or decaying over cohorts.
- **Mismatching grain to usage frequency** — measuring a monthly-use product on daily retention manufactures a fake cliff.
- **Trusting tiny or partial cohorts** — recent cohorts have small N and incomplete periods; never call a trend off a cohort with 3 periods of data and N=12.
- **Using a vanity return event** (any login) instead of a value moment — it flatters the curve and hides real churn.
- **Confusing the table's lower-right emptiness for churn** — those cells are blank because those cohorts are too young to have reached that period, not because users left.

## Tips
- The **plateau, not the slope, is the prize.** A curve that flattens at 30% beats one that starts at 60% and slides to zero. Find where it flattens.
- **Anchor every cohort-over-cohort claim to a ship date.** "P1 jumped after the new onboarding (released wk of [date])" is a story leadership can act on; a number alone isn't.
- **Compare to a benchmark band, not zero.** Know roughly what good looks like for your category (e.g. consumer social vs. B2B SaaS retain very differently) before declaring a curve "bad."
- **One inflection, one action per pass.** Pick the highest-leverage period, intervene there, and re-pull the table — don't try to fix the whole curve at once.
