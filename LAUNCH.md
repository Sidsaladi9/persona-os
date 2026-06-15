# Launch Plan — Persona OS (Product Manager OS first)

Internal playbook for shipping Product Manager OS as a free tool for The Product Channel. Not part of the user-facing product.

## 0. Pre-launch checklist

- [ ] **Battle-test green** — all 18 skills verified by the agent battle-test (see task #4). No skill below the quality bar.
- [ ] **Create the public repo** and push:
  ```bash
  cd ~/Claude_Code/Projects\ /persona-os
  gh repo create Sidsaladi9/persona-os --public --source=. --push
  ```
- [ ] **Confirm the repo name in all docs** — README, marketplace.json, plugin.json reference `Sidsaladi9/persona-os`. If the repo lands under a different owner/name, find-and-replace before pushing.
- [ ] **Test both install paths on a clean machine** (see §2). This is the "100% it works" gate.
- [ ] **Set the repo's About + topics** on GitHub: `claude-code`, `product-management`, `claude-skills`, `ai-pm`. Add the Substack URL as the website.
- [ ] **Add a LICENSE** (recommend MIT or CC BY 4.0 so people can fork freely — currently none committed).
- [ ] **Record a 60-second demo** (asciinema or screen capture): install → ask "write a PRD for X" → watch a skill fire. This is the single highest-converting asset.

## 1. Why this wins (positioning vs. the field)

The space already has Paweł Huryn's `pm-skills` (68 skills), Carl Vellotti's `carls-product-os`, deanpeters, and aakashg. We do **not** compete on skill count. Our angle:

> **The PM OS that's actually verified to work.** Curated, not bloated. 18 skills covering the real PM week, each grounded in a named framework, each battle-tested by AI agents before shipping — plus an operating brain and a memory that learns your product. Install in 60 seconds.

Lead the launch with **"battle-tested"** and **"learns your product"** — those are the two things the others don't say.

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
1. I built you a Product Manager OS (free, installs in 60 seconds)
2. 18 PM skills, one operating system, $0
3. Steal my Product Manager OS

**Body skeleton:**
- Hook: every PM is drowning in the same recurring work — specs, prioritization, OKRs, stakeholder updates, interview synthesis. What if Claude already knew how to do all of it your way?
- What it is: a free, installable "OS" — 18 skills across discovery → strategy → execution → launch, an operating brain (CLAUDE.md), a memory that learns your product/team, and weekly automations.
- The differentiator: I didn't just write them — I had AI agents **battle-test every single skill** on a realistic product and verified the output was shippable. (Drop the scorecard screenshot.)
- Proof: show one real before/after (rough idea → full PRD).
- CTA: two install lines + the repo link. "Reply and tell me which skill you want for the next OS."
- PS: Team OS, Founder OS, and Marketer OS are coming — this is just the first.

## 4. Social cuts (X / LinkedIn)

- The demo GIF + "I built a Product Manager OS for Claude. 18 skills, an operating brain, and a memory that learns your product. Every skill battle-tested by AI agents. Free. 🧵"
- Carousel: one slide per lifecycle category (Discovery / Strategy / Execution / Launch) listing the skills.
- A "watch Claude turn a one-line idea into a full PRD" screen recording.

## 5. Distribution to the destination DBs (TPC convention)

If any skill or prompt from this OS is featured in a newsletter article, run it through `scripts/upload_newsletter_assets.py` so prompts → getprompts.org and skills → getskillsai.org with permalinks, per the TPC publishing rules. The OS itself lives on GitHub; the *article about it* follows the normal asset-permalink workflow.

## 6. Post-launch loop

- Watch GitHub stars + which install path dominates (issues/discussions will tell you).
- Open a GitHub Discussions board for skill requests — that's your roadmap for OS #2.
- Track replies asking for other personas → pick the most-requested as Team OS vs Founder OS vs Marketer OS.
- Feed any "this skill didn't work for X" reports back into the battle-test harness and reship.

## 7. Next personas (same repo, same structure)

Each new persona is one folder under `plugins/`. Candidates in likely demand order: **Team OS** (eng/product leads), **Founder OS**, **Marketer OS**, **Engineering Lead OS**. Reuse this exact build → battle-test → launch pipeline.
