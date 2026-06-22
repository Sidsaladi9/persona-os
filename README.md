# Persona OS — by The Product Channel

**Drop-in operating systems for knowledge workers.** Each "OS" turns Claude Code into a senior partner for one role — an operating brain, a memory that learns you, 40+ book-grounded skills, and automations for your weekly work.

The part nothing else has: **it gets better the more you use it.** The OS watches the work you repeat and builds you custom skills for it — drafted from how *you* did it, all on your machine. A static skill pack is something the platform now gives away free; an OS that learns you and grows its own toolkit is a category of one.

Built by [Sid Saladi](https://sidsaladi.substack.com) for **The Product Channel**.

---

## Available now

| OS | For | What's inside |
|---|---|---|
| 🧭 **[Product Manager OS](plugins/product-manager-os)** | Product managers | operating brain · learning memory + `/setup` · **self-improving loop** · 40+ book-grounded skills · live connectors + write-back · automations · getprompts + getskills |

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

A Persona OS isn't a prompt pack — it's a stack:

1. **An operating brain** (`CLAUDE.md`) — how Claude behaves in the role: how to think, which skill to reach for, how to push back, how to format.
2. **A memory that learns you** — Claude reads it each session and writes to it as it learns your product, team, and preferences. A 3-minute `/setup` fills it, and it stops asking the same questions twice.
3. **A self-improving loop** — the OS logs the work you repeat and offers to build you a custom skill for it, drafted from how *you* did it (you accept, tweak, or reject — nothing is automatic). This is the part a static pack structurally can't be: it gets sharper the more you use it.
4. **40+ skills** — focused, book-grounded playbooks Claude reaches for by intent ("write a PRD", "review our metrics"). You describe what you need; you don't memorize commands.
5. **Connected, not copy-paste** — pull live data from your tools and write the work back (stories → tracker, spec → docs, update → Slack). `/connect` wires them up; it always drafts and asks before posting.
6. **Automations + bundled libraries** — weekly reviews, sprint kickoffs, and the self-improvement tune-up, runnable on a schedule; plus [getprompts](https://getprompts.org) (900+ PM prompts) and [getskills](https://getskillsai.org) (3,000+ skills + a PM pack), wired in zero-config.

It works with **zero connected accounts** — paste your data and go. Connect your tools (Linear, Jira, Amplitude, Notion, Slack…) and it goes hands-free.

---

## License & sharing

Free for subscribers of The Product Channel. Use it, fork it, adapt it to your team. If it helps, share the newsletter — that's the only ask.

📬 **[Subscribe to The Product Channel](https://sidsaladi.substack.com)** for more tools like this.
