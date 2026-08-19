# Product Manager OS — Cursor

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **53 skills** in `.cursor/rules/`
- **Operating brief:** `AGENTS.md`
- **Workflows:** `COMMANDS.md` (invoke by name)
- **Memory:** `memory/` · **Workspace:** `workspace/`
- **Workers:** `WORKERS.md` (described — this host has no subagents)
- **Bundled libraries:** `.cursor/mcp.json` — loads automatically

## Install

Copy into your project root. Cursor reads `AGENTS.md`, and the
skills land in `.cursor/rules/` where they're picked up as rules.

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
