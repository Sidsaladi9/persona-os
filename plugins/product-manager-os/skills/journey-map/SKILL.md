---
name: journey-map
description: Build a customer journey map across stages — actions, thoughts, emotions, touchpoints, pain points, and the single biggest opportunity per stage — grounded in evidence with assumptions flagged. Use when someone says "map the customer journey", "build a journey map", "where do users drop off", "what's the experience from awareness to renewal", or "turn this research into a journey".
---

# Journey Map

A customer journey map traces one persona's experience through the stages of using your product — what they do, think, and feel at each step, where they touch you, where it hurts, and where the biggest opportunity to improve sits. Done well, it converts scattered research into a shared, prioritized view of where to fix the experience. Done badly, it's a colorful grid of guesses nobody acts on.

**Grounded in:** *Mapping Experiences* — Jim Kalbach: align stages, emotions, and pain points to find the biggest opportunity per stage.
**Go deeper (The Product Channel):** [User Journey Map](https://sidsaladi.substack.com/p/week-13-user-journey-map)

The discipline is twofold: **one persona + one scenario per map**, and **every cell traces to evidence or is flagged as an assumption.** Mixing personas or laundering guesses as fact is how journey maps become wall art.

## When to use this
- You have research (interviews, support tickets, analytics funnels, session recordings, sales/CS notes) and need to see the end-to-end experience, not isolated metrics.
- Users are dropping off and you don't yet know at which stage or why — you need to localize the pain before you fix it.
- A cross-functional team (design, eng, support, marketing) keeps optimizing their own slice and nobody owns the whole experience.
- You're entering onboarding, activation, or renewal work and want to know where the highest-leverage fix lives.
- You're aligning a team early with thin data and want an explicit, testable map of assumptions rather than a vibe.

## Before you start (gather these)
- **The persona** — whose journey is this? One persona per map. If you're tempted to map "all users," you're about to make an unusable average.
- **The scenario and scope** — the specific goal and the start/end boundary (e.g. "first-time user, signup → first value" or "existing customer, renewal decision"). One scenario per map.
- **The stages** — either a known stage model (Awareness → Consideration → Onboarding → Activation → Habit → Renewal/Advocacy) or let them emerge from the research. Don't force a generic funnel if the real journey differs.
- **Evidence** — interview quotes, support-ticket tags and volumes, funnel/analytics drop-off points, session recordings, NPS/CSAT verbatims, sales-call notes. List what you actually have.

If the persona OR the scenario is missing or vague, or you have no evidence to anchor cells, **ASK 2–4 sharp clarifying questions before mapping** — e.g. "Which persona is this for?", "Where does the journey start and end?", "What research can I ground this in?", "Is the goal to find drop-off or to design a new flow?" If the inputs are already provided, proceed and **state assumptions inline** as you go (tag `[ASSUMPTION]`).

## Process
1. **Lock the persona and scenario.** Write them at the top of the map. Every cell below answers "for *this* persona, doing *this* thing." If a finding belongs to a different persona, it doesn't go on this map.
2. **Define the stages.** Use 4–7 stages. Prefer stages the user would recognize from their own experience over internal funnel labels. Name them as the user's progress, not your process ("Trying to get it working," not "Activation phase 2").
3. **Fill each stage across six lanes:** *Actions* (what they actually do), *Thoughts* (the question or self-talk in their head), *Emotions* (the felt state + intensity), *Touchpoints* (where they interact with you — product, email, support, docs, sales), *Pain points* (friction, confusion, blockers). Use real user language wherever you have it.
4. **Plot the emotional curve.** Rate emotion at each stage on a numeric **−2 to +2 scale** (−2 = frustrated/blocked, 0 = neutral, +2 = delighted). Use one consistent scale across the whole map — never mix numbers with frown→smile icons. The lowest valleys are your priority — a dip that coincides with a drop-off in analytics is the most actionable signal a map produces.
5. **Tag evidence on every cell.** Cite the source inline ("8/12 interviews," "support tag = 22% of volume," "analytics: 47% drop at step 3"). Anything not backed by data gets `[ASSUMPTION]` plus how you'll validate it. A map where most cells are assumptions is a *hypothesis map* — say so.
6. **Name ONE biggest opportunity per stage.** Not a list — the single highest-leverage improvement for that stage, tied to the pain and the evidence. Forcing one sharpens prioritization; a stage with five "opportunities" has none.
7. **Rank opportunities across the whole journey.** Pull the per-stage opportunities into a prioritized shortlist (impact × evidence-strength × effort), capped at the **top 3–5**. Assign each an **owner**. When two opportunities tie on score, break the tie by preferring **lower effort first**, and if still tied, the one **upstream in the journey** (fixing an earlier stage compounds downstream). This is what the team acts on Monday.

## Output template

```
# Journey Map: [Persona name] — [scenario, e.g. "first-time user: signup → first value"]

**Persona:** [name + one-line descriptor]
**Scenario / scope:** [goal] · [start boundary] → [end boundary]
**Evidence base:** [what this is grounded in — e.g. "14 interviews, support tags, activation funnel"] · [HYPOTHESIS MAP if assumptions outnumber sourced cells]
**Data gaps / not available:** [what you could NOT ground — e.g. "no analytics funnel for renewal stage; no CS notes; emotions inferred, not interview-sourced"]

## Stage-by-stage
<!-- Column count scales with your chosen stage count (4–7), not a fixed 5. Add or remove stage columns across every lane row. -->

| Lane | [Stage 1] | [Stage 2] | [Stage 3] | [Stage 4] | [Stage 5] |
|---|---|---|---|---|---|
| **Actions** | [what they do] | [...] | [...] | [...] | [...] |
| **Thoughts** | "[the question in their head]" | [...] | [...] | [...] | [...] |
| **Emotions** | [feeling] (score: [-2..+2]) | [...] | [...] | [...] | [...] |
| **Touchpoints** | [channel/surface] | [...] | [...] | [...] | [...] |
| **Pain points** | [friction/blocker] | [...] | [...] | [...] | [...] |
| **Evidence** | [source] / [ASSUMPTION — validate by: …] | [...] | [...] | [...] | [...] |

## Emotional curve
One row, numeric −2..+2 scale (same scale as the Emotions lane). One column per stage.

| Stage | [Stage 1] | [Stage 2] | [Stage 3] | [Stage 4] | [Stage 5] |
|---|---|---|---|---|---|
| **Emotion (−2..+2)** | [+1] | [0] | [−2] | [−1] | [+1] |

Lowest point: **[Stage X]** — [one line on why this valley matters most]

## Biggest opportunity per stage
| Stage | Biggest opportunity (one only) | Tied to pain | Evidence strength |
|---|---|---|---|
| [Stage 1] | [the single highest-leverage fix] | [which pain it removes] | [strong / medium / assumption] |
| [Stage 2] | [...] | [...] | [...] |
| [Stage 3] | [...] | [...] | [...] |
| [Stage 4] | [...] | [...] | [...] |
| [Stage 5] | [...] | [...] | [...] |

## Prioritized shortlist (act on these — top 3–5 only)
1. **[Opportunity]** — [stage] · impact: [H/M/L] · evidence: [strong/medium/assumption] · effort: [H/M/L] · owner: [name/role] — [why it's #1; on a tie, lower effort wins, then upstream stage]
2. **[Opportunity]** — [...] · owner: [name/role]
3. **[Opportunity]** — [...] · owner: [name/role]

## Open questions to validate
- [ASSUMPTION on stage X] — validate by: [5 interviews / funnel analysis / survey question / session replays]
```

## Avoid (anti-patterns)
- **Mapping multiple personas on one map.** Averaging a power user and a first-timer produces a journey nobody actually has. One persona, one scenario, or split it into two maps.
- **Guesses dressed as findings.** Unsourced emotions and pains presented as fact mislead the whole team. Tag `[ASSUMPTION]` and say when the map is mostly hypothesis.
- **Five opportunities per stage.** That's a backlog, not a prioritization. Force exactly one biggest opportunity per stage — the constraint is the value.
- **Internal-process stages.** "Activation phase 2" means nothing to the user. Name stages as the user's lived progress, or the emotions and pains won't line up with anything real.
- **A beautiful map that changes no decision.** If it doesn't end in a ranked shortlist someone owns, it's wall art. The output is the prioritized fix list, not the grid.

## Tips
- Anchor the emotional curve to your analytics funnel — the stage where an emotional valley and a drop-off point coincide is almost always your #1 opportunity.
- Quote users verbatim in the Thoughts and Pain lanes. "I have no idea if it saved" is more persuasive and harder to argue with than "user feels uncertain."
- If a connector is available (Amplitude, Pendo, Intercom, Zendesk, GA), pull real drop-off rates and top support tags per stage — but the map must still work end-to-end from pasted data alone.
- Build it once with the team in the room, then keep it living: re-walk it after a major release and retire stages or opportunities that no longer reflect reality.

---
*Make it shareable: the `visualize` skill renders this as a swimlane — a self-contained HTML visual you can screenshot into a deck or Slack.*
