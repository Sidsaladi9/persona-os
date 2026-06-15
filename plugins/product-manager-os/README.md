# 🧭 Product Manager OS

A complete operating system for product managers, running on Claude Code. It turns Claude into a senior PM partner — one that drafts your specs, reviews your metrics, preps your stakeholder updates, and remembers your product across sessions.

From **The Product Channel** by Sid Saladi.

---

## What's inside

```
product-manager-os/
├── CLAUDE.md            # The operating brain — how Claude behaves as your PM partner
├── skills/              # 8 focused playbooks Claude uses by intent
│   ├── write-spec/          turn an idea into a PRD/spec
│   ├── metrics-review/      build a metrics scorecard, investigate spikes/drops
│   ├── competitive-brief/   competitor teardowns + sales battlecards
│   ├── roadmap/             Now/Next/Later, reprioritization with trade-offs
│   ├── sprint-planning/     capacity-aware sprint plans with a clear goal
│   ├── stakeholder-update/  exec / eng / customer status in one pass
│   ├── synthesize-research/ interviews + surveys + tickets → ranked insights
│   └── product-brainstorm/  a sharp sparring partner for ideas
├── memory/              # Claude learns your product, team & preferences here
│   ├── MEMORY.md            index, loaded every session
│   ├── product.md           what you're building (template)
│   ├── team.md              who's who, rituals, tools (template)
│   ├── preferences.md       how you like to work (template)
│   └── strategy.md          goals, bets, constraints (template)
└── automations/         # Ready-to-wire weekly routines
    ├── sprint-kickoff.md
    ├── weekly-metrics-review.md
    └── daily-standup.md
```

## Quick start

1. **Install it** (see the [repo README](../../README.md) for both install paths).
2. **Fill in your memory** — open `memory/product.md`, `team.md`, and `strategy.md` and replace the templates with your reality (or just start working and let Claude fill them in as it learns).
3. **Ask for something.** You don't name skills — you describe the work:
   - *"Turn this idea into a spec: [paste idea]"* → `write-spec`
   - *"Why did activation drop this week? Here are the numbers: [paste]"* → `metrics-review`
   - *"Build me a battlecard against [competitor]"* → `competitive-brief`
   - *"Plan next sprint — here's the backlog and who's out"* → `sprint-planning`
   - *"Draft a leadership update on where we are"* → `stakeholder-update`
   - *"Help me think through whether we should build X"* → `product-brainstorm`
4. **Wire up automations** (optional) — see `automations/README.md` to run weekly reviews and sprint kickoffs on a schedule.

## How it gets smarter

The first time you work on something, Claude may ask a couple of setup questions. It writes the answers to `memory/`, so the next session it already knows your north-star metric, your team's sprint cadence, and how you like updates formatted. The more you use it, the less it asks.

## Works with your tools (optional)

Zero accounts required — paste your data and go. But if you connect them, it pulls live:

- **Linear / Jira / Asana** → backlog + sprints
- **Amplitude / Mixpanel / GA** → metrics
- **Notion / Confluence / Drive** → existing docs
- **Slack** → post updates
- **Web search** → competitor research

---

📬 More OS kits and tools at **[The Product Channel](https://theproductchannel.substack.com)**.
