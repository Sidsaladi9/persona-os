---
name: personas
description: Create evidence-based user personas — or honest proto-personas when data is thin. Use when someone says "create a persona", "build user personas", "proto-persona for X", "who are our users", or "turn this research into personas". Focuses on goals, jobs-to-be-done, pains, and real behavior, then shows how to use personas to make product decisions.
---

# Personas

A persona is a decision tool, not a character study. Done well, it compresses what you know about a real segment of users into the few attributes that change what you build. Done badly, it's a stock photo with an invented name and a coffee habit that nobody ever opens again. This skill helps you build the first kind: grounded in evidence where you have it, and honestly labeled as a hypothesis where you don't.

The test for every line in a persona: **does this change a product decision?** If it doesn't, cut it.

## When to use this
- You have research (interviews, support tickets, analytics, sales calls) and need to turn it into something the team can act on.
- You keep saying "the user" in meetings and realize different people mean different users.
- You're prioritizing and need a shared, concrete picture of who you're building for.
- You're entering a new space with little data and want an explicit set of assumptions to validate — not a guess dressed up as fact.

## Evidence-based vs proto-persona
Be explicit about which one you're making. Mixing them silently is how fiction gets treated as fact.

- **Evidence-based persona** — built from actual research: interviews, behavioral data, support volume, win/loss notes. Every claim traces to a source. Cite the evidence inline so anyone can challenge it.
- **Proto-persona** — a hypothesis you build when you lack data. Legitimate and useful for aligning a team early — *as long as you label it.* Mark every assumption and state how you'll validate it. A clearly-labeled proto-persona beats both analysis paralysis and a fake "real" persona.

When in doubt, you probably have a proto-persona. Don't promote it until the evidence arrives.

## Before you start (gather these)
- **Research and data, if any** — interview notes, survey results, support tickets, session recordings, analytics segments, sales/CS call notes. List what you actually have.
- **Product context** — what you build, the problem it solves, where it sits in the user's day.
- **How many segments you're seeing** — a rough count of distinct behavior patterns in the data (not job titles).
- **No data?** Say so out loud, build a proto-persona, and write down what you'd need to observe to confirm it.

## Process
1. **Cluster by behavior and needs, not demographics.** Group users by what they're trying to accomplish, how they currently do it, and what blocks them. Two people with the same job title can be different personas; two with different titles can be the same one.
2. **Find the distinct segments.** Look for clusters where the *product decision would differ* — different goals, different triggers, different workarounds. If two clusters would lead you to build the same thing, merge them.
3. **For each segment, capture:** goals, jobs-to-be-done ("when I ___, I want to ___, so I can ___"), pains and frustrations, context and triggers (what's happening when they reach for a solution), current behavior and workarounds (what they do today, including the spreadsheet/hack/competitor), and what success looks like.
4. **Keep only decision-changing attributes.** For every attribute, ask "if this were different, would we build differently?" If no, delete it. This is the step that separates a useful persona from fluff.
5. **Mark every assumption.** Tag anything not backed by evidence as `[ASSUMPTION]` with a validation plan. Tag backed claims with their source.
6. **Limit to 2–4 personas.** More than that and the team can't hold them in their head, so none of them get used. This cap counts personas only — anti-personas are excluded from the 2–4 count.

## Output template
Copy-paste one block per persona.

```
### [Name] — [one-line descriptor of role + defining behavior] [PROTO-PERSONA: optional — add this marker if assumptions outnumber sourced lines]

**Goals**
- [What they're ultimately trying to achieve]

**Jobs-to-be-done**
- When [situation], I want to [motivation], so I can [outcome].

**Pains / frustrations**
- [What's hard, slow, or broken today]

**Context & triggers**
- [What's happening in their world when they reach for a solution]

**Current behavior / workarounds**
- [What they do today — the tool, hack, spreadsheet, or competitor they use now]

**How this changes what we build**
- [The concrete product implication — a feature we prioritize, a flow we simplify, a thing we deliberately don't build]

**Evidence**
- [Source: "12 of 18 interviews said…", "support tag X = 30% of volume", "analytics: 60% drop off at step 3"]
- [ASSUMPTION — validate by: e.g. 5 interviews with segment, funnel analysis, survey question]

### Anti-persona: [Name] — who we are explicitly NOT building for, and why optimizing for them would hurt a real persona
- [Optional. The segment whose needs you'll deliberately decline to serve, and the real persona that would suffer if you tried to serve both.]
```

To decide whether to label the whole thing a **proto-persona**, count every `[ASSUMPTION]` tag *anywhere* in the block (including inline ones in Goals, Jobs-to-be-done, behavior, and triggers bullets — not just the Evidence section) against every sourced/Evidence line. If the `[ASSUMPTION]` tags outnumber the sourced lines, mark it a proto-persona using the `[PROTO-PERSONA: …]` marker on the header line at the top.

## Avoid (anti-patterns)
- **Demographic fluff.** Age, "loves coffee," favorite TV show, a smiling stock photo — unless it genuinely changes a decision (rare), it's noise that makes the persona feel real while teaching you nothing.
- **Invented personas with no evidence, presented as fact.** If you made it up, it's a proto-persona. Label it. Pretending otherwise launders a guess into a "finding."
- **Too many personas.** Five-plus personas means focus dies and the team builds for everyone (i.e., no one). 2–4 max in almost every case.
- **Shelf-ware personas.** A persona that lives in a deck and never gets referenced in a prioritization call, spec, or design review was a waste of time. If it doesn't inform a decision, it doesn't exist.
- **Persona theater.** Don't manufacture distinct personas to look thorough. If two segments lead to the same build, they're one persona.

## Tips
- Name personas by behavior so they're memorable: "Firefighting Felix" beats "User B." A good name encodes the defining trait.
- Quote real user language verbatim where you can — it's more persuasive than your paraphrase and harder to argue with.
- Pair each persona with one anti-persona (who you're explicitly *not* building for). It sharpens scope as much as the personas do.
- Treat personas as living docs. Re-validate when the product, market, or data shifts; retire ones that no longer drive decisions.
- The fastest way to test a persona: bring it into the next prioritization meeting and see if it actually settles a debate. If it can't, it's not done.
