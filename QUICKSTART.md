# Quickstart — Product Manager OS

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
cd /path/to/your/project        # the project you'll open in Claude Code
bash /path/to/persona-os/install.sh
```
`install.sh` places everything where Claude Code loads it natively (see below). No ZIP? Use GitHub's **Code → Download ZIP**.

---

## What gets installed (and where)

```
your-project/
├── CLAUDE.md              ← the OS "brain" (auto-loaded every session)
├── .mcp.json              ← getprompts + getskills libraries (Claude asks to approve)
├── .claude/
│   ├── skills/            ← 41 skills (auto-trigger by intent)
│   └── commands/          ← /setup /new-feature /discovery /launch /strategy /weekly
└── memory/                ← product.md, team.md, strategy.md, preferences.md,
                              house-style.md  (you fill these in; Claude reads them)
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
If your org blocks MCP servers, skip this — the 41 skills still work fully.

---

## Use it
1. **Set up once (optional but recommended):** run **`/setup`** — a 3-minute guided onboarding that fills your memory so the OS stops asking the basics. Prefer to do it by hand? Fill `memory/product.md`, `team.md`, `strategy.md`, and `memory/house-style.md`, or paste a real doc and say *"use the house-style skill to capture our format."* You can skip setup entirely — the OS learns as you work.
2. **Just describe the work** (you don't name skills):
   - "Turn this idea into a spec: …" → `write-spec`
   - "Why did activation drop this week? [numbers]" → `metrics-review`
   - "Prioritize these features against retention" → `prioritize`
   - "Plan next sprint — backlog + who's out" → `sprint-planning`
   - "Draft a leadership update on the launch" → `stakeholder-update`
3. **Run a whole workflow:** `/new-feature [idea]`, `/discovery [question]`, `/launch [thing]`, `/strategy [area]`, `/weekly`.

See [`plugins/product-manager-os/examples/SAMPLE-OUTPUTS.md`](plugins/product-manager-os/examples/SAMPLE-OUTPUTS.md) for what every skill produces.
