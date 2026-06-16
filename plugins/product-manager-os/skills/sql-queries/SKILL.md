---
name: sql-queries
description: Translates a product question into clean, correct SQL against a described schema and explains it line by line. Covers the core product-analytics patterns — funnels, retention and cohorts, DAU/MAU stickiness, and event counts — plus how to sanity-check the output. Use when you say "write me a query for", "how many users did X then Y", "what's our 7-day retention", "DAU/MAU by week", "build a funnel from signup to activation", or "is this number right?"
---

# SQL Queries

Turn a product question into trustworthy SQL using a small set of battle-tested product-analytics patterns. Most product questions reduce to one of four shapes — funnel, retention/cohort, active-user ratio, or event count — and getting the shape right matters more than clever syntax.

**Grounded in:** *Lean Analytics* — Croll & Yoskovitz: answer the product question (funnels, retention windows, DAU/MAU) — correctly, not approximately.
**Go deeper (The Product Channel):** [Product Metrics](https://sidsaladi.substack.com/p/week-5-week-in-product-series-product)

## When to use this
- A PM or analyst asks "how many users went from signup to first key action, and where do they drop off?"
- You need 1/7/30-day retention or a weekly cohort triangle and want it correct, not approximately correct.
- You want DAU, WAU, MAU, or the DAU/MAU stickiness ratio over time.
- You need to count events or unique users per feature, segment, or time bucket — and trust the number.
- A dashboard figure looks off and you want a query plus a sanity-check protocol to confirm or debunk it.

## Before you start (gather these)
- **The question, stated as a metric** — e.g. "7-day retention of users who signed up in May," not "how's retention."
- **The schema** — table names, key columns, and grain. At minimum: the events/activity table, its user-id column, its timestamp column, and how an "event type" is identified.
- **The SQL dialect** — Postgres, BigQuery, Snowflake, Redshift, MySQL, DuckDB. Date functions differ; this matters.
- **Definitions** — what counts as "active," "activated," "retained"? What's the time grain (day/week/month) and timezone?

If two or more of these are missing or vague, ASK 2–4 sharp questions before writing SQL (e.g. "Which table holds events and what's the user-id column?", "Postgres or BigQuery?", "Is retention day-N exact, or N-day-window?", "What event defines activation?"). If the schema and question are already provided, proceed and state every assumption inline as a `-- comment` in the query.

## Process
1. **Classify the shape.** Decide which of the four patterns fits: funnel, retention/cohort, active-user ratio, or event count. Say which one and why. Most questions are exactly one; some compose two.
2. **Pin the grain and the definitions.** One row per *what*? (user, user-day, cohort-week.) Write the definition of the metric in one sentence before any SQL.
3. **Anchor the population.** Define the cohort/denominator first — the set of users in scope and their anchor date (signup, first event). Retention and funnels live or die on a correct denominator.
4. **Handle time deliberately.** Truncate to the grain (`date_trunc`), be explicit about timezone (e.g. `DATE_TRUNC('day', event_time AT TIME ZONE 'America/New_York')` to bucket by account-local days instead of UTC), and use half-open intervals `[start, end)` to avoid double-counting boundary rows.
4b. **Exclude incomplete cohorts.** For any windowed/day-N metric, drop cohorts whose window hasn't fully elapsed — `WHERE cohort_start + window <= now()` (use the window END for ranges). A cohort from 3 days ago can't have day-7 retention yet; including it silently understates the number.
5. **De-dupe to the grain.** Use `COUNT(DISTINCT user_id)` for people, raw `COUNT(*)` for events — never confuse the two. Collapse multiple events per user per period before joining.
6. **Write the query with CTEs, not nesting.** One named CTE per logical step (cohort → activity → join → aggregate). Readable beats clever.
7. **Sanity-check before you trust it.** Run the checks in the template: row counts, denominator size, a spot-check on one known user, and monotonicity (retention and funnels only ever decrease).
8. **Explain it.** Two or three sentences: what each CTE does, what one row of output means, and the one assumption most likely to be wrong.

## Output template

```markdown
## Question
[Restate the product question as a precise metric, with grain and timezone.]

## Shape
[Funnel | Retention/Cohort | Active-user ratio | Event count] — [one line: why this shape.]

## Assumptions
- Dialect: [Postgres | BigQuery | Snowflake | …]
- Events table: `[table]`, user id: `[col]`, timestamp: `[col]`, event type: `[col] = '[value]'`
- "[Metric term, e.g. retained]" means: [exact definition].
- Timezone: [UTC | account tz]; grain: [day | week | month].

## SQL
\`\`\`sql
-- PATTERN: RETENTION (day-N exact). Swap pattern block as needed.
-- NOTE: both sides of the day-N comparison MUST be day-truncated. cohort_day is
-- DATE_TRUNC'd and active_day is DATE_TRUNC'd, so they align. If you compare a
-- DATE_TRUNC'd anchor against a RAW timestamp signup column, `= cohort_day + INTERVAL '7 day'`
-- almost never matches (timestamps land at 14:32:07, not midnight) → silent zero retention.
WITH cohort AS (                       -- denominator: who, anchored when
  SELECT
    user_id,
    DATE_TRUNC('day', MIN(event_time)) AS cohort_day
  FROM [events_table]
  GROUP BY user_id
),
activity AS (                          -- one row per user per active day
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('day', event_time) AS active_day
  FROM [events_table]
)
SELECT
  c.cohort_day,
  COUNT(DISTINCT c.user_id)                          AS cohort_size,
  COUNT(DISTINCT CASE
    WHEN a.active_day = c.cohort_day + INTERVAL '7 day'
    THEN c.user_id END)                              AS retained_d7,
  ROUND(100.0 * COUNT(DISTINCT CASE
    WHEN a.active_day = c.cohort_day + INTERVAL '7 day'
    THEN c.user_id END) / NULLIF(COUNT(DISTINCT c.user_id), 0), 1) AS retention_d7_pct
FROM cohort c
LEFT JOIN activity a ON a.user_id = c.user_id
-- Drop incomplete cohorts: a cohort hasn't had time to reach day 7 yet if
-- cohort_day + 7d is still in the future. Including it understates retention.
WHERE c.cohort_day + INTERVAL '7 day' <= DATE_TRUNC('day', now())
GROUP BY c.cohort_day
ORDER BY c.cohort_day;
\`\`\`

**Retention — N-day WINDOW `[+7d, +14d)` (the canonical "week-2 retention"):**
\`\`\`sql
-- "Week-2 retention" = active ANY time in the window [cohort_day + 7d, cohort_day + 14d),
-- NOT active exactly on day 7. Half-open interval avoids double-counting the boundary.
WITH cohort AS (
  SELECT user_id, DATE_TRUNC('day', MIN(event_time)) AS cohort_day
  FROM [events_table]
  GROUP BY user_id
),
activity AS (
  SELECT DISTINCT user_id, DATE_TRUNC('day', event_time) AS active_day
  FROM [events_table]
)
SELECT
  c.cohort_day,
  COUNT(DISTINCT c.user_id)                          AS cohort_size,
  COUNT(DISTINCT CASE
    WHEN a.active_day >= c.cohort_day + INTERVAL '7 day'
     AND a.active_day <  c.cohort_day + INTERVAL '14 day'
    THEN c.user_id END)                              AS retained_w2,
  ROUND(100.0 * COUNT(DISTINCT CASE
    WHEN a.active_day >= c.cohort_day + INTERVAL '7 day'
     AND a.active_day <  c.cohort_day + INTERVAL '14 day'
    THEN c.user_id END) / NULLIF(COUNT(DISTINCT c.user_id), 0), 1) AS retention_w2_pct
FROM cohort c
LEFT JOIN activity a ON a.user_id = c.user_id
-- Exclude recency-truncated cohorts: the FULL window must have elapsed (use the
-- window END, +14d, not +7d) or late-window returns are silently missing.
WHERE c.cohort_day + INTERVAL '14 day' <= DATE_TRUNC('day', now())
GROUP BY c.cohort_day
ORDER BY c.cohort_day;
\`\`\`

### Pattern swaps (drop in place of the SELECT above)

**Funnel (ordered steps, drop-off):**
\`\`\`sql
WITH steps AS (
  SELECT user_id,
    MIN(CASE WHEN event_type = 'signup'     THEN event_time END) AS t1,
    MIN(CASE WHEN event_type = 'activated'  THEN event_time END) AS t2,
    MIN(CASE WHEN event_type = 'purchased'  THEN event_time END) AS t3
  FROM [events_table]
  GROUP BY user_id
)
SELECT
  COUNT(*) FILTER (WHERE t1 IS NOT NULL)                       AS step1_signup,
  COUNT(*) FILTER (WHERE t2 >= t1)                             AS step2_activated,
  COUNT(*) FILTER (WHERE t3 >= t2 AND t2 >= t1)                AS step3_purchased
FROM steps;  -- t2 >= t1 enforces order; add `AND t2 <= t1 + INTERVAL '7 day'` for windowed funnels
\`\`\`

**DAU / MAU stickiness:**
\`\`\`sql
-- One CTE per step, no correlated per-day subquery. The trailing-30 MAU is a
-- COUNT(DISTINCT ...) over a 30-day window frame, so the events table is scanned
-- once instead of re-scanned for every day (the correlated-subquery trap).
WITH user_days AS (                        -- de-dupe to one row per user per active day
  SELECT DISTINCT user_id, DATE_TRUNC('day', event_time) AS day
  FROM [events_table]
),
dau AS (                                   -- distinct users active each day
  SELECT day, COUNT(DISTINCT user_id) AS dau
  FROM user_days
  GROUP BY day
),
mau AS (                                   -- trailing-30 distinct users via window frame
  SELECT day,
    COUNT(DISTINCT user_id) OVER (
      ORDER BY day
      RANGE BETWEEN INTERVAL '29 day' PRECEDING AND CURRENT ROW
    ) AS mau_trailing_30
  FROM user_days
)
SELECT
  d.day,
  d.dau,
  m.mau_trailing_30,
  ROUND(100.0 * d.dau / NULLIF(m.mau_trailing_30, 0), 1) AS stickiness_pct
FROM dau d
JOIN (SELECT DISTINCT day, mau_trailing_30 FROM mau) m USING (day)
ORDER BY d.day;
-- PERF CAVEAT: COUNT(DISTINCT ...) as a window aggregate isn't supported in every
-- engine (e.g. older Postgres). If it errors, fall back to a self-join on user_days
-- over the [day-29, day] range with COUNT(DISTINCT) grouped by day — still one pass
-- per day but no correlated scalar subquery in the SELECT list.
\`\`\`

**Event count (per feature per week):**
\`\`\`sql
SELECT DATE_TRUNC('week', event_time) AS wk, event_type,
       COUNT(*) AS events, COUNT(DISTINCT user_id) AS unique_users
FROM [events_table]
GROUP BY 1, 2 ORDER BY 1, 2;
\`\`\`

## Result
| [cohort_day] | [cohort_size] | [retained_d7] | [retention_d7_pct] |
|---|---|---|---|
| [2026-05-01] | [1,240] | [388] | [31.3] |

## Sanity checks (run before trusting)
- [ ] **Denominator size** is the number you expect (e.g. cohort_size ≈ known signups for the period).
- [ ] **People vs events:** used `COUNT(DISTINCT user_id)` for users, `COUNT(*)` for events — not swapped.
- [ ] **Spot-check one user:** pick a known user_id, verify their row matches raw events by hand.
- [ ] **Monotonicity:** funnel steps and retention curves only ever go *down* — any increase is a bug.
- [ ] **Boundaries:** half-open intervals `[start, end)`; no row counted in two buckets; timezone explicit.
- [ ] **Complete cohorts only:** excluded any cohort where `cohort_start + window > now()` — recency-truncated cohorts haven't had time to mature and drag the metric down.
- [ ] **Anchor alignment:** both sides of a day-N comparison are day-truncated (a raw-timestamp anchor vs a truncated one = silent zero matches).
- [ ] **Nulls & div-by-zero:** `NULLIF(denominator, 0)`; LEFT JOIN didn't silently drop the cohort.

## Read of the result
[2–3 sentences: what one row means, the headline number, and the single assumption most likely to flip the answer.]
```

## Avoid (anti-patterns)
- **Counting events when you mean users** (or vice versa) — `COUNT(*)` where you needed `COUNT(DISTINCT user_id)` silently inflates every number.
- **INNER JOIN on the cohort** — drops users who never returned, turning a retention denominator into only the retained. Use LEFT JOIN and anchor on the cohort table.
- **Off-by-one time windows** — `BETWEEN` is inclusive on both ends and double-counts midnight rows; use half-open `>= start AND < end`. Forgetting timezone shifts whole cohorts by a day.
- **Day-N exact vs N-day-window confusion** — "day-7 retention" (active exactly on day 7) and "week-1 retention" (active any time in days 1–7) give very different numbers. State which.
- **Trusting the first run** — shipping a number without the spot-check and monotonicity checks. A query that runs is not a query that's correct.

## Tips
- **Build the denominator first and confirm its size against a known figure** before adding any retention/funnel logic — most wrong answers are wrong denominators.
- **Prefer CTEs over nested subqueries.** One CTE per step reads like the explanation you'll have to write anyway, and is far easier to debug.
- **Window functions earn their keep for "first/next event" logic:** `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_time)` to grab a user's first action beats a self-join every time.
- **State the dialect up front and use its native date functions** — `DATE_TRUNC` (Postgres/Snowflake) vs `TIMESTAMP_TRUNC`/`DATE_TRUNC` (BigQuery) vs `DATE_FORMAT` (MySQL). A query for the wrong dialect is a query that doesn't run.
