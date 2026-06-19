# Memory Index — Product Manager OS

This file is loaded at the start of every product-work session. It's the index of everything Claude has learned about your product, team, and how you work. Each line points to a file in this folder.

Keep entries to one line. Put the actual content in the linked file, never here.

## Knowledge — what's true about you (read these at session start)

- [Product](product.md) — what we're building, for whom, the business model, the goals.
- [Team](team.md) — who's on the team, who owns what, our rituals and tools.
- [Preferences](preferences.md) — how I like to work, tone, formats I prefer.
- [House style](house-style.md) — the company's format: voice, formatting, terminology, doc templates, branding (every skill conforms to this).
- [Strategy](strategy.md) — current bets, themes, constraints, deadlines.

> The files above start as **templates**. Run `/setup` to fill them in fast, or let Claude fill them in as you work, so every session starts with context instead of questions. Add new files as you accumulate knowledge (e.g. `product-<slug>.md` for a second product), and add a one-line pointer here for each.

## Behavior — what you've been doing (the self-improvement layer)

- [Activity log](activity-log.md) — one line per meaningful task; how the OS spots work you repeat. Local-only.
- OS suggestions (`os-suggestions.md`) — pending "want me to build/tune a skill?" proposals; created when the first suggestion appears.
