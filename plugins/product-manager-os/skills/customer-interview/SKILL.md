---
name: customer-interview
description: Plans and scripts customer discovery interviews using The Mom Test. Use when a user wants to plan a customer interview, write discovery interview questions, build an interview script, generate Mom Test questions, or talk to users about a problem. Produces a non-leading question script grounded in past behavior, plus a note-taking template.
---

# Customer Interview

Most interviews fail before they start: the interviewer pitches their idea, asks people to predict the future, and walks away with polite lies that feel like validation. The Mom Test (Rob Fitzpatrick) fixes this — talk about the customer's life and what they've actually done, not your idea or what they think they'd do. This skill plans a discovery interview and writes a script that can't be answered with empty compliments. It's the BEFORE; once you've run the interviews, use the `synthesize-research` skill to analyze what you heard.

## When to use this
- You're about to talk to users and want a plan + question script, not just a vibe
- You're testing a risky assumption (is this problem real? painful enough? who has it?)
- You keep getting "yeah I'd totally use that" and want truth instead of flattery
- You're doing problem discovery, not a demo or a sales call

## The Mom Test rules (the spine of a good interview)
- **Talk about THEIR life and past behavior, not your idea.** Their world is fact; your idea is a hypothetical they'll be nice about.
- **Ask about specifics in the past, not generics or the future.** "Tell me about the last time…" beats "Do you usually…" beats "Would you…".
- **Talk less, listen more.** Aim for them talking ~80% of the time. Silence is a tool — let them fill it.
- **Dig:** "tell me about the last time that happened" · "what did you do about it?" · "how much does it cost you today (time/money/sanity)?" · "what have you already tried?" · "why is that hard?"

## Retention / churn / win-back interviews (invert the frame)
The standard problem-story frame assumes the pain is external to your product — you're hunting for a problem worth solving. For retention, churn, and win-back interviews the product is already in the story, so **invert it**: anchor on the last time they actually USED the product and the specific moment or week engagement trailed off, not on a generic problem.
- **Start from real usage, not the problem.** "Walk me through the last time you used <product>" → "When was the last time before that?" Find the moment the rhythm broke.
- **Pinpoint the drop-off.** "Which week did you stop reaching for it, and what changed that week?" Dated specifics beat "I just got busy."
- **Find who disengaged first.** In a team or household, one person usually drifts first — "who stopped using it before you did?" surfaces the real failure mode.
- **Ask what filled the gap.** "What do you do now instead?" The replacement (a competitor, a spreadsheet, nothing) tells you what job you stopped doing well.
- **Stay out of pitch mode.** It's tempting to defend or re-sell the product when they describe leaving it. Don't — the goal is the honest story of why it stopped earning their time, not a save attempt.

## Before you start (gather these)
- **Who** you're interviewing and which segment they represent (role, context, why them)
- **The riskiest assumption** you're trying to kill — the one belief that, if wrong, sinks the idea
- **The learning goal**: the single most important thing you must learn from this conversation
- **Logistics**: length (20–40 min is plenty), recording consent, who takes notes

If any of these are unclear, ask the user before generating the script — a script with no learning goal produces unfocused interviews.

## Process
1. **Define the learning goal + riskiest assumption.** Write one sentence: "I believe [X], and if it's false, [consequence]." That's what the interview must test.
2. **Write past-behavior questions mapped to it.** For each assumption, draft questions that surface real, dated behavior ("the last time…", "walk me through how you…"). Every question should trace back to the learning goal — cut the rest. **Budget the time:** cap the script to the handful of questions that map to the riskiest assumption, and treat the probe follow-ups as optional depth you reach for when an answer is rich — not a checklist to grind through. That keeps a session to ~30 min and leaves room for them to talk.
3. **Sequence the conversation:** warm-up (rapport, context on their role) → context (how their day/workflow actually works) → problem story (the last time the pain hit) → current workarounds (what they do today, what they've already tried, what they've paid for) → wrap (anyone else I should talk to? anything I should've asked?).
4. **Prep follow-up probes.** For each main question, stage 2–3 digging probes so you can go deeper on the spot instead of moving on too soon.
5. **Set up note capture.** Have the note template open so you log verbatim quotes and signals live, not from memory afterward.

## Output template
Produce three copy-pasteable blocks.

**1. Interview plan**
```
LEARNING GOAL: <the one thing this interview must teach you>
RISKIEST ASSUMPTION: I believe <X>; if false, <consequence>.
SEGMENT: <segment this plan targets> — chosen because <why this segment>
WHO (repeat per interviewee; same plan reused across the segment):
  - <name/role> — <any context specific to this person>
  - <name/role> — …
LOGISTICS: <length> · recording consent? <y/n> · notetaker: <who>
SUCCESS LOOKS LIKE: <what a useful interview surfaces>
```

**2. Question script** (grouped, non-leading, with probe follow-ups)
```
WARM-UP
- Tell me a bit about your role and what a typical week looks like.

CONTEXT
- Walk me through how you currently handle <relevant task/area>.
  ↳ probe: What tools or people are involved? Where does it break down?

PROBLEM STORY
- Tell me about the last time <problem area> came up.
  ↳ probe: What did you do about it? How long did it take?
  ↳ probe: How much did that cost you — in time, money, or stress?
  ↳ probe: When did you first notice this was a problem?
  ⤿ RETENTION / CHURN VARIANT — swap this whole block for the inverted frame:
    - Walk me through the last time you actually used <product>.
      ↳ probe: When was the time before that? (find where the cadence thinned)
      ↳ probe: Which week did it stop being part of your routine — what changed that week?
      ↳ probe: Who stopped first, and what filled the gap?

CURRENT WORKAROUNDS
- What have you already tried to fix this?
  ↳ probe: Why did/didn't that work? Have you paid for anything to solve it?
  ↳ probe: What do you do today when it happens?

WRAP
- What's the hardest part of this for you, and why?
- Who else deals with this that I should talk to?
- Is there anything I should have asked but didn't?
```

**3. Note template**
```
| Quote (verbatim) | Observation | Pain (1–5) | Workaround | Surprise |
|------------------|-------------|-----------|------------|----------|
|                  |             |           |            |          |
```

After the interviews, hand the filled-in notes to the `synthesize-research` skill to cluster themes, rank findings by frequency and impact, and turn them into recommendations.

## Avoid (anti-patterns)
- **Leading questions / pitching your solution** — "Don't you hate when…?" or "Would this feature help?" plants the answer.
- **Hypothetical "would you use…" questions** — people are terrible at predicting their own future behavior; ask what they did, not what they'd do.
- **Asking for opinions instead of past behavior** — "Do you think this is a good idea?" gets you flattery, not facts.
- **Fishing for compliments** — if you leave feeling great, you probably learned nothing. Useful interviews surface friction, not praise.

## Tips
- Bad data is worse than no data — a false "yes" sends you building the wrong thing.
- Anchor every claim to a specific moment: "when exactly?" turns a generic into evidence.
- Watch for emotion and curse words — that's where the real pain lives.
- If they say a problem matters, ask what they've spent (time/money) on it. Commitment > compliments.
- Embrace awkward silence after a question; the second thing they say is usually the honest one.
- Take notes in their words, not your paraphrase — verbatim quotes are gold in synthesis.
