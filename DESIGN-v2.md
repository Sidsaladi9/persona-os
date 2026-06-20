# Persona OS v2 — Design Notes

Working doc for the next phase of Product Manager OS. Three threads, one goal: turn a strong-but-static skill pack into an OS that **activates on day one** and **gets better the more you use it**.

Status: proposal. Argue with it, then we build in phases.

---

## The problem we're solving

v1 ships everything an OS needs — 41 skills, an operating brain, a memory system, automations. But two gaps keep it from feeling like a living product:

1. **Memory ships empty.** The `memory/` files are the moat (they're what make the OS know *your* product instead of a generic one), but they ship as blank templates almost nobody fills in. So the best feature is effectively off on day one.
2. **It doesn't learn.** Today the OS is exactly as smart on day 90 as on day 1. A static pack can be copied; an OS that learns you can't.

Three pieces close those gaps: **Onboarding** (activation), the **Self-Improving Loop** (compounding value), and **Visual Outputs** (polish + shareability).

---

## Pillar 1 — Onboarding (`/setup`)

**Goal:** in under 5 minutes, go from empty memory to an OS that knows your product, team, cadence, and format — using Claude Code's *native* option-picker UI, not a wall of text.

### Behavior
- **First-run trigger.** If `memory/` is still all templates, the brain offers setup on the first real request: *"Want to spend 3 minutes setting me up so I stop asking the same questions? (`/setup`)"* — offered, never forced.
- **Skippable, always.** Every prompt carries *"Skip for now — I'll learn as we go."* You can skip the whole onboarding or any single question. Nothing blocks you from working; skipped fields fill in later via passive capture or a `/setup` re-run.
- **Gap-aware + resumable.** On return, `/setup` only asks what's still missing. It never re-onboards a configured user.
- **Three ways to answer, user picks:**
  - **Guided** — the enriched questions below, via the `AskUserQuestion` picker.
  - **Bootstrap from a doc** — *"paste your latest PRD / strategy doc / point me at a Notion page"* → infer `product.md` + `house-style.md` automatically. Lower friction; reuses the existing `house-style` skill.
  - **Let me infer, you confirm** — for anything skipped, the OS takes its best guess from what it's seen and shows it for a one-tap confirm, so you edit instead of write from scratch.

### Multiple products / teams
Ask one branching question up front: **"Do you run one product, or several?"**
- **One** → single `product.md` / `team.md` (default — keeps it simple).
- **Several** → the OS creates one file per product (`product-<name>.md`, `team-<name>.md`) and asks which one a given request is about, remembering the last-used so it's not asked every time. Same for multiple teams. `strategy.md` stays shared unless you split it. This keeps a portfolio PM or an agency from cramming everything into one file.

### The questions — with guidance + an example each
Each question carries a one-line *why we ask* (so the user gives a useful answer, not a vague one) and an example to anchor it.

| # | Question — *why we ask* | Type | Example | Writes to |
|---|---|---|---|---|
| 1 | **What are you building?** *Anchors every artifact to your real product, not a generic SaaS.* | text | *"A tool that auto-fills last-minute clinic cancellations."* | `product.md` |
| 2 | **Who's it for? (ICP)** *So personas, positioning & prioritization weight the right user.* | text | *"Office managers at 5–20-person dental practices."* | `product.md` |
| 3 | **Stage?** *Changes what I push — 0→1 favors speed & discovery; mature favors rigor & scale.* | pick: 0→1 / scaling / mature | *scaling* | `product.md` |
| 4 | **Business model?** *Drives pricing, metrics & growth-loop choices.* | pick: SaaS / marketplace / consumer / other | *"SaaS, $99/mo per location"* | `product.md` |
| 5 | **Your role + team size?** *Calibrates altitude (IC PM vs Head of Product) and who outputs are written for.* | text | *"Sole PM; 6 eng, 1 designer."* | `team.md` |
| 6 | **Planning cycle?** *Sprint-planning, roadmap & OKR cadence all key off this.* | pick: 1-wk / 2-wk / monthly / quarterly | *"2-wk sprints, quarterly OKRs"* | `team.md` + `strategy.md` |
| 7 | **North-star metric?** *Every metrics-review & prioritization ties back to it.* | text | *"Weekly active clinics filling ≥1 cancellation."* | `strategy.md` |
| 8 | **Top goal this quarter?** *Focuses recommendations on what matters now.* | text | *"Cut activation from 14 days to 3."* | `strategy.md` |
| 9 | **How should I communicate?** *Tone, brevity & how hard to push back.* | pick: terse exec / detailed · push vs. just-do-it | *"terse exec + push hard"* | `preferences.md` |

Keep it to these **9**. The OKR/doc format (originally Q10) is **not** asked in the guided flow — it's captured via "bootstrap from a doc" or on the first artifact (*"match this format going forward?"*), since format is better learned from a real sample than asked cold. More than ~9 questions and completion drops — skip and passive capture cover the rest.

### Passive capture (the other half)
Onboarding gets you to ~60%. The `CLAUDE.md` brain should also **write to memory as it learns** during normal work ("user mentioned 2-week sprints → `team.md`"). Upfront-only goes stale. This shares the capture mechanism with Pillar 2.

---

## Pillar 2 — The Self-Improving Loop

**The differentiator.** "An OS that learns you" becomes literally true: it watches your repeated work, proposes custom skills, and you accept or reject. We already ship `skill-creator` (manual: *"turn this into a skill"*) — this makes that loop **proactive**.

### Memory is three layers, not one
This is the key model. v1 ships layer 1; the loop adds layers 2 and 3.

| Layer | File(s) | Holds | Read by |
|---|---|---|---|
| **1. Knowledge** *(today)* | `product.md`, `team.md`, `strategy.md`, `preferences.md`, `house-style.md` + `MEMORY.md` | *What's true about you* — product, team, format, goals | The brain, at **session start**, to set defaults |
| **2. Activity log** *(new)* | `memory/activity-log.md` | *What you've been doing* — one line per meaningful task | The detector, to spot repetition |
| **3. Suggestion queue** *(new)* | `memory/os-suggestions.md` | *Pending "improve myself?" proposals* | Session-start nudge + weekly tune-up |

Layer 1 is **knowledge** ("we run 2-week sprints"). Layer 2 is **behavior** ("you drafted a launch email by hand, again"). Keeping them separate stops the log from polluting the clean knowledge files. Layer 1 already works: the brain reads `MEMORY.md` at session start and writes durable facts back (one fact, right file, update don't duplicate, dates absolute, fix stale).

### The loop

1. **Capture** — after each meaningful task, the brain appends one line to `activity-log.md`. Three fields do all the work — *what you asked · which skill fired (or none) · how much you edited the output.* Local-only.
   ```
   - 2026-06-19 · asked: "draft launch email for v2"  · skill: none (hand-rolled) · edited: heavy
   - 2026-06-19 · asked: "prioritize Q3 backlog"       · skill: prioritize        · edited: changed RICE weights
   ```
2. **Detect** — two patterns, each at **~3× threshold**:
   - *Repeated job + `skill: none`* → **a skill is missing.**
   - *Repeated `skill: X` + same edit* → **a skill needs tuning.**
   - (Plus a third source needing no log: memory contradictions the brain notices reading layer 1.)
3. **Suggest (accept/reject/tweak)** — detection writes a proposal to the queue, then surfaces it. *"You've drafted launch-comms 3× this month by hand. Make a `launch-comms` skill? [yes / tweak / no]."* Never auto-applied.
4. **Generate from YOUR examples** — on accept, `skill-creator` writes the skill grounded in *how you actually did it the last 3 times* — your format, your tone. Marked `draft/learned` until it proves out.
5. **Tune what exists** — the under-rated half. `prioritize` output always gets RICE weights changed → *"bake your weights in?"* Outputs keep getting shortened → update `house-style.md`. Sharpens without adding bloat.
6. **Graduate** — a `draft/learned` skill auto-promotes to permanent after **3 clean uses** (used without a heavy edit), with a heads-up notification; you can bless it manually anytime.

### What we suggest — three kinds, one always preferred
1. **New skill** — repeated job, no skill covers it.
2. **Tune existing skill** — skill fires but output always gets the same edit. **Always prefer this over a new skill** when there's overlap — the anti-bloat rule (41 skills already).
3. **Fix memory** — stale, contradictory, or thin knowledge files.

### When + where we suggest — three venues, least intrusive first
Decides whether it feels helpful or naggy.

| Venue | When | What surfaces | Tone |
|---|---|---|---|
| **Weekly "OS tune-up"** *(primary)* | Scheduled (sibling to `weekly-metrics-review.md`) | **All** pending suggestions, batched | *"Here's how I'd improve myself — approve what you like."* |
| **Session-start nudge** *(light)* | Top of session, only if something's queued | One-liner: *"1 suggestion waiting — say `review`."* | Easy to ignore |
| **Mid-task** *(rare)* | When the 3rd repeat happens *now* and it's obvious | A single offer: *"That's the 3rd by hand — want a skill?"* | **Max 1 per session**, dropped instantly if declined |

Default home is the **weekly batch.** Mid-task is rationed hard — max one per session, only on a clear no-skill 3× repeat — the moment it nags, people turn it off.

### Worked example
You draft launch-comms by hand on Jun 5, 12, 19 — each logged `skill: none · edited: heavy`. On the 3rd, the detector queues a proposal. Sunday's tune-up opens: *"You've hand-written launch comms 3× this month. Want a `launch-comms` skill built from how you actually did them? [yes / tweak / no]."* You hit **yes** → `skill-creator` writes `skills/launch-comms/SKILL.md` (`draft`), modeled on your three emails. Next launch it fires automatically; after 3 clean uses it graduates.

### Guardrails (these are the design, not footnotes)
- **No background daemon.** A plugin can't truly watch you 24/7. The honest scope: *log to memory + scheduled/session-start review + explicit accept/reject.* That's ~90% of the value and fully real today. "Fully autonomous" stays aspirational.
- **Skill bloat is the real risk.** 41 skills already. Before suggesting a *new* skill, check overlap with existing ones and prefer *improving* the existing one. Auto-generated skills are visibly `draft` until they earn their place.
- **Annoyance budget.** Suggest sparingly, batch weekly, never auto-add without explicit accept. The moment it feels pushy, people turn it off.
- **Privacy is a feature.** The activity log is local-only. Say it loudly: *it learns you, on your machine, nothing leaves.* Otherwise "it watches what I do" reads as creepy.

---

## Pillar 3 — Visual Outputs (the "UI")

**Don't build a separate web app** — it fights the grain of a native Claude Code plugin (you'd own hosting/auth/sync for something users must leave the terminal to use). Use Claude Code's native visual surfaces instead:

- **`AskUserQuestion` widgets** → already covered by onboarding. That *is* a clickable UI.
- **Inline rendered widgets** → make the *outputs* visual. The high-value move:

| Skill | Renders as |
|---|---|
| `prioritize` | RICE / Kano matrix |
| `roadmap` | Now / Next / Later board |
| `okrs` | Objective → Key Result tree |
| `metrics-review` | Scorecard with trend arrows |
| `journey-map` | Swimlane |

Turns dry markdown into things that look like a product and are screenshot-shareable — which doubles as marketing for The Product Channel.

A read-only **"PM home" dashboard** generated from `memory/` (current OKRs, roadmap snapshot, what the OS knows) is the one web-ish surface worth considering — but **last**, and only if people ask.

---

## Build order

Each phase ships on its own and sets up the next.

| Phase | Ship | Why this order |
|---|---|---|
| **1** | `/setup` onboarding + passive memory capture | Fixes activation (empty memory). Also lays down the `activity-log.md` Phase 2 needs. |
| **2** | Self-improving loop: capture → detect → suggest → generate → tune + weekly tune-up automation | The differentiator and the retention story. Depends on Phase 1's capture. |
| **3** | Visual output widgets (start: `prioritize`, `roadmap`, `okrs`) | Polish + shareability once the engine works. |
| **4** *(maybe)* | Read-only "PM home" dashboard | Only if users ask for a glanceable surface. |

---

## Decisions (resolved)

- **Q9 (OKR/doc format) is out of the guided flow.** Guided flow = **9 quick questions**; format is captured via "bootstrap from a doc" or on the first artifact (*"match this format going forward?"*). Learned from a real example, not asked cold.
- **`strategy.md` is shared by default in multi-product mode**, split only on request (portfolio PM has one strategy; agencies are the exception).
- **Skills graduate auto after 3 clean uses** (used without a heavy edit), with a heads-up notification; manual bless allowed anytime.
- **Mid-task suggestions: max 1 per session**, only on a clear no-skill 3× repeat, dropped instantly if declined. Everything else waits for the weekly batch.

## Open questions

- **Onboarding question set** — is the 9 above the right cut? Anything missing / droppable?
- **Detection threshold** — is 3× the right trigger, or tune per job type?
- **Activity log shape** — one file, or per-week rotation to keep it small?
- **Marketing line** — *"the only PM toolkit that gets better the more you use it — it builds you custom skills from your repeated work, all on your machine."* Lead with this?
