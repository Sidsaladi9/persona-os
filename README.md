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

## Install

**First, pick a folder.** The OS keeps your product context on disk — what you're building, your team, every artifact it writes. It all lives in the folder you run it in. Use your product's repo, or `mkdir ~/product-work`. Open that same folder every time; it's where the OS remembers you.

**Claude Code**

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

**Cursor · Codex · Gemini · anything else**

```bash
curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash
```

Restart, then type `/setup`. No git, no Python, nothing system-wide.

**Every path — Cowork, ZIP download, what lands where, troubleshooting → [INSTALL.md](INSTALL.md).**

---

## Why an OS and not a prompt pack

A prompt pack is static. It can't remember your product, so you retype the context every session. It has no opinion, so it gives you the average PRD. And it never changes, so the work you keep repeating stays work you keep repeating.

An OS fixes all three: an operating brain, a memory that learns your product, a workspace your artifacts land in, and **a loop that turns the work you repeat into skills you didn't have to write.** Nobody else in this space has the last one — the closest thing is a memory tool bolted on beside the skills, not inside them.

**[→ What's actually in Product Manager OS](plugins/product-manager-os)** — the 53 skills, the two isolated workers, the three-signal improvement loop.

---

## Why you can trust the skills

Every skill is **scored, not vibe-checked**. `tests/score_skill.py` grades each one out of 100 across six dimensions; `tests/check_all_artifacts.py` then checks a real produced artifact against the output template that skill promised. A third check verifies that every file the OS tells you to use actually exists in every shipped bundle.

All of it runs in CI, and CI fails when a score goes **down**, not just when a file breaks.

Current: **53 skills, all 53 at 100/100** — [see the scoreboard](plugins/product-manager-os/tests/RESULTS.md).

That's the difference between "battle-tested" as a claim and as something you can check out and run.

---

## Runs on more than Claude Code

The skills are plain markdown; the packaging isn't. Each host looks for its brief in a different place and not all have slash commands, so the OS ships a **pre-built bundle per host** — Claude Code, Cowork, Codex, Cursor, Gemini CLI, and a generic one. Browse them in [`dist/`](plugins/product-manager-os/dist) or let `get.sh` pick.

Two things degrade honestly off Claude: slash commands become named workflows in `COMMANDS.md`, and the two workers become briefs in `WORKERS.md` — with the skill saying plainly that the result is a self-review rather than an independent one.

---

## Questions, bugs, contributions

- **Something broken?** [Open an issue](https://github.com/Sidsaladi9/persona-os/issues) — say which host you installed on and what you ran. Bugs that only show up after install are the valuable ones.
- **Want to add a skill?** [CONTRIBUTING.md](CONTRIBUTING.md). `skill-creator` writes most of it for you; the bar is a 100 on the scorer.
- **Curious what it looks like?** Every skill's real output is in [SAMPLE-OUTPUTS.md](plugins/product-manager-os/examples/SAMPLE-OUTPUTS.md), run against one demo company.
- **Want a different persona?** Team OS, Founder OS, Marketer OS and Engineering Lead OS are next. Open an issue and say which.

---

## License & sharing

Free for subscribers of The Product Channel. Use it, fork it, adapt it to your team. If it helps, share the newsletter — that's the only ask.

📬 **[Subscribe to The Product Channel](https://sidsaladi.substack.com)** for more tools like this.
