---
name: stakeholder-update
description: Generate a stakeholder update tailored to audience and cadence. Use when the user wants to "write a stakeholder update", "exec update", "weekly status", "monthly status", "announce the launch", "escalate this blocker", or "make a leadership-friendly version" — and when the same progress needs to be re-cut for execs, engineers, or customers.
---

# Stakeholder Update

A stakeholder update is not a list of everything you did. It's a deliberate act of communication: tell the right person the one thing they need to know, the decision you need from them, and how worried they should be. The fastest way to lose a stakeholder's trust is to make them dig for the status, bury a risk on line nine, or send an exec a wall of engineering detail. This skill turns raw progress into a clean update, sized and toned for whoever is reading it.

## When to use this
- Recurring weekly or monthly status to leadership or a steering committee.
- Announcing a launch, milestone, or GA to a broad internal or external audience.
- Escalating a risk or blocker that needs a decision, resource, or unblock.
- Re-cutting the same update for a different audience (exec vs. engineering vs. customer).
- Translating a messy Slack thread or tracker dump into something a busy reader can scan in 20 seconds.

## Before you start (gather these)
- **Audience** — exec / engineering / customer / cross-functional. This drives depth and jargon more than anything else.
- **Cadence** — one-off announcement vs. recurring weekly/monthly (affects what "since last time" means).
- **What happened since the last update** — shipped, learned, slipped, decided.
- **Status** — on track 🟢 / at risk 🟡 / off track 🔴, against the goal or date that matters.
- **Asks / decisions needed** — what you need from the reader, who owns it, by when. "Nothing, FYI only" is a valid answer — say so.

**Owner convention:** owner = the single person accountable for resolving the item. If a decision is needed from someone else, that person is not the owner — name them separately as the approver/decider (e.g. "owner: Priya · approver: VP Eng").

If any of these are missing, ask before drafting. The single most common failure is guessing the audience or the status color. Don't.

## Process
1. **Identify the audience and what they care about.** Execs care about outcome, risk, and money/time. Engineers care about scope, dependencies, and technical decisions. Customers care about the benefit to them and when they get it. Write to that, not to yourself.
2. **Lead with the headline + status color.** First line answers "should I worry?" and "what's the one thing?" — status color, then the single most important sentence. Never make the reader scroll to find the status.
3. **Summarize progress against goals**, not activity. Tie what happened to the objective or date it serves. "Shipped X" is weak; "X is live, putting us on track for the Q3 GA date" is the update.
4. **Surface risks with mitigation.** Every risk gets a paired mitigation and an owner. A risk with no plan is just anxiety. If it needs a decision, that's an ask — promote it.
5. **Make asks explicit.** Each ask names the owner and a deadline. Vague asks ("we may need help") get ignored; specific ones ("Need legal sign-off on terms by Thu — owner: Priya") get done.
6. **Adapt depth and jargon to the audience.** Strip internal acronyms and ticket numbers for exec and customer versions. Keep them for engineering. Same facts, different altitude.

## Output templates
Produce all three variants of the **same** update so the user can pick or send in parallel. Keep the facts identical across versions — only depth and tone change.

**Status legend:** 🟢 on track · 🟡 at risk · 🔴 off track

### 1. Exec brief (headline + 5 fields)
The headline line does not count toward the field cap. Use exactly the 5 labeled fields below after it — no more.
```
[🟢/🟡/🔴] <Project> — <one-line headline>
Status: <on track / at risk / off track> against <goal or date>
Progress: <the one outcome that matters since last update>
Risk: <top risk + one-line mitigation, or "None">
Ask: <decision needed — owner + deadline, or "FYI only, no ask">
```

### 2. Detailed update
```
[🟢/🟡/🔴] <Project> — <headline> · <date / period>

Progress
- <outcome tied to goal>
- <outcome tied to goal>

Metrics
- <metric>: <value> (<vs. target / vs. last period>)

Risks & mitigations
- 🟡 <risk> → Mitigation: <plan> (owner: <name>)
- 🔴 <risk> → Mitigation: <plan> (owner: <name>)

Decisions needed
- <ask> — owner: <name>, by <date>

Next
- <what happens before the next update>
```

### 3. Customer / external-friendly
```
<Benefit-led headline — what's new and why it's good for you>

What's changing: <plain-language description, no internal jargon>
What it means for you: <the benefit, concretely>
When: <date or "available now">
<Optional: what to do next / where to learn more>
```

## Quality bar
- [ ] The headline is in the **first line** — reader knows the gist without scrolling.
- [ ] Status color (🟢/🟡/🔴) is stated explicitly, not implied.
- [ ] Progress is framed against a goal or date, not as a raw activity list.
- [ ] **Every** risk has a paired mitigation and an owner.
- [ ] Every ask is explicit with an owner **and** a deadline — or the update says "no ask, FYI."
- [ ] Exec and customer versions contain **zero** internal jargon, acronyms, or ticket numbers.
- [ ] The three versions state the same facts and the same status color — no version softens the truth.

## Tips
- **Bury nothing.** If there's bad news, it goes near the top with the mitigation, not in a footnote. Stakeholders forgive problems; they don't forgive being surprised.
- **Lead with the ask if there is one.** If you need a decision, make that the reason the email exists — don't make the reader earn it.
- **One status color, not hedged.** "Mostly on track but a bit at risk" reads as 🔴 with extra steps. Pick the color that's true and own it; use the risk line to add nuance.
- **Recurring updates: keep a stable shape.** Readers learn where to look. Same sections, same order, every week — only the content changes.
- **Cut activity that doesn't change the outcome.** If shipping it didn't move the goal or the date, it probably doesn't belong in an exec update.
- **Multiple same-color risks?** Order them by severity, set the program status color to the worst single risk (not an average), and name that lead risk in the headline. Three 🟡s don't make a 🔴 — but they also shouldn't hide the one that actually threatens the date.
- **Asks are audience-scoped.** Internal or financial asks (headcount, budget, legal sign-off, cross-team unblock) appear only in the exec and engineering versions — never in the customer version. A customer update has no internal ask in it.
- **Internal codenames in customer-facing copy.** Strip internal product codenames (e.g. "Blocker Detector") from the customer version unless it's the actual shipped, public-facing name. The gray zone: if the codename will become the customer-visible name, introduce it as such; if it's internal jargon, replace it with the benefit or the public feature name. When unsure, describe the capability, not the codename.
