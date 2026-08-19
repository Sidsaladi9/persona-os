---
name: gtm-strategy
description: Chooses the go-to-market motion and channel mix for a product or segment, and checks the unit economics that make it survivable. Use when a PM or founder says "what's our GTM", "should we go sales-led or product-led", "how do we sell this", "which channel", "our CAC doesn't work", or when a launch plan exists but nobody has decided how the product actually reaches buyers at scale.
tier: guided
time: 90 min+
inputs: ACV or price point, current channels and their cost, and who signs the cheque
outputs: strategy/gtm-<segment>.md
---

# GTM Strategy

Decides *how* the product reaches buyers repeatably — the motion, the channels, and the economics that have to hold for it to work. This is the layer above a launch plan: `launch-plan` runs one release, this decides the machine that runs every release.

**Grounded in:** *Crossing the Chasm* — Geoffrey Moore: pick one beachhead segment and dominate it before widening, because a GTM motion that serves everyone reaches no one. Paired with the SaaS unit-economics discipline (CAC payback and LTV:CAC as constraints, not scorecards) — the motion you can afford is determined by your ACV, and most GTM failures are a motion/ACV mismatch rather than an execution problem.

**The load-bearing idea:** your price point chooses your motion. A $40/year product cannot support a salesperson, and a $200k product will not close itself through a self-serve funnel. Decide the motion the economics permit, then build the channels that feed it.

## When to use this
- Entering a new segment, geography, or market where the existing motion may not carry over.
- CAC payback has stretched and nobody can say which channel is responsible.
- Deciding between self-serve, sales-assisted, and enterprise motions for the same product.
- A launch plan exists but the question "who does this reach, and how, after launch week?" has no answer.
- Before hiring the first salesperson, or before deciding not to.
- When two motions are running at once and quietly competing for the same buyer.

## Before you start (gather these)
- **ACV or price point** — the single biggest determinant of which motions are even available to you.
- **Who signs** — an individual with a credit card, a team lead with a budget, or a procurement process. These need different machines.
- **Current channel performance** — spend and result per channel, however rough. "We don't measure it" is itself a finding.
- **Sales cycle length and touches** — how long from first contact to closed, and how many humans it took.
- **The ICP** — run `icp` first if it doesn't exist. GTM without a defined buyer is channel spending.

If two or more are missing, **ask 2-4 clarifying questions before recommending a motion.** The essential one: *"what's the annual contract value, and who signs it?"* Everything downstream follows from those two. If `workspace/strategy/` already holds the ICP and pricing, open with an Assumptions block instead of re-asking.

## Process
1. **Anchor on the economics first.** Compute what you can afford to spend to acquire a customer: a rough rule is CAC should be recovered inside 12 months of gross profit, and LTV:CAC above 3 is healthy. This number, not preference, eliminates most motions immediately.
2. **Match motion to ACV and buyer.** Roughly: under ~$1k ACV needs self-serve or it loses money on every deal; $1k-$25k supports sales-assisted with inbound doing the qualifying; above ~$25k with a procurement process needs a real sales motion; above ~$100k needs a named-account motion with multi-threading. State the band you're in and what that rules out.
3. **Pick one beachhead.** Name a single segment specific enough that you could list twenty real companies in it. Say explicitly which adjacent segments you are *not* serving yet and what would trigger expansion.
4. **Design the channel mix against the buyer's actual search path.** Where does this buyer already look when they have this problem? Pick two or three channels, not seven. For each, state the expected cost per qualified opportunity and how long it takes to know if it's working.
5. **Check the loop, not just the funnel.** Which part of this compounds — content that ranks, users who invite colleagues, integrations that carry you into new accounts? A GTM with no loop is a treadmill you must keep paying for. Reach for `growth-loops` here.
6. **Name the constraint that breaks first.** At 3x current volume, what fails — lead supply, sales capacity, onboarding, support? Naming it now is what makes the plan survivable.
7. **Define the proof points and the kill criteria.** What result at 30, 60, and 90 days says this motion works, and what result says stop. Write both numbers before you spend.

## Output template
```markdown
# GTM Strategy — [segment]

**TL;DR**
- **Motion:** [self-serve / sales-assisted / enterprise / hybrid] — because [ACV] and [who signs].
- **Beachhead:** [specific segment]. **Not yet:** [adjacent segments, and the trigger to expand].
- **Channels:** [2-3], leading with [one]. **Loop:** [what compounds].
- **Breaks first at 3x:** [the constraint].

## Economics (the constraint everything else obeys)
| | Value | Source |
|---|---|---|
| ACV / price point | | |
| Gross margin | | |
| Max affordable CAC (12-mo payback) | | derived |
| Current CAC | | |
| LTV:CAC | | |
| Sales cycle | | |

**What the economics rule out:** [motions that cannot work at this ACV, stated plainly.]

## Motion
**Chosen:** [motion] — [2-3 sentences on why this and not the alternatives.]
**Rejected:** [motion] — [why: economics, buyer, or capability.]

| Stage | Who does it | Human touch? | Target conversion |
|---|---|---|---|

## Beachhead segment
- **Definition:** [tight enough to list 20 real companies]
- **Why them first:** [most acute pain / fastest to reach / best reference value]
- **Deliberately not yet:** [segment] — expand when [specific trigger]

## Channels
| Channel | Why this buyer is there | Cost per qualified opp | Time to signal | Owner |
|---|---|---|---|---|

## The loop
[What compounds, and the mechanism. If nothing compounds, say so — that's a strategic gap, not an omission.]

## What breaks first
| At 3x volume | What fails | Early warning | Mitigation |
|---|---|---|---|

## Proof points and kill criteria
| Horizon | Works if | Stop if |
|---|---|---|
| 30 days | | |
| 60 days | | |
| 90 days | | |

## What we're explicitly not doing
- [Channel or segment] — [why now is the wrong time.]
```

## Avoid (anti-patterns)
- **Choosing the motion before the economics.** Wanting an enterprise motion on a $600 ACV is the most expensive mistake in this document.
- **A beachhead you can't enumerate.** "Mid-market SaaS companies" is not a segment. If you can't name twenty real targets, tighten it.
- **Seven channels at 10% effort each.** Two channels done properly beat seven done badly, and only the properly-done ones produce a readable signal.
- **A funnel with no loop.** If every customer costs full price to acquire forever, growth is a budget line, not a strategy.
- **Copying a competitor's motion without their economics.** They may have a different ACV, a different margin, or be losing money on it.
- **No kill criteria.** A channel with no stop condition runs for four quarters on hope.
- **Running two motions at the same buyer.** Self-serve and sales at the same account teaches buyers to wait for the discount.

## Tips
- 💡 **Compute max affordable CAC before anything else.** It's one line of arithmetic and it eliminates most of the debate before it starts.
- For example, at a $4,800 ACV with 80% gross margin, a 12-month payback allows roughly $3,800 of CAC — which supports inbound plus a light sales assist, and does not support outbound SDRs at typical loaded cost.
- Write the "explicitly not doing" section first if the team is scattered. It's faster to agree on exclusions than on priorities.
- Revisit when ACV moves by more than ~30% in either direction. A price change is a motion change, whether or not anyone decides it is.
