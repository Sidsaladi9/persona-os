---
name: opportunity-solution-tree
description: Builds a Teresa Torres-style opportunity solution tree that maps customer opportunities to a desired outcome, then to solutions and experiments. Use when the user asks to "build an opportunity solution tree", "map opportunities to our outcome", "OST for X", "structure our discovery", or "what should we focus discovery on". Keeps the team from jumping straight to solutions.
---

# Opportunity Solution Tree

A visual model from Teresa Torres' *Continuous Discovery Habits* that connects a single desired outcome to the customer opportunities (unmet needs, pains, desires) that could drive it, then to candidate solutions, then to the experiments that test the assumptions each solution rests on. The tree forces a clear line of sight from business outcome to customer problem, and keeps discovery focused on the opportunity space before the solution space.

**Grounded in:** *Continuous Discovery Habits* — Teresa Torres: the opportunity solution tree (outcome → opportunities → solutions → experiments).
**Go deeper (The Product Channel):** [Jobs-to-be-Done](https://sidsaladi.substack.com/p/week-28-uncover-your-customers-deepest)

## When to use this
- You have an outcome to move but aren't sure which customer problem to attack first.
- The team keeps debating features before agreeing on the problem.
- You've done (or are about to do) customer interviews and need to structure what you heard.
- You want to make prioritization defensible — show *why* this opportunity, not that one.
- A stakeholder asks "what are we working on and why does it ladder up?"

## The structure
- **OUTCOME** — one measurable business or product outcome at the root (e.g. "increase weekly active teams by 15%"). Not a feature, not a vanity metric. One tree, one outcome.
- **OPPORTUNITIES** — customer needs, pain points, and desires surfaced from research, phrased as *problems* ("I can't tell which teammate changed the doc"), not solutions. Group and nest related ones into themes and sub-opportunities.
- **SOLUTIONS** — concrete ideas that address one specific target opportunity. Always generate several per opportunity so you have real options.
- **EXPERIMENTS** — assumption tests that de-risk a solution before you build it (prototype, fake door, concierge, interview, A/B). One solution depends on *several* assumptions; the tree shows the **lead experiment** (the test of the single riskiest assumption) per solution, and a separate assumptions block carries the rest. Test the riskiest first.
- **Non-target opportunity branches carry no solutions until promoted** — only the target opportunity is expanded into solutions and experiments; the rest stay as bare problem nodes until you pick them next.

## Before you start (gather these)
- **The target outcome** — a single metric with a direction. If the user only has an output ("ship the redesign") or an input metric, push to reframe as an outcome.
- **Research inputs** — interview notes, support tickets, survey verbatims, session recordings, sales-call themes. Opportunities should be *harvested* from these, not invented.
- **If there's no research:** say so plainly. Every opportunity is then an assumption to validate, label them as such, and offer the customer-interview skill to generate real evidence before committing roadmap to the tree.

## Process
1. **State the outcome.** Write one measurable outcome at the root. If it's a feature or output, reframe it as the customer/business change you actually want.
2. **Harvest opportunities from research.** Pull every distinct need, pain, and desire from the notes. Phrase each as a customer problem in their words. If you catch yourself writing a feature, ask "what problem would that solve?" and write *that*.
3. **Group and nest.** Cluster related opportunities into themes; break big opportunities into sub-opportunities. The tree should read top-down from broad need to specific moment.
4. **Pick ONE target opportunity.** Score each candidate **1–5** on three dimensions, then compare totals so the choice is defensible:
   - **Reach** (1 = a sliver of users, 5 = nearly everyone) — how many hit it.
   - **Impact** (1 = mild annoyance, 5 = blocks the job-to-be-done) — how badly it hurts.
   - **Strategic fit** (1 = tangential, 5 = directly moves *this* outcome) — does solving it ladder up.

   | Opportunity | Reach (1–5) | Impact (1–5) | Strategic fit (1–5) | Total |
   |---|---|---|---|---|
   | <opportunity A> | 4 | 5 | 5 | 14 |
   | <opportunity B> | 5 | 3 | 2 | 10 |

   Choose the highest-scoring one to attack now; the rest stay on the tree as future targets.
5. **Generate 3+ solutions for the target.** Diverge. Multiple distinct ideas, not one obvious one — you need options to compare.
6. **Identify the riskiest assumptions.** For your leading solution(s), list what must be true for it to work (desirability, viability, feasibility, usability). Flag the assumptions that would kill it if false.
7. **Define experiments.** For each riskiest assumption, design the smallest test that would expose it. Cheapest, fastest test first.

## Output template
```
OUTCOME: <one measurable outcome>

├─ OPPORTUNITY (theme): <customer problem>
│   ├─ <sub-opportunity / problem>
│   └─ <sub-opportunity / problem>
│
├─ OPPORTUNITY (theme): <customer problem>
│   └─ ...
│
└─ ★ TARGET OPPORTUNITY: <customer problem>   (only the target carries solutions)
     ├─ SOLUTION 1: <idea>
     │     └─ LEAD EXPERIMENT: <test of its single riskiest assumption>
     ├─ SOLUTION 2: <idea>
     │     └─ LEAD EXPERIMENT: <test>
     ├─ SOLUTION 3: <idea>
     │     └─ LEAD EXPERIMENT: <test>
     └─ … (add more solutions as needed — 3 is a floor, not a cap)
```
*The tree shows one LEAD experiment per solution. The full set of assumptions each solution rests on lives in the block below.*

**Target opportunity + why:** <which one, and the reach × impact × strategic-fit scores and reasoning>
**Riskiest assumptions (leading solution):** the beliefs that must be true, by category —
- *Desirability* — <do customers want it?>
- *Viability* — <does it work for the business?>
- *Feasibility* — <can we build it?>
- *Usability* — <can customers figure it out?>
(Mark which one is riskiest — that's what the LEAD experiment tests; map any others to their own experiment.)
**Next experiment:** <the single cheapest test to run first, and what result would change the plan>

## Avoid (anti-patterns)
- Opportunities written as solutions — "add a dashboard" is a solution; the opportunity is "I can't see status at a glance."
- A tree with no outcome at the root — without it, nothing can be prioritized.
- Skipping straight to solutions before the opportunity space is mapped.
- One opportunity with one solution — that's a decision already made, not a tree with options.
- Opportunities invented from opinion instead of harvested from research.
- A sprawling outcome (two or three metrics at once) — split into separate trees.

## Tips
- Use the customer's words for opportunities — it keeps them as problems, not solutions in disguise.
- Sized right: an opportunity is solvable by a few solutions. Too broad ("be easier to use") → break it down.
- Solve one opportunity well before widening the tree; depth beats breadth.
- Revisit weekly. New interviews add opportunities; experiment results prune branches. The tree is living, not a one-time artifact.
- Test the riskiest assumption first, not the easiest — that's where the learning is.
