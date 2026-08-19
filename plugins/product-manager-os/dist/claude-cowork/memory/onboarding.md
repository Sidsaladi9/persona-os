# Onboarding State

> How much the OS knows about you, and what it still doesn't. Claude reads this at session start
> and writes to it after `/setup` or any meaningful passive capture. **Local-only — never leaves your machine.**
>
> This file exists so the OS can do two things it otherwise can't: (1) resume a setup you skipped
> or abandoned, instead of starting over, and (2) know whether it has already asked, so it nudges
> at most twice and then shuts up for good.

**Status:** `not-started`
<!-- one of: not-started | in-progress | skipped | complete -->

**Last offered:** never
**Times offered:** 0
**Last updated:** never

---

## Coverage

Claude updates this table as fields get filled — by `/setup`, by passive capture, or by you editing
the files directly. A field is `filled` only when it holds a real answer, not a template placeholder.

| Field | File | Status |
|---|---|---|
| What you're building | `product.md` | empty |
| Primary user / ICP | `product.md` | empty |
| Stage | `product.md` | empty |
| Business model | `product.md` | empty |
| Your role + team size | `team.md` | empty |
| Planning cycle | `team.md` | empty |
| North-star metric | `strategy.md` | empty |
| Top goal this quarter | `strategy.md` | empty |
| How to communicate with you | `preferences.md` | empty |
| House style / doc format | `house-style.md` | empty (captured from a real doc, not asked) |

**Coverage:** 0 / 10

---

## Skipped questions

When you skip a single question, Claude logs it here with the date so it can offer that one again
later — in context, at the moment it would actually help — rather than re-running the whole flow.

_(none yet)_

---

## Re-offer rule (for Claude, not the user)

- Offer onboarding **at most twice, ever.** Count is tracked above.
- **Offer 1** — the first real request of the first session, if `Status: not-started`.
- **Offer 2** — only when a missing field is *actively costing the user something in the task at hand*
  (e.g. asked for a prioritization with no north-star metric on file). Name the specific gap and the
  specific cost, offer to capture just that one field inline, and mention `/setup` as the fuller option.
- After two offers, or after `Status: skipped` is set twice, **never offer again.** Fall back to passive
  capture only. The user knows the command exists; nagging costs more trust than the missing context is worth.
- Never block a request on onboarding. Never re-run a completed flow — fill gaps only.
