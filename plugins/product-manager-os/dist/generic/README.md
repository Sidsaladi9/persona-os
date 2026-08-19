# Product Manager OS — Any agent (plain files)

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **53 skills** in `skills/`
- **Operating brief:** `AGENTS.md`
- **Workflows:** `COMMANDS.md` (invoke by name)
- **Memory:** `memory/` · **Workspace:** `workspace/`
- **Workers:** `WORKERS.md` (described — this host has no subagents)
- **Bundled libraries:** not included — this target has no MCP support

## Install

Point your agent at `AGENTS.md` as its system/context file and
give it read access to `skills/`. Everything is plain markdown.

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
