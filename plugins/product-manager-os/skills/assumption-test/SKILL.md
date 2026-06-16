---
name: assumption-test
description: Surfaces the hidden assumptions an idea depends on, sorts them by risk (likelihood-it's-false × damage-if-false) across desirability, viability, feasibility, and usability, then designs the cheapest test for the riskiest ones. Use when you say "what has to be true for this to work," "what's the riskiest assumption," "should we validate before building," "how do we de-risk this bet," or "this idea feels shaky and I can't say why."
---

# Assumption Test

This skill runs a riskiest-assumption test on an idea. It decomposes the idea into the leap-of-faith assumptions it silently depends on, classifies each across the four risk lenses — **desirability** (do they want it?), **viability** (does it make us money / fit strategy?), **feasibility** (can we build it?), and **usability** (can they use it?) — then ranks by risk and designs evidence-cheap experiments for the top few. The goal is not to validate the idea. It's to find the assumption that, if false, kills the idea, and test that first for the least money and time.

**Grounded in:** *Testing Business Ideas* — David J. Bland & Alex Osterwalder: map desirability/viability/feasibility risks and test the riskiest cheaply.
**Go deeper (The Product Channel):** [Learning from Experiments](https://sidsaladi.substack.com/p/learning-from-experiments-a-superpower)

## When to use this
- A new feature, product, or business idea has momentum but no one has named what has to be true for it to work.
- You're about to commit engineering or budget to a bet and want to de-risk before building.
- A pitch or PRD reads confident but rests on guesses dressed as facts.
- Two stakeholders disagree on whether an idea is good — usually they're betting on different assumptions.
- A launch underperformed and you want to reconstruct which assumption was actually false.

## Before you start (gather these)
- **The idea, stated in one sentence** — what you'd build/launch and for whom.
- **The target user/segment** and the job or problem it addresses.
- **The intended business outcome** (revenue, retention, acquisition, cost) and roughly how it's supposed to happen.
- **What's already known vs. believed** — any data, prior tests, or customer signal.
- **Constraints** — timeline, budget, team, technical limits.

If two or more of these are missing or vague, ASK 2–4 sharp clarifying questions before proceeding — e.g. "Who specifically is this for, and what do they do today instead?", "How does this make money — new revenue, retention, or cost?", "What's the one thing you're most/least sure of?", "What's your time and budget ceiling to validate before building?". If the inputs are already provided, proceed and state any assumptions you're making inline.

## Process
1. **Restate the idea as a chain of dependencies.** Write the idea, then "For this to succeed, the following must all be true…" Force the implicit into the open. Every "they'll obviously…" and "we can just…" is an assumption.
2. **Enumerate assumptions across all four lenses.** Don't stop at desirability (the usual blind spot in reverse — teams over-test "do they want it" and skip viability/feasibility). Aim for 8–15 raw assumptions. Tag each: Desirability / Viability / Feasibility / Usability.
3. **Score each on two axes, 1–5.** *Likelihood it's false* (how much is this a guess vs. evidenced?) and *Damage if false* (does the idea survive, wobble, or die?). Risk = Likelihood × Damage. Be honest: an assumption you have data for scores low on likelihood even if damage is high.
4. **Rank and draw the line.** Sort by risk score. The top 1–3 are your **riskiest assumptions** — the leap-of-faith bets. Everything else can wait or be monitored.
   - **Nested / correlated assumptions:** if a top-3 assumption can only be answered *inside* another's experiment (e.g. a pricing assumption that's really observed during the same fake-door test that probes demand), collapse it into that experiment as a second measured metric rather than designing a duplicate test — note it as "tested within RA_". Give it a **standalone test only if** it can fail independently of the parent (the parent could pass while this fails) or it needs a different population, channel, or fidelity to get a clean read. When in doubt, keep them separate: a collapsed test that conflates two failures tells you nothing about which assumption broke.
5. **For each riskiest assumption, design the cheapest decisive test.** Define: the precise hypothesis, the test (smallest possible — interview, fake door, concierge, prototype, spreadsheet model, spike), the **metric**, the **pass/fail threshold set in advance**, the cost/time, and what you'll do on pass vs. fail. Prefer evidence you can get this week over a perfect study next quarter.
6. **State the kill criteria.** Name the result that should stop the idea. If no result would stop you, you're not testing — you're seeking permission.

## Output template

```markdown
# Assumption Test: [Idea name]

**Idea (one sentence):** [What we'd build/launch, for whom]
**Target user:** [Segment + the job they're hiring this for]
**Intended outcome:** [Business result + the mechanism that produces it]
**Known vs. believed:** [What we have evidence for; what's still a guess]
**Constraints:** [Time / budget / team / technical]

## For this to succeed, all of these must be true
[Plain-language dependency chain — 2–4 sentences walking from idea to outcome, exposing the leaps.]

## Assumption inventory

| # | Assumption (stated as a claim) | Lens | Likelihood false (1–5) | Damage if false (1–5) | Risk | Evidence today |
|---|-------------------------------|------|:---:|:---:|:---:|----------------|
| 1 | [e.g. "Users will switch from their current workaround"] | Desirability | [4] | [5] | [20] | [None / anecdote / data] |
| 2 | [e.g. "We can charge $X and stay above CAC"] | Viability | [ ] | [ ] | [ ] | [ ] |
| 3 | [e.g. "We can ship the core flow in one quarter"] | Feasibility | [ ] | [ ] | [ ] | [ ] |
| 4 | [e.g. "Users complete setup without help"] | Usability | [ ] | [ ] | [ ] | [ ] |
| … | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

> Lens key — **D**esirability: do they want it? **V**iability: does it make us money / fit strategy? **F**easibility: can we build it? **U**sability: can they use it?
> Risk = Likelihood × Damage. Score guesses high on likelihood; score evidenced claims low.
> **Tie-break (clustered scores):** when several assumptions land on the same risk score, break the tie by (1) **cost-to-test** — test the cheapest first, since a cheap fail kills the idea for less — and (2) **dependency order** — test the most-upstream assumption first, because if a foundational one is false the downstream ones may not be worth testing at all.

## Riskiest assumptions (the leap-of-faith bets)
The top [1–3] by risk score — test these before building anything:

### RA1 — [Assumption restated] (Lens: [D/V/F/U] · Risk: [score])
- **Hypothesis:** [Specific, falsifiable: "At least __% of [segment] will __."]
- **Cheapest test:** [Smallest experiment — interviews / fake door / concierge / prototype / pricing test / model / spike]
- **Metric:** [The single number that decides it]
- **Baseline or holdout:** [The counterfactual the metric is read against — current/control rate, an unexposed holdout, or a comparable benchmark. Behavioral metrics are meaningless without one: "12% clicked" only matters vs. what they'd do otherwise. State "N/A — absolute threshold" only if the metric is self-contained.]
- **Pass / fail threshold (set now):** Pass if [≥ X]; fail if [< X]
- **Cost & time:** [$ / days]
- **If pass →** [next move]  ·  **If fail →** [pivot or kill]

### RA2 — [...]
[Repeat structure.]

### RA3 — [...]
[Repeat structure.]

## Kill criteria
[The result(s) that should stop this idea outright. If you can't name one, you haven't designed a real test.]

## Test sequence
1. [RA_ — cheapest/fastest first] — owner: [name] · by: [date]
2. [RA_] — owner: [name] · by: [date]
[Run in order; a fail early kills the idea before you spend on later tests.]

**Budget reconciliation:** Total cost of all tests above = [$ / days]. This must fit under the validate-before-build ceiling stated in *Before you start*. If the sum exceeds the ceiling, you are over-investing to validate — drop to cheaper test methods, cut to fewer riskiest assumptions, or sequence so an early cheap fail removes the need for later spend. State the ceiling and the sum explicitly so the gap (or headroom) is visible.
```

## Avoid (anti-patterns)
- **Only testing desirability.** Most idea graveyards are full of things people wanted but that couldn't make money (viability) or ship in time (feasibility). Force all four lenses.
- **Confirmation-seeking tests.** A survey that asks "would you use this?" is theater. Test behavior (will they click, pay, or do the work), not stated intent.
- **No pre-set threshold.** Without a pass/fail number decided *before* the test, any result gets rationalized as a green light.
- **Testing the cheap-and-comfortable assumption instead of the riskiest one.** Teams test what's easy to test. Rank by risk and test the top of the list even if it's awkward.
- **Treating evidenced facts as assumptions (and vice versa).** Padding the inventory with things you already know wastes test budget; smuggling a guess in as a "known" hides the bet that will kill you.

## Tips
- A useful gut check for "likelihood it's false": *Would I bet my own money on this at even odds?* If you hesitate, it's a guess — score it high.
- The riskiest assumption is usually the one nobody wants to test because the answer might be no. That avoidance is the signal.
- Cheapest tests in rough order: existing data → customer interviews → fake door / smoke test → concierge / Wizard-of-Oz → clickable prototype → engineering spike. Climb only as far as you must to get a decisive answer.
- Re-run this whenever a test result comes back — answering one assumption often promotes a new one to riskiest. The inventory is a living document, not a one-time gate.
