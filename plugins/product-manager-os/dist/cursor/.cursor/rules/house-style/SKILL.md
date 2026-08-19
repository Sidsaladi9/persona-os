---
name: house-style
description: Capture the company's house style (voice, formatting, terminology, templates, branding) so every other skill generates in your format. Use when the user says "match our format", "use our style", "here's an example doc — write like this", "set up our house style", "make outputs look like ours", or pastes a sample doc / brand guide to learn from.
tier: quick
time: 10 min
inputs: one real company doc to learn the format from
outputs: memory/house-style.md
---

# House Style

Every other skill in this OS produces a generic-but-solid format by default. This skill captures *your company's* format once — voice, structure, terminology, templates, branding — into `memory/house-style.md`, so from then on every spec, update, and plan comes out looking like it was written inside your company, not by a tool.

**Grounded in:** style-guide practice (e.g. *The Elements of Style*; Mailchimp / Atlassian content design systems): codify voice + structure once, apply it everywhere.

## When to use this
- First-time setup: you want all outputs to match your company's format.
- You have an existing doc (a real PRD, a brand guide, a great stakeholder update) and want Claude to write like that.
- Your outputs keep coming out in a style you have to re-edit every time.
- Onboarding the OS for a new team with its own conventions.

## Before you start (gather these)

Format is learned from an example, never asked cold. Get one of these in hand:
- **A real document the company published** — a shipped PRD, a launch update, a board memo. The more recent and the more "normal" it is, the better; a showpiece teaches you the exception.
- **The audience it was written for** — an exec memo and a team update follow different rules, and merging them produces a style that fits neither.
- **Anything already written down** — a style guide, a brand doc, a template someone maintains. Even a stale one tells you what they *think* the rules are.
- **The terminology that matters** — what they call their users, their teams, their releases. Getting "teams" vs "customers" wrong is the fastest way to sound external.

One good sample beats a description of the style. If they offer to describe it instead, ask for the document anyway — people describe the style they intend, not the one they write.

## Process
1. **Ingest the sample(s).** If the user pastes a doc, read it as evidence — don't ask what you can observe.
2. **Extract the style** along these axes: voice & tone, formatting conventions (headings, bullets vs prose, length, TL;DR, status markers, tables), terminology & naming (what they call customers/the product, preferred vs banned terms, internal codenames), document templates (required section structures per doc type), branding (colors/fonts), and audience defaults.
3. **Infer, then confirm.** State what you extracted as a draft and flag anything you're guessing. Ask only about what the sample can't tell you.
4. **Write it to `memory/house-style.md`** in that file's structure, replacing the template placeholders. Keep it tight — it's read every session, so no essays.
5. **Confirm the apply rule:** from now on, every skill conforms outputs to this file; where a doc type has a house template, it overrides the skill's default structure.

## Output template
Write/overwrite `memory/house-style.md` using its section headers (Voice & tone, Formatting conventions, Terminology & naming, Document templates, Branding, Audience defaults). Then reply to the user with a short summary:
```
HOUSE STYLE CAPTURED
- Voice: [one line]
- Formatting: [one line]
- Key terms: [the 2-3 that matter most]
- Doc templates captured: [which doc types now have a house format]
- Assumptions to confirm: [anything you guessed]
Every skill will now generate in this style. Edit memory/house-style.md anytime.
```

## Avoid (anti-patterns)
- **Interrogating when a sample exists** — extract from the doc; only ask about gaps.
- **Over-stuffing the file** — it loads every session; capture rules, not a brand bible.
- **Inventing rules from one data point** — mark low-confidence extractions as assumptions to confirm.
- **Locking in a banned term you only saw once** — distinguish a real convention from a one-off word choice.

## Tips
- The single highest-leverage input is one excellent real doc — ask for it.
- Re-run this whenever the company rebrands or changes conventions; it just overwrites the file.
- Keep internal codenames in the "must NOT appear in customer-facing docs" list — it stops leaks in `release-notes` and `stakeholder-update`.
