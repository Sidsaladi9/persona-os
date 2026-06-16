---
name: retro
description: Facilitates a structured team retrospective using the well/wrong/confusing framework — gathering observations, tracing them to root causes instead of symptoms, and committing to 2-3 specific improvements with named owners and due dates. Use when you say "let's run a retro," "what went well and what didn't," "sprint retrospective," "post-mortem the launch," or "we keep making the same mistakes."
---

# Retro

A retrospective that actually changes behavior: collect what went **well / wrong / confusing**, dig past symptoms to **root cause**, and walk out with 2-3 owned **actions**. The point isn't to vent — it's to fix the system that produced the outcome.

**Grounded in:** *Agile Retrospectives* — Esther Derby & Diana Larsen: set the stage → gather data → generate insight → decide what to do, blamelessly.

## When to use this
- End of a sprint, cycle, or milestone and you want a repeatable retro instead of an unstructured gripe session.
- A launch, incident, or project just wrapped (good or bad) and you need a blameless post-mortem.
- The same problem keeps recurring and prior retros produced action items nobody did.
- A new or distributed team needs a lightweight, async-friendly retro format.
- You've collected raw notes/feedback from the team and need them synthesized into themes, causes, and a short action list.

## Before you start (gather these)
- **Scope & period:** what are we retro-ing (which sprint/project/incident) and over what dates?
- **Raw observations:** the team's well / wrong / confusing notes, OR the source material to derive them (Slack threads, sprint board, incident timeline, survey responses).
- **Outcomes/metrics:** what actually happened vs. what was planned — shipped vs. committed, dates, defects, key numbers.
- **Prior retro actions:** open action items from last time, so you can check follow-through.

**If raw observations ARE attached** (notes, a thread, survey responses, an incident timeline): synthesize directly. Don't interrogate — proceed to the Process and state any assumptions inline (e.g., "Assuming the 3 spillover stories are the 'wrong' signal since no per-person notes were attached"). Ask at most one scope-confirming question only if the period is genuinely ambiguous.

**If NO raw observations exist yet:** don't interrogate the user for them — offer to run a collection round. Say something like: "I don't have the team's observations yet. I can either (a) run a quick collection round — I'll give you three prompts to send the team and synthesize what comes back, or (b) work from source material if you point me at the Slack thread / sprint board / incident timeline." If they choose the collection round, supply these prompts:
- **Well:** "What went well this period that we should deliberately keep doing?"
- **Wrong:** "What hurt us — a known problem that cost us time, quality, or trust?"
- **Confusing:** "Where was ownership unclear, a process ambiguous, or something a surprise — anything that *will* bite us if left alone?"

Only fall back to clarifying questions for genuinely missing scope (which sprint/incident, committed vs. delivered, the triggering outcome, prior retro actions) — and ask those in one batch, not as an interrogation.

## Process
1. **Set scope and ground rules.** State the period and the one prime directive: blameless. We critique systems and decisions, not people. Anonymize observations if the team isn't safe being attributed.
2. **Collect into three buckets.** Sort every observation into **Well**, **Wrong**, or **Confusing**. Disambiguate the last two — they're easy to conflate:
   - **Well** — something that worked and is worth deliberately protecting (keep doing).
   - **Wrong** — a *known* problem that already hurt us: it cost time, quality, money, or trust this period. You can name the damage. (e.g., "the migration broke staging for two days.")
   - **Confusing** — *ambiguity* that hasn't fully detonated yet: unclear ownership, an undefined process, a hand-off with no definition-of-ready, a surprise nobody owned. It didn't necessarily hurt us *this* time, but it will bite. Confusing is the most undervalued bucket — it's where future failures incubate. When unsure: did it already cost us (Wrong) or is it a latent ambiguity that *could* (Confusing)?
3. **Cluster into themes.** Group related items. Five notes about "PR reviews were slow" are one theme, not five. Note frequency — recurring mentions signal systemic, not one-off, issues.
4. **Find root cause, not symptom.** For each Wrong/Confusing theme, run 3-5 Whys until you hit a cause the team can actually change (process, tooling, communication, capacity, unclear ownership). "We missed the deadline" is a symptom; "we never re-estimated after scope grew mid-sprint" is closer to root.
5. **Triage ruthlessly — score, don't argue.** You cannot fix everything; pick the top 2-3 root causes reproducibly rather than by whoever lobbies hardest. Use one of two lightweight methods:
   - **Impact × Recurrence score (default for async / when you have notes).** For each theme, rate **Impact** 1-3 (1 = mild annoyance, 2 = real cost, 3 = serious damage or repeat offender) and **Recurrence** 1-3 (1 = one-off, 2 = a few times, 3 = chronic/every period). Multiply. Sort descending; the top 2-3 are your candidates. Show the table so the ranking is auditable.
   - **Dot-voting (default for a live group).** Give each participant 3 dots; they place them on the themes they most want fixed (multiple dots on one theme allowed). Tally; the top 2-3 by dot count win. Fast, visible, and surfaces shared pain over individual hobbyhorses.
   Break ties toward the theme whose fix is most *actionable this period*. Record the scores/votes in the output so next retro can see why these three were chosen.
6. **Convert to owned actions.** Each chosen root cause gets ONE specific, verifiable action with a named owner and a due date. "Improve communication" is not an action; "Owner posts a mid-sprint scope-change check-in every Wednesday, starting next sprint" is.
7. **Check last retro's actions.** Mark each prior action Done / Partial / Dropped. Repeatedly dropped actions are themselves a root-cause signal (no follow-through mechanism) — fix that.
8. **Close the loop.** Decide where actions live (sprint board, tracker) and who reviews them at the next retro. An action not in a tracker is a wish.

## Facilitating live (when running the retro in real time)

Run it on a clock so it doesn't sprawl. A tight 60-minute retro:

| Bucket / step | Timebox | What you do |
|---|---|---|
| Set scope + ground rules | 5 min | State period and the blameless prime directive. |
| Silent write — all three buckets | 10 min | Everyone writes Well/Wrong/Confusing independently (sticky notes / shared doc), no talking yet. |
| **Well** | 5 min | Read out, cluster, celebrate briefly — don't over-dwell. |
| **Wrong** | 10 min | Read out, cluster, name the cost of each. |
| **Confusing** | 10 min | Read out, cluster; pull on every "who owned this?" thread. |
| Root cause (top themes) | 8 min | 3-5 Whys on the heaviest themes. |
| Triage (dot-vote) | 4 min | 3 dots each, tally, pick top 2-3. |
| Owned actions + last retro check | 8 min | One owner + date per chosen cause; mark prior actions Done/Partial/Dropped. |

**Elicitation prompts to keep it moving:**
- Opening each bucket: "60 seconds — write before we talk." (silent-first prevents anchoring.)
- Wrong: "What did this actually cost us — hours, a defect, a missed commitment?"
- Confusing: "Who owned this? If three of you just hesitated, that's the theme."
- Drilling a Why: "And what made *that* happen?" — repeat until you hit something the team controls.
- Stuck/quiet: "What would you warn a new teammate about before next sprint?"
- Before closing a theme: "If we changed exactly one thing here, what would it be?"

**Psychological safety — reframe blame in the moment.** When an observation names a person or team ("Engineering dropped the ball," "Maria forgot to update the ticket"), reframe it to the system gap *right then*, out loud: "Let's restate that as a system gap — sounds like the hand-off had no definition-of-ready," or "so the ticket-update step isn't built into our workflow." Record the systemic version, not the name. If the team clearly isn't safe being attributed — junior members silent, a manager in the room, a high-stakes post-mortem — **default to anonymous collection**: gather observations in writing without names (anonymous form / shuffled stickies) and facilitate from the anonymized set.

## Output template

```markdown
# Retrospective — [Sprint / Project / Incident] ([Start date]–[End date])

**Facilitator:** [Name] · **Participants:** [N people / teams] · **Prime directive:** Blameless — we fix systems, not blame people.

## Outcome snapshot
| Planned | Actual | Delta |
|---|---|---|
| [e.g., 24 pts committed] | [e.g., 18 pts delivered] | [-6 pts / 3 stories spilled] |
| [Target date / metric] | [Actual] | [Gap] |

## 1. What went well (keep doing)
- **[Theme]** ([×N mentions]) — [what specifically worked and why it's worth protecting]
- **[Theme]** — [observation]

## 2. What went wrong (hurt us)
- **[Theme]** ([×N mentions]) — [the observable problem and its impact]
- **[Theme]** — [observation]

## 3. What was confusing (unclear / surprised us)
- **[Theme]** — [where ownership, process, or expectations were ambiguous]
- **[Theme]** — [observation]

## 4. Root cause analysis (top themes only)
| Theme | Symptom (what we saw) | Root cause (3-5 Whys) | Bucket | Triage (I×R or dots) |
|---|---|---|---|---|
| [Theme] | [Surface observation] | [The changeable underlying cause] | Process / Tooling / Comms / Capacity / Ownership | [e.g., 3×3=9 / 5 dots] |
| [Theme] | [Symptom] | [Root cause] | [Category] | [score] |
| [Theme] | [Symptom] | [Root cause] | [Category] | [score] |

## 5. Actions for next period (2-3 max — owned & dated)
| # | Action (specific & verifiable) | Addresses root cause | Owner | Due | Tracked in |
|---|---|---|---|---|---|
| 1 | [Concrete, observable change] | [Theme] | [Name] | [Date] | [Board/ticket link] |
| 2 | [Action] | [Theme] | [Name] | [Date] | [Link] |
| 3 | [Action] | [Theme] | [Name] | [Date] | [Link] |

## 6. Last retro's actions — follow-through
| Prior action | Owner | Status | Note |
|---|---|---|---|
| [Action] | [Name] | Done / Partial / Dropped | [Why, if not done] |

## Decisions & parking lot
- **Decided:** [Any decision made in the room]
- **Parked (out of scope / needs separate discussion):** [Item] → [Owner to follow up]
```

## Avoid (anti-patterns)
- **Symptom-fixing.** Stopping at "we were slow" without a Why chain produces actions that treat the rash, not the infection. Push to a cause the team controls.
- **The action-item graveyard.** Generating 8 vague to-dos with no owner or date. Two owned, dated actions beat ten orphaned ones — every action needs a name and a date.
- **Skipping "confusing."** Teams happily debate wins and losses but glide past ambiguity. Unclear ownership is where the next failure is already brewing.
- **Blame leakage.** "Engineering dropped the ball" kills psychological safety and honest input. Reframe to the system: "handoffs lacked a definition-of-ready."
- **Recency bias.** Letting the last bad day dominate a two-week period. Weight by frequency and impact across the whole window, not by what stings most right now.

## Tips
- **Collect silently first, discuss second.** Have people write their well/wrong/confusing independently before the group talks — it prevents the loudest voice from anchoring everyone.
- **One action per root cause, owned by one person.** Shared ownership is no ownership. If two people must collaborate, one is still accountable.
- **Open with last retro's scorecard.** Reviewing prior follow-through first creates accountability gravity for this retro's actions.
- **Rotate the facilitator.** It spreads skill, surfaces different themes, and stops the retro from becoming one person's pet agenda.
