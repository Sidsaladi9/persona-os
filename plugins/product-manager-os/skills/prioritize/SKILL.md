---
name: prioritize
description: Score and rank features, ideas, or bets and produce a defensible ranked list plus a clear recommendation. Use when the user wants to prioritize these features, decide what to build first, RICE score this backlog, rank these ideas, run a value vs effort 2x2, or pick the right prioritization framework. Picks the framework, defines the scale, scores consistently, and surfaces the close calls.
---

# Prioritize

Prioritization fails in two ways: a gut-feel ranking nobody can defend, or a precise-looking spreadsheet built on guesses. This skill avoids both. You pick the framework that fits the decision, define the scoring scale before you score anything, score every item against the same goal, then sanity-check the result against your gut. The number is an input to the call, not the call itself.

**Grounded in:** *Escaping the Build Trap* — Melissa Perri: prioritize by outcome with RICE/Kano as inputs, not as the decision.
**Go deeper (The Product Channel):** [6 Prioritization Frameworks](https://sidsaladi.substack.com/p/6-most-effective-problem-prioritization-92d)

## When to use this
- A backlog or idea list is too long and you need a build order you can defend to eng and leadership.
- Stakeholders disagree on what's most important and you need a shared, transparent rubric.
- You're choosing between a few big bets and want to compare them on the same axes.
- Someone asks "why is X above Y?" and you need a real answer, not "it felt right."
- You're deciding scope for a release, sprint, or quarter against a specific goal or metric.

## Pick the right framework
- **RICE** — many comparable features competing for the same roadmap; you have rough reach data. The default for ongoing backlog triage.
- **ICE** — RICE without trustworthy reach data, or you need a fast first-pass cut. Lighter, more subjective.
- **Value vs Effort (2x2)** — small list, mixed audience, you need a fast visual to find quick wins and money pits. Great for workshops.
- **Kano** — you're balancing table-stakes vs differentiators and want to know what *delights* vs what's merely expected. Best with survey/customer input.
- **Weighted Scoring** — the decision has several competing criteria (revenue, strategic fit, risk, effort) that matter unequally; you need to make the trade-offs explicit. Best for big bets and exec alignment.
- **MoSCoW** — fixed-scope or fixed-deadline release where you must draw a "won't do this cycle" line. Scope-cutting, not fine-grained ranking.

## Before you start (gather these)
- **The items** — a clean list of the features/ideas/bets being compared. Comparable grain (don't pit "add a button" against "rebuild billing").
- **The goal/metric** — the ONE outcome these should move (activation, retention, expansion revenue, NPS…). Everything is scored relative to this. If unclear, ask first.
- **Rough inputs for the chosen factors** — reach numbers, effort estimates, evidence for impact. Real data where it exists.
- **Missing data is fine** — don't stall. Estimate, then apply **confidence discounting** (lower the Confidence %), and **label every estimate** so the reader knows what's solid vs. a guess.

## Process
1. **Pick the framework** using the guide above. State why in one line.
2. **Define the scale precisely — before scoring.** Lock the rubric so scores mean the same thing across items. Examples:
   - **RICE**: Reach = # users/accounts affected per quarter (real count). Impact = 3 massive / 2 high / 1 medium / 0.5 low / 0.25 minimal. Confidence = 100% / 80% / 50% (and you MAY go below 50% for a genuine guess — see the Tips note on the floor). Effort = person-months. **Score = (Reach x Impact x Confidence) / Effort.**
   - **ICE**: Impact, Confidence, Ease each 1-10. **Score = I x C x E** (or average).
   - **Weighted Scoring**: pick 3-6 criteria, assign weights summing to 100%, score each item 1-5 per criterion, **Score = Σ(weight x score)**.
   - **Value/Effort**: Value and Effort each High/Med/Low → plot to quadrants.
   - **Kano**: classify each item Delighter / Performance / Basic / Indifferent.
   - **MoSCoW**: tag each Must / Should / Could / Won't (this cycle).
3. **Score every item** against the same goal. Note the evidence (or "estimate") behind each factor as you go.
4. **Compute and sort** — show the math, rank descending. Sort rows descending by score, THEN number the Rank column; verify no rank disagrees with its score before writing.
5. **Sanity-check top and bottom.** Does the #1 pass the gut check? Is anything obviously misranked? Find the **closest call** (two items within noise of each other) and name what's driving it. Re-examine any score doing the heavy lifting in the ranking.
6. **Recommend** a build order and say why — in plain language, not just the number.

## Output template

**Framework:** RICE — *[one line on why it fits]*
**Goal/metric this ranks against:** *[the single outcome]*

| Item | Reach | Impact | Confidence | Effort (pm) | RICE Score | Rank | Notes |
|------|-------|--------|-----------|-------------|-----------|------|-------|
| Feature A | 8,800 | 2 | 100% | 3 | 5,867 | 1 | solid data |
| Feature B | 4,000 | 2 | 100% | 1.5 | 5,333 | 2 | tie on score — won tiebreak (ships first, unblocks C) |
| Feature C | 8,000 | 2 | 100% | 3 | 5,333 | 3 | tie on score — depends on B |
| Feature D | 12,000 | 1 | 50% | 2 | 3,000 | 4 | reach = est. ⚠ |

*(Note the close cluster: A's 5,867 barely clears B and C, which tie at 5,333. Don't eyeball the order — compute every score, sort descending, then assign ranks. Break the B/C tie on a real reason (dependency: B unblocks C), not a decimal, and write it in Notes. Swap columns for the chosen framework — Weighted Scoring shows one column per criterion with its weight; Value/Effort shows a quadrant list; Kano shows the category; MoSCoW shows the bucket. Flag every estimated cell with ⚠.)*

**Recommended order + why**
1. *[Item]* — *[plain-language reason: best return for the effort, unblocks others, etc.]*
2. …

**Close calls to discuss**
- *[Item X vs Item Y]* — separated by *[what factor]*; flip if *[condition]*.

**What would change the ranking**
- *[Which assumption is load-bearing and what evidence would move it — e.g. "if Feature D's reach is real, it jumps to #1; validate before committing."]*

**Strategic exceptions (scored against a different goal)**
- *[Item ranked low here but pulled forward anyway — name the OTHER goal it serves (a strategic bet, a key-account commitment, a compliance deadline, an unblock) and why that goal beats the rubric this cycle. This is a deliberate override, not a misranking: the item scored honestly against the stated goal and lost, and you're choosing it for a reason the formula doesn't measure. Leave empty if there are none.]*

## Avoid (anti-patterns)
- **Precise-looking scores built on guesses.** A "6,400" off three estimates isn't precise. Discount Confidence and label estimates so nobody mistakes a guess for a measurement.
- **Effort estimated by the PM, not eng.** You don't size the build — engineering does. PM-invented effort numbers quietly rig every ratio.
- **The loudest stakeholder overriding the score silently.** Overrides are fine — but write down *why* the strategic exception beats the rubric, so it's a decision, not a hijack.
- **Treating the number as the decision.** The score ranks; you decide. Strategy, sequencing, dependencies, and timing live outside the formula.
- **Mixing grains.** Don't score a one-day tweak against a quarter-long rebuild in the same table — split them.
- **Re-scoring to justify a predetermined answer.** If you're nudging inputs to make your favorite win, stop and say so out loud instead.

## Tips
- Score the inputs, not the rank. Get Reach/Impact/Effort right per item and let the order fall out.
- One goal per prioritization pass. Two metrics = two rankings; don't blend them.
- When two items tie, the tie-breaker is usually a dependency or a strategic bet, not a decimal.
- Treat 50% Confidence as a "go validate first" floor for items you intend to commit to — but you MAY score below 50% to reflect an honest guess on a genuinely speculative item. A sub-50% score isn't forbidden; it's a flag that says "validate before committing," and it keeps a speculative item from being silently inflated to look more certain than it is.
- Keep a one-line evidence note per score. Future-you (and skeptics) will ask "where did this come from?"
- Re-run after big launches or data changes — priorities are perishable, not permanent.
