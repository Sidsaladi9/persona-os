---
name: release-notes
description: Turns a list of shipped changes into audience-tiered release notes — a benefit-led user-facing changelog, a what/why/impact internal log, and a short social announcement cut. Use when you say "write release notes," "draft the changelog," "we just shipped X, announce it," "turn these tickets into release notes," or "summarize this release for customers and the team."
---

# Release Notes

Built on the audience-tiered changelog framework: one set of shipped changes, three lenses. The same release reads differently to a user (what's in it for me), an internal team (what changed, why, and what it affects), and a social audience (a hook worth clicking). You write all three from a single source of truth so nothing drifts.

**Grounded in:** *Working Backwards* — Bryar & Carr: lead with the customer benefit, audience-tiered.
**Go deeper (The Product Channel):** [The Beginner's Guide to a Product Launch](https://sidsaladi.substack.com/p/week-19-the-beginners-guide-to-a)

## When to use this
- A sprint or release closed and you have a pile of merged PRs, tickets, or commit messages to turn into something readable.
- You're shipping a customer-facing feature and need both an in-app/email changelog and a Slack/social post.
- Support or sales keeps asking "what actually changed in this release?" and you need an internal log they can scan.
- You want to announce a launch on LinkedIn/X without leaking jargon, internal names, or unshipped roadmap.
- You're standardizing a recurring changelog (weekly/biweekly) and want a repeatable format.

## Before you start (gather these)
- **The raw change list** — PR titles, ticket IDs, commit messages, or a plain list of what shipped.
- **Release identity** — version/date/name (e.g. `v2.4` or `Week of June 14`).
- **Audience reach** — who sees the user-facing tier (all users? a plan tier? beta cohort?).
- **Change types** — which items are new features, improvements, fixes, deprecations, or breaking changes.
- **The "why"** — the user problem or business reason behind the marquee items (for the internal tier).

If 2+ of these are missing or vague, ASK 2–4 sharp questions before drafting — e.g. "What's the version/date label?", "Which of these are user-visible vs. internal-only?", "Any breaking changes or deprecations users must act on?", "What's the one headline item worth leading with?" If the data is already provided, proceed and state assumptions inline (e.g. *Assuming all items ship to all users; flag any beta-gated.*).

## Process
1. **Normalize the raw list.** Strip ticket prefixes and internal codenames. Group every item into one bucket: New, Improved, Fixed, Deprecated, Breaking, or Infra/Internal. Drop anything user-invisible (refactors, CI, internal tooling) from the user tier and tag it **Infra/Internal** — keep it for the internal tier only.
2. **Pick the headline.** Identify the single most valuable change. It leads all three tiers. Everything else is supporting cast.
3. **Write the user tier benefit-first.** Each line answers "what can I now do / what got better for me?" Lead with the verb and the outcome, not the mechanism. No ticket numbers, no component names, no "refactored." Breaking changes and required actions go at the top with a clear **Action required** flag. If only a *subset* of users must act, say so and scope it — don't make everyone read an alarm that isn't theirs (e.g. *"Most users: nothing to do. If you use the legacy API key format, rotate your key before [date]."*).
   *Sizing:* keep the user tier scannable — aim for ~3–7 lines per section. If you have more than ~5 fixes, collapse the small ones into a single "Plus a batch of smaller fixes" line and only break out the user-visible ones by name.
4. **Write the internal tier as what / why / impact.** For each meaningful item: what changed, why it shipped (the problem/bet), and what it touches (surfaces, teams, metrics, support implications). This is the artifact sales/support/eng actually use.
   *Sizing:* one row per *meaningful* change, not per PR. Group trivial or near-identical items into a single row (e.g. "12 dependency bumps", "misc Infra/Internal cleanup") so the table stays readable; reserve full rows for anything with user, support, or on-call impact.
5. **Cut the social tier to one hook.** First pick the platform and write to its constraints: **X** ≈ 280 chars, tight hook + link, expect the link to eat ~23 chars; **LinkedIn** rewards a strong first line before the "…more" fold, room for 2–3 benefit bullets; **Slack** is internal — drop the marketing voice, name the team impact and where to find the full notes. Lead with the headline item as a benefit or a curiosity gap. One to three lines, link to the full notes, one CTA. No changelog dump. If asked for more than one platform, write a separate cut per platform rather than one generic post.
6. **Self-check against the anti-patterns** below, then state any assumptions you made about audience reach or change classification.

## Output template

```markdown
# [Product] Release Notes — [vX.Y / Date label]

> **Headline:** [One sentence on the single most valuable change in this release.]

---

## 1. User-facing changelog (benefit-led)

**[Product] [vX.Y] is here.** [One-line framing of what this release means for users.]

> ⚠️ **Action required:** [What users must do, by when, or "None — nothing to do on your end." If only some users are affected, scope it: "Most users: nothing to do. If you [condition], do [action] by [date]."]

### ✨ New
- **[Benefit headline]** — [What you can now do, in plain language. Outcome first.]
- **[Benefit headline]** — [...]

### ⚡ Improved
- **[What got better]** — [The before → after in user terms. e.g. "Exports that used to take minutes now finish in seconds."]
- **[...]**

### 🐛 Fixed
- [Plain-language description of the problem that's now gone — no ticket IDs.]
- [...]

### 🔻 Deprecated / changing
- **[What's going away]** — [What replaces it and the date it sunsets.]

---

## 2. Internal release log (what / why / impact)

**Release:** [vX.Y] · **Date:** [date] · **Reach:** [all users / plan / cohort] · **Owner:** [name]

| Change | Type | Why (problem / bet) | Impact (surfaces · teams · metrics) |
|---|---|---|---|
| [What changed] | New | [The problem or hypothesis] | [What it touches; what to watch; support notes] |
| [What changed] | Improved | [...] | [...] |
| [What changed] | Fixed | [Root cause, 1 line] | [Who was affected; is a comms note needed?] |
| [What changed] | Breaking | [...] | [Migration path · who must act NOW · what breaks if they don't] |
| [What changed] | Deprecated | [...] | [Replacement named · still works until [date] · migration window] |
| [What changed] | Infra/Internal | [Refactor / CI / tooling reason] | [No user impact; what eng/on-call should know] |

> **Breaking vs. Deprecated:** **Breaking** = the user must migrate *now* or it breaks on ship — no working fallback. **Deprecated** = it still works until a named sunset date *and* you name the replacement; users have a window to migrate, not an emergency.

**Watch after ship:** [Metric or signal that tells us this worked — e.g. activation rate, error rate, ticket volume.]
**Known gaps / follow-ups:** [What deliberately didn't make it; next-release intent.]
**Support / sales notes:** [Canned answer for the predictable inbound question this release creates.]

---

## 3. Social / announcement cut

**[Platform: LinkedIn / X / Slack]** — [note the constraint you're writing to: X ~280 chars · LinkedIn front-load before the fold · Slack = internal, team-impact voice]

[Hook line — lead with the headline benefit or a curiosity gap. 1 sentence.]

[Optional 1–2 lines of supporting color — who it's for, why it matters now.]

What's new in [vX.Y]:
→ [Top benefit 1]
→ [Top benefit 2]
→ [Top benefit 3]

Full notes: [link]

[Single CTA — "Try it," "Read the changelog," "Reply with what you'd ship next."]
```

## Avoid (anti-patterns)
- **Pasting PR titles as the user changelog.** "Refactor auth middleware (#4821)" means nothing to a user. Translate every line to an outcome or cut it.
- **Burying a breaking change in the middle of the list.** Required actions and deprecations go at the top with a flag — users skim and will miss them otherwise.
- **One tier for all audiences.** A benefit line for users is too thin for support; a what/why/impact table is too dense for social. Write all three or you'll be answering the same questions in DMs.
- **Leaking the roadmap.** "Coming soon: AI summaries" in a shipped changelog reads as a promise you may not keep. Notes are for what shipped, not what's next (except a deliberate deprecation date).
- **Vague fixes.** "Various bug fixes and improvements" tells no one anything. Name the user-visible problem that's now gone.

## Tips
- **Lead every user-facing line with a verb and an outcome.** "Search now ranks recent items first" beats "Improved search ranking algorithm." If you can't state a user benefit, the item belongs only in the internal tier.
- **Keep the internal log even when the user changelog is empty.** Infra-only releases still need a what/why/impact record for the next on-call and for sales context.
- **Steal your own headline.** The marquee item that leads the user tier is also your social hook — write it once, well, and reuse it across all three cuts.
- **Make it repeatable.** Save this as your team's template and fill it the same way every release; a predictable changelog format trains users to actually read it.
