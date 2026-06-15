---
name: okrs
description: Helps draft and pressure-test OKRs with outcome-based objectives and measurable key results. Use when someone says "draft our OKRs", "set quarterly goals", "are these good key results", "turn this goal into OKRs", "help me write objectives and key results", or "pressure-test our OKRs". Catches the classic failure modes — output KRs, missing baselines, and sandbagged targets.
---

# OKRs

OKRs work when the Objective says *where we're going and why it matters*, and the Key Results prove *we actually got there* with movement on a number — not a checklist of shipped work. This skill helps you draft a tight, focused set and then stress-test it against the anti-patterns that quietly kill most OKR cycles. The single hardest discipline: Key Results are **outcomes**, not the tasks you'll do to reach them.

## When to use this
- A new quarter or planning cycle is starting and you need to set goals.
- You have a strategy or company objective and need to translate it into team/individual OKRs.
- Someone hands you a draft and asks "are these good?" — you need to grade and fix them.
- Your KRs feel like a project plan and you suspect they're really just a to-do list.
- You want to align a goal up the ladder (company → team → individual) so the levels reinforce each other.

## What good looks like
- **Objective:** qualitative, ambitious, time-bound, and memorable. A sentence a teammate could repeat from memory and feel pulled toward. No metrics in it.
- **Key Result:** a measurable OUTCOME with **baseline → target** and a named data source. It answers "how will we *know* we hit the Objective?" — not "what will we *do*?"
- **Shape:** ~1 Objective with ~3 Key Results. More than that and focus dies.
- **Ladder:** each level's Objective ladders up to the level above — a team KR is often the parent of a team-member's Objective.

## Before you start (gather these)
- **The higher-level goal/strategy** this ladders up to (company or team objective). If you don't have it, ask — OKRs that don't ladder up are just a wish list.
- **The metric(s) you can actually move** this cycle, and who owns them.
- **The timeframe** (usually a quarter).
- **Current baselines** for each candidate metric — today's number, with its source. If a baseline is unknown, flag it; "establish the baseline" can itself be a KR — but it burns one of your ~3 scarce slots. Decision rule: only spend a KR slot on baseline-setting when the metric is already core to the Objective and instrumented this quarter; otherwise make it a beta/initiative.
Ask for anything missing before drafting. Don't invent baselines or targets.

## Process
1. **Anchor up.** Restate the higher-level objective/strategy this serves. Every KR you propose should be a believable contributor to it.
2. **Draft the Objective.** Write the qualitative, inspiring "where we're going and why." Make it memorable and time-bound. Strip out any numbers.
3. **Derive 3 outcome KRs.** For each, name a metric, its baseline, its target, and its data source. Ask of each: *if this number moves, did the world actually change for a user or the business?* If not, it's an output — rewrite it.
4. **Separate KRs from initiatives.** List the projects/features/work *separately* as initiatives. Initiatives are the bets that *drive* the KRs; they are never KRs themselves. "Ship feature X" belongs here, not in the KRs.
5. **Pressure-test against the anti-patterns** below. Grade each KR pass/fail and rewrite the failures.
6. **Set cadence + scoring.** Define a weekly or biweekly check-in and the 0.0–1.0 scoring convention (1.0 = target hit, ~0.7 = solid stretch progress, 0.0 = no movement). Label type **per KR**, not just for the set as a whole — a single set often mixes aspirational growth KRs (~0.7 is a win) with a committed guardrail KR you must hold (e.g. KR3 = committed). Mark each KR `[committed]` or `[aspirational]` so the scoring bar is unambiguous.

## Output template
```
OBJECTIVE: <qualitative, ambitious, time-bound, memorable — no numbers>
  Ladders up to: <the company/team objective above this>
  Timeframe: <e.g. Q3 2026>

KEY RESULTS (outcomes — tag each [committed] or [aspirational]):
  KR1 — <metric> | baseline <X> → target <Y> | source: <where the number comes from> | [aspirational]
  KR2 — <metric> | baseline <X> → target <Y> | source: <...> | [aspirational]
  KR_g — <metric> | hold ≥ <floor> (target <Y>) | source: <...> | [committed]   # guardrail/floor KR — no baseline→target arrow

INITIATIVES (the work that drives the KRs — NOT key results):
  - <project / feature / experiment> → drives <KR#>
  - <...>

HOW WE'LL SCORE & CHECK IN:
  Cadence: <weekly / biweekly>, owner: <name>
  Scoring: 0.0–1.0 per KR (1.0 = target, ~0.7 = strong progress); type: <committed | aspirational>

RISKS / SANDBAGGING CHECK:
  - Targets we're confident we'll hit (too soft?): <...>
  - Targets that may be impossible (too hard?): <...>
  - Baselines we're unsure of: <...>
```

## Avoid (anti-patterns)
- **Output/task KRs.** "Ship feature X", "launch the redesign", "hire 3 engineers" — these are work, not results. Move them to Initiatives and ask what *outcome* they should produce.
- **No baseline or no number.** "Improve activation" is not a KR. "Activation 38% → 50%" is. If there's no baseline, you can't score it.
- **Too many objectives.** Five "top priorities" means none. Cut to one Objective per team per cycle.
- **Sandbagged targets.** A target you're 95% sure you'll hit isn't a goal, it's a forecast. Stretch it until it's uncomfortable but plausible.
- **Impossible targets.** The opposite failure — a 10x target nobody believes demotivates and gets ignored. Aim for ~0.7-likely.
- **A KR that's a to-do list.** If your KR has multiple sub-bullets of tasks, it's a project, not a key result.

## Tips
- If you can complete a KR without anyone's behavior or the business changing, it's an output — rewrite it.
- One Objective, three KRs is the sweet spot. Resist the urge to add a fourth.
- Pair "grow" KRs with a "guardrail" KR (e.g. grow signups *without* dropping retention below baseline) so you don't win the metric and lose the war. A guardrail KR uses a floor, not a baseline→target arrow — write it `hold ≥ <floor>` and tag it `[committed]`.
- Keep Objectives free of numbers and KRs free of adjectives — the Objective inspires, the KRs measure.
- **Launch-coupled KRs** (a KR whose number can only move after a dated mid-quarter dependency — a feature GA, migration, or partner launch): write the gating date into the KR and set a conditional re-baselining rule up front — if the dependency slips past <date>, re-cut the target to the time actually left rather than scoring it 0.0. And don't concentrate multiple KRs on a single unproven dependency; if one launch underpins the whole set and it slips, the entire quarter scores zero.
- Review weekly, score at quarter-end. OKRs you only look at twice a year are theater.
