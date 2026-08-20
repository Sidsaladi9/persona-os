# Launch Plan — Persona OS (Product Manager OS first)

Internal playbook for shipping Product Manager OS as a free tool for The Product Channel. Not part of the user-facing product.

## 0. Pre-launch checklist

**Done**

- [x] **Repo is public** — `Sidsaladi9/persona-os`, MIT licensed. This launch is an *announcement*, not a publish.
- [x] **Quality is measurable, not asserted** — 53 skills scored by `tests/run_all.py` — **all 53 at 100/100**, floor 100, 51 worked examples checked against their own output templates by `tests/check_all_artifacts.py`. CI fails on **regression**, not just breakage.
- [x] **Resumable onboarding** — `/setup` · `/setup status` · `/setup reset`, with state in `memory/onboarding.md`. Skipping is a first-class path.
- [x] **Artifacts land somewhere** — `workspace/` (projects · research · strategy · metrics · meetings · comms · decisions).
- [x] **Failure + relevance loops** — `memory/incidents.md` (1× threshold) and `tests/relevance_report.py` feed `/tune-up`.
- [x] **Two isolated workers** — `critic` and `researcher` in `agents/`, used by 9 skills.
- [x] **Runs beyond Claude Code** — `scripts/build_targets.py` emits 6 bundles (Claude Code, Cowork, Codex, Cursor, Gemini CLI, generic).
- [x] **`dist/` ships committed**, marked `linguist-generated` so diffs collapse, with a CI gate that fails if it drifts from a fresh build. A Cursor user needs no toolchain.
- [x] **Repo About, website, and topics set** — description reflects 53 scored skills across 6 hosts; website fixed from a 404 (`theproductchannel.substack.com`) to `sidsaladi.substack.com`; 8 topics.
- [x] **All 26 Go-deeper newsletter links verified live** — 0 broken.
- [x] **Bundled MCPs are published and installable** — `getprompts-mcp` v0.1.0 and `getskills-mcp` v0.2.3 both resolve on npm. (Still worth confirming `claude mcp list` shows Connected after a real install.)

**Still to do before announcing**

- [ ] **Run the live test** — step-by-step protocol with pass conditions: [`demo/LIVE-TEST.md`](demo/LIVE-TEST.md). 20 minutes, 7 checks. Test 6 (`/tune-up` proposes a skill from a 3× pattern) is the gate — **the self-improving loop is the headline claim and nothing in CI can prove it works.** Note: this cannot be automated from a headless session; `claude -p` has no credentials and computer-use blocks typing into terminals.
- [ ] **Test both install paths on a clean machine.** The `get.sh` path is verified live from GitHub; the `/plugin install` path has zero automated coverage and is step 1 of the live test.
- [ ] **Confirm bundled MCPs connect** — step 7 of the live test. Both packages verified published on npm (`getprompts-mcp` v0.1.0, `getskills-mcp` v0.2.3).
- [ ] **Record a 60-second demo.** Shot list and the exact lines to type: [`demo/SCRIPT.md`](demo/SCRIPT.md). Build the recordable environment first — `bash demo/setup-demo-env.sh ~/demo-cadence` — it seeds an activity log so `/tune-up` actually has a pattern to find on camera. Without that, the closing shot doesn't happen.
- [ ] **Publish the launch article** — `output/articles/product-manager-os-101-2026-08-18.md` in TPC-OS, framed as a 101 guide, **not** "Introducing X" (that framing converted 1 free sub on GetSkills).

## 1. Why this wins (positioning vs. the field)

The space has skill packs (Paweł Huryn's `pm-skills`, Carl Vellotti's `carls-product-os`, deanpeters, aakashg) — and, now, Anthropic's own free `product-management` plugin that overlaps a generic skill pack nearly 1:1. **Competing on skill count is a losing game against the platform vendor.** Don't. Our angle:

> **The only PM toolkit that gets better the more you use it.** Not a skill pack — an OS: an operating brain, a memory that learns your product, and a self-improving loop that watches the work you repeat and builds you custom skills for it, all on your machine. Plus 53 book-grounded skills — every one scored in CI, so "battle-tested" is a number you can check out and run — and live connectors that write your work back to Linear/Notion/Slack. Install in 60 seconds.

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
- What it is: a free, installable "OS" — an operating brain (CLAUDE.md), a memory that learns your product/team (3-min `/setup`), 53 scored, book-grounded skills across discovery → strategy → execution → launch, connectors that write your work back to Linear/Notion/Slack, and weekly automations.
- The differentiator: it **watches the work you repeat and builds you a custom skill for it** — drafted from how *you* did it, on your machine, only when you say yes. The more you use it, the more it's yours. Nothing static can do that. (Drop the `/tune-up` proposing-a-skill screenshot.)
- Proof: show one real before/after (rough idea → full PRD), and the loop minting a `launch-comms` skill from three hand-written emails.
- CTA: two install lines + the repo link. "Reply and tell me which role OS you want next."
- PS: Team OS, Founder OS, and Marketer OS are coming — this is just the first.

## 4. Social cuts (X / LinkedIn)

- The demo GIF + "I built a Product Manager OS for Claude that **gets better the more you use it** — it watches the work you repeat and builds you custom skills for it. Operating brain, a memory that learns your product, 53 scored, book-grounded skills. Free. 🧵"
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

---

# Distribution plan — how this gets stars

## The honest starting position

| Repo | Stars | Created |
|---|---|---|
| `phuryn/pm-skills` | **25,430** | 2026-03-01 |
| `deanpeters/Product-Manager-Skills` | 6,545 | 2026-02-05 |
| `carlvellotti/carls-product-os` | 222 | 2026-02-05 |
| **`Sidsaladi9/persona-os`** | **0** | 2026-06-18 |

Two months public, zero stars. Not because the product is worse — because **nothing has ever pointed at it.** That's the entire diagnosis.

**You will not out-volume Pawel.** He has 25k stars, 100+ skills, and a five-month head start. Any plan whose thesis is "more skills" is already lost.

**But he did you a favour.** He proved the category and pre-qualified 25,000 people who star PM skill repos. That's your exact audience, already identified, already interested. The play is to be *the other one worth having* — not to pretend he doesn't exist.

## The one claim to lead with

Every competitor is a skill pack. **Only this one learns your product and writes you new skills from the work you repeat.** Pawel bolted a separate memory tool on beside his; ours is inside.

> *The PM toolkit that gets better the more you use it.*

Do not lead with 53 skills. Skill count is the axis where you lose, and it's a number a competitor can beat in a weekend. Memory + the self-improving loop is the thing nobody can screenshot back at you.

## What your own data says will travel

Your biggest post ever is **"50+ Product Management Prompts for ChatGPT" — 16,923 views, 235 subs, 29% of traffic from LinkedIn, 6% from Reddit.**

Every post of yours that travelled off-platform is a **numbered giveaway**: 50+ prompts · 20+ plugins · 20 AI tools · 100+ resources. That's the proven shape, and *53 free PM skills* fits it exactly.

Your traffic mix across the catalogue:

| Channel | Share | Read |
|---|---|---|
| Email | **39.5%** | Biggest lever. But it converts *subscribers*, not stars — needs an explicit ask |
| Google | 14.9% | Compounds later, irrelevant on launch day |
| Direct | 13.0% | |
| **LinkedIn** | **12.0%** | Hits 29–30% on numbered-list posts. Proven and currently underused |
| Substack app / Notes | 6.2% | Pawel's actual mechanism |
| Reddit | 2.7% | But 6–9% on list posts. **Most under-exploited channel you have** |

## The mechanic everyone forgets

**A GitHub star is a bookmark.** People star what they intend to come back to. Most of your readers will not star anything unless you ask, in one line, and give them a reason:

> *If you'll want this later, star it — that's how you find it again, and it's the only thing that helps other PMs find it.*

Put that line in the article, the LinkedIn post, and the repo README. Pawel posted **star milestones as content** ("1,300 in 72 hours", "star history 😀"). Momentum is itself the story once it starts.

## Launch sequence

Don't fire everything at once. Stars compound visibly, and each wave becomes evidence for the next.

**Day 0 — Tuesday or Wednesday morning**
1. Publish the 101 article. Email it — this one clears the send bar.
2. LinkedIn post (not a link-dump): the *problem*, the loop, one screenshot of `/tune-up` proposing a skill, link last.
3. Substack Note with the demo GIF. Short, "steal this" framing.
4. X thread — same beats, 6–8 posts, GIF on post 1.

**Day 0 evening — Reddit.** Your least-used, best-fit channel. `r/ProductManagement`, `r/ClaudeAI`, `r/ChatGPTCoding`. Read each sub's self-promo rules first. Lead with the free thing and the honest limits; never with the newsletter.

**Day 1–2 — ask for amplification.** Pawel's launch was boosted when Jeff Gothelf shared it. Pick 5–10 PM voices who've engaged with you, send a *personal* note with the repo and one line on why it's different. Not a broadcast.

**Day 2–3 — Show HN.** Free lottery ticket. Title it plainly: *"Show HN: An open-source PM operating system for Claude Code that writes its own skills."* Be present in the comments all day or don't post.

**Day 3–7 — milestone content.** First 100 stars, first outside contribution, first "it built me a skill" reply. Each is a Note and a LinkedIn post.

**Ongoing — the owned surfaces.** getprompts.org and getskillsai.org both have traffic and neither points at this yet. Add it. Also cross-link from the 26 newsletter articles the skills already reference — those posts get Google traffic forever.

## What not to do

- **Don't lead with skill count.** You lose that comparison and it invites it.
- **Don't post the same text to five channels.** Native format per channel or the reach collapses.
- **Don't launch without the demo.** The loop is unbelievable in prose and obvious in 15 seconds of video.
- **Don't hide the limits.** "It's not multiplayer, memory is local, needs two weeks of use before the loop has signal" buys more credibility than it costs.
- **Don't buy or trade stars.** It's detectable, and it poisons the only signal you're trying to build.

## What's realistic

Your median post is ~3,000 views. If the launch lands at 2–3× that and 3–5% of readers star it, that's **150–400 stars in week one.** Pawel's 1,300-in-72-hours came off a much larger audience and an established X presence.

The number that actually matters in month one isn't stars — it's **installs that survive to a second session**, and whether anyone replies saying `/tune-up` built them something. One of those replies is worth more than 500 stars, because it's the only proof the differentiator is real.

