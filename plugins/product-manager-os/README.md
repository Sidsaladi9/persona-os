# 🧭 Product Manager OS

A complete operating system for product managers. It turns your AI assistant into a senior PM partner — one that drafts your specs, reads your metrics, preps your stakeholder updates, and **remembers your product across sessions**.

The part nothing else has: **it gets better the more you use it.** It watches the work you repeat and offers to build you a custom skill for it, drafted from how *you* did it.

**53 skills, every one scoring 100/100 · [see the scoreboard](tests/RESULTS.md)** — every skill is graded in CI, and CI fails when a score goes *down*.

From **The Product Channel** by Sid Saladi. MIT.

---

## Install

**Claude Code** — one command:

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

**Cursor · Codex · Gemini · anything else** — one command:

```bash
curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash
```

Run it in the folder you want the OS to live in — that folder becomes your product brain. Full per-tool steps and troubleshooting → **[INSTALL.md](../../INSTALL.md)**.

---

## The 53 skills

You never name them. You describe the work and the right one fires. Each declares a **tier** so you know what it costs you before you start:

⚡ `quick` — paste in, get the artifact (5–40 min) · 🧭 `guided` — asks 3–5 questions first (30–90 min) · 🗓 `campaign` — runs across sessions (days–weeks)

| Area | Skills |
|---|---|
| 🔍 **Discovery** | 🗓 `customer-interview` · 🧭 `synthesize-research` · 🗓 `opportunity-solution-tree` · 🧭 `assumption-test` · ⚡ `triage-requests` · 🧭 `product-brainstorm` |
| 📊 **Research & market** | 🧭 `personas` · 🧭 `journey-map` · 🧭 `segmentation` · ⚡ `market-sizing` · 🧭 `feedback-analysis` · 🧭 `market-analysis` · 🧭 `win-loss` |
| 🧭 **Strategy & positioning** | 🧭 `product-vision` · 🧭 `product-strategy` · 🧭 `positioning` · 🧭 `value-proposition` · 🧭 `competitive-brief` · 🧭 `business-model` · 🧭 `pricing` · 🧭 `business-case` · ⚡ `north-star` |
| 🛠️ **Planning & execution** | 🧭 `write-spec` · ⚡ `prioritize` · 🗓 `okrs` · 🗓 `roadmap` · ⚡ `user-stories` · 🧭 `sprint-planning` · ⚡ `stakeholder-map` · ⚡ `test-scenarios` · ⚡ `spec-vs-shipped` |
| 📈 **Data & analytics** | 🧭 `metrics-review` · 🗓 `experiment-analysis` · ⚡ `cohort-analysis` · ⚡ `sql-queries` · 🧭 `tracking-plan` |
| 🚀 **Go-to-market & growth** | 🧭 `gtm-strategy` · 🗓 `launch-plan` · 🧭 `press-release` · ⚡ `battlecard` · ⚡ `release-notes` · 🧭 `icp` · 🧭 `growth-loops` · 🧭 `activation-flow-design` |
| 📣 **Run the team** | ⚡ `stakeholder-update` · ⚡ `meeting-notes` · 🧭 `retro` · 🧭 `pre-mortem` · 🧭 `red-team` · ⚡ `incident-comms` |
| 🎨 **Make it shareable** | ⚡ `visualize` — renders any artifact as a self-contained HTML page, built to screenshot |
| 🧱 **Extend** | 🧭 `skill-creator` · ⚡ `house-style` |

**Every skill names the book it's grounded in.** Not decoration — an instruction it follows. `customer-interview` won't write "Would you use this?" because the Mom Test discipline is in the skill. `experiment-analysis` won't read significance without a pre-registered metric because Kohavi is. See all 53 with their sources in [CLAUDE.md](CLAUDE.md), and the output of every one in [examples/SAMPLE-OUTPUTS.md](examples/SAMPLE-OUTPUTS.md).

---

## What's in the box

```
product-manager-os/
├── CLAUDE.md          the operating brain — how it thinks, when to push back, what to remember
├── skills/            53 book-grounded playbooks, reached for by intent
├── agents/            critic + researcher — two isolated workers (see below)
├── commands/          /setup /connect /tune-up + 5 chained workflows
├── memory/            what it learns about you — product, team, strategy, style
├── workspace/         where your artifacts land — projects, research, strategy,
│                      metrics, meetings, comms, decisions
├── automations/       sprint kickoff · weekly metrics · daily standup · weekly tune-up
├── examples/          every skill run against one demo company, so you can see it first
├── tests/             the loss function — every skill scored, gated against regression
└── .mcp.json          getprompts + getskills, wired in zero-config
```

---

## Five things that make it an OS, not a prompt pack

**1. It remembers your product.** `memory/` holds what you're building, your team, your north star, and how you like things written. Run `/setup` — nine questions, ~3 minutes, all skippable. Fastest path is *"bootstrap from a doc"*: paste a real PRD and it infers your product **and** your house format in one pass.

Skipped it? Nothing is lost. `/setup` resumes and only asks what's still blank; `/setup status` shows what it knows and what it's missing.

**2. Your work lands somewhere.** Every artifact is written to a predictable path under `workspace/` instead of scrolling away in a chat window. Skills **read it before asking you anything**, so you stop re-pasting context you already gave. `workspace/decisions/` is the record of *why*, six months later.

**3. It improves itself from three signals.** `/tune-up` (or the weekly automation) proposes new and tuned skills — you accept, tweak, or reject; nothing is automatic.

| Signal | Fires at | Because |
|---|---|---|
| Repeated **corrections** | 3× | three edits of the same kind is a preference worth encoding |
| An **incident** — output you couldn't use | **1×** | that's a defect, and waiting for it to recur is waiting to get burned again |
| **Dead artifacts** — never opened again | ≥3, ⅔ dead | the skill is producing the wrong thing, or at the wrong moment |

New skills are drafted from **your last ~3 real examples**, marked `status: draft`, and graduate after 3 clean uses.

**4. Two workers, where isolation actually matters.**

- **`critic`** receives your spec, strategy, or plan **alone** — none of the conversation that produced it. By the time you've helped write a document you've been persuaded by it, and so has any review run in that context. Used by `red-team`, `pre-mortem`, `assumption-test`.
- **`researcher`** reads a corpus cold and returns attributed, verbatim evidence with counts and distribution — and deliberately does *not* conclude. It's what stops the first theme you noticed from becoming the only one you find. Used by `synthesize-research`, `feedback-analysis`, `win-loss`, `competitive-brief`, `market-analysis`, `triage-requests`.

They keep no memory — the learning belongs to the calling skill. Nine of 53 skills delegate; the rest don't, because most work doesn't need it.

**5. It's scored, not vibe-checked.** [`tests/score_skill.py`](tests/score_skill.py) grades each skill out of 100 across six dimensions. [`tests/check_all_artifacts.py`](tests/check_all_artifacts.py) then checks a real produced artifact against the output template that skill promised. Both run in CI, and **CI fails when a score regresses**, not just when a file breaks.

That found two genuine defects on its first run — `product-brainstorm` at 68 and `skill-creator` at 81. Both fixed, both now 100.

---

## Commands

You rarely need these — describing the work is enough. They exist for the multi-step jobs where the order matters.

| Command | What it does |
|---|---|
| `/setup` | 3-minute onboarding that fills `memory/` so it stops asking you the basics. **`/setup status`** shows what it knows and what's missing. **`/setup reset`** wipes back to templates. Re-run any time — it resumes and only asks what's still blank. |
| `/tune-up` | Reads your activity log, incidents, and relevance report, then proposes new or tuned skills. You accept, tweak, or reject. |
| `/connect` | Wires up your tracker, analytics, docs, and chat so the OS pulls live data and writes work back. |
| `/new-feature [idea]` | Raw idea → build-ready backlog. Chains brainstorm → opportunity tree → assumption-test → prioritize → spec → user-stories. |
| `/discovery [question]` | A discovery cycle: interview plan → synthesize → opportunity map. |
| `/strategy [area]` | Build or pressure-test strategy: market-analysis → product-strategy → positioning → red-team. |
| `/launch [thing]` | Launch end-to-end: launch-plan → pre-mortem → release-notes → stakeholder-update. |
| `/weekly` | Your weekly review: metrics scorecard → leadership update. |

*On hosts without slash commands (Codex, Cursor, Gemini), these ship as `COMMANDS.md` and you invoke them by name — "run the weekly workflow".*

---

## Automations

Four routines in `automations/`, ready to put on a schedule with `/schedule` or cron. They're plain markdown prompts, so edit them freely.

| Routine | When | What it does |
|---|---|---|
| `daily-standup` | each morning | Drafts your standup from what actually moved |
| `sprint-kickoff` | start of sprint | Runs `sprint-planning` against the backlog and who's out |
| `weekly-metrics-review` | Friday | Metrics scorecard plus a stakeholder update draft |
| `weekly-os-tuneup` | weekly | The self-improvement pass — proposes skills from your repeated work |

---

## Memory — what it learns about you

Nine files in `memory/`. Claude reads them at session start and writes to them as it learns. All local; nothing syncs anywhere.

`MEMORY.md` is the index Claude reads first — one line pointing at each file below. The rest:

**What's true about you**

| File | Holds |
|---|---|
| `product.md` | What you're building, for whom, business model, goals |
| `team.md` | Who's on the team, who owns what, rituals and tools |
| `strategy.md` | Current bets, themes, constraints, deadlines |
| `preferences.md` | How you like to work — tone, formats, how hard to push |
| `house-style.md` | Your company's format: voice, terminology, doc templates. **Every skill conforms to this**, which is what makes output look like it came from inside your company |

**What it's noticed** — the self-improvement layer

| File | Holds |
|---|---|
| `onboarding.md` | How much it knows about you, what's missing, whether setup was offered or skipped |
| `activity-log.md` | One line per real task. How it spots work you repeat |
| `incidents.md` | Output you couldn't use, and why. Acted on at 1×, not 3× |
| `os-suggestions.md` | Pending "want me to build you a skill?" proposals |

---

## Workspace — where the work lands

Artifacts get written to a predictable path instead of scrolling away in chat. Skills **read this before asking you anything**, so you stop re-pasting context.

| Folder | Holds |
|---|---|
| `projects/<slug>/` | Everything about one piece of work — spec, stories, prioritization, launch plan, pre-mortem |
| `research/` | Interviews, synthesis, personas, journeys, market and competitor work |
| `strategy/` | The slow-changing calls — strategy, vision, positioning, pricing, ICP, roadmap, OKRs |
| `metrics/` | Reviews, cohorts, experiment readouts, saved queries |
| `meetings/` | Notes and retros, by date |
| `comms/` | Stakeholder updates, release notes, incident comms |
| `decisions/` | One file per call you don't want to relitigate. Six months later, this is the only record of *why* |

Confidential product context? Add `workspace/` to `.gitignore`. Everything works the same.

---

## Tools you can run

Plain Python 3, no dependencies. The OS points you at these; you don't have to go looking.

| Command | When you'd run it |
|---|---|
| `python3 tests/relevance_report.py` | Which artifacts you never opened again — a skill producing the wrong thing, or at the wrong moment. `/tune-up` runs it for you |
| `python3 tests/score_skill.py skills/<name>/SKILL.md` | After writing your own skill with `skill-creator`. Ship at 100 |
| `python3 tests/run_all.py` | Score every skill you have, including yours |
| `python3 tests/check_artifact.py --skill <name> <file>` | Does a produced artifact match what the skill promised? |
| `python3 tests/index_workspace.py` | Regenerate `workspace/INDEX.md` |

*The repo also runs `audit.py`, `check_all_artifacts.py` and `build_sample_outputs.py` in CI — those are for maintaining the OS, not using it.*

---

## Using it

You describe the work:

- *"Turn this into a spec: sales keeps asking for bulk CSV export, but I think the real problem is they can't get data out at all. Here's the thread: [paste]"* → `write-spec`
- *"Activation dropped 34% → 27% week over week. Here's the funnel: [paste]. What happened?"* → `metrics-review`
- *"Why are we losing deals to [competitor]?"* → `win-loss`
- *"Plan next sprint — here's the backlog and who's out"* → `sprint-planning`
- *"Should we build X?"* → `product-brainstorm`

Or run a whole workflow: `/new-feature [idea]` · `/discovery [question]` · `/launch [thing]` · `/strategy [area]` · `/weekly`.

---

## Bundled libraries

Two MCP servers ship wired in — no account, no API key, read-only:

- **[getprompts](https://getprompts.org)** — 900+ battle-tested PM prompts. *"Find me a proven pain-point analysis prompt."*
- **[getskills](https://getskillsai.org)** — 3,000+ installable skills including a PM starter pack.

Active automatically on a plugin install. Otherwise:

```bash
claude mcp add getprompts -- npx -y getprompts-mcp
```
```bash
claude mcp add getskills -- npx -y getskills-mcp
```

Needs Node 18+. If your org blocks MCP servers, skip it — all 53 skills work without them.

---

## Works with your tools (optional)

Zero accounts required — paste your data and go. Connect them and it pulls live, then **writes the finished work back**: stories → your tracker, spec → your docs, update → your channel. It always drafts and asks before posting.

**Linear · Jira · Asana** → backlog and sprints · **Amplitude · Mixpanel · GA** → metrics · **Notion · Confluence · Drive** → existing docs · **Slack · Teams** → updates · **web search** → competitor research

Run `/connect` to wire them up.

---

📬 More OS kits and tools at **[The Product Channel](https://sidsaladi.substack.com)**.
