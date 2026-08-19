# Product Manager OS — Gemini CLI

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **53 skills** in `skills/`
- **Operating brief:** `GEMINI.md`
- **Workflows:** `COMMANDS.md` (invoke by name)
- **Memory:** `memory/` · **Workspace:** `workspace/`
- **Workers:** `WORKERS.md` (described — this host has no subagents)
- **Bundled libraries:** `MCP-SETUP.md` — this host's MCP config path varies, so the server definition ships instead

## Install

Copy into your project root. Gemini CLI reads `GEMINI.md`.
Workflows are in `COMMANDS.md`; invoke them by name.

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
