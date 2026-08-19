# Product Manager OS — Claude Code

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **53 skills** in `.claude/skills/`
- **Operating brief:** `CLAUDE.md`
- **Workflows:** `.claude/commands/` (8 slash commands)
- **Memory:** `memory/` · **Workspace:** `workspace/`
- **Workers:** `.claude/agents/` (critic + researcher)
- **Bundled libraries:** `.mcp.json` — loads automatically

## Install

Copy the contents of this folder into your project root.
Claude Code loads `CLAUDE.md`, `.claude/skills/`, `.claude/commands/`
and `.mcp.json` automatically — nothing to configure.

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
