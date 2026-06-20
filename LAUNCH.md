# Launch Plan — Persona OS (Product Manager OS first)

Internal playbook for shipping Product Manager OS as a free tool for The Product Channel. Not part of the user-facing product.

## 0. Pre-launch checklist

- [ ] **Battle-test green** — all 40+ skills verified by the agent battle-test. No skill below the quality bar.
- [ ] **Run the live test** — install into a clean project, run `/setup`, do a few tasks, confirm capture fires in `memory/activity-log.md`, then `/tune-up` proposes a skill. The self-improving loop is the headline claim — it has to visibly work.
- [ ] **Create the public repo** and push:
  ```bash
  cd ~/Claude_Code/Projects\ /persona-os
  gh repo create Sidsaladi9/persona-os --public --source=. --push
  ```
- [ ] **Confirm the repo name in all docs** — README, marketplace.json, plugin.json reference `Sidsaladi9/persona-os`. If the repo lands under a different owner/name, find-and-replace before pushing.
- [ ] **Test both install paths on a clean machine** (see §2). This is the "100% it works" gate.
- [ ] **Confirm bundled MCPs connect** — after install, run `claude mcp list` and verify `getprompts` and `getskills` both show **Connected** (needs Node 18+). They're zero-config public npm packages (`getprompts-mcp`, `getskills-mcp`); no keys to set.
- [ ] **Set the repo's About + topics** on GitHub: `claude-code`, `product-management`, `claude-skills`, `ai-pm`. Add the Substack URL as the website.
- [ ] **Add a LICENSE** (recommend MIT or CC BY 4.0 so people can fork freely — currently none committed).
- [ ] **Record a 60-second demo** (asciinema or screen capture): install → ask "write a PRD for X" → watch a skill fire. This is the single highest-converting asset.

## 1. Why this wins (positioning vs. the field)

The space has skill packs (Paweł Huryn's `pm-skills`, Carl Vellotti's `carls-product-os`, deanpeters, aakashg) — and, now, Anthropic's own free `product-management` plugin that overlaps a generic skill pack nearly 1:1. **Competing on skill count is a losing game against the platform vendor.** Don't. Our angle:

> **The only PM toolkit that gets better the more you use it.** Not a skill pack — an OS: an operating brain, a memory that learns your product, and a self-improving loop that watches the work you repeat and builds you custom skills for it, all on your machine. Plus 40+ book-grounded skills and live connectors that write your work back to Linear/Notion/Slack. Install in 60 seconds.

Lead the launch with **"gets better the more you use it"** and **"learns your product"** — the static packs (and the free base plugin) structurally can't say either. Skill count is a footnote, not the headline.

## 2. Install paths (what subscribers do)

**A — One command (Claude Code / Cowork):**
```
/plugin marketplace add Sidsaladi9/persona-os
/plugin install product-manager-os
```
**B — Clone-and-drop (no plugin system):**
```bash
git clone https://github.com/Sidsaladi9/persona-os.git
cp -r persona-os/plugins/product-manager-os/* /path/to/your/project/
```
**C — ZIP (non-technical):** GitHub → Code → Download ZIP → copy the `product-manager-os` folder into your project.

All three are documented in the repo README. Verify each before announcing.

## 3. Newsletter announcement (draft)

**Subject line options:**
1. I built you a Product Manager OS that gets smarter the more you use it (free)
2. The PM toolkit that builds its own skills from your work
3. Steal my Product Manager OS

**Body skeleton:**
- Hook: every PM is drowning in the same recurring work — specs, prioritization, OKRs, stakeholder updates, interview synthesis. What if Claude already knew how to do all of it *your* way — and got better every week?
- What it is: a free, installable "OS" — an operating brain (CLAUDE.md), a memory that learns your product/team (3-min `/setup`), 40+ book-grounded skills across discovery → strategy → execution → launch, connectors that write your work back to Linear/Notion/Slack, and weekly automations.
- The differentiator: it **watches the work you repeat and builds you a custom skill for it** — drafted from how *you* did it, on your machine, only when you say yes. The more you use it, the more it's yours. Nothing static can do that. (Drop the `/tune-up` proposing-a-skill screenshot.)
- Proof: show one real before/after (rough idea → full PRD), and the loop minting a `launch-comms` skill from three hand-written emails.
- CTA: two install lines + the repo link. "Reply and tell me which role OS you want next."
- PS: Team OS, Founder OS, and Marketer OS are coming — this is just the first.

## 4. Social cuts (X / LinkedIn)

- The demo GIF + "I built a Product Manager OS for Claude that **gets better the more you use it** — it watches the work you repeat and builds you custom skills for it. Operating brain, a memory that learns your product, 40+ book-grounded skills. Free. 🧵"
- Carousel: the stack — brain · memory · self-improving loop · skills · connectors — one slide each.
- A screen recording of the loop: do a task 3×, run `/tune-up`, watch it propose and write a new skill.

## 5. Distribution to the destination DBs (TPC convention)

If any skill or prompt from this OS is featured in a newsletter article, run it through `scripts/upload_newsletter_assets.py` so prompts → getprompts.org and skills → getskillsai.org with permalinks, per the TPC publishing rules. The OS itself lives on GitHub; the *article about it* follows the normal asset-permalink workflow.

## 6. Post-launch loop

- Watch GitHub stars + which install path dominates (issues/discussions will tell you).
- Open a GitHub Discussions board for skill requests — that's your roadmap for OS #2.
- Track replies asking for other personas → pick the most-requested as Team OS vs Founder OS vs Marketer OS.
- Feed any "this skill didn't work for X" reports back into the battle-test harness and reship.

## 7. Next personas (same repo, same structure)

Each new persona is one folder under `plugins/`. Candidates in likely demand order: **Team OS** (eng/product leads), **Founder OS**, **Marketer OS**, **Engineering Lead OS**. Reuse this exact build → battle-test → launch pipeline.
