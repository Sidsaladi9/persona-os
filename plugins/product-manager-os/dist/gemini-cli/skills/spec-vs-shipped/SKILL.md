---
name: spec-vs-shipped
description: Audits what actually shipped against what the spec promised, and turns the gap into a decision list. Use when a PM says "did we build what we specced", "what's actually in this release", "the spec says X but the product does Y", "check this against the PRD", "what got dropped", or before writing release notes, a launch announcement, or a retro on a delivery that drifted.
tier: quick
time: 30-45 min
inputs: the spec or acceptance criteria, plus the shipped changes (PRs, tickets, changelog, or the running product)
outputs: projects/<project>/spec-vs-shipped.md
---

# Spec vs. Shipped

Compares the promise to the artifact. Produces a line-by-line reconciliation — shipped as specced, shipped differently, silently dropped, or shipped but never in the spec — and turns each gap into a decision rather than a complaint.

**Grounded in:** *Inspired* — Marty Cagan: the spec exists to manage value, usability, feasibility, and viability risk, so a gap between spec and build is a risk that came back unpriced. Paired with blameless postmortem practice from *The DevOps Handbook* — Gene Kim et al.: the drift is almost always a rational local decision made under pressure, and the useful question is what made it invisible, not who made it.

**The load-bearing idea:** most delivery drift is never decided, only accumulated. Nobody chose to drop the empty state — it just never came up again. This skill makes the accumulation visible while it's still cheap.

## When to use this
- Before writing release notes or a launch announcement, so you don't announce something that didn't ship.
- At the end of a milestone, before the retro, so the retro argues about causes instead of facts.
- When the product and the PRD have visibly diverged and nobody can say by how much.
- Before a stakeholder update where you'll be asked "is it done?" and need a defensible answer.
- When taking over someone else's project and needing to know what the spec still describes accurately.
- After an incident traced to behavior nobody remembered agreeing to.

## Before you start (gather these)
- **The spec or acceptance criteria** — the version that was actually agreed, not the latest edit.
- **What shipped** — merged PRs, closed tickets, the changelog, or access to the running product. More than one source is better; they disagree in useful ways.
- **The date boundary** — which release or window you're auditing.
- **Any decisions made mid-flight** — Slack threads, ticket comments, a decision log. Much of the "drift" turns out to have been decided and never written down.

If the spec is missing entirely, say so and stop — reconstruct it with `write-spec` first, or audit against the acceptance criteria alone and label the result as partial. Auditing against a remembered spec produces confident fiction.

## Process
1. **Extract the promises as a checklist.** Pull every requirement, acceptance criterion, and stated non-goal out of the spec into numbered rows. Non-goals matter as much as requirements — shipping one is drift too.
2. **Extract what shipped.** From PRs, tickets, and the product itself. Where you can, verify against the running product rather than the ticket title; tickets describe intent, products describe reality.
3. **Reconcile each row into exactly one bucket.** ✅ as specced · 🟡 shipped differently · 🔴 not shipped · ➕ shipped but never specced · ⬜ can't verify. Force a bucket for every row; "partially" is a 🟡 with a description of what's missing.
4. **For every 🟡 and 🔴, find whether it was decided.** Search the tickets and threads. Mark each as **decided** (with a link and a date) or **drifted** (no record). The decided/drifted split is the most valuable output of this skill — decided gaps are fine, drifted ones are the finding.
5. **Check the ➕ column hard.** Unspecced additions are where scope, risk, and support burden enter unpriced. For each: was it necessary, and does it need a spec entry now, retroactively?
6. **Assess the outcome, not just the checklist.** The spec's success metrics were the point. State whether what shipped can still move them — a release that's 90% complete but missing the one thing that drove the metric is a 🔴 release.
7. **Convert every gap into a decision.** Each row ends as ship-as-is / fix-now / backlog / retroactively-accept / revert. No gap leaves the document without one.

## Output template
```markdown
# Spec vs. Shipped — [project], [release/window]

**TL;DR**
- [n] of [m] requirements shipped as specced. [x] shipped differently, [y] not shipped, [z] shipped without a spec entry.
- **Decided vs. drifted:** [a] of the [x+y] gaps were decided and recorded. [b] drifted with no record. 🟡
- **Can it still move the metric?** [yes / at risk / no] — [one line].

**Spec version audited:** [link/date] · **Shipped window:** [dates] · **Verified against:** [PRs / product / both]

## Reconciliation
| # | Spec said | What shipped | Status | Decided? | Decision |
|---|---|---|---|---|---|
| 1 | [requirement] | [what's actually there] | ✅ | — | ship as is |
| 2 | [requirement] | [the difference] | 🟡 | [link, date] | accept |
| 3 | [requirement] | not present | 🔴 | drifted | fix now |

## Non-goals check
| Non-goal | Held? | Notes |
|---|---|---|

## Shipped but never specced
| What | Why it appeared | Risk / support burden | Decision |
|---|---|---|---|

## Success metrics — can they still move?
| Metric | Target | Depends on | Status after this release |
|---|---|---|---|

## The drifted gaps (the real finding)
For each gap with no decision record:
- **[Gap]** — [what was lost]. **Why it went unnoticed:** [the mechanism, not the person]. **Prevention:** [the specific check that would have caught it].

## Decisions
| # | Gap | Decision | Owner | By |
|---|---|---|---|---|

## Spec updates required
- [Retroactive edits so the spec describes reality — otherwise the next person audits against fiction.]
```

## Avoid (anti-patterns)
- **Blaming rather than tracing.** Drift is a process signal. "Who dropped this?" ends the conversation; "what made this invisible until now?" produces the fix.
- **Auditing against the latest spec.** Compare against the version agreed at kickoff, then note spec edits separately. Otherwise a spec quietly rewritten to match the build shows zero drift.
- **Trusting ticket titles over the product.** A ticket says "add empty state"; the empty state may be a blank div. Verify where you can.
- **Ignoring the ➕ column.** Unspecced additions carry support cost and risk forever, and they're the easiest thing to wave through.
- **Marking things "partial" and moving on.** Partial is a 🟡 that needs a sentence and a decision, not a shrug.
- **Stopping at the checklist.** 47 of 50 requirements shipped sounds excellent until the 3 missing were the ones the metric depended on.
- **Producing this and not updating the spec.** If the spec still describes what you didn't build, you've moved the problem, not fixed it.

## Tips
- 💡 **The decided-vs-drifted ratio is the number to watch across releases.** Gaps are normal and often correct. Gaps that nobody decided are the health signal, and the trend matters more than any single release.
- Run this *before* the retro, not in it. A retro that spends its first 30 minutes establishing what happened never gets to why.
- For example, on a release with 9 gaps where 7 were recorded decisions and 2 drifted, the useful conversation is entirely about those 2 — and it takes ten minutes instead of an hour.
- Feed the output straight into `release-notes` (so you announce what exists), `retro` (as the factual base), and `write-spec` (as the retroactive edit list).
