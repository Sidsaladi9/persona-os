# hooks/ — why this exists

A plugin can ship skills, commands, agents and MCP servers. **It cannot ship a
`CLAUDE.md` that Claude reads.** Only the project's own `CLAUDE.md` is loaded.

That single fact broke the primary advertised install path. `get.sh` / `install.sh`
copy the brain to the project root, so those work. `/plugin install` had no
equivalent, so it delivered 53 skills and none of the OS:

| | via `install.sh` | via `/plugin install` (before this hook) |
|---|---|---|
| Skills, commands, agents, MCP | ✅ | ✅ |
| Operating brain in context | ✅ | ❌ |
| First-run bootstrap of `memory/` + `workspace/` | ✅ | ❌ |
| Artifacts written to `workspace/` | ✅ | ❌ — offered to save, wrote nothing |
| Activity log → self-improving loop | ✅ | ❌ |

Everything people install this for lives in the brain. Without it the plugin is a
prompt pack that happens to be good.

## What was measured, and what it ruled out

Same prompt (`"Turn this into a spec: sales keeps asking for bulk CSV export…"`),
same empty folder, `--permission-mode acceptEdits`:

1. **No hook.** Good spec. Nothing on disk. No `memory/`, no `workspace/`.
2. **Hook emitting a ~40-line condensed brain.** Good spec. Still nothing on disk —
   it *offered* to save the file instead. A summary of the brain is not the brain.
3. **Hook emitting the whole brain on stdout (260 lines).** Model reported only a
   "~2KB preview" reached it; it could not quote a sentence from the middle.
4. **Hook emitting the whole brain as JSON `hookSpecificOutput.additionalContext`
   (26,615 chars).** Same truncation. **SessionStart context is capped at ~2KB
   regardless of the output form.**
5. **Hook emitting a <2KB directive that orders the model to read the brain file.**
   Bootstrapped `memory/` (10 files), `workspace/` (7 folders), `automations/`,
   `tests/`, and wrote the spec to `workspace/projects/data-export/spec.md` — the
   exact path `write-spec` declares in its `outputs:` frontmatter.

So the shipped design is (5): stay under the cap, and spend one `Read` call to get
the real thing. The cap is the constraint that decides this — not taste.

## Rules for anything added here

- **Never write to the user's disk from a hook.** Session start is not consent. The
  hook may only *tell* the model to bootstrap; the model asks, or acts in the open.
- **Stay under ~2KB of output.** Above that it is silently truncated, which is the
  worst possible failure: the plugin looks installed and behaves like a prompt pack.
- **Fail loud.** If the brain is missing, say so in the output rather than degrading
  quietly. `tests/audit.py` also fails the build for it.
- **Say nothing when it isn't product work.** The hook fires in every project the
  user opens. It ends with an explicit instruction not to mention the OS unless
  asked for product work.
