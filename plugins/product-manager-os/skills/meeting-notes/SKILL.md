---
name: meeting-notes
description: Turns raw, messy meeting notes or a transcript into a crisp, shareable summary. Use when someone says "summarize these meeting notes", "turn this transcript into action items", "what did we decide", "clean up my notes", or "send a recap". Works for any meeting type — standup, planning, review, 1:1, or stakeholder sync — from pasted notes or a connected transcript tool.
---

# Meeting Notes

Meetings end and the value leaks out — decisions get forgotten, action items lose their owners, and the recap never gets sent. This skill takes whatever you have (scribbled notes, a wall-of-text transcript, or a connected transcript source) and turns it into a clean, skimmable summary you can paste into Slack or email the same day. The goal is extraction, not transcription: surface what was decided, who owns what by when, and what's still open.

**Grounded in:** *Death by Meeting* — Patrick Lencioni: separate decisions from discussion; every action has an owner and date.
**Go deeper (The Product Channel):** [The Product Channel](https://sidsaladi.substack.com)

## When to use this
- You have raw notes or a transcript and need a usable summary fast.
- You ran a standup, planning, review, 1:1, or stakeholder sync and owe people a recap.
- You want a clean list of action items with owners and due dates pulled out of the noise.
- Someone asks "what did we actually decide?" and you need a clear answer.

## Before you start (gather these)
- The raw notes or transcript. If the user hasn't pasted it, ask them to — or pull it from a connected transcript tool (e.g. Fireflies, Granola) if one is available.
- The meeting type (standup, planning, review, 1:1, stakeholder sync) — it shapes what matters most.
- Who was in the room — needed to assign action item owners by name.

## Process
1. **Read everything first.** Don't summarize as you go. Take in the whole input before extracting, so you understand the arc of the conversation and don't mistake early discussion for final decisions.
2. **Extract DECISIONS** — anything the group agreed on or settled. State each as a clear, standalone sentence. If a decision was implied but not confirmed, mark it "(tentative)".
3. **Extract ACTION ITEMS** — every commitment to do something. For each, capture: the action (a clear next step, not a vague topic), the owner (a named person), and the due date. Resolve relative dates (today, Friday, next Tue, EOW) against the meeting date and render them as absolute YYYY-MM-DD — this is resolution, not invention. Write "TBD" only when no date is recoverable — don't invent one.
4. **Extract OPEN QUESTIONS** — anything raised but unresolved, blockers, or items explicitly deferred to a later discussion.
5. **Capture KEY CONTEXT** — the few facts, numbers, or rationale worth keeping that aren't decisions or actions (e.g. "Q3 budget is locked at $40K", "legal flagged the data clause").
6. **Flag ownerless commitments.** If something sounds like a commitment but no one clearly owns it, still list it as an action item with "owner: TBD" and surface it — these are the items that fall through the cracks.
7. **Stated vs. inferred work.** Only surface work that was actually stated. If you want to surface latent or unspoken follow-ups that no one explicitly committed to, that's allowed — but put them under a separate **"Suggested follow-ups (not committed)"** heading so they're never mistaken for agreed action items.

## Output template

> **Recap: [Meeting name] — [date]**
>
> **TL;DR**
> - [Line 1: the headline outcome or biggest decision]
> - [Line 2: the most important action / who's doing what next]
> - [Line 3: anything still open or needing a follow-up]
>
> **Decisions**
> - [Decision stated as a clear sentence]
> - [Decision stated as a clear sentence] (tentative)
>
> **Action items**
>
> | Action | Owner | Due |
> |---|---|---|
> | [Clear next step] | [Name] | 2026-06-20 |
> | [Latent / ownerless item that was flagged] | TBD | TBD |
>
> **Open questions**
> - [Unresolved item or blocker]
> - [Deferred decision]
>
> **Suggested follow-ups (not committed)**
> - [Inferred next step no one explicitly committed to]
>
> **Notes / context**
> - [Fact, number, or rationale worth keeping]

Keep it tight and skimmable — the TL;DR alone should be enough for someone who wasn't there to know what happened.

## Avoid (anti-patterns)
- Transcribing everything instead of extracting what matters — a summary that's as long as the transcript is useless.
- Action items with no owner or no due date. Aim for both owner and due on every action; use "TBD" rather than leaving a field blank. The exception: flagged ownerless or latent items (Step 6) may legitimately carry "TBD" in both Owner and Due — that's how they get surfaced rather than dropped.
- Burying the decision inside a paragraph of prose. Decisions go in their own list, stated plainly.
- Inventing owners, decisions, or dates that aren't in the source. If it's ambiguous, mark "owner: TBD" or "(tentative)" — don't guess.

## Tips
- Assign owners by name, not by role ("Priya" not "the design team") — accountability needs a person.
- Separate decisions from discussion: a thing someone *suggested* isn't a decision until the group agreed.
- Send the recap the same day, while it's fresh and people can still correct it.
- When in doubt about a due date, write "TBD" and let the owner fill it in — a flagged gap beats a wrong date.
