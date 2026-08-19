# Persona OS — by The Product Channel

[![Skills](https://github.com/Sidsaladi9/persona-os/actions/workflows/skills.yml/badge.svg)](https://github.com/Sidsaladi9/persona-os/actions/workflows/skills.yml)
[![Skills scored](https://img.shields.io/badge/53%20skills-mean%20100.0%2F100-2ea44f)](plugins/product-manager-os/tests/RESULTS.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Drop-in operating systems for knowledge workers.** Each "OS" turns Claude Code into a senior partner for one role — an operating brain, a memory that learns you, 53 book-grounded skills, and automations for your weekly work.

The part nothing else has: **it gets better the more you use it.** The OS watches the work you repeat and builds you custom skills for it — drafted from how *you* did it, all on your machine. A static skill pack is something the platform now gives away free; an OS that learns you and grows its own toolkit is a category of one.

Built by [Sid Saladi](https://sidsaladi.substack.com) for **The Product Channel**.

---

## Available now

| OS | For | What's inside |
|---|---|---|
| 🧭 **[Product Manager OS](plugins/product-manager-os)** | Product managers | operating brain · learning memory + resumable `/setup` · **self-improving loop** · **53 scored, book-grounded skills** · a workspace the work lands in · live connectors + write-back · automations · getprompts + getskills |

**Coming next:** Team OS · Founder OS · Marketer OS · Engineering Lead OS.

---

## Install (pick one)

**First, pick a folder.** The OS keeps your product context on disk — what you're building, your team, your north star, plus every artifact it writes. All of it lives in the folder you run it in. Use your product's repo, or make one: `mkdir ~/product-work && cd ~/product-work`. Open that same folder every time; it's where the OS remembers you.

**Step-by-step for every tool → [INSTALL.md](INSTALL.md).** The short version:

### Claude Code — one command

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

Restart Claude Code, type `/setup`, and start asking. (Slash-command equivalent: `/plugin marketplace add Sidsaladi9/persona-os` then `/plugin install product-manager-os`.)

### Cursor · Codex · Gemini · anything else — one command

```bash
curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash
```

Detects your tool, no git, no Python. Run it in the folder you want the OS to live in.

### No terminal at all

Download the repo as a ZIP (green **Code** button → **Download ZIP**), unzip, open `plugins/product-manager-os/dist/`, and copy the folder matching your tool into your project.

**Full per-tool steps, including what lands where and how to troubleshoot → [INSTALL.md](INSTALL.md).**

---

## What "an OS" actually means

A Persona OS isn't a prompt pack — it's a stack:

1. **An operating brain** (`CLAUDE.md`) — how Claude behaves in the role: how to think, which skill to reach for, how to push back, how to format.
2. **A memory that learns you** — Claude reads it each session and writes to it as it learns your product, team, and preferences. A 3-minute `/setup` fills it, and it stops asking the same questions twice. Skip it and the OS still learns as you work — `/setup` later picks up exactly where you left off, and `/setup status` shows what it knows and what it's missing.
3. **A self-improving loop, fed by three signals** — it logs the work you repeat and offers to build you a custom skill for it, drafted from how *you* did it (you accept, tweak, or reject — nothing is automatic). Three inputs, at deliberately different thresholds:
   - **corrections → 3×** — three edits of the same kind is a preference worth encoding
   - **incidents → 1×** — output you couldn't use is a defect, and waiting for it to recur is waiting to get burned again
   - **dead artifacts** — a skill whose outputs you never open again is producing the wrong thing, or producing it at the wrong moment. Nothing else in this category measures that.

   This is the part a static pack structurally can't be: it gets sharper the more you use it.
4. **53 skills, each labelled with what it costs you** — focused, book-grounded playbooks Claude reaches for by intent ("write a PRD", "review our metrics"). You describe what you need; you don't memorize commands. Every skill declares its **tier**, its **time**, and the **inputs** you need in hand, so you can tell whether you can start right now:

   | Tier | Feels like | Time | Count |
   |---|---|---|---|
   | ⚡ `quick` | paste something in, get the artifact | 5–40 min | 17 |
   | 🧭 `guided` | it asks 3–5 sharp questions, then produces | 30–90 min | 30 |
   | 🗓 `campaign` | a process across sessions, state kept in memory | days–weeks | 6 |
5. **A workspace the work lands in** — every artifact is written to a predictable path under `workspace/` (`projects/`, `research/`, `strategy/`, `metrics/`, `decisions/`, …) instead of scrolling away in a chat window. Skills read it before they ask you anything, so you stop re-pasting context you already gave.
6. **Two workers, where isolation actually matters** — a `critic` that reviews your spec having never seen the conversation that produced it (any reviewer who watched you write it has already been persuaded), and a `researcher` that reads a corpus cold so the first theme you noticed doesn't become the only one you find. Nine skills delegate to them; the rest don't, because most work doesn't need it.
7. **Connected, not copy-paste** — pull live data from your tools and write the work back (stories → tracker, spec → docs, update → Slack). `/connect` wires them up; it always drafts and asks before posting.
8. **Automations + bundled libraries** — weekly reviews, sprint kickoffs, and the self-improvement tune-up, runnable on a schedule; plus [getprompts](https://getprompts.org) (900+ PM prompts) and [getskills](https://getskillsai.org) (3,000+ skills + a PM pack), wired in zero-config.

**The commands**, when you want them: `/setup` (+ `status` / `reset`) · `/tune-up` · `/connect` · `/new-feature` · `/discovery` · `/launch` · `/strategy` · `/weekly`. You rarely need them — describing the work is enough.

It works with **zero connected accounts** — paste your data and go. Connect your tools (Linear, Jira, Amplitude, Notion, Slack…) and it goes hands-free.

---

## Why you can trust the skills

Every skill is **scored, not vibe-checked**. `tests/score_skill.py` grades each `SKILL.md` out of 100 across six dimensions; `tests/check_all_artifacts.py` then checks a real produced artifact against the output template that skill promised. Both run in CI, and CI fails when a score goes **down**, not just when a file breaks.

Current: **53 skills · all 53 at 100/100** — [see the scoreboard](plugins/product-manager-os/tests/RESULTS.md).

That's the difference between "battle-tested" as a claim and as something you can check out and run.

---

## Runs on more than Claude Code

The skills are plain markdown. The packaging isn't — each host looks for its brief in a different place, and not all of them have slash commands. So the OS ships a **pre-built bundle per host**. No build step, no Python:

```bash
bash install.sh --target cursor ~/code/my-project
```

Or browse [`plugins/product-manager-os/dist/`](plugins/product-manager-os/dist) on GitHub, download the ZIP, and copy the folder you want. The bundles are committed on purpose — you shouldn't need a toolchain to install a pile of markdown. CI rebuilds them on every push and fails if what's committed has drifted.

| Target | Entry file | Slash commands |
|---|---|---|
| Claude Code | `CLAUDE.md` | native |
| Claude Cowork | `CLAUDE.md` | native |
| Codex CLI | `AGENTS.md` | inline (`COMMANDS.md`) |
| Cursor | `AGENTS.md` | inline |
| Gemini CLI | `GEMINI.md` | inline |
| Any agent | `AGENTS.md` | inline |

`install.sh` never overwrites your `CLAUDE.md`/`AGENTS.md`, your `memory/`, or your `workspace/` — it seeds what's missing and leaves what's yours.

---

## License & sharing

Free for subscribers of The Product Channel. Use it, fork it, adapt it to your team. If it helps, share the newsletter — that's the only ask.

📬 **[Subscribe to The Product Channel](https://sidsaladi.substack.com)** for more tools like this.
