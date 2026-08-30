---
name: win-loss
description: Runs a win/loss analysis across decided deals to find why you actually win and lose, separating stated reasons from real causes. Use when a PM or PMM says "why are we losing deals", "run a win-loss", "analyze these lost deals", "what's killing our close rate", "sales says it's price", or when the same objection keeps surfacing and nobody has checked it against the data.
tier: guided
time: 60-90 min
inputs: close reasons or deal notes for at least 10 decided deals, wins and losses both
outputs: research/win-loss-<period>.md
---

# Win/Loss Analysis

Turns a pile of decided deals into the two or three things that actually move your close rate — and separates them from the things sales *says* are killing deals. Those are rarely the same list.

**Grounded in:** *The Mom Test* — Rob Fitzpatrick, applied to deals rather than users: a stated reason is an opinion, a behavior is data. Ask what happened, in what order, and what they did instead — never "why didn't you buy?", which reliably returns "price" regardless of the truth. Paired with standard win/loss practice: always analyze wins alongside losses, or you have no control group.

**The load-bearing idea:** "we lost on price" is the most common close reason in every CRM on earth and is usually a proxy for *value not established*. Price is what a buyer says when the answer is no and they'd rather not explain.

## When to use this
- Close rate has moved and nobody can say why with evidence.
- The same objection appears in every deal review and has never been checked against outcomes.
- Before a pricing change, a positioning rewrite, or a roadmap commitment justified by "sales keeps asking for it."
- Quarterly, as a standing input to `positioning`, `pricing`, and `roadmap`.
- When you're about to build a feature because one loud lost deal asked for it.

## Before you start (gather these)
- **At least 10 decided deals** — closed-won and closed-lost both. Under ~10 you have anecdotes; say so rather than producing a confident chart.
- **The stated close reason** for each, from the CRM.
- **Something behavioral per deal** — how far it got, who was in the room, how long it sat, what the last activity was. This is what lets you go past the stated reason.
- **The segment for each deal** — size, industry, inbound vs outbound. Aggregate win/loss across mixed segments hides the answer.
- **Who they went with instead** — including "nothing" and "built it internally", which are competitors and are systematically under-recorded.

If two or more are missing, **ask 2-4 clarifying questions before analyzing.** The one that matters: *"do we have the wins too, or only the losses?"* A loss-only analysis cannot tell you what's different about losing. If the context is already in `workspace/`, open with an Assumptions block instead.

## Process

**Run the `researcher` brief from `WORKERS.md`.** This host has no subagents, so you cannot get a genuinely independent read inside this session. Do it anyway — the brief is worth following — but **label the result a self-review, not an independent critique**, and tell the user how to get the real thing: a fresh session with the artifact pasted in alone. Send the deal notes to `researcher` — wins and losses in **separate** invocations, so neither read is anchored by the other. Ask it to tag every item `stated` or `behavioural`; the whole analysis turns on keeping those apart.
1. **Segment before you count.** Split by deal size, source, and competitor faced. A 22% overall close rate that's 40% inbound and 9% outbound is two different businesses with one misleading number.
2. **Separate stated reasons from causes.** Tabulate the CRM close reasons, then set them aside. They are the starting hypothesis, not the finding. Note the share that say "price" — you will come back to it.
3. **Find where deals die, not why.** Map each deal to the last stage it reached. Losses cluster at a stage, and the stage tells you more than the reason field: dying at first demo is a positioning problem, dying at security review is a product problem, dying after a verbal yes is a champion problem.
4. **Compare wins to losses on the same variables.** For each candidate cause, check the win side. If 60% of losses had no economic buyer in the room but so did 55% of wins, it isn't the cause. **This step is the whole analysis** — everything before it is description.
5. **Test the price claim explicitly.** Compare discount depth on wins vs losses, and check whether "price" losses clustered in a segment where you're genuinely mispriced or spread evenly (which means it's a value problem wearing a price costume).
6. **Rank by frequency × addressability.** A cause in 40% of losses that you cannot change is context. A cause in 15% that you can fix this quarter is a roadmap item. Say which is which.
7. **Write findings as claims with a confidence level and a sample size.** Every finding gets `n=` attached. Then name the two or three actions, each owned, each with the metric that would show it worked.

## Output template
```markdown
# Win/Loss — [period]

**TL;DR**
- [Finding 1 — the cause, the segment, and the size of the effect] *(n=[x])*
- [Finding 2] *(n=[x])*
- [The thing everyone believed that the data does not support]

**Sample:** [n] decided deals ([w] won / [l] lost), [date range]. **Confidence:** [high/medium/low] — [why].

## Where deals die
| Stage | Wins reaching | Losses dying here | Read |
|---|---|---|---|
| [stage] | [n] | [n] | [what dying here means] |

## Stated reasons vs. what the data shows
| Stated reason | Share of losses | Holds up? | What's actually going on |
|---|---|---|---|
| Price | [x]% | [yes/no/partly] | [evidence from the win side] |

## Wins vs. losses on the same variables
| Variable | Wins | Losses | Difference real? |
|---|---|---|---|
| [economic buyer engaged] | [x]% | [y]% | [yes — n=, or no] |

## Findings
### 1. [Finding stated as a claim]
- **Evidence:** [the comparison, with numbers and n]
- **Segment:** [where it's true — and where it isn't]
- **Addressable?** [yes/no, by whom, roughly how long]
- **Confidence:** [high/medium/low] — [what would raise it]

## What we believed that isn't supported
- **[The belief]** — [what the data actually shows]. [Why the belief persisted.]

## Actions
| # | Action | Owner | Metric that proves it worked | By |
|---|---|---|---|---|

## Limits of this analysis
- [Sample size, self-selection, missing segment, CRM data quality — stated plainly.]
- **Not asked:** [the question this data can't answer, and how you'd get it — usually buyer interviews.]
```

## Avoid (anti-patterns)
- **Analyzing losses without wins.** Without a control you can only describe losers, never explain losing. This is the single most common way win/loss goes wrong.
- **Treating CRM close reasons as causes.** They're picked from a dropdown by someone moving on to the next deal.
- **Accepting "price" at face value.** Check discount depth on both sides before you believe it. For example, if losses averaged a 12% discount request and wins averaged 14%, price was not the deciding variable.
- **Aggregating across segments.** Enterprise and self-serve lose for unrelated reasons; averaged together they produce a finding that's true of neither.
- **Sample sizes under ~10 presented as trends.** Report the number, state that it's directional, and resist the chart.
- **Forgetting "no decision" as a competitor.** Deals lost to inertia are usually the largest single bucket and the most fixable.
- **Ending with findings and no owner.** A win/loss with no action is a document, not an analysis.

## Tips
- 💡 **The most useful column is "last stage reached."** It requires no interviews, exists already in your CRM, and tells you more than the reason field ever will.
- If a finding survives only in one segment, that's not a weakness — that's the precision you were looking for. Say where it holds.
- Feed confirmed findings straight into `positioning` (if you're losing at first demo), `pricing` (if discount depth differs), or `roadmap` (if a capability gap repeats across segments).
- Re-run it every quarter with the same method. The trend across quarters is worth more than any single run's finding.
