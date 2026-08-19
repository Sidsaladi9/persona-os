# Quickstart — Product Manager OS

> Looking for per-tool install steps (Cursor, Codex, Gemini, Cowork)? → **[INSTALL.md](INSTALL.md)**

Two ways to install. **If `/plugin` is disabled in your Claude Code (common on enterprise), use Option B.** Both give you the same thing.

---

## Option A — Plugin (if your org allows the marketplace)
```
/plugin marketplace add Sidsaladi9/persona-os
/plugin install product-manager-os
```

## Option B — Files (works everywhere, no marketplace needed)
```bash
git clone https://github.com/Sidsaladi9/persona-os.git
bash persona-os/install.sh /path/to/your/project
```
`install.sh` places everything where Claude Code loads it natively (see below). No git? Use GitHub's **Code → Download ZIP**, unzip, and run the same command.

**It won't clobber your work.** An existing `CLAUDE.md` is left alone (the OS brain lands beside it as `CLAUDE-product-manager-os.md`), and `memory/` and `workspace/` are only seeded where files are missing.

---

## What gets installed (and where)

```
your-project/
├── CLAUDE.md              ← the OS "brain" (auto-loaded every session)
├── .mcp.json              ← getprompts + getskills libraries (Claude asks to approve)
├── .claude/
│   ├── agents/            ← critic + researcher (isolated workers)
│   ├── skills/            ← 53 skills (auto-trigger by intent)
│   └── commands/          ← /setup (+ status|reset) /connect /tune-up
│                             /new-feature /discovery /launch /strategy /weekly
├── memory/                ← product.md, team.md, strategy.md, preferences.md,
│                             house-style.md, onboarding.md  (Claude reads + fills these)
└── workspace/             ← where your artifacts land: projects/ research/
                              strategy/ metrics/ meetings/ comms/ decisions/
```

Claude Code loads `CLAUDE.md`, `.claude/skills/`, `.claude/commands/`, and `.mcp.json` automatically from your project — no plugin system involved.

---

## Turn on the libraries (one time, needs Node 18+)
If `.mcp.json` didn't auto-load (or you merged into an existing one):
```bash
claude mcp add getprompts -- npx -y getprompts-mcp
claude mcp add getskills  -- npx -y getskills-mcp
claude mcp list   # both should say "Connected"
```
If your org blocks MCP servers, skip this — the 53 skills still work fully.

---

## Use it
1. **Set up once (optional but recommended):** run **`/setup`** — a 3-minute guided onboarding that fills your memory so the OS stops asking the basics. Prefer to do it by hand? Fill `memory/product.md`, `team.md`, `strategy.md`, and `memory/house-style.md`, or paste a real doc and say *"use the house-style skill to capture our format."* You can skip setup entirely — the OS learns as you work.
   **Skipped it and want it back?** `/setup` resumes where you left off (it only asks what's still blank), and `/setup status` shows what the OS knows about you and what it's still missing. `/setup reset` starts clean.
2. **Just describe the work** (you don't name skills):
   - "Turn this idea into a spec: …" → `write-spec`
   - "Why did activation drop this week? [numbers]" → `metrics-review`
   - "Prioritize these features against retention" → `prioritize`
   - "Plan next sprint — backlog + who's out" → `sprint-planning`
   - "Draft a leadership update on the launch" → `stakeholder-update`
3. **Run a whole workflow:** `/new-feature [idea]`, `/discovery [question]`, `/launch [thing]`, `/strategy [area]`, `/weekly`.

See [`plugins/product-manager-os/examples/SAMPLE-OUTPUTS.md`](plugins/product-manager-os/examples/SAMPLE-OUTPUTS.md) for what every skill produces.

---

## Picking a skill: the three tiers

Every skill declares how long it takes and what you need in hand, so you can tell whether you can start right now.

| Tier | Feels like | Time | Count |
|---|---|---|---|
| `quick` | paste something in, get the artifact | 5–40 min | 17 |
| `guided` | it asks 3–5 sharp questions, then produces | 30–90 min | 30 |
| `campaign` | a process across multiple sessions, state kept in `memory/` | days–weeks | 6 |

You never have to name a tier — Claude matches it to how much time you have. It matters when you're choosing for yourself.

---

## Where your work goes

Artifacts are written to disk, not left in the chat:

```
workspace/
├── projects/<slug>/   spec, stories, prioritization, launch plan, pre-mortem
├── research/          interviews, synthesis, personas, journeys, competitors
├── strategy/          strategy, vision, positioning, pricing, ICP, roadmap, OKRs
├── metrics/           reviews, cohorts, experiment readouts, saved queries
├── meetings/          notes and retros, by date
├── comms/             stakeholder updates, release notes, incident comms
└── decisions/         one file per call you don't want to relitigate
```

Skills read this before asking you anything. If your product context is confidential, add `workspace/` to `.gitignore` — everything works the same.

---

## Running it on Codex, Cursor, Gemini, or Cowork

One command, no Python, no build step:

```bash
bash install.sh --target cursor ~/code/my-project
```

```bash
bash install.sh --list
```

Targets: `claude-code` · `claude-cowork` · `codex` · `cursor` · `gemini-cli` · `generic`.

The bundles are pre-built and committed under `plugins/product-manager-os/dist/`, so you can also just browse them on GitHub, download the ZIP, and copy the folder you want. Each one has the right entry file (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`), the right skills directory, and its own README.

*Maintainers:* `python3 plugins/product-manager-os/scripts/build_targets.py` regenerates them. CI fails if the committed copies drift.

---

## The two workers

Nine skills hand part of their job to a subagent that runs in its own context:

- **`critic`** — gets your spec, strategy, or plan **alone**, with none of the conversation that produced it, and attacks it cold. Used by `red-team`, `pre-mortem`, `assumption-test`. The isolation is the point: by the time you've written a spec you've been persuaded by it, and so has any reviewer who watched.
- **`researcher`** — reads a slice of a corpus (interviews, tickets, deal records, competitors) and returns attributed, verbatim evidence with counts and distribution. It deliberately does **not** conclude. Used by `synthesize-research`, `feedback-analysis`, `win-loss`, `competitive-brief`, `market-analysis`, `triage-requests`.

They keep no memory and never write to `memory/` or `workspace/` — they're workers, not agents. On hosts without subagents the same briefs ship as `WORKERS.md`, and the skill says plainly that the result is a self-review rather than an independent one.
