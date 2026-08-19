---
name: value-proposition
description: Maps what customers actually want against what your product relieves and creates, using the Value Proposition Canvas, and produces the fit assessment plus the statements that come out of it. Use when a PM says "what's our value prop", "map the value proposition", "why do customers care", "our messaging isn't landing", or when the product does many things and nobody can say which one is the reason people buy.
tier: guided
time: 45-90 min
inputs: evidence of customer jobs, pains, and gains — interviews, tickets, or sales calls
outputs: strategy/value-proposition.md
---

# Value Proposition

Maps the customer side (jobs, pains, gains) against the product side (pain relievers, gain creators), then judges the fit honestly — including the features that relieve nothing. Distinct from `positioning`, which decides the competitive frame you compete inside; this decides whether the value is real before you go frame it.

**Grounded in:** *Value Proposition Design* — Osterwalder, Pigneur, Bernarda & Smith: profile the customer *before* the product, rank jobs by importance and pains by severity, and score fit only where a reliever meets a ranked pain. The rule that does the work: **fit is claimed only against a pain or gain the customer ranked highly**, not against every feature you can attach to something.

**The load-bearing idea:** most value propositions fail on the customer side, not the product side. A beautifully specified reliever aimed at a pain nobody ranks is the most common form of wasted engineering.

## When to use this
- Messaging isn't landing and you suspect the problem is upstream of the copy.
- The product does eight things and the team disagrees about which one people buy it for.
- Before `positioning` or `pricing` — both need a settled view of what value exists.
- Evaluating a new feature: does it relieve a ranked pain, or is it interesting?
- Entering a new segment where the same product meets a different set of jobs.
- After research synthesis, to turn themes into a fit assessment.

## Before you start (gather these)
- **Evidence of customer jobs** — what they're trying to get done, functional and emotional. From interviews, not imagination.
- **Pains, with severity** — obstacles, risks, and bad outcomes, and how much each actually hurts.
- **Gains, with desirability** — what they'd call a better outcome, including the unspoken ones.
- **Your feature list** — what the product actually does today, plainly stated.
- **The segment** — one at a time. A canvas averaged across segments describes nobody.

If two or more are missing, **ask 2-4 clarifying questions before mapping** — starting with *"which single segment is this for?"* If the evidence base is thin, say so and run `synthesize-research` or `customer-interview` first; a canvas built from assumptions is a team's opinions in a diagram, which is worse than no diagram because it looks like evidence. Where `workspace/research/` already holds the inputs, open with an Assumptions block.

## Process
1. **Build the customer profile first, and finish it before looking at the product.** Jobs, pains, gains — sourced, with a quote or number against each. Looking at your feature list first contaminates the profile with what you happen to have built.
2. **Rank ruthlessly.** Jobs by importance, pains by severity, gains by desirability. Most items are not important, and saying so is the point. An unranked canvas cannot produce a fit assessment.
3. **Map the product side.** For each thing the product does, state which ranked pain it relieves or gain it creates. Be strict: "helps with" is not relieving.
4. **Score the fit, honestly, per pairing.** Strong fit = a severe pain met by a reliever that clearly works. Weak = a real pain met partially. None = a feature attached to nothing ranked. **Publish the "none" list** — it's the most useful column on the page.
5. **Find the unrelieved severe pains.** Ranked high, nothing pointed at them. This is your roadmap input, and it's why the canvas is worth doing.
6. **Find the relievers with no pain.** Features that relieve nothing ranked. Candidates for deprecation, or evidence your profile is missing a job.
7. **Write the statements last.** One primary value proposition and two or three supporting ones, each traceable to a strong-fit pairing. A statement that can't be traced back to a ranked pain is copywriting, and you should mark it as such.

## Output template
```markdown
# Value Proposition — [product], [segment]

**TL;DR**
- **Primary value:** [one sentence, traceable to a strong-fit pairing]
- **Strongest fit:** [pain] ← [reliever]. **Weakest link:** [severe pain with no reliever]
- **Fit verdict:** [strong / partial / weak] — [one line]

**Segment:** [one segment only] · **Evidence base:** [n interviews / n tickets / date range]

## Customer profile
### Jobs (ranked by importance)
| # | Job | Type | Importance | Evidence |
|---|---|---|---|---|
| 1 | [what they're trying to get done] | functional/emotional/social | high | [quote or number] |

### Pains (ranked by severity)
| # | Pain | Severity | Evidence |
|---|---|---|---|

### Gains (ranked by desirability)
| # | Gain | Desirability | Expected or delighter? |
|---|---|---|---|

## Product side
### Pain relievers
| Reliever | Relieves pain # | How completely | Evidence it works |
|---|---|---|---|

### Gain creators
| Creator | Creates gain # | How much |
|---|---|---|

## Fit assessment
| Pairing | Fit | Why |
|---|---|---|
| P1 ← [reliever] | 🟢 strong | [severe pain, reliever demonstrably works] |
| P4 ← [reliever] | 🟡 partial | [real pain, partially addressed] |
| — ← [feature] | ⚪ none | [relieves nothing ranked] |

## The gaps that matter
**Severe pains with no reliever** *(roadmap input)*
- **[Pain]** (severity: high, n=[x]) — nothing today addresses this. [What would.]

**Relievers with no ranked pain** *(deprecation or research gap)*
- **[Feature]** — relieves nothing customers ranked. Either the profile is missing a job, or this shouldn't exist.

## Statements
**Primary:** [statement] → traces to [pairing]
**Supporting:**
- [statement] → traces to [pairing]

*Any statement without a traceable pairing is marked `[unsupported]` and should not ship in messaging.*
```

## Avoid (anti-patterns)
- **Building the product side first.** It guarantees a profile shaped like your feature list, and the exercise then confirms whatever you already built.
- **An unranked canvas.** Without severity and importance rankings you cannot distinguish a strong fit from a coincidence.
- **Averaging segments.** Two segments on one canvas produce a value proposition that fits neither. Run it twice.
- **Claiming fit for "helps with".** If it doesn't remove the pain, it's partial — say partial. Inflated fit scores are how teams stop noticing their weakest link.
- **Hiding the "none" column.** Features attached to nothing ranked are the finding. Publishing them is uncomfortable and useful.
- **Writing statements first.** Copy written before the mapping determines what the mapping is allowed to conclude.
- **Treating a delighter as a driver.** For example, a gain customers describe as "nice" will not carry a value proposition, however much the team enjoys it.

## Tips
- 💡 **The unrelieved severe pains list is the highest-value output.** It's a roadmap ranked by customer evidence rather than by whoever argued loudest, and it takes ten minutes once the canvas exists.
- Use verbatim customer language in the pains column. The moment you paraphrase into internal terms, the messaging downstream inherits your jargon.
- Feed the primary statement into `positioning` (to place it competitively) and `pricing` (a value metric should track the strong-fit pairing).
- Re-run when the segment changes, not on a calendar. Same product, new segment, entirely different canvas.
