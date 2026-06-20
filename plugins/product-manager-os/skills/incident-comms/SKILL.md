---
name: incident-comms
description: Drafts the communications a PM owns when something is breaking or just broke — an internal escalation note, customer-facing status updates on the right cadence, a resolution/all-clear, and a short blameless postmortem for leadership. Use when you say "we have an incident", "the launch broke", "draft a customer notice", "status page update", "outage comms", "customers are hitting errors", "we're down", or "write the postmortem". Reactive comms only — not pre-mortem (failure before launch), release-notes (what shipped), or stakeholder-update (routine status).
---

# Incident Comms

When something is breaking or just broke, the comms *are* the product. This skill drafts the words a PM owns during an incident — grounded in the discipline behind Google's SRE incident response and Atlassian's incident handbook: a single comms owner, a predictable update cadence, say only what you know, and stay blameless. It produces four artifacts on demand — an internal escalation note, customer-facing status updates, a resolution/all-clear, and a leadership postmortem — not an engineering root-cause analysis.

**Grounded in:** *Site Reliability Engineering* — Beyer et al. (Google) + Atlassian's Incident Handbook: single incident commander, designated comms lead, fixed status cadence, blameless postmortem.
**Go deeper (The Product Channel):** [The Beginner's Guide to a Product Launch](https://sidsaladi.substack.com/p/the-beginners-guide-to-a-product)

> **Not this skill:** *pre-mortem* (imagine failure *before* you ship), *release-notes* (announce what shipped, on a good day), *stakeholder-update* (routine status when nothing is on fire). This skill is **reactive** — use it only when something is going wrong or just went wrong.

## When to use this
- Production is degraded or down, a launch broke, or customers are hitting errors, and you need words out *now*.
- You need a customer-facing status-page or in-app notice that's honest without over-promising a fix time.
- Leadership is asking "what's going on?" mid-incident and you need one escalation note that aligns everyone.
- The incident is resolved and you owe customers an all-clear and leadership a blameless postmortem.
- A vendor/dependency outage is hitting your users and you have to communicate something you don't fully control.

## Before you start (gather these)
- **What's broken, for whom** — the user-visible symptom (not the stack trace), and which segment/feature/region is affected.
- **Severity & scope** — how many users, is it total or partial, is data or money at risk. (SEV1 = broad/critical, SEV2 = significant, SEV3 = minor/contained.)
- **Timeline so far** — when it started, when you detected it, what's happened since (in UTC or one stated zone).
- **Current status** — investigating / identified / mitigating / monitoring / resolved, and the *next* concrete step.
- **Owners** — who is the incident commander (decides), who is the comms owner (you, usually), who is the customer audience.
- **Constraints** — is there a known ETA (rarely — don't invent one), a workaround, contractual/SLA or security/privacy implications.

If two or more of these are missing or vague, **ASK 2-4 sharp questions before drafting** — e.g., "What does the user actually see — error, slowness, wrong data, or nothing loading?", "Roughly what share of users, and is anyone's data at risk?", "When did it start and when did we detect it?", "Where are we now — still investigating, or do we have a fix deploying?" If you have enough to write something true, proceed and state your assumptions inline. **Never invent an ETA, a root cause, or a customer count to fill a gap** — "we don't yet know X" is a valid, trust-preserving line.

## Process
1. **Set severity and the comms cadence first.** Severity drives how often you update and who you wake up. Lock a cadence and *commit to it in the first message*: SEV1 → every 30 min, SEV2 → every 60 min, SEV3 → at status changes. The next update time is a promise — meeting it, even with "no change," is what builds trust.
2. **Name the single comms owner.** One person speaks publicly (you). The incident commander runs the response; you translate it outward. Don't let five people post five versions.
3. **Write the internal escalation note before anything customer-facing.** Leadership and support need the full picture (scope, impact, who's on it, the ask) so they stop pinging the responders. Internal can be blunt; customer-facing must be careful.
4. **Draft the customer update at the right altitude — say what you know.** State impact in user terms, what you're doing, and when the next update lands. Acknowledge → impact → action → next-update-time. Omit internal hostnames, blame, speculation, and any ETA you can't stand behind.
5. **Match honesty to the audience, not to your discomfort.** Customers don't need the cause; they need to know you see it, you're on it, and when they'll hear from you again. Under-claim on the fix, over-deliver on the cadence.
6. **Keep updating on cadence until resolved — even "still investigating" is an update.** Silence reads as "they don't know it's broken" or "they've given up." A boring on-time update beats a detailed late one.
7. **Send the resolution / all-clear when it's actually fixed** — confirmed by monitoring, not hope. State what's restored, residual effects (e.g., delayed data catching up), any user action needed, and a brief, sincere apology proportional to the impact. Promise the postmortem if SEV1/2.
8. **Write the blameless postmortem for PM/leadership, not eng.** Lead with customer impact and the one-line cause in plain language. Frame the timeline and prevention as system/process fixes, never "Marcus deployed the bad config." Owners and dates on every action item, or it's theater. This is a leadership decision document, not the engineering RCA — point to that doc, don't reproduce it.

## Output template
Pick the artifact(s) you need. Each numbered block is independently copy-pasteable. Fill in every `[bracket]`. Use one consistent timezone and label it.

```markdown
# Incident: [short name] — [SEV1 / SEV2 / SEV3]
**Comms owner:** [you] · **Incident commander:** [name] · **Status:** [Investigating / Identified / Mitigating / Monitoring / Resolved]
**Started:** [time TZ] · **Detected:** [time TZ] · **Next update:** [time TZ]

---

## 1. Internal escalation note (Slack / email to leadership + support)
**🔴 [SEV_] [Product/feature] [is down / is degraded] — [one-line symptom]**
- **Impact:** [who/what is affected — segment, %, surface]. [Is data/revenue/SLA at risk? y/n + detail.]
- **Started / detected:** [time] / [time TZ]. **Duration so far:** [Xm].
- **Status:** [Investigating / Identified / Mitigating / Monitoring]. **Current theory:** [what we suspect — label as unconfirmed].
- **What we're doing:** [the active step].
- **On it:** IC [name] · Eng [name(s)] · Comms [you].
- **For support — holding line, read verbatim:** "[one self-contained sentence support can paste to any inbound — what's affected, that data is safe if true, and when we'll next update]." Do not speculate on cause or ETA.
- **Ask of leadership:** [decision needed, or "none — informational, next update [time]"].

## 2. Customer-facing status update (status page / in-app banner / email)
> Post the first one fast; repeat on cadence until resolved. No internal names, no cause speculation, no ETA you can't keep.

**[Investigating] [Product] — [plain-language symptom]**
[Timestamp TZ] — We're aware that [what users are experiencing, in their words]. [Who/what is affected, if it's a subset.] Our team is actively investigating. We'll post another update by **[next update time TZ]**.

<!-- Follow-ups reuse this shape, status tag changes: -->
**[Identified]** [time TZ] — We've identified the cause and are working on a fix. [Affected functionality] may still be [symptom]. Next update by **[time TZ]**.
**[Monitoring]** [time TZ] — A fix is deployed and [functionality] is recovering. We're monitoring to confirm full recovery. Next update by **[time TZ]**.

## 3. Resolution / all-clear
**[Resolved] [Product] — service restored**
[time TZ] — This is resolved. [What was affected] is fully operational as of **[time TZ]**, after [duration] of impact. [Residual note, e.g., "Delayed [data] is backfilling and will be current within [X]."] [Any user action needed, or "No action needed on your part."]
We're sorry for the disruption[ and for any [specific cost to them, e.g., missed digests]]. [For SEV1/2: A full postmortem will follow by [date].]

## 4. Blameless postmortem (for PM / leadership)
**Incident:** [name] · **Severity:** [SEV_] · **Duration:** [start–end TZ, total Xh Ym] · **Author:** [you] · **Date:** [date]

**TL;DR:** [1-2 sentences: what broke, who it hit, how long, and that it's resolved. A reader who stops here knows the impact.]

**Customer impact**
- **Who:** [segment / count / %]. **What they experienced:** [symptom]. **Business impact:** [SLA credits, churn risk, revenue, support volume — quantify if you can].

**Timeline** (all [TZ])
| Time | Event |
|------|-------|
| [t0] | [trigger — e.g., "Config change deployed"] |
| [t1] | [first user impact] |
| [t2] | [detected — by alert or customer report? note which] |
| [t3] | [mitigated] |
| [t4] | [resolved] |

**Root cause (plain language):** [the *system/process* reason, one or two sentences — no individual named]. [Point to the eng RCA for technical depth.]

**What went well / what hurt**
- ✅ [e.g., "Alert fired in 4 min."]  ⚠️ [e.g., "No customer-facing status update for the first 40 min."]

**Prevention — action items**
| Action | Type (Detect / Prevent / Mitigate) | Owner | Due |
|--------|-----------------------------------|-------|-----|
| [specific change] | Prevent | [name] | [date] |
| [specific change] | Detect | [name] | [date] |
```

## Avoid (anti-patterns)
- **Inventing an ETA to calm people down.** "Fixed within the hour" that slips destroys more trust than the outage. Promise the *next update time*, never the fix time, unless eng has truly committed.
- **Going silent between updates.** A missed cadence reads as "they've lost control." Ship the on-time update even when it's "still investigating, next update [time]."
- **Naming a person or guessing the cause in customer comms.** "A bad deploy by [name]" or an unconfirmed theory in public is a credibility (and HR) grenade. Cause talk is blameless, internal, and confirmed-only.
- **Copy-pasting the internal note to customers.** Internal carries scope %, theories, and hostnames; customers get impact + action + next update. One leak of an internal note becomes a tweet.
- **A postmortem with no owners or dates.** "We should add monitoring" with nobody on the hook is a wish. Every action item gets a name and a date or it didn't happen.
- **Apologizing before you've resolved it.** A grand apology mid-incident reads as panic; the apology belongs in the all-clear, sized to the actual impact.
- **Declaring "resolved" on hope, not monitoring.** An all-clear that bounces back into a second incident burns trust twice — confirm recovery on the dashboard before you post it.

## Quality bar
Before delivering, verify every box:
- [ ] Severity is set, and the matching cadence (SEV1→30m / SEV2→60m / SEV3→status-change) is committed *in the first message*.
- [ ] Every customer-facing message ends with a concrete **next-update time** — never a fix time you can't stand behind.
- [ ] The internal note and the customer note are genuinely different: no scope %, theory, hostname, or person's name leaked into anything customer-facing.
- [ ] No invented ETA, root cause, or customer count anywhere — gaps are stated as "we don't yet know X."
- [ ] The support holding line is self-contained and verbatim-safe (a support rep could paste it without asking you a question).
- [ ] The all-clear is sent only after monitoring confirms recovery, and includes residual effects + any user action.
- [ ] The postmortem leads with a TL;DR a leader can stop reading after, and states impact in customer/business terms.
- [ ] The postmortem root cause names a system/process, not a person — and points to the eng RCA rather than reproducing it.
- [ ] Every prevention action item has an owner and a due date.
- [ ] One consistent, labeled timezone across all artifacts.

## Tips
- **First message in 5 minutes beats a perfect one in 30.** "We're aware and investigating, update by [time]" is enough — acknowledgement is the product early on.
- **Severity sets cadence, cadence sets trust.** Decide SEV first; everything (update frequency, who you wake up, customer tone) falls out of it.
- **Write the next-update timestamp into every message.** It converts "are they even looking?" anxiety into a wait with a deadline — and forces you to actually post.
- **Separate the comms owner from the incident commander.** The person fixing it should not be the person tweeting; split the roles even on a small team so neither job starves.
