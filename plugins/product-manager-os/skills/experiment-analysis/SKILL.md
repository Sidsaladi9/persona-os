---
name: experiment-analysis
description: Designs and reads A/B tests end to end — a sharp hypothesis, a primary metric plus guardrails, sample size and power, and a frequentist read (significance, confidence interval, practical effect) leading to a clear ship/kill call. Use when you say "design this A/B test," "is this result significant," "how many users do I need," "can we ship this," or "did the experiment win?"
---

# Experiment Analysis

A rigorous frequentist framework for designing and analyzing A/B tests: state a falsifiable hypothesis, pre-register one primary metric plus guardrails, compute the sample size needed to detect a meaningful effect, then read the result honestly — without peeking or p-hacking — and convert it into a ship/kill decision.

**Grounded in:** *Trustworthy Online Controlled Experiments* — Kohavi, Tang & Xu: pre-registered metric, power, and an honest read of significance vs. MDE.
**Go deeper (The Product Channel):** [Learning from Experiments](https://sidsaladi.substack.com/p/learning-from-experiments-a-superpower)

## When to use this
- You're about to launch an A/B test and need a design that won't be ambiguous later ("here's the change, help me set it up properly").
- A test has finished (or is mid-flight) and you need to interpret the numbers and decide ship vs. kill.
- Someone shows you a "significant" result and you suspect peeking, a tiny sample, or a cherry-picked metric.
- You need to estimate how long a test must run, or whether you even have the traffic to detect the effect you care about.
- You're refereeing a debate where two people read the same dashboard and reached opposite conclusions.

## Before you start (gather these)
- **The change and the mechanism** — what's different in treatment, and *why* you believe it moves the metric.
- **Primary metric** — the single conversion/rate/continuous metric that decides the test. One. Plus its current baseline value.
- **Guardrail metrics** — what must NOT get worse (latency, churn, refunds, revenue per user, support tickets).
- **Traffic & allocation** — users/sessions per day eligible, split (50/50?), and the analysis unit (user vs. session).
- **Minimum Detectable Effect (MDE)** — the smallest lift worth shipping for, in business terms, not just "statistically detectable."

If two or more of {primary metric, baseline, MDE, traffic} are missing or vague, STOP and ask 2–4 sharp questions before designing — e.g.: "What's the one metric that decides this?", "What's its current baseline rate?", "What's the smallest lift that would actually be worth shipping?", "How many eligible users/day and what split?" If the data is already provided, proceed and state assumptions inline (α=0.05, power=0.80, two-sided) so they're visible and challengeable.

## Process
1. **Write a sharp hypothesis.** Format: "Because [mechanism/insight], changing [X] will [increase/decrease] [primary metric] by at least [MDE], without harming [guardrails]." If you can't name the mechanism, you're guessing, not experimenting.
2. **Lock the primary metric — exactly one.** Multiple "primary" metrics inflate false positives. Everything else is secondary or a guardrail. Define it precisely: numerator, denominator, attribution window, unit (per user, not per session, unless you have a reason).
3. **Set decision thresholds up front.** α = 0.05 (two-sided unless you have a strong directional prior), power = 0.80. These are pre-registered, not chosen after seeing data.
4. **Compute sample size & runtime BEFORE launch.** For a proportion metric: **n per arm ≈ 16 × p₀(1−p₀) / MDE_abs²** at α=0.05, power=0.80 (the 16 bundles the two-sided z-values; `MDE_abs` is the absolute lift, e.g. +2pp = 0.02, not a relative %). When the treatment variance may exceed control (e.g. a feature that could move the rate well past p₀), plug in the **larger** of the two plausible p values to get a conservative n. Then convert to runtime — but the conversion depends on the metric type:
   - **Immediate metrics** (click, signup, same-session conversion): days = (n per arm × number of arms) / daily eligible traffic.
   - **Lagging / maturation metrics** (retention, week-2 active, renewal, anything observed W days after enrollment): **total runtime = enrollment window + maturation window W.** You must keep enrolling until you've accrued n per arm AND then wait W more so the *last-enrolled* cohort has had its full chance to mature. Never read the metric before the last-enrolled cohort has matured — the naive `days = n / daily traffic` ignores W and yields absurdly short tests where most users haven't had time to retain/renew yet.
   If runtime is impractical, raise the MDE or reduce variants — don't launch an underpowered test you'll be tempted to over-read.
5. **Pre-commit to a fixed horizon and ONE analysis.** Pick the end date from step 4 and analyze once. If you need to look early, you need sequential testing or always-valid CIs — otherwise every peek inflates your false-positive rate.
6. **Sanity-check before reading the result.** Sample Ratio Mismatch: does the actual split match intended (e.g., 50/50)? A skew (p < 0.01 on a chi-square of assignment counts) means the experiment is broken — stop, don't interpret the lift.
7. **Read the primary metric.** Report the observed effect, its 95% confidence interval, and the p-value. The CI is the headline: it tells you the *range* of plausible true effects, not just yes/no significance.
8. **Apply the five-way read** (significance × practical effect):
   1. Significant + entire CI above MDE → clean ship signal.
   2. Significant but CI entirely below MDE → real but too small to matter.
   3. Significant but the CI **straddles the MDE** (lower bound below it, upper bound above) → the effect is real but the verdict hinges on guardrails/cost: the true lift might or might not clear your bar. Consider a **staged ship with a holdback** (ship to most, keep a control slice to keep measuring) or **EXTEND** to tighten the interval before committing.
   4. Not significant but CI spans meaningful lift → underpowered/inconclusive (don't call it "no effect").
   5. Not significant + tight CI around zero → genuine flat result, kill.
9. **Check guardrails — and don't over-kill on noise.** A primary win with a guardrail breach is not a win, so evaluate each guardrail's CI too. But with many guardrails you're running many comparisons: by chance alone one marginal CI will look "breached." **Pre-rank guardrails into hard-stops** (latency, revenue/user, churn — a real breach kills the ship) **vs. monitor-only** (nice-to-watch, won't block ship). Don't kill a winning test on a single marginally-breached monitor-only guardrail; require a hard-stop breach, or a clear/replicated breach, before blocking.
10. **Decide and document.** Ship / Kill / Iterate / Extend, with the one-line reason and the numbers that drove it.
11. **Guard against novelty/primacy on engagement features.** For engagement or retention changes, an early lift can be users reacting to *newness*, not durable value — and it can decay (novelty) or take time to appear (primacy). When you ship one of these, **hold back a slice** of users on control post-ship and keep measuring; only treat the lift as real once it survives the novelty window (typically a few weeks). If the gap collapses once the shine wears off, roll back.

## Output template

```markdown
# Experiment Read: [Test name]
**Status:** [Design / Mid-flight / Final read]  ·  **Date:** [date]  ·  **Owner:** [name]

## Hypothesis
Because [mechanism/insight], changing [X → Y] will [increase/decrease]
**[primary metric]** by at least **[MDE]**, without harming [guardrails].

## Design
| Parameter | Value |
|---|---|
| Primary metric | [exact definition: numerator / denominator / window] |
| Analysis unit | [user / session] |
| Baseline | [p₀ or mean] |
| MDE | [absolute + relative, e.g. +2pp / +8% rel] |
| Variants | [Control + N treatments], split [50/50] |
| α (two-sided) | 0.05 |
| Power | 0.80 |
| Required n / arm | [n] |
| Daily eligible traffic | [n/day] |
| Planned runtime | [X days], end date [date] — **analyze once** |

## Guardrails
| Metric | Direction that's bad | Tolerance |
|---|---|---|
| [latency] | [increase] | [≤ +Xms] |
| [revenue/user] | [decrease] | [≥ flat] |
| [churn/refunds] | [increase] | [≤ +X%] |

## Validity checks
- [ ] Sample Ratio Mismatch: actual split [a/b] vs intended [50/50] — SRM p = [value] ([pass/FAIL])
- [ ] Ran full planned horizon (no early peek-driven stop)
- [ ] No mid-test changes to allocation, eligibility, or metric definition
- [ ] Novelty/seasonality considered

## Results — primary metric
| Arm | Users | [Metric] | Lift vs control | 95% CI | p-value |
|---|---|---|---|---|---|
| Control | [n] | [value] | — | — | — |
| Treatment | [n] | [value] | [+X% / +Xpp] | [lo, hi] | [p] |

**Read:** [Significant & CI ≥ MDE / Significant but CI < MDE / Significant but CI straddles MDE / Inconclusive–underpowered / Genuinely flat]
The CI [lo, hi] [excludes / includes] zero and [is entirely above / is entirely below / straddles] the MDE → [interpretation in one sentence].

## Results — guardrails
| Guardrail | Effect | 95% CI | Breached? |
|---|---|---|---|
| [metric] | [value] | [lo, hi] | [No / YES] |

## Decision: [SHIP / STAGED SHIP + HOLDBACK / KILL / ITERATE / EXTEND]
**Why:** [one or two sentences tied to the primary CI + guardrail hard-stops vs monitor-only].
**If EXTEND:** need total n = [N] per arm to reach power for [MDE]; with [n] per arm so far → [N − n] more to accrue ≈ [(N − n) × arms / daily traffic] more enrollment days, **plus the W-day maturation window** for lagging metrics before the next read.
**If novelty risk (engagement/retention):** ship with a [X%] control holdback; confirm the lift survives the [~few-week] novelty window before full rollout.
**Next:** [rollout plan / next hypothesis / what to monitor post-ship].
```

## Avoid (anti-patterns)
- **Peeking + stopping when it's green.** Checking daily and calling it the moment p < 0.05 can push your real false-positive rate above 30%. Fix the horizon, or use sequential/always-valid methods.
- **Promoting metrics after the fact.** Running 8 metrics and headlining the one that won is p-hacking. Pre-register one primary; treat the rest as directional.
- **Reading "p > 0.05" as "no effect."** A wide CI that still spans your MDE means underpowered, not flat. Absence of evidence ≠ evidence of absence.
- **Significant but trivial = ship.** With huge n, a +0.1% lift can be "significant" and worthless. The MDE, not the p-value, decides if it matters.
- **Ignoring SRM.** A 52/48 split when you intended 50/50 usually means broken assignment or logging — the lift is uninterpretable until you fix it.

## Tips
- **The confidence interval is the answer, not the p-value.** "True lift is somewhere between +1% and +9%" tells you more than "p = 0.03" ever will — design your read around the interval.
- **Analyze on the unit you randomized on.** If you split by user, don't analyze by session — it understates variance and fakes significance.
- **Pre-write the decision rule before launch.** "We ship if the primary CI lower bound clears [X] and no guardrail CI breaches." Deciding the rule after seeing data is how teams talk themselves into bad ships.
- **If you must read early, budget for it.** Sequential testing or a Bonferroni-style correction lets you look mid-flight honestly; naive peeking does not.
