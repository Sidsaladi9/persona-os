---
name: feedback-analysis
description: Turns a large volume of customer feedback (support tickets, app-store reviews, NPS verbatims, survey free-text) into ranked themes with sentiment, volume, and trend-over-time. Use when you have hundreds or thousands of comments and need to know "what are people complaining about," "what changed since last quarter," or "which theme should we fix first." The quant/at-scale complement to interview-depth synthesis.
---

# Feedback Analysis

At-scale feedback theming using the theme + sentiment + trend framework: cluster raw verbatims into recurring themes, score each theme's sentiment and volume, track how each moves over time, then rank by priority so the roadmap reflects what the data actually says — not the loudest anecdote. Use this for volume; use synthesize-research for the depth of a handful of interviews.

**Grounded in:** *Continuous Discovery Habits* — Teresa Torres: theme at scale and weight by frequency and impact, not loudness.
**Go deeper (The Product Channel):** [How Do You Learn from Users](https://sidsaladi.substack.com/p/how-do-you-learn-from-users-to-build)

## When to use this
- You exported 800 support tickets / app reviews / NPS comments and need themes, not a wall of text.
- Leadership asks "what are the top 5 things customers are unhappy about, and is it getting better or worse?"
- You want to compare this quarter's feedback to last quarter and surface what's rising or fading.
- You need to rank issues by a defensible signal (volume × sentiment × trend), not by who shouted loudest in Slack.
- You're triaging a spike — a bad release, a pricing change, a viral complaint — and need to size it fast.

## Before you start (gather these)
- **The raw feedback** — pasted text, CSV, or a connector pull (Intercom/Zendesk/App Store/Typeform/Delighted). One comment per row is ideal. If a connector is available, you may pull from it; otherwise work entirely from pasted data.
- **A timestamp per comment** — required for trend. Without dates you can theme + sentiment but must skip the trend dimension and say so.
- **Source/segment fields if available** — channel, plan tier, NPS score, platform, version. These let you slice themes.
- **The decision this feeds** — roadmap prioritization, a launch retro, a churn investigation. Shapes how you rank.

If 2+ of these are missing or vague, ASK 2–4 sharp questions before analyzing: *What's the date range and is each comment dated? Which channels is this from? What decision will this inform? Roughly how many comments?* If the data is already pasted and dated, proceed and state assumptions inline (e.g., "treating NPS ≤6 as detractors; binning by week since dates span 11 weeks").

## Process
1. **Profile the corpus first.** Count comments, date range, channels, and segments. Flag dupes, bot/auto-replies, and non-English entries. State N and any data you're excluding — never silently drop rows.
2. **Build a theme taxonomy bottom-up.** Read a representative sample, draft 6–12 mutually-distinct themes (e.g., "Onboarding friction," "Pricing/value," "Mobile bugs," "Missing integration X"). Keep themes about the *problem*, not the feature. One catch-all "Other" is fine; if it exceeds ~15%, your taxonomy is too coarse — split it.
3. **Tag every comment.** Assign each to its primary theme (a comment may carry a secondary tag). Be consistent — same language, same theme. Tally volume per theme as a count *and* a % of total.
4. **Score sentiment per comment** on a 3-point scale (positive / neutral / negative). For NPS, anchor to the score (0–6 detractor, 7–8 passive, 9–10 promoter) and use the verbatim to explain *why*. Roll up to a **net sentiment per theme = %positive − %negative**, expressed on a −100..+100 scale (e.g., a theme that's 10% positive / 70% negative / 20% neutral scores −60). Report the raw positive/neutral/negative split alongside the net number so the rollup is auditable.
5. **Compute trend.** Bin by week or month. **Size your bins so each holds ~20+ comments** — that's roughly the floor at which a period's share is stable enough to compare. If weekly bins fall below ~20 comments, collapse into fewer, larger periods (fortnights, months, or just "first half vs. second half") and **say so explicitly** in the caveats. For each theme, compare its share and sentiment in the most recent period vs. the prior one. Label each ↑ rising / → flat / ↓ falling, with the delta.
6. **Rank by priority.** Score each theme on three factors, then combine:
   - **Severity** (sentiment-driven, 1–3): 3 = net sentiment ≤ −50 (sharply negative); 2 = net −20 to −49; 1 = net > −20 (mild/mixed/positive).
   - **Trend** (−1 / 0 / +1): +1 = rising (share or negativity climbing vs. prior period); 0 = flat; −1 = improving/falling.
   - **Volume** = the theme's % of total comments.
   - **Priority score = severity × volume%, then bump up one band if trend = +1, down one band if trend = −1.** Bands: P0 (act now), P1, P2, P3.
   - *Worked example:* "Mobile crashes" is 22% of volume (volume% = 22), net sentiment −68 → severity 3, and its share rose +6pp vs. last period → trend +1. Base = 3 × 22 = 66 (a high score), and the rising trend bumps it up a band → **P0**. Contrast: a 22%-volume theme at net −68 but *improving* (trend −1) would compute the same base but drop a band to P1 — already being handled.
   A high-volume, sharply-negative, *rising* theme is P0. A high-volume but *improving* theme may already be handled. Surface the top 5 with a one-line "so what."
7. **Pull representative quotes.** 1–2 verbatim quotes per top theme — the ones that capture the pattern, not the most extreme. Quotes make themes credible and unblock decisions.
8. **Recommend actions.** For each top theme: the likely root cause, who owns it, and the next step. Separate "fix now" from "watch."

## Output template

```markdown
# Feedback Analysis — [Product/Area]
**Range:** [start] → [end] · **N:** [count] comments · **Sources:** [channels] · **Prepared:** [date]

## TL;DR
- **#1 issue:** [theme] — [X]% of volume, [net sentiment], **[↑/→/↓ trend]**. [One-line so-what.]
- **Biggest mover:** [theme] [↑/↓ Δ] vs. prior period — [why it matters].
- **Quietly improving:** [theme] [↓ Δ] — [likely cause, e.g., "v2.3 onboarding fix landing"].
- **Recommendation:** [the single most important action.]

## Theme ranking
| # | Theme | Volume | % of total | Net sentiment | Trend (vs. prior) | Priority |
|---|-------|-------:|-----------:|---------------|-------------------|:--------:|
| 1 | [theme] | [n] | [%] | [😠 −X / 😐 / 🙂 +X] | [↑ +Xpp] | **P0** |
| 2 | [theme] | [n] | [%] | [...] | [→ flat] | P1 |
| 3 | [theme] | [n] | [%] | [...] | [↓ −Xpp] | P2 |
| 4 | [theme] | [n] | [%] | [...] | [...] | P2 |
| 5 | [theme] | [n] | [%] | [...] | [...] | P3 |
| — | Other | [n] | [%] | — | — | — |

*Priority = volume × sentiment severity × trend. Rising + negative + high-volume → P0.*

## Trend over time
| Theme | [Period 1] | [Period 2] | [Period 3] | Direction |
|-------|-----------:|-----------:|-----------:|-----------|
| [theme] | [%] | [%] | [%] | [↑/→/↓] |
| [theme] | [%] | [%] | [%] | [↑/→/↓] |

[Optional ASCII sparkline or note on inflection points, e.g., "spike in week of [date] aligns with [release/incident]."]

> **Launch-driven themes:** when a theme is triggered by a dated event (a release, pricing change, outage), compute its share **within the post-event period**, not across the whole corpus — and label the inflection. A theme that's only 8% of all-time volume can be 35% of comments *since the launch*; the whole-corpus number understates the spike. State both: "Theme X = 8% of corpus, but **35% of post-[event] comments** (inflection at [date])."

## Sentiment summary
- **Overall:** [X]% negative · [Y]% neutral · [Z]% positive [+ NPS: X promoters / Y passives / Z detractors if applicable].
- **Most negative theme:** [theme] ([net]). **Most positive:** [theme] ([net]).
- **Shift vs. prior period:** overall sentiment [improved/declined] by [Δ].

## Top themes in detail

### 1. [Theme] — P0
- **What:** [the recurring problem in one sentence.]
- **Volume / trend:** [n] comments ([%]), [↑/→/↓] [Δ] vs. prior.
- **Voice of customer:** "[representative verbatim quote]" "[second quote]"
- **Likely root cause:** [hypothesis grounded in the data.]
- **Recommendation:** [next step] · **Owner:** [team] · **When:** [now/watch].

### 2. [Theme] — P1
[same structure]

### 3. [Theme] — P2
[same structure]

## Slices worth noting
- **By segment:** [e.g., "Enterprise tier drives 70% of integration complaints despite being 20% of volume."]
- **By channel/platform:** [e.g., "Mobile bugs are 3× more frequent in App Store reviews than in support tickets."]

## Assumptions & data caveats
- [e.g., "No dates on 40 comments — excluded from trend. NPS mapping: ≤6 detractor. 'Other' at 12%."]
- **Reliability:** [coder count + subjectivity note, e.g., "Single-coder tagging at N=380 — theme assignment and sentiment are one analyst's judgment, not inter-rater-validated; treat ±1 band as noise. At low-hundreds N, a 2–3pp share shift is within margin." Note bins collapsed for size if applicable.]
```

## Avoid (anti-patterns)
- **Feature-shaped themes instead of problem-shaped ones.** "Dark mode" is a request; "Hard to use the app at night / eye strain" is the theme. Themes around problems survive; themes around solutions fragment.
- **Reporting volume without sentiment or trend.** A theme that's high-volume but *improving* is a very different decision than one that's *rising* — collapsing them hides the signal.
- **Cherry-picking the spiciest quote.** Pick verbatims that are *representative* of the cluster, not the one angry outlier that misleads the reader on severity.
- **Letting "Other" swallow the signal.** A 25% catch-all means your taxonomy failed. Re-cluster until each kept theme is distinct and "Other" is small.
- **Trending on noisy bins.** Don't call a 3-comment week a "trend." Note small-N periods and require a meaningful delta before labeling ↑/↓.

## Tips
- **Theme on a sample, then tag the full set.** Drafting the taxonomy from a ~10% read is far cheaper than re-clustering 1,000 rows twice — lock the 6–12 themes, then tag everything against them.
- **Weight by who's speaking.** A churned enterprise account and a free-tier user are not equal signal. If you have plan/revenue data, show a revenue-weighted view alongside the raw count.
- **Anchor sentiment to outcome, not tone.** A politely-worded "I'm switching to a competitor" is more negative than an all-caps minor gripe. Score impact, not volume of exclamation marks.
- **Always tie a trend spike to a date.** When a theme jumps, name the release, incident, or pricing change in that week — correlation you surface turns a chart into an action.
