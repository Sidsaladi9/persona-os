---
name: activation-flow-design
description: Designs a new-user onboarding/activation flow that gets users to the aha-moment fast — defines the activation event, maps the current first-run path, locates the drop-off, and redesigns the step sequence with triggers, nudges, and empty states. Use when a PM says "design our onboarding", "improve activation", "get users to the aha moment", "redesign first-run", "new-user flow", "why aren't new users sticking", or "activation flow".
---

# Activation Flow Design

Designs the specific first-run path that carries a brand-new user from signup to their aha-moment — the activation event — as fast as possible. This is a *design* skill, not a measurement one: it produces a re-sequenced step flow with triggers, nudges, and empty states, not a retention chart.

**Grounded in:** *Hooked* — Nir Eyal: the **Trigger → Action → Reward → Investment** loop, applied to onboarding. Activation is getting the user through their first full loop before they quit — so they experience the variable reward (the aha) and make a small investment that pulls them back.
**Go deeper (The Product Channel):** [The Activation Playbook](https://sidsaladi.substack.com/)

## When to use this
- New signups try the product once and never come back, and you need to redesign the first run — not just measure that it's leaking.
- You're launching a new product or major surface and need to design the onboarding/first-run flow from scratch.
- Activation rate is below benchmark and you want a concrete, re-sequenced step flow to fix it — "get users to the aha moment sooner."
- Users finish setup but never hit the moment that makes the product click; the path to value is too long or buried.
- A redesign or pricing change shifted who signs up, and the old first-run no longer lands them at value.

> **Not this skill:** if you need to *measure* activation or retention curves, use `cohort-analysis` / `metrics-review`. To map the *whole* customer journey end-to-end, use `journey-map`. To model the *whole-product* compounding loop (virality, content, expansion), use `growth-loops`. This skill designs the narrow first-run path to the first aha only.

## Before you start (gather these)
- **The activation event (the aha)** — the single observable action that reliably predicts retention (not "signed up", not "logged in"). If you don't have one, deriving it is step 1.
- **The current first-run steps** — the literal screens/actions a new user hits from signup to first value, in order.
- **Where users drop** — the step-level funnel (or your best read of it) showing where new users quit.
- **The user / segment** — who you're activating, their job-to-be-done, and how they arrive (self-serve vs. sales-assisted, solo vs. team).
- **Time-to-value reality** — how long the current path takes, and any hard dependencies (an invite, an integration, data import) that gate the aha.

If **two or more** are missing or vague, **ASK 2–4 sharp questions before designing** — especially "what single action best predicts a user sticks around?" and "what are the literal first-run steps today?" If you have enough, proceed and open the output with an explicit **Assumptions** block stating what you took as given.

## Process
1. **Define the activation event precisely.** It must be (a) a *value* moment, not a setup chore; (b) observable as one event; (c) correlated with retention. State it as "user [does X] within [time/visit window]." If a candidate is really a proxy for setup ("connected Slack"), push past it to the moment value is *felt* ("read their first digest that surfaced a real blocker"). Name the **time-to-activate target** (e.g. "within first session", "within 48h").
2. **Map the current first-run path as an ordered step list.** Every screen, decision, and wait between signup and the activation event. For each step capture: the user's intent, the friction, and — critically — whether it's *on the critical path to value* or just *setup we've front-loaded*. Mark dependencies that block progress (invite, integration, import).
3. **Locate the drop-off and diagnose its type.** Find the biggest step-level fall. Classify it: **friction** (too hard — fix the step), **confusion** (don't know what to do — fix the empty state / guidance), **no-trigger** (nothing pulls them back to the next step — add a trigger), or **premature-value-ask** (we demanded work before showing the reward — re-sequence). The diagnosis dictates the fix; don't jump to "add a tooltip."
4. **Re-sequence to shorten time-to-aha.** Apply two moves: **defer** every setup step that isn't on the critical path to *after* the aha (the user invests once hooked, not before), and **pull forward / fake** value so the reward arrives sooner — seeded sample data, a pre-filled first action, a templated starting point. The target: the user feels the variable reward before you ask them to invest.
5. **Design the Trigger → Action → Reward → Investment loop for the redesigned path.** For each step name the **trigger** (external: email/Slack/in-app nudge — what brings them to the action), the **action** (the simplest thing they can do), the **reward** (the value they feel — make it visible and ideally variable), and the **investment** (the small bit of data/effort that loads the *next* trigger and pulls them back). The first loop must close before the user quits.
6. **Specify empty states and nudges at each fragile step.** Empty states are first-run UI, not edge cases — design the zero-data screen to teach the next action. For each likely-stall point, define the nudge: trigger, timing, channel, copy intent, and the **exit condition** (when it stops firing) so nudges never become nagging.
7. **Specify what to instrument** — the events needed to *prove the redesign worked*, step by step. Name the activation event, each step-completion event, and the **one north-star activation metric** (e.g. % of new users activated within target window). Define the holdout/cohort comparison so the lift is real, not seasonal. (Measuring it is `cohort-analysis`' job — here you just specify the events the redesign requires.)
8. **Self-check:** does the redesigned path get the user to the aha in fewer steps and less time than today? Does the first loop close before the likely quit point? Have you deferred every non-critical setup step? Then deliver.

## Output template
Fill in completely. Replace every `[bracket]`. TL;DR first.

```markdown
# Activation Flow Design — [product / surface], [segment]

**TL;DR.** Activation = **[the aha event]**, target **[within X]**. Today [N]% of new [users] get there; the path is **[K] steps / [T] minutes** and the biggest leak is **[step → diagnosis]**. The redesign cuts it to **[K'] steps** by **[the one re-sequencing move]**, closing the first Trigger→Reward loop before the week-1 quit point. Expected: activation **[N]% → [N']%**.

## The activation event (the aha)
- **Event:** [user does X] within **[time/visit window]**.
- **Why this is the aha (not a proxy):** [the value felt here; evidence it predicts retention — e.g. "users who do X by day 2 retain 3x"].
- **Time-to-activate target:** [within first session / 48h / week 1].
- **Rejected candidates:** [e.g. "'connected integration' — that's setup, value isn't felt yet"].

## Current first-run path
| # | Step | User intent | On critical path to value? | Friction | Drop-off |
|---|------|-------------|----------------------------|----------|----------|
| 1 | [screen/action] | [what they want] | ✅ value / ⚙️ setup | [what's hard] | [%] |
| 2 | [step] | [intent] | ⚙️ setup | [friction] | [%] |
| … | | | | | |

**Time-to-value today:** [T]. **Hard dependencies gating the aha:** [invite / integration / import].

## The drop-off, diagnosed
- **Biggest leak:** Step [N] ([step name]) — **[X]%** quit here.
- **Type:** 🔴 [friction / confusion / no-trigger / premature-value-ask] — [one line of why].
- **Root cause:** [what's actually wrong — e.g. "we ask the user to invite teammates before they've seen any value, so solo evaluators stall"].

## Redesigned path (re-sequenced)
**Moves applied:** [defer X setup until after aha] · [pull-forward value via Y] · [add trigger at Z].

| # | Step | Trigger | Action | Reward (the value felt) | Investment (loads next trigger) |
|---|------|---------|--------|-------------------------|---------------------------------|
| 1 | [step] | [external: email/Slack/in-app] | [simplest action] | [visible/variable reward] | [data/effort that pulls them back] |
| 2 | [step] | [trigger] | [action] | [reward] | [investment] |
| … | | | | | |

**Deferred to post-activation:** [setup steps moved after the aha — invite, full profile, advanced config].
**Time-to-value, redesigned:** [T'] (was [T]) · **steps:** [K'] (was [K]).

## Empty states & nudges (at the fragile steps)
| Step | Empty state (zero-data screen teaches…) | Nudge: trigger → channel → intent | Exit condition (stops firing when…) |
|------|-----------------------------------------|-----------------------------------|-------------------------------------|
| [step] | [what the empty screen shows/teaches] | [e.g. "no action in 24h → email → 'here's your first X, 1 click'"] | [user completes step / N sends] |

## Instrumentation (to prove it worked)
- **North-star activation metric:** [% of new [users] who [aha event] within [window]].
- **Step events to fire:** [step_1_complete, …, activation_event] with [key properties].
- **Read method:** compare **post-redesign signup cohorts vs. pre** (or holdout) on the activation metric — not a before/after blended number. Re-pull at [N] weeks.
- **Guardrail:** [what must not get worse — e.g. quality of activated users, downstream week-2 retention, support load].

## Assumptions
- [Load-bearing bets — e.g. "the aha event is correlated with retention but not yet causally proven"; "step drop-off %s are estimated from X"].

## What I'd test first
[The single highest-leverage change to ship and measure first, and why — usually the re-sequencing move at the biggest leak.]
```

## Avoid (anti-patterns)
- **Picking a setup step as the activation event.** "Connected the integration" or "completed profile" is work the user did, not value they felt. If your aha is a chore, you'll optimize people *into* setup and still lose them at value. Push to the felt-reward moment.
- **Adding a product tour instead of cutting steps.** A 6-step coachmark tour over a broken flow is lipstick. The fix is almost always *fewer steps to value*, not more overlay explaining the steps. Defer and pull-forward before you decorate.
- **Asking for investment before the user has felt the reward.** Demanding invites, payment, or heavy config before the aha inverts the Hooked loop — investment comes *after* the variable reward, never before. Front-loaded asks are the most common premature-value-ask leak.
- **Designing empty states as an afterthought.** The zero-data screen is the first thing every new user sees and the highest-traffic screen in the product. An empty state that just says "No items yet" wastes the single best teaching moment.
- **Nudges with no exit condition.** A reminder that fires until the user complies reads as nagging and trains people to ignore you. Every nudge needs a stop rule and a channel budget.
- **Designing one flow for two arrival types.** Self-serve solo evaluators and sales-assisted teams hit value differently; a blended flow under-serves both. Segment the path if the drop-off differs by how they arrive.

## Tips
- **Find the aha empirically, then design backward from it.** The strongest activation events come from "users who did X by day N retain at K×" analysis. Design the whole first run to make X happen sooner — that's the entire job.
- **Time-to-value is the metric behind the metric.** Activation rate rises mostly by shrinking the minutes/steps to first value. Count both and put them on the redesigned path.
- **Seed the empty state with fake-but-real value.** A pre-filled first action, a sample record, a templated start — anything that lets the user feel the reward before doing the work — is usually the single biggest lever.
- **The first investment is the hook, not the upsell.** The small bit of data the user leaves behind (a saved item, a connected source, an answered prompt) is what loads the next trigger. Design that loop-closing investment explicitly, or the user never comes back for loop two.
