---
name: tracking-plan
description: Designs the event tracking plan for a feature or product area — the event taxonomy, naming convention, properties, and QA checklist that make a metric answerable later. Use when a PM says "what should we instrument", "write a tracking plan", "what events do we need", "we can't answer that from the data", "define the analytics for this feature", or is about to ship something with no way to tell whether it worked.
tier: guided
time: 60-90 min
inputs: the feature or funnel, the questions you'll need to answer, and your existing event names
outputs: metrics/tracking-plan-<area>.md
---

# Tracking Plan

Designs the instrumentation *before* the feature ships, so the question you'll be asked in six weeks is answerable. Produces an event taxonomy with names, properties, triggers, and owners — plus the QA steps that catch the events that silently never fire.

**Grounded in:** *Lean Analytics* — Croll & Yoskovitz: instrument the One Metric That Matters and its inputs deliberately, before you need them. Paired with the tracking-plan discipline standardized by Segment and Amplitude: one event per user intent, properties for the dimensions you'll slice by, and a naming convention decided once.

**The load-bearing idea:** you cannot retroactively instrument the past. Every question you fail to anticipate costs a release cycle to answer.

## When to use this
- A feature is about to ship and nobody has said what gets tracked.
- You keep hitting *"we can't answer that from the data"* in metric reviews.
- Event names have drifted — `signup_completed`, `completeSignup`, and `user_signed_up` all exist and mean the same thing.
- You're standing up analytics on a product area for the first time.
- An experiment is being designed and the metric it needs isn't instrumented yet.
- Before a funnel analysis you already know you'll want (activation, onboarding, checkout).

## Before you start (gather these)
- **The user journey for this area** — the actual steps, in order, including the failure paths.
- **The questions you'll need to answer** — write them as questions, not metrics. *"What share of teams that invite a second member post a check-in that week?"*
- **Your existing event names** — a sample from the current schema, so the new work matches the convention rather than starting a third one.
- **Who owns the implementation** — the engineer or team who will actually add the calls.
- **The analytics tool** — Amplitude, Mixpanel, GA4, or a warehouse. Property limits and naming rules differ.

If two or more are missing, **ask 2-4 clarifying questions before designing anything.** The most important is always the questions-to-answer one — a tracking plan built without it instruments what's easy rather than what's needed. If you already hold the context from `memory/` or `workspace/`, open with an explicit Assumptions block instead so they can correct it in one line.

## Process
1. **Start from the questions, not the events.** List 5-10 questions the business will ask about this area in the next two quarters. Each becomes a row you must be able to answer. Anything you can't trace to a question is instrumentation you don't need — cut it. Anything asked twice is your priority.
2. **Map the journey to intents.** Walk the flow and mark each point where the *user forms an intent* — started, submitted, succeeded, failed, abandoned. One event per intent, not one per click. A button that does the same thing in three places is one event with a `source` property, not three events.
3. **Fix the naming convention before naming anything.** Decide once and write it at the top: `object_action`, past tense, snake_case (`check_in_posted`, not `PostCheckin` or `posted-checkin`). Convention beats taste; the cost is entirely in the inconsistency.
4. **Design the properties.** For each event, the properties are the dimensions you'll slice by — pulled directly from your step-1 questions. Include the identifiers that make joins possible (`team_id`, `plan`, `days_since_signup`). Mark each property required or optional, with its type and allowed values. Enums beat free text.
5. **Name what you will NOT track.** Explicitly. This is where the plan earns trust with engineering, and it stops the taxonomy from doubling every quarter.
6. **Write the QA checklist.** For every event: how do we verify it fires, exactly once, with correct properties, in staging *and* the first day of production. Include the negative case — the event must not fire on error.
7. **Assign owners and a review date.** One implementer per event, one reviewer for the whole plan, and a date to check that the events are actually flowing.

## Output template
```markdown
# Tracking Plan — [area]

**Owner:** [PM] · **Implementer:** [eng] · **Tool:** [Amplitude/Mixpanel/GA4/warehouse]
**Status:** draft | approved | implemented · **Verify by:** [date]

## Questions this plan must answer
| # | Question | Answered by |
|---|---|---|
| 1 | [the real question, in business language] | [event(s) + property] |

## Naming convention
`object_action`, past tense, snake_case. Properties snake_case. Enum values lowercase.
Examples: `check_in_posted` · `digest_opened` · `invite_sent`

## Events
### `[event_name]`
- **Fires when:** [the precise trigger — not "when the user clicks", but the state change]
- **Fires once per:** [session / action / day]
- **Owner:** [eng]
- **Answers:** Q[n]

| Property | Type | Required | Allowed values | Notes |
|---|---|---|---|---|
| `team_id` | string | yes | — | join key |
| `source` | enum | yes | `web`, `slack`, `email` | where the action started |

## Identity & joins
- **User identifier:** [what identifies a person across sessions/devices]
- **Account identifier:** [team/org id — required on every event for B2B]
- **Known gap:** [anywhere identity breaks, stated honestly]

## Explicitly NOT tracked
- [thing] — [why: no question needs it / privacy / cost]

## QA checklist
- [ ] Every event fires in staging with all required properties present
- [ ] No event fires on the error path
- [ ] No event double-fires on retry or re-render
- [ ] Property values match the declared enums (no free-text drift)
- [ ] Events appear in [tool] within [expected latency]
- [ ] Day-1 production spot check against a known user session

## Deprecations
| Old event | Replaced by | Stop date |
|---|---|---|
```

## Avoid (anti-patterns)
- **Instrumenting clicks instead of intents.** `button_clicked` with a label property is a taxonomy that answers nothing. Track what the user accomplished.
- **Starting from events instead of questions.** You end up with 200 events and still can't answer the one thing the CEO asks.
- **Free-text properties.** `plan: "Team "` and `plan: "team"` are two segments six months from now. Use enums and say so.
- **No account identifier on a B2B event.** Every B2B question is eventually "by account", and you cannot backfill it.
- **Skipping the negative case in QA.** The most expensive tracking bug is an event that fires on failure too, quietly inflating your success metric for a quarter.
- **A plan with no deprecation section.** Old events never die on their own; they just make every future query ambiguous.
- **Tracking everything "just in case."** Cost, noise, and privacy exposure all scale with the taxonomy. If no question needs it, it is not free to collect.

## Tips
- 💡 **Write the SQL for your top question before finalizing the plan.** If you can't write the query against your proposed events, the plan is wrong — and it's ten minutes to find out now versus a release cycle later.
- The property you'll wish you had is almost always **time since something** — `days_since_signup`, `days_since_last_active`. Add it up front.
- Ship the plan as a PR against the schema, not a doc. Docs drift from code; a PR gets reviewed by the person implementing it.
- If an existing event is 80% right, extend it with a property rather than adding a near-duplicate. The `deprecations` table is there for the times you can't.
