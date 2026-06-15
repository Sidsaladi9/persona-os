---
name: write-spec
description: Turns a vague feature idea or problem statement into a structured, review-ready feature spec or PRD with goals, non-goals, success metrics, and testable acceptance criteria. Use when a PM says "write a PRD", "spec this feature", "turn this idea into a spec", "scope this", "define success metrics", "write acceptance criteria", or needs to break a big ask into a phased spec.
---

# Write Spec

Produces a tight, review-ready feature spec / PRD from a rough idea, problem statement, or stakeholder request — built for product managers and the engineers, designers, and execs who review their work.

## When to use this
- A stakeholder or customer dropped a one-line "can we build X?" and you need a real document.
- You have a problem to solve but the solution and scope are still fuzzy.
- You're about to brief engineering/design and need goals, non-goals, and acceptance criteria locked.
- A feature is too big for one spec and you need to phase it (MVP → fast-follow → later).
- You need to align reviewers on success metrics *before* anyone writes code.

## Before you start (gather these)
You need enough to write something true, not generic. Collect:
- **The problem** — who's hurting, what they can't do today, how you know it's real (data, tickets, quotes).
- **The audience / user** — which segment(s), and their job-to-be-done.
- **The desired outcome** — what "better" looks like, ideally as a measurable shift.
- **Constraints** — deadline, team size, platforms, dependencies, anything off-limits.
- **Existing context** — current behavior, related features, prior attempts.

If two or more of these are missing or vague, **ASK 2-4 sharp clarifying questions before writing.** Make them specific and answerable, e.g.:
- "Who exactly hits this problem — all users, or a segment like new/enterprise/mobile?"
- "What's the one metric that would prove this worked?"
- "What's explicitly *out* of scope for v1?"
- "Is there a hard deadline or dependency driving timing?"

Don't write a spec on guesses. A spec built on a wrong problem statement wastes a whole team.

## Process
1. **Restate the problem in one sentence** and confirm it. If you can't state it crisply, you don't understand it yet — ask.
2. **Write non-goals first.** Listing what you're *not* doing is the fastest way to find the real scope. Every non-goal you name kills a future argument.
3. **Set goals, each paired with a metric.** A goal without a measurable signal is a wish. If a goal can't be measured, either find a proxy or demote it to a non-goal.
4. **Map users and use cases** — primary first. Note the edge users you're deliberately not serving in v1.
5. **Sketch the solution at the right altitude.** Describe behavior and the user experience, not implementation. Leave room for engineering to own *how*.
6. **Write requirements as testable statements.** Prefer "The system must X when Y" over adjectives like "fast" or "intuitive." Tag each P0 / P1 / P2.
7. **Define acceptance criteria** in given/when/then or checklist form — concrete enough that QA and eng can verify them without asking you.
8. **Surface risks and open questions** honestly. Unknowns hidden now become fire drills later.
9. **Phase it if it's big.** Cut to the smallest version that delivers the core outcome (MVP), then list fast-follows and later. If the ask fits in one release, skip phasing.
10. **Self-check against the Quality bar** below, then deliver. Offer a one-page summary up top for exec reviewers.

## Output template
Fill this in completely. Replace every `[bracket]`. Delete sections that genuinely don't apply rather than leaving them empty.

```markdown
# [Feature name] — Product Spec

**Author:** [name] · **Status:** Draft · **Last updated:** [date]
**Reviewers:** [eng lead, design lead, PM peer, exec sponsor]

## TL;DR
[2-3 sentences: the problem, what we're building, and the one outcome it drives. A reviewer should be able to read only this and get the gist.]

## Problem
[What's broken or missing today, for whom. Lead with evidence: support volume, drop-off rate, sales blockers, user quotes. State the cost of doing nothing.]
- **Evidence:** [metric / ticket count / quote]
- **Why now:** [trigger — deadline, competitor move, strategic bet]

## Goals
[Each goal has a metric and a target. No metric → not a goal.]
1. [Goal] — measured by [metric], target [number / direction] by [timeframe].
2. [Goal] — measured by [metric], target [number / direction] by [timeframe].

## Non-goals
[What this explicitly does NOT do. Be specific — these are the boundaries reviewers will hold you to.]
- [Out of scope for now: e.g., "No bulk import — single-record only in v1."]
- [Deliberately not serving: e.g., "Not optimizing for mobile this release."]

## Users & use cases
- **Primary user:** [segment] — job-to-be-done: [what they're trying to accomplish].
- **Secondary user:** [segment] — [their need].
- **Key use cases:**
  1. As a [user], I want to [action] so that [outcome].
  2. As a [user], I want to [action] so that [outcome].
- **Out of scope users:** [segments deliberately not served in v1].

## Solution overview
[Describe the experience and behavior, not the implementation. 1-2 paragraphs + the happy path. Add a wireframe link or ASCII flow if helpful.]

**Happy path:** [Step 1] → [Step 2] → [Step 3] → [outcome].

## Requirements
[Testable statements. Tag priority. Avoid vague adjectives.]

| # | Priority | Requirement |
|---|----------|-------------|
| R1 | P0 | The system must [behavior] when [condition]. |
| R2 | P0 | [Requirement] |
| R3 | P1 | [Requirement] |
| R4 | P2 | [Nice-to-have] |

## Success metrics
- **North-star for this feature:** [the one number that matters].
- **Supporting metrics:** [secondary indicators of health].
- **Guardrail metrics:** [what must NOT get worse — e.g., latency, churn, support load].
- **Measurement plan:** [event/instrumentation needed; where it's tracked].

## Acceptance criteria
[Concrete and verifiable — QA and eng should not need to ask you what "done" means.]
- [ ] Given [context], when [action], then [observable result].
- [ ] Given [context], when [action], then [observable result].
- [ ] Edge case: when [boundary/failure condition], the system [expected behavior].
- [ ] Instrumentation: [event] fires with [properties] on [action].

## Risks & open questions
| Risk / question | Impact | Owner | Status |
|-----------------|--------|-------|--------|
| [What might go wrong or what's unknown] | [High/Med/Low] | [name] | [open / resolved] |

## Rollout / phasing
- **Phase 1 (MVP):** [smallest version that delivers the core outcome]. Gate: [what proves it's ready to expand].
- **Phase 2 (fast-follow):** [next increment].
- **Phase 3 (later):** [deferred scope].
- **Launch plan:** [flag / % rollout / beta cohort], **rollback trigger:** [condition].

## Appendix
- **Dependencies:** [teams, services, third parties].
- **Open design questions:** [link to Figma / docs].
- **References:** [research, related specs, prior art].
- **Changelog:** [date — what changed].
```

## Quality bar
Before delivering, verify every box:
- [ ] The problem is stated in one sentence and backed by at least one piece of evidence.
- [ ] **Every goal has a metric and a target.** No bare aspirations.
- [ ] Non-goals are explicit and specific — not "we'll figure it out later."
- [ ] Requirements are testable statements, not adjectives; each is tagged P0/P1/P2.
- [ ] Every acceptance criterion is verifiable by someone other than the author.
- [ ] At least one guardrail metric is named (what must not regress).
- [ ] Risks and open questions are listed honestly, each with an owner.
- [ ] If the scope spans more than one release, it's phased with a clear MVP.
- [ ] A reviewer reading only the TL;DR understands what's being built and why.
- [ ] No implementation details masquerading as requirements (the "how" is left to eng).

## Tips
- **Write non-goals before goals.** Naming what you won't do is the fastest path to real scope.
- **One-pager before full PRD.** Get alignment on TL;DR + goals + non-goals first; expand only after reviewers nod.
- **If a goal has no metric, it's not a goal** — it's a feeling. Find a proxy or cut it.
- **Cut to the smallest thing that delivers the core outcome.** The MVP is a scoping tool, not a quality compromise.
- **Acceptance criteria are a contract with QA.** If you'd have to explain "done" in a meeting, the criteria aren't sharp enough.
- **Name guardrails early.** "Don't make latency or churn worse" prevents shipping a local win that's a global loss.
- **Date and version it.** Specs are living documents; a stale spec misaligns more than no spec.
