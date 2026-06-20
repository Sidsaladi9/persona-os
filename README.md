# Persona OS — by The Product Channel

**Drop-in operating systems for knowledge workers.** Each "OS" turns Claude Code into a senior partner for one role — a complete kit of skills, an operating brain, a memory that learns you, and automations for the work you do every week.

Built by [Sid Saladi](https://theproductchannel.substack.com) for **The Product Channel**.

---

## Available now

| OS | For | What's inside |
|---|---|---|
| 🧭 **[Product Manager OS](plugins/product-manager-os)** | Product managers | 40+ book-grounded skills · `/setup` + 5 chained commands · operating brain · learning memory · automations · getprompts + getskills |

**Coming next:** Team OS · Founder OS · Marketer OS · Engineering Lead OS.

---

## Install (pick one)

### Option A — One command (recommended)
If you use Claude Code, add this marketplace and install the OS you want:

```
/plugin marketplace add Sidsaladi9/persona-os
/plugin install product-manager-os
```

That's it. The skills, memory, and automations are live. Restart Claude Code and start asking.

### Option B — Clone and drop in
Prefer to keep it in your own project folder?

```bash
git clone https://github.com/Sidsaladi9/persona-os.git
cp -r persona-os/plugins/product-manager-os/* /path/to/your/project/
```

Now open that project in Claude Code. The `CLAUDE.md` loads automatically, the `skills/` are available, and `memory/` is yours to fill in.

> No GitHub? Download the repo as a ZIP (green **Code** button → **Download ZIP**), unzip, and copy the `product-manager-os` folder into your project.

---

## What "an OS" actually means

Every Persona OS is built from four parts:

1. **Skills** — focused, reusable playbooks Claude reaches for by intent (e.g. "write a PRD", "review our metrics"). You don't memorize commands; you just describe what you need.
2. **A CLAUDE.md operating brain** — defines how Claude behaves in that role: how to think, which skill to use when, how to push back, how to format.
3. **A memory system** — Claude reads it at the start of each session and writes to it as it learns your product, team, and preferences. It stops asking the same questions twice.
4. **Automations** — ready-to-wire routines for the recurring work of the role (weekly reviews, sprint kickoffs, daily summaries), runnable on a schedule.
5. **Bundled libraries** — MCP servers wired in so the OS can pull from curated prompt/skill libraries live. Product Manager OS ships [getprompts](https://getprompts.org) (900+ PM prompts) and [getskills](https://getskillsai.org) (3,000+ skills + a PM pack), zero-config.

It works with **zero connected accounts** — paste your data and go. Connect your tools (Linear, Jira, Amplitude, Notion, Slack…) and it gets hands-free.

---

## License & sharing

Free for subscribers of The Product Channel. Use it, fork it, adapt it to your team. If it helps, share the newsletter — that's the only ask.

📬 **[Subscribe to The Product Channel](https://theproductchannel.substack.com)** for more tools like this.
