---
name: synthesize-research
description: Synthesize user research from interviews, surveys, and feedback into structured, evidence-backed insights. Use when you have a pile of notes to make sense of and say things like "synthesize these interviews", "find themes in this feedback", "what are users telling us", "turn this research into insights", or "analyze these support tickets". Extracts themes ranked by frequency and impact, then translates them into roadmap recommendations.
---

# Synthesize Research

Raw research is a pile of quotes; synthesis is a ranked set of decisions. This skill turns interview notes, survey responses, support tickets, and reviews into a structured synthesis: themes counted by frequency and weighted by impact, insights that each cite evidence, and recommendations a team can act on. The discipline here is resisting the two failure modes of synthesis — cherry-picking the quote that confirms what you already believed, and over-generalizing from three loud users.

**Grounded in:** *Continuous Discovery Habits* — Teresa Torres: turn interview snapshots into opportunities, separating observation from interpretation.
**Go deeper (The Product Channel):** [How Do You Learn from Users](https://sidsaladi.substack.com/p/week-7-how-do-you-learn-from-users)

## When to use this
- You have a stack of interview notes, survey free-text, support tickets, app-store reviews, or sales-call transcripts and need to find the signal.
- You need themes ranked by how *often* they came up AND how *much they matter*, not just a wall of quotes.
- You're turning qualitative feedback into prioritized roadmap or backlog recommendations.
- You need to separate "what users said and did" (observations) from "what we think it means" (interpretations) before a decision.
- You want a defensible artifact stakeholders can challenge — every claim traceable to a quote.

## Before you start (gather these)
- **The raw material** — interview notes, survey responses, support tickets, reviews, transcripts. Ask the user to paste them inline or point you to the files. The more verbatim, the better; cleaned-up summaries lose the evidence.
- **The research question** — what decision this is meant to inform (e.g., "should we build X?", "why is onboarding churn high?"). Without it, synthesis drifts into a generic listicle.
- **The sample** — how many participants/responses (n), how they were recruited, and any segments (plan tier, role, tenure, new vs. power user). Segment labels make impact-weighting possible.
- If any of these are missing, ask before synthesizing — don't invent a sample size or a question.
- But if the research question AND the sample are already provided up front, proceed without asking — state any assumptions inline rather than stopping to ask theatrical clarifying questions.

## Process
1. **Read everything once, end to end, before tagging.** Resist forming conclusions on the first transcript. You're building a mental map of the territory first.
2. **Tag observations atomically.** Go back through and mark each discrete observation — a behavior, a complaint, a workaround, a request, a moment of friction or delight. Tag with a short label and keep the participant ID + a verbatim snippet attached to every tag. One observation = one taggable unit; don't merge two ideas into one tag.
3. **Cluster tags into themes.** Group related tags. A theme is a recurring pattern, not a single quote. Name themes in the users' language, not your feature names ("I can't tell if it saved" beats "needs save-state indicator").
4. **Count frequency.** For each theme, count *distinct participants* who raised it (not total mentions — one person saying it five times is still n=1). Only participants who **explicitly** raised a theme count toward its frequency; implied or partial signals (someone who skirted near it but never stated it) go in a note, not the count. Frequency is your floor, not your verdict.
5. **Weight by impact and segment.** A theme raised by 3 of your highest-value users can outrank one raised by 8 trial users who churned anyway. Note severity (blocker vs. annoyance), and which segments each theme concentrates in. Flag themes that are loud in one segment and silent in others.
6. **Separate observations from interpretations — explicitly.** "7/12 users hesitated at the pricing page" is an observation. "Pricing is confusing" is an interpretation. Keep them in different columns. Interpretations are hypotheses; label them as such.
7. **Pull one strong verbatim quote per theme** as evidence. Pick the quote that best captures the pattern, not the most extreme one. Attribute it (segment, not name).
8. **Rank insights** by frequency × impact, adjusted for confidence (how strong is the evidence, how big is n). Order with this heuristic: a **Blocker** outranks a **High** regardless of frequency when it's concentrated in a key segment; within the same severity tier, order by participant count (more participants first); then demote anything low-confidence (thin n, weak evidence) below higher-confidence peers in the same tier. State the small-sample caveat out loud wherever n is thin — "directional, n=4" is honest; presenting it as fact is not.
9. **Translate to recommendations.** Each recommendation ties back to a named theme and says what to do, not just what's wrong. Distinguish "ship this" from "investigate further."

Throughout: actively look for **disconfirming evidence**. Before you lock a theme, ask "who said the opposite?" Note contradictions rather than smoothing them over — they're often the most interesting finding.

## Output template
Produce a copy-pasteable **Research Synthesis**:

```
# Research Synthesis: [topic]

**Research question:** [the decision this informs]

**Method & sample:** [interviews/survey/tickets] · n=[X] · [recruitment] · Segments: [e.g., 5 power users, 4 new, 3 churned]

## Top themes
Surface the top 4–6 themes here; fold the rest into the residual line below.

| Theme | Frequency | Impact | Representative quote |
|-------|-----------|--------|----------------------|
| [user-language name] | [X/n participants] | [Blocker/High/Med/Low + segment] | "[verbatim]" — [segment] |

**Also raised (residual):** [one-line list of remaining lower-frequency/lower-impact themes]

## Key insights
1. **[Insight]**
   - Observation: [what users said/did, factual — counts, behaviors, verbatim signals]
   - Interpretation (hypothesis): [what we think it means — labeled as a hypothesis, not fact]
   - Evidence: [themes/quotes/counts it rests on]
   - So what: [why it matters for the decision]
   - Confidence: [High / Directional, n=X]

## Surprises & contradictions
- [Something that defied expectations, or where users disagreed with each other]

## Recommendations (ranked)
1. **[Action]** — addresses [theme]. [Ship now / investigate]. [rationale]

## Open questions / research next
- [What this round couldn't answer + how to find out]

## Tag log / evidence appendix (optional)
The raw tag trail — what makes the synthesis defensible. One row per tagged observation so any theme can be drilled back to source.

| Theme | Participant | Verbatim quote |
|-------|-------------|----------------|
| [theme name] | [participant ID / segment] | "[verbatim]" |
```

## Quality bar
- [ ] Every insight cites specific evidence (a count, a theme, a quote) — no unsupported assertions.
- [ ] Every theme has BOTH a frequency count AND an impact assessment — neither alone.
- [ ] Frequency counts distinct participants, not total mentions.
- [ ] Small-sample caveats are stated explicitly wherever n is thin; nothing directional is dressed up as conclusive.
- [ ] Observations and interpretations are visibly separated, never blurred.
- [ ] At least one contradiction or surprise is surfaced (or it's stated that none was found).
- [ ] Themes are named in users' language; quotes are verbatim and attributed to a segment.
- [ ] Every recommendation ties back to a named theme.

## Tips
- **Count before you conclude.** Form the theme list from the tags, not from the two interviews that stuck in your memory — recency and vividness are not frequency.
- **One strong quote per theme beats five weak ones.** Evidence is about representativeness, not volume.
- **Watch confirmation bias actively.** The quote that confirms your roadmap is the one to scrutinize hardest. Deliberately hunt for the user who disagrees.
- **n matters, and so does who's in it.** Eight trial users and eight enterprise admins tell you different things. Always read frequency through the lens of segment.
- **A loud minority isn't a trend.** Three intense complaints can be a real blocker for a key segment *or* an unrepresentative edge case — impact-weighting and segment data tell you which.
- **Keep the raw tags.** When a stakeholder challenges a theme, being able to drill from insight → theme → tagged quote → participant is what makes the synthesis defensible.
