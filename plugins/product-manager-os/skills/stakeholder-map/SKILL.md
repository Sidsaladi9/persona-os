---
name: stakeholder-map
description: Maps stakeholders onto an influence/interest grid, captures each one's stance, motivations, and decision power, and derives a per-person engagement plan with a RACI overlay. Use when you say "who do I need to get on board," "map my stakeholders," "build a power/interest grid," "figure out who's blocking this," "who decides vs. who's just informed," or "I keep getting surprised by the same exec."
---

# Stakeholder Map

A stakeholder map built on the influence/interest (power/interest) grid plus a RACI overlay: place each person by how much power they hold and how much they care, mark their current stance, then assign decision roles so you know exactly who to win, who to manage, and who to keep warm.

**Grounded in:** *Mendelow's power-interest grid* — Aubrey Mendelow: map influence × interest and tailor engagement per quadrant.
**Go deeper (The Product Channel):** [9 Ways to Influence Without Authority](https://sidsaladi.substack.com/p/week-12-9-ways-to-influence-people)

## When to use this
- Kicking off an initiative that needs sign-off or resources from people outside your direct team.
- A decision keeps stalling and you can't tell who actually has veto power.
- You're repeatedly blindsided by an exec or function that "should have been looped in."
- A launch, migration, or reorg touches multiple teams with conflicting incentives.
- You're new to a role or org and need to map the political terrain before you push anything.

## Before you start (gather these)
- **The initiative**: one sentence on what you're trying to ship, change, or get approved.
- **The decision at stake**: what specifically needs a yes (budget, headcount, scope, go/no-go).
- **The cast**: names + roles of everyone who could approve, block, influence, or be affected.
- **What you know per person**: their stance (supporter → blocker), what they care about, their formal power over this decision.

If you have the initiative but the cast or per-person detail is thin or missing, ASK 2-4 sharp questions before building anything, e.g.: "Who can say no to this and make it stick?" / "Who's the loudest skeptic, and what's their objection?" / "Whose team gets more work if this ships?" / "Who do leadership listen to on topics like this?" If the data is already provided, proceed and state any assumptions (stance, power level) inline so they're easy to correct.

## Process
1. **List the cast.** Every name who can approve, block, influence, fund, or feels the impact. Include the quiet power — the trusted advisor, the skip-level, the eng lead whose word leadership takes.
2. **Score two axes, High/Low each.** *Influence* = formal + informal power over THIS decision (not seniority in general). *Interest* = how much they personally care about the outcome. Be honest, not aspirational.
   - **Tie-break for borderline placement:** when someone sits on the High/Low line, place them by their influence over THIS decision — not their title or seniority. A line VP with no real say here goes Low; a staff eng whose word leadership takes goes High.
3. **Place each into a quadrant** and apply the default play:
   - **High influence / High interest → Manage Closely.** Co-create, give them airtime, no surprises.
   - **High influence / Low interest → Keep Satisfied.** Brief, don't bury; raise their interest only if you need them.
   - **Low influence / High interest → Keep Informed.** Use as champions and a feedback loop; they amplify.
   - **Low influence / Low interest → Monitor.** Light touch; revisit if the initiative grows.
4. **Mark current stance** on a 5-point scale: Blocker · Skeptic · Neutral · Supporter · Champion. Flag each stance with its evidence basis — ✅ confirmed (they told you, you saw it) or ❓ assumed (your read, unverified). Note the gap between where they are and where you need them.
5. **Capture motivation and currency** per person: what they care about (the metric, the risk, the credit) and what would move them. This is the lever, not a personality note.
6. **Overlay RACI for the decision.** Exactly one **A** (Accountable — the single yes/no). Assign **R** (does the work), **C** (consulted before deciding), **I** (informed after). If you have two A's, you have an unresolved fight — flag it. **If the initiative bundles more than one real decision** (e.g. go/no-go AND eng-allocation), split RACI per decision — each gets its own A, R, C, I. The same person can be A on one decision and merely C on another; collapsing them hides the real owner.
7. **Derive one next action per Manage-Closely and per stance gap.** Owner, channel (1:1, group, async doc), and timing relative to the decision date. The map is worthless without these.
8. **Spot the risks**: blockers with high influence, a missing or contested A, coalitions, and anyone you're assuming is a supporter without evidence.

## Output template

```markdown
# Stakeholder Map — [Initiative]

**Decision at stake:** [the specific yes you need]
**Decision date / forcing function:** [date or milestone]
**Owner:** [you]   **Last updated:** [date]

## Influence / Interest Grid

|                    | **Low Interest**            | **High Interest**            |
|--------------------|-----------------------------|------------------------------|
| **High Influence** | Keep Satisfied: [names]     | Manage Closely: [names]      |
| **Low Influence**  | Monitor: [names]            | Keep Informed: [names]       |

## Stakeholder Register

| Stakeholder | Role | Influence | Interest | Stance (now → needed) | Cares about / lever | RACI | Quadrant play |
|-------------|------|-----------|----------|-----------------------|---------------------|------|---------------|
| [Name] | [title] | High/Low | High/Low | ✅ Skeptic → Supporter | [the metric/risk they own; what moves them] | A/R/C/I | Manage Closely |
| [Name] | [title] | High/Low | High/Low | ❓ [now] → [needed] | [...] | C | Keep Satisfied |
| [Name] | [title] | High/Low | High/Low | ❓ [now] → [needed] | [...] | I | Keep Informed |

**Stance scale:** Blocker · Skeptic · Neutral · Supporter · Champion
**Stance flag:** ✅ confirmed (stated/observed) · ❓ assumed (your read, unverified)

## RACI check
_If the initiative bundles more than one real decision, repeat this block per decision — each gets its own single A._

**Decision: [e.g. go/no-go]**
- **Accountable (exactly one):** [name] — [confirmed? or "assumed, needs confirming"]
- **Responsible:** [names]
- **Consulted (before the decision):** [names]
- **Informed (after):** [names]
- ⚠️ [Flag: two A's / no clear A / key person uncategorized]

**Decision: [e.g. eng-allocation]**
- **Accountable (exactly one):** [name] — [confirmed? or "assumed, needs confirming"]
- **Responsible:** [names]
- **Consulted (before the decision):** [names]
- **Informed (after):** [names]
- ⚠️ [Flag: two A's / no clear A / key person uncategorized]

## Engagement plan

| Stakeholder | Goal | Action | Channel | By when |
|-------------|------|--------|---------|---------|
| [Name] | Move Skeptic → Supporter | [address objection X with data on Y] | 1:1 | [date, before decision] |
| [Name] | Keep Satisfied, no surprises | [2-line async pre-read] | Email/Slack | [date] |
| [Name] | Activate as champion | [give talking points for their team] | 1:1 | [date] |

## Risks & watch-items
- **Blocker with power:** [name] — [their objection + plan to neutralize]
- **Contested ownership:** [where the A is unclear or fought over]
- **Unverified supporter:** [name you're assuming is on-side without confirmation]
- **Coalition:** [who aligns with whom, and what that bloc wants]
```

## Avoid (anti-patterns)
- **Scoring influence by org chart, not by this decision.** A senior VP with no stake here is Keep Satisfied, not Manage Closely. The grid is decision-specific.
- **Two people marked Accountable.** That's not a map, it's a future deadlock. Force a single A or escalate to get one named.
- **Treating stance as fixed.** "Blocker" is a starting position, not a verdict. The whole point is the move from now → needed.
- **Vague levers** like "wants the project to succeed." Name the actual currency: the metric they're measured on, the risk they fear, the credit they want.
- **A beautiful grid with no actions.** If every Manage-Closely person doesn't have a next step with an owner and date, you've drawn a diagram, not a plan.

## Tips
- **Map the informal power explicitly.** The person leadership texts before deciding often outranks the person in the meeting. Put them on the grid.
- **Find the swing voter.** One High-influence Skeptic flipping to Supporter usually unlocks more than three Champions cheering. Spend your energy there.
- **Pre-wire the High-influence quadrant.** No one in Manage Closely or Keep Satisfied should hear your ask for the first time in the room — sequence 1:1s before any group decision.
- **Re-run this at every phase gate.** Interest rises as things get real and stances shift after the first demo; a stale map is worse than none because it breeds false confidence.
