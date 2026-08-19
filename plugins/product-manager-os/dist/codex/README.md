# Product Manager OS — Codex CLI (OpenAI)

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **53 skills** in `skills/`
- **Operating brief:** `AGENTS.md`
- **Workflows:** `COMMANDS.md` (invoke by name)
- **Memory:** `memory/` · **Workspace:** `workspace/` · **Automations:** `automations/` · **Tools:** `tests/`
- **Workers:** `WORKERS.md` (described — this host has no subagents)
- **Bundled libraries:** `MCP-SETUP.md` — this host's MCP config path varies, so the server definition ships instead

## Install

Copy into your project root. Codex reads `AGENTS.md` on start.
Slash commands are not native — the workflows are described in
`COMMANDS.md` and can be invoked by name in plain language
("run the weekly workflow").

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
