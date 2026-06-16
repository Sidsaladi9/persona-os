---
name: pre-mortem
description: Runs a Klein pre-mortem on a project — assumes it already failed, brainstorms why, scores each failure mode by likelihood × impact, and attaches a mitigation plus an early-warning signal to the top risks. Use when launching a feature, kicking off a quarter, or before a big bet and you want to ask "imagine this shipped and flopped — what killed it?" or "where is this most likely to go wrong?"
---

# Pre-Mortem

A pre-mortem (Gary Klein) flips a postmortem forward in time: you assume the project has already failed, then work backward to explain why. This "prospective hindsight" frames failure as a given, which licenses honest, specific concerns that optimism normally suppresses — and turns them into mitigations before they cost you anything.

**Grounded in:** *Performing a Project Premortem (HBR)* — Gary Klein: assume it failed, list why, rate likelihood × impact, mitigate the top modes.

## When to use this
- You're about to commit to a launch, migration, or large bet and want to stress-test it before sinking resources.
- The plan feels suspiciously smooth and nobody is raising objections in the room.
- Kicking off a quarter or epic where the cost of a wrong assumption is high.
- A senior stakeholder asked "what could go wrong?" and you want more than a hand-wavy risk slide.
- You've seen similar projects fail before and want to name the pattern before it repeats.

## Before you start (gather these)
- **The project + its definition of success**: what's shipping, by when, and the specific metric/outcome that means it worked.
- **The plan or approach**: how you intend to get there (key milestones, dependencies, owners).
- **Stakeholders and constraints**: who's involved, the deadline, budget, team capacity, technical or political constraints.

If two or more of these are missing or vague, ASK 2–4 sharp clarifying questions before generating anything — e.g., "What's the single metric that defines success here?", "What's the hard deadline and what's driving it?", "What's the riskiest dependency you're relying on?", "Has a project like this failed here before — how?" If the data is already provided, proceed and state your assumptions inline.

## Process
1. **Set the failure frame.** Write one sentence: "It is [date past the deadline]. The project has failed completely." Be concrete about what "failed" looks like against the success metric — not "it went poorly" but "we shipped 6 weeks late and adoption never crossed 5%."
2. **Brainstorm failure modes wide, then specific.** Generate 8–15 distinct reasons it failed. Force coverage across categories so you don't over-index on the obvious: scope/execution, team/capacity, dependencies/tech, market/user demand, stakeholder/political, data/measurement, external/timing. Each one is a complete causal sentence, not a label. Two modes are **distinct** only if they have a different *root cause* — not just a different symptom. "Adoption stalled because onboarding was confusing" and "adoption stalled because the value prop was unclear" are distinct (different causes); "adoption stalled in week 1" and "adoption stalled in week 4" are the same mode (one cause, two symptoms) — merge them.
3. **Score each by likelihood × impact.** Rate likelihood (1–5: how plausible this actually happens) and impact (1–5: how badly it sinks the project if it does). Multiply for a risk score (1–25). Resist flattening everything to 3s — spread the ratings.
4. **Rank and draw the line.** Sort by score. The **Top tier is capped at 5**: take every mode scoring ≥12, but if more than 5 qualify, keep only the 5 highest and demote the rest to Watch. **Tie-break** (when scores are equal): rank the higher-impact mode first; if impact also ties, the higher-likelihood mode wins. Everything below the line is logged but not actively managed.
5. **Attach a mitigation + early-warning signal to each top risk.** For every top risk: (a) a concrete preventive action with an owner, and (b) an early-warning signal — the specific, observable, *leading* indicator that tells you this failure is starting to materialize while there's still time to act.
6. **Name a trigger and a tripwire.** For the highest risks, decide in advance: if the warning signal fires, what's the predefined response? Pre-committing the reaction removes the in-the-moment hesitation.
7. **Assign and date.** Every mitigation gets an owner and a check-in date. A pre-mortem with no owners is a venting session, not a risk plan.

## Output template

```markdown
# Pre-Mortem: [Project Name]

**Date of exercise:** [today]
**Success defined as:** [specific metric/outcome + deadline]
**Failure frame:** It is [date past deadline]. The project failed — [concrete description of what failure looks like].
**Measurement & launch bar:** Pre-registered primary metric: [the single metric committed to *before* launch]. Control/holdout design: [how you isolate the effect — A/B split, holdout %, pre/post baseline]. Quality gate: [quantified pass threshold, e.g. "precision ≥ 0.85 on the eval set" or "p95 latency < 200ms"].

## Failure modes (ranked)

| # | Failure mode (why it failed) | Category | Likelihood (1–5) | Impact (1–5) | Score | Tier |
|---|------------------------------|----------|:---:|:---:|:---:|------|
| 1 | [Causal sentence — what specifically went wrong] | [Execution/Demand/Dependency/Team/Stakeholder/Data/External] | [ ] | [ ] | [ ] | Top |
| 2 | [ ] | [ ] | [ ] | [ ] | [ ] | Top |
| 3 | [ ] | [ ] | [ ] | [ ] | [ ] | Top |
| 4 | [ ] | [ ] | [ ] | [ ] | [ ] | Watch |
| ... | [ ] | [ ] | [ ] | [ ] | [ ] | Watch |

_Tier: Top = actively mitigated (score ≥12, capped at the 5 highest; ties broken by impact, then likelihood). Watch = logged, monitored, not actively managed._

## Top risks — mitigation & early warning

### Risk 1: [Failure mode] — Score [ ]
- **Why it's plausible:** [1 line grounding the likelihood]
- **Mitigation:** [concrete preventive action]
- **Early-warning signal:** [specific, observable, leading indicator — e.g. "design review slips past [date]" or "week-1 activation < X%"]
- **Tripwire → response:** If [signal fires], then [pre-committed action, e.g. cut scope to X, escalate to Y].
- **Owner:** [name] · **Check by:** [date]

### Risk 2: [Failure mode] — Score [ ]
- **Why it's plausible:** [ ]
- **Mitigation:** [ ]
- **Early-warning signal:** [ ]
- **Tripwire → response:** If [ ], then [ ].
- **Owner:** [ ] · **Check by:** [ ]

### Risk 3: [Failure mode] — Score [ ]
- **Why it's plausible:** [ ]
- **Mitigation:** [ ]
- **Early-warning signal:** [ ]
- **Tripwire → response:** If [ ], then [ ].
- **Owner:** [ ] · **Check by:** [ ]

## Watch list (monitored, not actively managed)
- [Failure mode] — early-warning signal: [ ]
- [Failure mode] — early-warning signal: [ ]

## Plan changes triggered by this pre-mortem
- [Concrete change to scope, sequence, staffing, or timeline made *because* of a risk above]
- [ ]

## Re-check date
- [ ] — revisit signals and re-score after [milestone/date].
```

## Avoid (anti-patterns)
- **Vague failure modes.** "Bad execution" or "lack of resources" can't be mitigated. Force a causal sentence: *what* failed, *because of what*.
- **All-3s scoring.** If every risk scores 9, you haven't prioritized — you've made a list. Spread likelihood and impact deliberately so a true top tier emerges. **Distribution heuristic:** no more than ~40% of modes should share a single score, and at least one mode should land in each band — low (1–6), mid (8–12), high (15–25). If the spread violates this, you're flattening; re-score.
- **Lagging signals dressed as early warnings.** "Adoption was low at launch" is a postmortem fact, not an early warning. The signal must be observable *before* the failure is locked in (e.g., "beta opt-in rate < 20% three weeks out").
- **Mitigations with no owner or date.** Unowned actions are wishes. Every top risk needs a name and a check-in date.
- **Mitigating everything.** Spreading effort across 12 risks dilutes all of them. Draw the line and let the watch list be watched, not worked.

## Tips
- **Run the brainstorm silently first.** With a group, have each person write failure modes alone for 5 minutes before sharing — it kills groupthink and surfaces the concern the most junior person was afraid to say. **Solo or AI-run:** there's no room to silence, so manufacture the diversity instead — cycle through distinct stakeholder lenses one at a time (engineering, CS/support, security, finance, exec/leadership, the churned user) and ask "how does this fail from *their* seat?" Each lens tends to surface a failure mode the others miss.
- **Mine real history.** "Has something like this failed here before?" is the single highest-yield question. Past failure patterns are the most likely future ones.
- **Pre-commit the tripwire response.** Deciding the reaction *now*, while calm, beats deciding it mid-crisis when sunk cost and politics distort judgment.
- **Time-box it.** A sharp pre-mortem is 45–60 minutes. The goal is to surface the top 3–5 risks and act, not to enumerate every conceivable mishap.
