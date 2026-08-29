# Install — Product Manager OS

53 skills, an operating brain, a memory that learns your product, and a workspace your work lands in. Free, MIT, runs entirely on your machine.

**Find your tool below.** Every path takes under two minutes.

---

## The short version — one command each

| Your tool | One step |
|---|---|
| **Claude Code** | `claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os` |
| **Cursor / Codex / Gemini / anything** | `curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh \| bash` |
| **Cowork** | Plugins → Personal → Add marketplace from GitHub → `Sidsaladi9/persona-os` |

Run it **inside the folder you want the OS to live in** — see below, it's the one thing worth thirty seconds of thought. Then restart your tool and type `/setup`.

> **A note on command names.** Installed as a plugin, Claude Code namespaces the commands: type **`/product-manager-os:setup`**, `/product-manager-os:tune-up`, `/product-manager-os:weekly`, and so on. Installed with `get.sh` or `install.sh`, they are the plain `/setup`, `/tune-up`, `/weekly`. Both are written as `/setup` throughout these docs for readability — prefix them if you installed the plugin, or just say what you want in plain English, which works either way.


The `get.sh` one-liner detects your tool, needs no git and no Python, installs nothing system-wide, and stops to ask if you're about to install into `~` or `~/Downloads`.

*Prefer not to pipe a script into bash? Reasonable:*

```bash
curl -fsSLO https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh
```
```bash
less get.sh && bash get.sh cursor
```

---

## Then the part nobody tells you

**Pick a folder first.** The OS keeps your product context on disk — what you're building, your team, your north star, plus every spec and update it writes. All of that lives in the folder you're working in.

If you write code, use your product's repo. If you don't, make a dedicated one:

```bash
mkdir ~/product-work && cd ~/product-work
```

That folder becomes your product brain. Open it in Claude Code every time — the OS gets smarter in the folder it remembers you in, and starting somewhere new means starting over.

---

## Claude Code — easiest

**Step 1.** Open a terminal in your folder and start Claude Code:

```bash
cd ~/product-work && claude
```

**Step 2.** Install — one command, from the terminal:

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

*Or from inside Claude Code, if you prefer slash commands: `/plugin marketplace add Sidsaladi9/persona-os` then `/plugin install product-manager-os`.*

**Step 3.** Restart Claude Code (quit and run `claude` again in the same folder).

**Step 4.** Type `/setup` and answer a few questions — or skip it and start working; it'll offer again when it matters.

That's it. You never `git clone` anything, and you don't need to know what a repo is.

*If your organization disables the plugin marketplace, use the file install below — same thing.*

---

## Claude Cowork

1. Open **Plugins** in the sidebar
2. **Personal** → **Add marketplace from GitHub**
3. Paste `Sidsaladi9/persona-os`
4. Install **product-manager-os**

---

## Cursor · Codex · Gemini CLI · anything else

One command. No Python, no build step.

```bash
cd ~/product-work && curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash
```

It detects your tool. To name one explicitly:

```bash
curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash -s -- codex
```

<details>
<summary>Prefer to clone it yourself?</summary>

```bash
git clone https://github.com/Sidsaladi9/persona-os.git
```
```bash
bash persona-os/install.sh --target cursor ~/code/my-project
```
</details>

Targets:

```bash
bash persona-os/install.sh --list
```

| Target | Use it for |
|---|---|
| `claude-code` | Claude Code, file install (no marketplace) |
| `claude-cowork` | Cowork, manual install |
| `codex` | Codex CLI |
| `cursor` | Cursor |
| `gemini-cli` | Gemini CLI |
| `generic` | Any other agent that reads a context file |

---

## No git? No terminal?

1. Go to the [repo](https://github.com/Sidsaladi9/persona-os) → green **Code** button → **Download ZIP**
2. Unzip it
3. Open `plugins/product-manager-os/dist/` and copy the folder matching your tool into your project

That's the whole install. The bundles are pre-built and committed for exactly this reason — you shouldn't need a toolchain to install a pile of markdown.

---

## What lands in your project

Each bundle carries the same OS, packaged the way that host expects.

| | Claude Code | Cursor | Codex | Gemini CLI |
|---|---|---|---|---|
| Operating brief | `CLAUDE.md` | `AGENTS.md` | `AGENTS.md` | `GEMINI.md` |
| Skills | `.claude/skills/` | `.cursor/rules/` | `skills/` | `skills/` |
| Workflows | `.claude/commands/` (8 slash commands) | `COMMANDS.md` | `COMMANDS.md` | `COMMANDS.md` |
| Workers | `.claude/agents/` | `WORKERS.md` | `WORKERS.md` | `WORKERS.md` |
| Memory | `memory/` | `memory/` | `memory/` | `memory/` |
| Workspace | `workspace/` | `workspace/` | `workspace/` | `workspace/` |
| Libraries | `.mcp.json` | `.cursor/mcp.json` | `MCP-SETUP.md` | `MCP-SETUP.md` |

**Slash commands are Claude-only.** On other hosts the same workflows live in `COMMANDS.md` and you invoke them by name — *"run the weekly workflow"*, *"new feature: bulk export"*.

**The two workers** — `critic` and `researcher` — run as real subagents on Claude. Elsewhere their briefs ship as `WORKERS.md`, and the skills that use them say plainly that the result is a self-review rather than an independent one.

---

## It won't overwrite your work

`install.sh` is careful about this, and it's worth knowing before you run it:

- An existing `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` is **left alone** — the OS brain lands beside it as `CLAUDE-product-manager-os.md`, and you decide what to merge.
- `memory/` and `workspace/` are **only seeded where a file is missing.** Anything you've filled in stays.
- Skills, commands, and workers are OS-owned and get replaced on reinstall. That's how you upgrade.

---

## First two minutes after installing

**1. Run setup.** On Claude: `/setup`. Anywhere else: just say *"set me up."*

The first time you ask for anything, the OS creates `memory/` and `workspace/` in your folder — that's where your product context and every artifact it writes will live. It'll say one line about it and then answer your question.

Nine short questions, about three minutes, and you can skip any of them or the whole thing. Fastest path is **"bootstrap from a doc"** — paste a real PRD or strategy doc and it infers your product *and* your house format in one pass. No doc handy? There's a sample one at [`examples/sample-prd.md`](plugins/product-manager-os/examples/sample-prd.md) you can paste to see what it does.

Skipped it? Nothing is lost. `/setup` resumes later and only asks what's still blank, and `/setup status` shows what it knows and what it's missing.

**2. Just describe the work.** You never name a skill:

```
Turn this into a spec: sales keeps asking for bulk CSV export,
but I think the real problem is they can't get data out at all.
Here's the ticket thread: [paste]
```

```
Activation dropped from 34% to 27% week over week.
Here's the funnel by step and by signup source: [paste]. What happened?
```

---

## Optional: the bundled libraries

The OS is fully functional without these. They add live access to [getprompts](https://getprompts.org) (900+ PM prompts) and [getskills](https://getskillsai.org) (3,000+ installable skills), so the OS checks whether a proven version of something already exists before hand-rolling it.

Two public npm packages. No account, no API key, read-only. Needs Node 18+.

On Claude Code they load automatically from `.mcp.json`. To check:

```bash
claude mcp list
```

Both should say **Connected**. If not:

```bash
claude mcp add getprompts -- npx -y getprompts-mcp
```

```bash
claude mcp add getskills -- npx -y getskills-mcp
```

On Cursor the config ships at `.cursor/mcp.json`. On Codex and Gemini CLI, see `MCP-SETUP.md` in your bundle — it has the server definition, and points you at your host's own MCP docs rather than guessing at a config path that moves between versions.

If your organization blocks MCP servers, skip this entirely. All 53 skills work without it.

---

## Troubleshooting

**`/plugin` does nothing.** Your org has the marketplace disabled. Use the file install — same content.

**Skills don't fire.** Confirm the operating brief is at your project root with the right name for your host (see the table above), and that you opened the *project folder*, not a parent directory.

**MCP servers show as failed.** They need Node 18+ (`node --version`). If your org blocks them, skip — nothing else depends on them.

**It keeps asking what my product is.** Memory isn't filled in. Run `/setup status` to see the gaps, then `/setup` to fill them.

**It forgot everything I told it.** You're almost certainly in a different folder. Memory lives in the folder you were working in — `pwd` to check, then `cd` back and restart. This is the single most common confusion for people new to Claude Code.

**Something produced output I couldn't use.** Log it in `memory/incidents.md` and run `/tune-up`. One real failure is enough for the OS to propose a fix — that's the whole point of the loop.

---

*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT licensed — fork it, adapt it, ship it to your team.*
