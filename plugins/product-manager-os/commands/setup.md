---
description: Set me up — a 3-minute guided onboarding that fills your memory so I stop asking the basics
---

Run onboarding for the Product Manager OS. Goal: fill `memory/` so every future session starts with context instead of questions. Keep it light — under 5 minutes — and **never block the user from working**.

## Before you ask anything
1. Read `memory/MEMORY.md` and the knowledge files (`product.md`, `team.md`, `strategy.md`, `preferences.md`, `house-style.md`).
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

## Finish
End with a short recap of what you now know (2–4 lines), note anything still blank ("I'll pick the rest up as we work"), and suggest one concrete next move that uses the new context — e.g. *"Want to start with `/weekly`, or turn an idea into a spec?"* Do not lecture; get them working.
