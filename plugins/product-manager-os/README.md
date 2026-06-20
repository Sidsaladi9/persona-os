# 🧭 Product Manager OS

A complete operating system for product managers, running on Claude Code. It turns Claude into a senior PM partner — one that drafts your specs, reviews your metrics, preps your stakeholder updates, and remembers your product across sessions.

From **The Product Channel** by Sid Saladi.

---

## What's inside

```
product-manager-os/
├── CLAUDE.md            # The operating brain — how Claude behaves as your PM partner
├── .mcp.json           # Bundled getprompts + getskills MCP libraries (zero-config)
├── skills/              # 40+ book-grounded playbooks Claude uses by intent
│   │  🔍 Discovery        customer-interview · synthesize-research · opportunity-solution-tree
│   │                      · assumption-test · triage-requests · product-brainstorm
│   │  📊 Research/market   personas · journey-map · segmentation · market-sizing
│   │                      · feedback-analysis · market-analysis
│   │  🧭 Strategy          product-strategy · positioning · competitive-brief
│   │                      · business-model · pricing · north-star
│   │  🛠️ Execution         write-spec · prioritize · okrs · roadmap · user-stories
│   │                      · sprint-planning · stakeholder-map · test-scenarios
│   │  📈 Data              metrics-review · experiment-analysis · cohort-analysis · sql-queries
│   │  🚀 Go-to-market      launch-plan · release-notes · icp · growth-loops
│   │  📣 Run the team      stakeholder-update · meeting-notes · retro · pre-mortem · red-team
│   │  🧱 Extend            skill-creator
│   └── …                 (each SKILL.md names the book it's grounded in + a TPC article)
├── commands/            # 5 chained slash-commands (multi-skill workflows)
│   ├── new-feature.md       brainstorm → opportunity tree → assumption-test → prioritize → spec → stories
│   ├── discovery.md         interview plan → synthesize → opportunity tree
│   ├── launch.md            launch-plan → pre-mortem → release-notes → stakeholder-update
│   ├── strategy.md          market-analysis → product-strategy → positioning → red-team
│   └── weekly.md            metrics-review → exec stakeholder-update
├── memory/              # Claude learns your product, team & preferences here
│   ├── MEMORY.md · product.md · team.md · preferences.md · strategy.md  (templates)
└── automations/         # Ready-to-wire routines: sprint-kickoff · weekly-metrics-review · daily-standup
```

> Full skill map (with the book each is grounded in) lives in [CLAUDE.md](CLAUDE.md).

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

## Bundled: getprompts + getskills libraries

This OS ships with two MCP servers wired in, so you also get live access to The Product Channel's curated libraries — **no account or API key needed** (read-only):

- **[getprompts](https://getprompts.org)** — 900+ battle-tested, most-copied PM prompts. Ask *"find me a proven pain-point analysis prompt"* and Claude pulls it.
- **[getskills](https://getskillsai.org)** — 3,000+ installable Claude skills, incl. a **PM starter pack**. Ask *"install the PM pack"* and Claude writes them into your skills folder.

If you installed via the **plugin**, these are automatically active. If you **cloned-and-dropped**, add them once:

```bash
claude mcp add getprompts -- npx -y getprompts-mcp
claude mcp add getskills  -- npx -y getskills-mcp
claude mcp list   # both should show "Connected"  (needs Node 18+)
```

## Works with your tools (optional)

Zero accounts required — paste your data and go. But if you connect them, it pulls live:

- **Linear / Jira / Asana** → backlog + sprints
- **Amplitude / Mixpanel / GA** → metrics
- **Notion / Confluence / Drive** → existing docs
- **Slack** → post updates
- **Web search** → competitor research

---

📬 More OS kits and tools at **[The Product Channel](https://theproductchannel.substack.com)**.
