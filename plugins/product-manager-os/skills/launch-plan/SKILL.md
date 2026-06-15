---
name: launch-plan
description: Builds a go-to-market launch plan for a feature or product, scaled to a launch tier. Use when someone asks to "plan the launch", build a "go-to-market plan" or "GTM for the new feature", needs a "launch checklist for X", or asks "how should we launch this". Produces audience, messaging, channels, a pre/launch/post timeline with owners, assets, success metrics, and a launch-day runbook.
---

# Launch Plan

A launch is a cross-functional event, not a ship date. This skill turns "we're shipping X" into a coordinated plan: the right tier of effort, a clear message, the channels that fit, a timeline with owners, the assets you need, the metrics that define success, and a runbook for launch day. Scale everything to impact — not every launch deserves a press release.

## When to use this
- A feature or product is about to ship and needs a coordinated rollout
- Marketing, sales, support, and eng need a single source of truth for who does what, when
- You need a launch checklist with owners and dates, not just a vibe
- You want to right-size effort: avoid over-launching a minor change or under-launching a flagship

## Pick the launch tier first
Decide impact before anything else — it sets the ceiling for every section below.
- **T1 (major)** — new product, flagship feature, repositioning. Full GTM: all channels, exec involvement, sales enablement, press/analyst, coordinated timeline, dry run.
- **T2 (standard)** — notable feature, meaningful expansion. Targeted comms on key channels (blog, email, in-app, social), light sales/support enablement, single owner per task.
- **T3 (minor)** — incremental improvement, fast-follow, fix. Changelog entry + in-app note + maybe one social post. No campaign.

**Boundary heuristic** (apply top-down, first match wins): new product / repositioning / press-worthy → **T1**; touches a core surface OR moves a top company metric → at least **T2**; no new user behavior, only a fix or polish → **T3**.

Scale audience, channels, timeline, assets, and metrics to the tier. When unsure, default down a tier — you can always amplify a winner.

## Before you start (gather these)
- **What's launching + why it matters** — the one-line value to the user
- **Target audience / segment** — who this is for (all users? a plan tier? a persona?)
- **The date** — hard date or target window, and what's gating it
- **Cross-functional partners** — named owners in PM, marketing, sales, support, eng
- **Success metric** — the one number that says this worked
Ask for anything missing before drafting — don't invent a date, an owner, or a metric.

## Process
1. **Set the tier.** Classify T1/T2/T3 by impact and state why. This caps scope.
2. **Define audience + core message + proof.** Who it's for, the single core message (problem → what changed → why they should care), and the proof (data, demo, customer quote, before/after).
3. **Choose channels.** Pick only channels that fit the tier and reach the audience: changelog, in-app, email, blog, social, docs, sales deck, webinar, press/analyst, community. Don't default to "all."
4. **Build the timeline (pre / launch / post) with a checklist and owners.** Every task gets an owner and a date. Pre-launch: enablement, assets, QA, staged rollout. Launch day: flip the switch, publish, monitor. Post-launch: follow-up comms, metric review, retro.
5. **List assets needed.** Each asset (copy, screenshots, demo, FAQ, sales one-pager, support macros) gets an owner and a due date that lands before launch day.
6. **Set success metrics + a rollback/abort trigger.** Define the target number, the window to hit it, and the explicit condition under which you pause, roll back, or abort.
7. **Write a launch-day runbook.** Hour-by-hour (or step-by-step) sequence: who flips what, in what order, who's watching which dashboard, who comms internally, and the go/no-go checkpoint.

## Output template
Copy-paste and fill in.

```
# Launch Plan: <name>

## Launch summary
- What: <one line on what's shipping>
- Why it matters: <value to the user>
- Tier: <T1 / T2 / T3> — <one line on why>
- Why this tier (evidence): <which boundary rule it hit + the fact behind it — e.g. "moves activation, a top metric" — not a hand-wave>
- Date: <date or window>

## Audience & message
- Audience / segment: <who>
- Core message: <problem → what changed → why they care>
- Proof: <data / demo / quote / before-after>

## Channels
- <channel> — <what goes out, owner>
- <channel> — <what goes out, owner>
- Not doing (and why): <channels deliberately reserved for a higher tier — e.g. "no press/analyst, this is T2">


## Timeline & checklist
### Pre-launch
| Task | Owner | When | Status |
|------|-------|------|--------|
| <task> | <name> | <date> | <todo/doing/done> |

### Launch day
| Task | Owner | When | Status |
|------|-------|------|--------|
| <task> | <name> | <time> | <todo/doing/done> |

### Post-launch
| Task | Owner | When | Status |
|------|-------|------|--------|
| <task> | <name> | <date> | <todo/doing/done> |

## Assets needed
| Asset | Owner | Due |
|-------|-------|-----|
| <asset> | <name> | <date> |

## Success metrics
- Primary: <metric> — target <number> by <date>
- Secondary: <metric(s)>
- What failure looks like: <the number/signal that means it flopped — define the abort thresholds HERE, once; the rollback trigger below references them>

## Launch-day runbook
> The "Launch day" table above is the checklist (what must happen); this runbook is the executable, cold-at-6am sequence derived from it (the exact order, who flips what, who watches what). For T3 — and optionally T2 — the runbook replaces the launch-day table; don't maintain both.

1. <time> — <who> does <what> (go/no-go checkpoint: <condition>)
2. <time> — <who> publishes <channel>
3. <time> — <who> monitors <dashboard/metric>
4. Internal comms: <who> posts in <channel> when <milestone>

## Risks & rollback trigger
- Risk: <risk> → Mitigation: <plan>
- Rollback / abort trigger: if the failure threshold above ("What failure looks like") is hit by <time>, then <pause/roll back/abort> — owner <name>. (Define the number once above; reference it here, don't restate it.)
```

## Avoid (anti-patterns)
- **Treating every launch as T1** — over-launching minor changes burns audience goodwill and team effort, and makes the next big launch land softer
- **No owner on launch tasks** — "the team" owns nothing; every row needs one name
- **Shipping with no success metric or no rollback plan** — you won't know if it worked and won't know when to pull back
- **Marketing / support / sales finding out at launch** — surprise launches mean unanswered tickets, off-message reps, and no enablement
- **Assets due "by launch"** — they need to land days earlier so reps and support can absorb them

## Tips
- Write the core message in one sentence first. If you can't, the launch isn't ready.
- Pull support and sales in during pre-launch, not launch day — they're your front line.
- Stage the rollout (internal → beta → %  → all) for T1/T2 so the rollback trigger is cheap to pull.
- The runbook is for the person who isn't you. Make it executable cold, at 6am, by whoever's on point.
- Schedule the post-launch retro before launch day — otherwise it never happens.
