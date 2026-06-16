---
name: red-team
description: Adversarially attacks a PRD, strategy, or plan to find its holes before reality does — naming load-bearing assumptions, weakest links, and what a skeptical exec or competitor would exploit. Steelmans the plan first, then attacks it hard. Use when you're about to ship a doc to leadership, "this feels too clean," "what am I missing," "poke holes in this," "what would kill this," or prepping for a tough review.
---

# Red Team

Adversarial review: steelman the plan in its strongest form, then attack it like a skeptical exec, a rival, and reality itself would. The goal is to surface the assumptions and weak links that decide success — while it's still cheap to fix them.

**Grounded in:** *Red Teaming* — Bryce Hoffman: attack the plan's load-bearing assumptions and diagnosis before reality does.
**Go deeper (The Product Channel):** [Why Every PM Needs to Master AI Evals](https://sidsaladi.substack.com/p/why-every-pm-needs-to-master-ai-evals)

## When to use this
- You're about to send a PRD, strategy memo, or business case to leadership and want it bulletproof before someone else finds the holes.
- A plan "feels right" and nobody's pushed back — which usually means nobody has looked hard enough.
- You're prepping for a tough review (exec, board, investor, architecture) and need to know the questions before they're asked.
- A bet is large, hard to reverse, or rests on a few key assumptions you haven't tested.
- A competitor or regulator could undercut the plan and you want to game out their move first.

## Before you start (gather these)
- **The artifact itself** — the full PRD, strategy doc, or plan text (not a summary).
- **The core claim** — what this plan asserts will happen and why (the thesis in one sentence).
- **Stakes & reversibility** — how big the bet is, how hard it is to undo, who's accountable.
- **The skeptic** — who will attack this in real life (CFO, eng lead, competitor, customer, regulator) and what they care about.

If two or more of these are missing or vague, ASK 2-4 sharp questions before attacking — e.g., "What's the one sentence this plan is betting on?", "Who's the toughest person in the room and what do they care about?", "What would have to be true for this to work?", "Is this reversible if it fails?" If the artifact and core claim are already provided, proceed and state your assumptions inline.

## Process
1. **Steelman first.** Restate the plan in its strongest, most charitable form — the version its author wishes they'd written. You haven't earned the right to attack until you can argue *for* it better than they did. If you can't steelman it, the plan is too vague to red-team; send it back.
2. **Extract load-bearing assumptions.** List every claim the plan silently depends on. For each, ask: *if this is false, does the plan collapse?* Keep only the ones that do — those are load-bearing. Rank them by how load-bearing and how shaky.
   - **Test the diagnosis, not just the solution.** Before attacking the fix, attack the problem statement. Does the plan *assume* the cause of the problem, or has it *proven* it? A flawless solution to the wrong root cause fails just as hard. Ask: "What's the evidence this is actually why X is happening — and not a correlated symptom?"
3. **Find the weakest link.** A plan fails at its weakest assumption, not its average. Identify the single assumption most likely to be wrong AND most catastrophic if it is. That's the kill shot — name it explicitly.
4. **Run the adversary lineup.** Attack from each hostile perspective in turn: the **skeptical exec** (why is this not worth the money/risk?), the **competitor** (how do I exploit or leapfrog this?), the **engineer** (what breaks at scale / what's hand-waved?), the **customer** (why won't I adopt/pay?), and **reality** (what second-order effect bites you in 6 months?).
5. **Pre-mortem.** Assume it's 6 months later and the plan failed. Write the post-mortem headline. Work backwards to the most probable failure path — usually it's already visible in step 3.
6. **Pressure-test the metrics.** Are the success metrics gameable, lagging, or vanity? Could the plan "hit its numbers" and still fail the real goal? Name the metric that would actually prove this worked.
   - **Demand a clean proof for behavior-change and retention claims.** If the plan claims it will change user behavior, lift retention, or move a conversion rate, ask: *does the proof require an A/B test or holdout?* A before/after number is almost always confounded — seasonality, a concurrent launch, audience mix, or selection all masquerade as the effect. Flag any "we'll know it worked because the number went up" as unproven until there's a control.
7. **Separate fatal from fixable.** Sort every hole into *fatal* (rethink the plan), *serious* (must address before shipping), or *minor* (note and move on). Don't drown a real kill shot in nitpicks.
8. **Prescribe.** For each serious-or-fatal hole, give the cheapest test that would resolve the uncertainty, or the specific change that closes it. A red team that only breaks things is half a red team.

## Output template

```markdown
# Red Team Review: [Plan / PRD name]
**Reviewer stance:** Adversarial • **Date:** [date] • **Stakes:** [size / reversibility]
<!-- Stakes examples: "~$2M and a quarter of eng time; hard to reverse once we migrate." • "Reputational — this is the board's first look at the new strategy." • "Low-cost, fully reversible — but it sets a precedent for how we scope the next three." -->


## The bet, stated plainly
This plan is betting that **[one-sentence thesis]**. If that's true, it works.

## Steelman (the strongest version)
[2-4 sentences arguing FOR the plan better than the original. The case at its best.]

## Verdict
**[SHIP / SHIP WITH FIXES / RETHINK]** — [one line: the single most important reason.]
> If the doc bundles a strategy claim *and* an artifact (e.g. a thesis plus the PRD that executes it), give a **SPLIT verdict** — name which part gets which call. E.g. *"Strategy: RETHINK (the market-size bet is unproven). Artifact: SHIP-WITH-FIXES (the spec is sound once the metric is fixed)."* Don't average a strong artifact and a broken thesis into one muddy verdict.
> **Assumptions I couldn't verify / inputs I'd need (optional):** [for partial-info reviews — list the claims you had to take on faith and the data that would let you finish the review.]

## Load-bearing assumptions
| # | Assumption | If false, then... | Confidence it's true | Load-bearing? |
|---|-----------|-------------------|----------------------|---------------|
| 1 | [assumption] | [consequence] | Low / Med / High | 🔴 Critical |
| 2 | [assumption] | [consequence] | Low / Med / High | 🟡 Important |
| 3 | [assumption] | [consequence] | Low / Med / High | ⚪ Minor |

## The kill shot
**Weakest link:** [the single assumption most likely wrong AND most catastrophic.]
**Why it's fragile:** [evidence / reasoning.]
**If it breaks:** [what happens to the plan.]

## The adversary lineup
| Attacker | Their move | How much it hurts |
|----------|-----------|-------------------|
| Skeptical exec | "[the question that derails the meeting]" | 🔴 / 🟡 / ⚪ |
| Competitor | [how they exploit or leapfrog this] | 🔴 / 🟡 / ⚪ |
| Engineer | [what's hand-waved / breaks at scale] | 🔴 / 🟡 / ⚪ |
| Customer | [why they won't adopt or pay] | 🔴 / 🟡 / ⚪ |
| Reality | [second-order effect in 6 months] | 🔴 / 🟡 / ⚪ |

## Pre-mortem
**It's [6 months out] and this failed. The headline:** "[failure headline]."
**Most probable failure path:** [step-by-step how it went wrong.]

## Metrics under pressure
- **Gameable / vanity metric:** [metric] — could hit it and still fail because [reason].
- **The metric that would actually prove this worked:** [the honest one].

## Holes, sorted
**🔴 Fatal (rethink):**
- [hole] → **Fix / test:** [cheapest way to resolve]

**🟡 Serious (fix before shipping):**
- [hole] → **Fix / test:** [specific change or experiment]

**⚪ Minor (note and move on):**
- [hole]

## If I had to save this plan
[2-3 sentences: the smallest set of changes that would move the verdict from RETHINK to SHIP.]
```

## Avoid (anti-patterns)
- **Nitpicking instead of finding the kill shot.** Twelve typo-grade objections bury the one assumption that actually sinks the plan. Lead with the kill shot.
- **Skipping the steelman.** Attacking a weak paraphrase is a strawman, not a red team. If you can't argue *for* it first, you'll attack the wrong thing.
- **Pessimism as a personality.** "This is risky" isn't a finding. Every objection must name *which* assumption is wrong and *what* breaks if it is.
- **Breaking without prescribing.** Listing holes with no cheapest-test-to-resolve makes the author defensive and the review useless.
- **Treating all holes as equal.** A fatal flaw and a wording quibble in the same bullet list tells the reader nothing about what to actually do.

## Tips
- The weakest assumption is usually the one the author was most confident about — confidence is where blind spots hide. Probe the parts stated as obvious.
- "What would have to be true?" is the sharpest single question. Run it on every claim until you hit one nobody can defend.
- Name a real adversary, not a generic one. "The CFO who killed the last two roadmap asks" generates sharper attacks than "a skeptic."
- Distinguish *risky* from *fragile*: a risky plan can fail in many small ways; a fragile one dies if one specific thing breaks. Fragile is more dangerous and easier to fix — hunt for it.
