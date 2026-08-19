# Workflows

This host has no native slash commands. Each workflow below is a multi-step process the agent should run when the user asks for it by name — *"run setup"*, *"do the weekly"*, *"new feature: dark mode"*.

## `connect`

> Connect your PM tools (tracker, analytics, docs, chat) so the OS can pull live data and write work back

Help me connect my tools so the OS stops asking me to paste and copy. Keep it short and concrete.

1. **See what's already connected.** Check which MCP servers / connectors are available in this session. If a connector registry or a `list_connectors` / `suggest_connectors` capability exists, use it. Report what's already wired (e.g. tracker, analytics, docs, chat) and what's missing.

2. **Recommend by gap, not by vendor.** Based on what I do most (and `memory/`), suggest the highest-value connections to add, mapped to what they unlock — e.g.:
   - **Issue tracker** (Linear/Jira/Asana) → `sprint-planning`, `roadmap`, and writing `user-stories` back as issues.
   - **Analytics** (Amplitude/Mixpanel/GA/warehouse) → live `metrics-review`, `cohort-analysis`.
   - **Docs** (Notion/Confluence/Drive) → read specs/research, write `write-spec`/`roadmap` back as pages.
   - **Chat** (Slack/Teams) → post `stakeholder-update`/`release-notes`.
   Don't assume a specific vendor — recommend whichever I actually use.

3. **Walk me through connecting one.** Connectors are authorized through the host's connector/OAuth flow — point me to it (the `/mcp` panel or the app's Connectors settings), don't try to run install commands for me. If the bundled libraries (getprompts/getskills) aren't active, note they're zero-config and how to enable them.

4. **Confirm it works.** After I connect something, verify the OS can see it, and name the first thing it now unlocks (e.g. "try `/weekly` — I'll pull the numbers myself now").

Note: every connection is optional. Without any, the OS still works — I'll just ask you to paste. With them, the work goes hands-free and writes back to where your team lives. The OS never writes or posts anything without showing you the draft first.

---

## `discovery`

> Run a discovery cycle — plan interviews, synthesize, map opportunities

Run a discovery cycle on: **$ARGUMENTS**

Read `memory/product.md` and `memory/strategy.md` first. Then:

1. **`customer-interview`** — define the learning goal + riskiest assumption, and produce the interview plan + non-leading script. If this is a retention/churn question, use the inverted frame.
2. **Pause** — I'll go run the interviews and paste back the notes (or paste existing research now).
3. **`synthesize-research`** — once I have notes, cluster them into ranked, evidence-backed insights.
4. **`opportunity-solution-tree`** — turn the insights into an outcome → opportunity → solution map and recommend where to focus.

If I've already pasted research, skip steps 1–2 and go straight to synthesis. Always separate observation from interpretation, and flag small samples.

---

## `launch`

> Plan a launch end-to-end — GTM plan, release notes, stakeholder comms

Plan the launch of: **$ARGUMENTS**

Read `memory/` for product, team, and audience context. Then chain:

1. **`launch-plan`** — set the launch tier (default down when unsure), audience, message, channels, timeline + checklist with owners, success metrics, and the rollback trigger.
2. **`pre-mortem`** — assume the launch flopped; surface the top failure modes and attach a mitigation + early-warning signal to each. Feed anything serious back into the plan.
3. **`release-notes`** — draft the user-facing, internal, and short announcement cuts.
4. **`stakeholder-update`** — draft the "we're launching X" update for exec/eng/customer audiences.

Show me each artifact. End with the single most likely reason this launch underperforms and how we'd catch it early.

---

## `new-feature`

> Take a raw feature idea from discovery all the way to a build-ready backlog

Run the full new-feature pipeline for: **$ARGUMENTS**

First read `memory/` (product, team, strategy) for context. Then chain these skills in order, pausing for my input where a real decision is needed:

1. **`product-brainstorm`** — sharpen the problem and the riskiest assumption. Don't accept the idea at face value.
2. **`opportunity-solution-tree`** — anchor it to an outcome, map the opportunity it serves, and generate solution options (not just this one).
3. **`assumption-test`** — surface the riskiest assumption and the cheapest way to test it. If it's clearly unvalidated, say so before we spec anything.
4. **`prioritize`** — sanity-check that this belongs above what's already in flight.
5. **`write-spec`** — write the PRD (problem, goals, non-goals, success metrics, assumptions, acceptance criteria).
6. **`user-stories`** — break the spec into stories with Given/When/Then acceptance criteria and a build order.

Stop after each major step and show me the output before continuing. End with: what to validate before we commit engineering time.

---

## `setup`

> Set me up (or finish setting me up) — a 3-minute onboarding that fills your memory so I stop asking the basics. Re-run any time to fill only what's still missing; `/setup status` shows what I know.

Run onboarding for the Product Manager OS. Goal: fill `memory/` so every future session starts with context instead of questions. Keep it light — under 5 minutes — and **never block the user from working**.

## Modes — pick from the argument, default to the smart one

`/setup` takes an optional argument. **Never make the user learn these** — infer the right mode from
`memory/onboarding.md` and just do it. The arguments exist so a user who skipped can come back on purpose.

| Invocation | What you do |
|---|---|
| `/setup` | Read `memory/onboarding.md`. `not-started` → run the full flow. `in-progress` / `skipped` → **resume**: say what you already know in one line, then ask only the still-empty fields (and any logged skipped questions). `complete` → don't re-run; show the coverage table and offer to update one specific thing. |
| `/setup status` | Read-only. Print the coverage table from `memory/onboarding.md`, name the gaps in plain language, say what each gap costs (*"no north-star metric means I can't rank your backlog by impact"*), and offer to fill them. Ask nothing unless they say yes. |
| `/setup reset` | Confirm first — this clears the knowledge files back to templates and sets `Status: not-started`. Only for "this is a different product now" / handing the OS to someone else. Never do it without an explicit yes. |

**If the user skipped onboarding earlier, this command is how they come back.** Resuming is the default —
they should never have to re-answer something they already answered.

## Step 0 — make sure the folders exist
Before any questions: if `memory/MEMORY.md` doesn't exist in the working directory, create `memory/`, `workspace/`, `automations/`, and `tests/` first (see the first-run section in `CLAUDE.md`). On a plugin install nothing is created in the user's project, so this is the common case, not the edge case. Do it quietly — one line, not a report.

If the working directory looks wrong for months of product context (`~`, `~/Downloads`, `/tmp`), ask where they'd like it before writing anything.

## Before you ask anything
1. Read `memory/onboarding.md` (status + coverage + previously skipped questions) and then `memory/MEMORY.md` and the knowledge files (`product.md`, `team.md`, `strategy.md`, `preferences.md`, `house-style.md`). The state file tells you whether this is a first run or a resume; the knowledge files are the ground truth for what's actually filled — if they disagree, believe the knowledge files and correct the state file.
2. **Be gap-aware.** Only ask about fields that are still template/empty. If a file is already filled, skip its questions. If everything is filled, say so and offer to update one specific thing instead — do **not** re-run the whole flow.

## Offer the path (let them pick)
Tell the user there are three ways to do this and let them choose:
- **Guided** — you ask the 9 quick questions below.
- **Bootstrap from a doc** — they paste a PRD / strategy doc / Notion content and you infer `product.md` + `house-style.md` from it (use the `house-style` skill for the format capture). Then only ask for whatever the doc didn't cover.
- **Let me infer, you confirm** — for anything they skip, take your best guess from what you've seen this session and show it for a one-tap confirm, so they edit instead of write from scratch.

Always include a **"Skip for now — I'll learn as we go"** option. They can skip the whole thing or any single question. Skipped fields get filled later by passive capture or a re-run of `/setup`.

## Branch first: one product or several?
Ask up front: **"Do you run one product, or several?"**
- **One** → use the single `product.md` / `team.md` (default).
- **Several** → for each product, create `memory/product-<slug>.md` (and `memory/team-<slug>.md` if teams differ), and add a one-line pointer for each in `MEMORY.md`. **Remove the default `memory/product.md` template** so it isn't left orphaned (the per-product files supersede it; update the `MEMORY.md` Product line to list the products instead). Going forward, when a request is product-specific, ask which one (remember the last-used so you're not asking every time). `strategy.md` stays **shared** unless they say products have separate strategies — only then split into `strategy-<slug>.md`.

## The 9 questions (use the AskUserQuestion picker for the "pick" ones)
Ask in small batches, not all at once. For each, the *why* is for your judgment — you don't have to read it aloud, but use it to push for a useful answer over a vague one. Offer the example if they stall.

| # | Question | Type | Example to offer | Write to |
|---|---|---|---|---|
| 1 | What are you building, in a sentence? | text | "A tool that auto-fills last-minute clinic cancellations." | `product.md` |
| 2 | Who's it for — your primary user / ICP? | text | "Office managers at 5–20-person dental practices." | `product.md` |
| 3 | What stage is it? | pick: 0→1 / scaling / mature | scaling | `product.md` |
| 4 | Business model? | pick: SaaS / marketplace / consumer / other | "SaaS, $99/mo per location" | `product.md` |
| 5 | Your role + team size? | text | "Sole PM; 6 eng, 1 designer." | `team.md` |
| 6 | Planning cycle? | pick: 1-wk / 2-wk sprints / monthly / quarterly | "2-wk sprints, quarterly OKRs" | `team.md` + `strategy.md` |
| 7 | North-star metric? | text | "Weekly active clinics filling ≥1 cancellation." | `strategy.md` |
| 8 | Top goal this quarter? | text | "Cut activation from 14 days to 3." | `strategy.md` |
| 9 | How should I communicate with you? | pick: terse exec / detailed · push hard / just-do-it | "terse exec + push hard" | `preferences.md` |

**Note:** OKR / document format is **not** a question here. Capture it from a real sample — when they pick "bootstrap from a doc," or the first time you produce an artifact (*"Want me to match this format going forward?"*) — and write it to `house-style.md` via the `house-style` skill. Format is better learned from an example than asked cold.

## Write the answers
As you collect answers, write each to the file in the table — replacing the template prompts, one fact per place it belongs, dates absolute. Don't dump everything into one file. After writing, update `MEMORY.md` pointers if you added any new files (multi-product).

**Then update `memory/onboarding.md` — this is what makes setup resumable.** Every run, without being asked:
- Flip each field you filled to `filled` in the coverage table and recount `Coverage: n / 10`.
- Log any question they skipped under **Skipped questions** with the date, so you can offer that one
  again later in context instead of re-running the whole flow.
- Set `Status:` — `complete` when every field is filled, `in-progress` when some are, `skipped` when
  they bailed out of the whole thing. Bump `Times offered` and `Last offered` if this run started from
  an offer you made. Stamp `Last updated` with today's absolute date.

Do the same bookkeeping after **passive capture** — if you learn the north-star metric mid-task and
write it to `strategy.md`, flip that row too. Otherwise the OS keeps offering to collect what it already has.

## Finish
End with a short recap of what you now know (2–4 lines), note anything still blank ("I'll pick the rest up as we work"), and suggest one concrete next move that uses the new context — e.g. *"Want to start with `/weekly`, or turn an idea into a spec?"* Do not lecture; get them working.

---

## `strategy`

> Build or pressure-test product strategy — analysis, strategy, positioning

Work the strategy for: **$ARGUMENTS**

Read all of `memory/` first. Then chain:

1. **`market-analysis`** — scan the environment (SWOT / PESTEL / Porter's Five Forces / Ansoff) and synthesize 2–3 strategic implications.
2. **`product-strategy`** — write the one-page strategy: diagnosis, where-to-play, how-to-win, 3–4 pillars, explicit non-goals, "success looks like", and the kill-criterion for the big bets.
3. **`positioning`** — craft the positioning statement + value prop + messaging pillars that follow from the strategy.
4. **`red-team`** — attack the result. Name the load-bearing assumptions and what a skeptical exec or competitor would exploit. Revise the weak spots.

Show me each step. The red-team pass is mandatory — don't skip it.

---

## `tune-up`

> Improve the OS from my recent work — propose new/tuned skills from patterns in my activity log

Run the OS tune-up now (the on-demand version of the weekly self-improvement pass). **Propose only — never apply anything without my explicit yes.**

1. **Read the three signals.**
   - `memory/incidents.md` → the `## Open` section. **Every open incident gets a proposal, at 1×.** No pattern required — a defect that produced unusable output does not need to recur to be worth fixing. Do these first; they outrank everything below.
   - `memory/activity-log.md` → the `## Log` section only, for 3× patterns.
   - `python3 tests/relevance_report.py` → skills whose artifacts are never referenced or revisited.
   - Skip anything already `[PENDING]` or rejected in `memory/os-suggestions.md`.

   If there are no open incidents **and** fewer than ~5 real log entries **and** no relevance flags, say there isn't enough signal yet and stop. Don't invent patterns to have something to say.

2. **Detect, at the right threshold for each source:**
   - **Incident → 1×.** Route the fix by root cause: a skill defect edits the skill; a missing input adds it to that skill's `inputs:`; a stale fact fixes the memory file; a wrong tier corrects the frontmatter. **A root cause that repeats across *different* skills is the highest-value finding available** — it means the problem is in `CLAUDE.md`, not in any one skill. Say so explicitly when you see it.
   - **Missing skill → 3×.** Same kind of job with `skill: none` 3+ times.
   - **Skill needs tuning → 3×.** Same skill + same `correction` 3+ times.
   - **Dead output → ≥3 artifacts, ≥2/3 never revisited.** The skill runs and the user never comes back to what it made. Propose a change to *what* it produces or *when* it fires — not a new skill. This is usually a wrong output template or a wrong tier.
   - **Stale memory:** a knowledge file the recent work shows is now wrong (only if obvious).

3. **Anti-bloat:** before proposing any *new* skill, find the nearest existing skill in `skills/` and prefer tuning/extending it. Only propose new if nothing covers the job; say which skill you checked.

4. **Queue + present.** Append each surviving pattern as a `[PENDING]` entry in `memory/os-suggestions.md`, then show me the batch for **accept / tweak / reject**.
   - Accept a *new skill* → use `skill-creator`, ground it in my last ~3 examples of that job, and mark it `status: draft`.
   - Accept a *tune* → make the specific change to the skill (or to `house-style.md` if it's formatting).
   - Reject → move it to `## Resolved` with the date so it's not re-proposed.

5. **Graduate drafts:** any `status: draft` skill used 3× with no correction **and no incident** → promote to permanent and tell me. An incident resets the count; a draft that failed once has not proven out.

6. **Close incidents you fixed.** When I accept a fix, move that incident to `## Resolved` in `memory/incidents.md` with the date and what changed. An open incident that's been fixed will keep generating the same proposal every week.

Keep it tight. End with: **open incidents / proposals made / accepted / drafts graduated / incidents closed.** If nothing cleared a threshold, say that in one line — a quiet week is a real result, not a failure to report.

---

## `weekly`

> Run my weekly PM review — metrics scorecard + leadership update

Run my weekly review.

Read `memory/product.md` and `memory/strategy.md` for the North Star, the metrics we watch, their targets, and this quarter's goals. Then:

1. **`metrics-review`** — pull this week's numbers (from a connector if available, else ask me to paste them) and build the scorecard: each metric vs prior vs target with a 🟢/🟡/🔴 status, a hypothesis for every red/yellow, and 2–3 recommended actions with owners.
2. **`stakeholder-update`** — draft the exec-brief version of this week's status: headline first, status color, one ask if there is one.

Show me both. Keep the exec brief to the headline + 5 fields.

---
