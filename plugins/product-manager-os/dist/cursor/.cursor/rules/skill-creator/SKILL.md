---
name: skill-creator
description: Create a new skill for this Product Manager OS — in the same format and quality bar as the built-in skills. Use when the user says "make a skill for X", "add a skill", "I keep doing X manually, turn it into a skill", or wants to extend the OS with their own framework or workflow.
tier: guided
time: 30-60 min
inputs: 3 real examples of the job you keep hand-rolling
outputs: skills/<new-skill>/SKILL.md
---

# Skill Creator

Turns a repeatable PM task into a proper OS skill — a `SKILL.md` that drops into `skills/` and gets picked up automatically. This is how the OS grows past what shipped: when you find yourself doing the same thing twice, make it a skill.

**Grounded in:** *The Pragmatic Programmer* — Andy Hunt & Dave Thomas: the DRY principle applied to your own judgment. A process you re-derive by hand every time is duplication; encode it once, in one place, and improve it there. The corollary matters as much — don't encode a process you've only run once; you'll encode the accident, not the pattern.

## When to use this
- You keep running the same PM workflow by hand and want Claude to own it.
- You have a framework (yours or a book's) you want encoded as a guided skill.
- A built-in skill is close but you want a specialized variant for your domain.
- You're contributing a skill back to the OS.

## Before you start (gather these)
- **What the skill does** in one sentence, and the *trigger* — what would someone say to invoke it.
- **The framework or process** it should apply (steps, not vibes).
- **The output** it should produce (the artifact).
If any are vague, ask 2–3 sharp questions before writing — a skill built on a fuzzy job triggers wrong and produces mush.

## Process
1. **Name it** — short, kebab-case, verb-or-noun that matches how people ask (`pricing`, `retro`, `journey-map`). The folder and the frontmatter `name` must match exactly.
2. **Write the description for triggering** — third person, 2–4 sentences, and pack in the literal phrases a user would type ("Use when ... 'do X', 'help me Y'"). This is what makes Claude reach for it at the right moment; spend real effort here.
3. **Draft the body** using the OS skill template (below). The *output template* is the centerpiece — make it copy-pasteable and genuinely usable.
4. **Add anti-patterns** — the 3–5 ways this task is commonly done badly. This is half the value.
5. **Score it — this is not optional.** Run the loss function and fix what it flags:
   ```bash
   python3 tests/score_skill.py skills/<name>/SKILL.md
   ```
   **A new skill ships at 100, never at the 85 floor.** The floor is what a skill is allowed to decay to, not what it's allowed to arrive at. Every failed check is a real gap: no `Avoid` section means you never wrote down how this goes wrong; a failed `asks_before_producing` on a `guided` skill means it will confidently invent the inputs it should have asked for.
6. **Battle-test it** — run it once on a realistic input, then read the output as a skeptic: could a real PM ship this? Is the template complete? Does the artifact land at the declared `outputs` path? Fix what breaks.
7. **Place it and re-run the suite** — write to `skills/<name>/SKILL.md`, then `python3 tests/run_all.py`. That checks the whole set, so you find out immediately if the new skill collides with an existing one or routes somewhere that doesn't exist. It's live next session.


## The frontmatter contract (get this right or nothing else matters)
Four fields decide whether a PM can tell, at a glance, if they can start this right now. Fill them honestly — an optimistic `time` is worse than no estimate.

| Field | Rule |
|---|---|
| `tier` | **`quick`** = they paste input, they get the artifact, no interrogation (5–40 min). **`guided`** = you ask 3–5 sharp questions first, then produce (30–90 min). **`campaign`** = runs across multiple sessions with state in `memory/` and `workspace/` (days to weeks). Pick by *how it feels to run*, not by how important it is. |
| `time` | A range a busy person can plan around. If you're unsure, take your estimate and widen it. |
| `inputs` | What they need in hand. Be concrete: "a retention table by signup cohort", not "data". This is the field that prevents confident artifacts built on nothing. |
| `outputs` | Where the artifact lands, relative to `workspace/` — `projects/` · `research/` · `strategy/` · `metrics/` · `meetings/` · `comms/` · `decisions/`. Use `<project>` and `<date>` placeholders. Slow-changing calls go in `strategy/`; anything about one named piece of work goes in `projects/<slug>/`. |

Get `tier` wrong and the OS offers a two-week process to someone with fifteen minutes. Get `outputs` wrong and the artifact never lands anywhere the next skill can find it.

## Draft skills (when the self-improvement loop creates one)
When a skill is born from the tune-up (the OS noticed you'd hand-rolled the same job 3×), it's created from your last ~3 real examples — so it captures *your* format and tone, not a generic template. Mark these **provisional** by adding `status: draft` to the frontmatter:
```
---
name: <kebab-name>
description: <trigger-rich, as below>
status: draft   # loop-generated; fires normally but provisional until it proves out
---
```
A draft skill triggers and runs exactly like any other — the flag is just a promise that the OS will keep an eye on it. It **graduates** (drop the `status: draft` line) after it's been used **3 times without a correction** (per `memory/activity-log.md`). If a draft keeps drawing the same correction, tune it instead of graduating. User-authored skills don't need this flag — they're permanent from the start.

## Output template (the skill scaffold)
```
---
name: <kebab-name — matches the folder exactly>
description: <2-4 sentences, third person, trigger-rich. What it does, then "Use when ..." with literal phrases. Under ~70 words.>
tier: quick | guided | campaign
time: <honest estimate, e.g. "45-90 min">
inputs: <what the user must have in hand before starting>
outputs: <workspace path, e.g. projects/<project>/spec.md>
---

# <Title>

<1-2 sentence intro grounding it in its framework.>

## When to use this
- 4-5 concrete situations

## Before you start (gather these)
- the inputs needed; instruct to ASK if 2+ are missing, or proceed + state assumptions if provided

## Process
- numbered, opinionated steps that apply the framework

## Output template
- a complete, copy-pasteable markdown artifact with [bracketed] placeholders


## Worked example (a real one, end to end)
The tune-up notices three hand-rolled win/loss write-ups in `memory/activity-log.md`, all `skill: none`. Here's the skill that comes out of it:

- **Name** — `win-loss`. Kebab-case, matches how someone asks ("run a win-loss on the Q3 losses").
- **Description** — packs the literal phrases: *"Use when a PM says 'why are we losing deals', 'win-loss analysis', 'analyze these lost deals'…"* Without those strings it never fires.
- **Contract** — `tier: guided` (it needs to ask which segment and what time window before it can say anything useful), `time: 60-90 min`, `inputs: deal notes or CRM close reasons for at least 10 decided deals`, `outputs: research/win-loss-<quarter>.md`.
- **Grounded in** — a named source, so the judgment isn't invented.
- **Anti-patterns** — pulled from the three real examples: *counting stated close-reasons as causes*, *analyzing losses without the wins as a control*, *sample sizes under ~10 treated as signal*.
- **Score** — 92 on the first pass, failing `has_concrete_example` and `output_template_is_concrete`. Both are real: the template was a bullet list, not an artifact. Fixed, re-scored, 100. Ships.

The whole thing took 40 minutes, and the anti-patterns section is the part that makes it better than the hand-rolled versions it replaced.

## Avoid (anti-patterns)
- 3-5 concrete failure modes specific to this skill

## Tips
- 3-4 sharp pro tips
```

## Avoid (anti-patterns)
- **A vague description** — if it doesn't contain the words a user would actually say, the skill never triggers.
- **A skill that's really a prompt** — if there's no framework, no process, and no reusable output template, it's a one-off, not a skill.
- **Skipping the battle-test** — shipping it unread is how broken templates and wrong frameworks sneak in. Our whole edge is "verified."
- **Overlap creep** — if it's 80% an existing skill, extend that one or make a clearly-scoped variant; don't fork a near-duplicate.
- **Wall-of-text body** — keep it skimmable; the template does the heavy lifting, not prose.
- **A dishonest `time` or a wrong `tier`.** Labelling a two-week campaign as `guided` is how a PM gets ambushed. If you're not sure, pick the heavier tier and say so.
- **Shipping at the floor.** 85 is the decay limit, not the bar. A skill that arrives at 86 has nowhere to go but out of the suite.

## Tips
- Steal the structure of the closest existing skill in `skills/` — consistency makes the whole OS feel like one thing.
- Write the *output template* first; the process is just "how to fill it in well."
- Name anti-patterns from real scars — the failure modes you've personally hit.
- If it's broadly useful, contribute it back so every TPC subscriber gets it.
