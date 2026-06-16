---
name: skill-creator
description: Create a new skill for this Product Manager OS — in the same format and quality bar as the built-in skills. Use when the user says "make a skill for X", "add a skill", "I keep doing X manually, turn it into a skill", or wants to extend the OS with their own framework or workflow.
---

# Skill Creator

Turns a repeatable PM task into a proper OS skill — a `SKILL.md` that drops into `skills/` and gets picked up automatically. This is how the OS grows past what shipped: when you find yourself doing the same thing twice, make it a skill.

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
5. **Battle-test it** — run it once on a realistic input, then read the output as a skeptic: could a real PM ship this? Is the template complete? Fix what breaks. (Mirror how the OS skills were verified.)
6. **Place it** — write to `skills/<name>/SKILL.md`. It's live next session.

## Output template (the skill scaffold)
```
---
name: <kebab-name — matches the folder exactly>
description: <2-4 sentences, third person, trigger-rich. What it does, then "Use when ..." with literal phrases. Under ~70 words.>
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

## Tips
- Steal the structure of the closest existing skill in `skills/` — consistency makes the whole OS feel like one thing.
- Write the *output template* first; the process is just "how to fill it in well."
- Name anti-patterns from real scars — the failure modes you've personally hit.
- If it's broadly useful, contribute it back so every TPC subscriber gets it.
