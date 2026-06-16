---
name: icp
description: Defines the Ideal Customer Profile — the firmographic and behavioral traits of accounts that get the most value and convert and retain best, plus qualifying signals, anti-signals, and where to find them. Use when you say "who's our ICP", "who should sales target", "which accounts retain best", "we're closing the wrong customers", or "tighten our targeting" — for B2B accounts, not individual buyer personas.
---

# Ideal Customer Profile

An ICP describes the *accounts* worth winning — the firmographic and behavioral shape of companies that extract the most value, convert efficiently, and stick. It is a filter, not a wish list. The job is to point everyone (sales, marketing, product, success) at the same narrow target and give them the signals to recognize it and the anti-signals to walk away.

A real ICP is grounded in your own retention and conversion data, not aspiration. The sharpest move is naming who to *avoid*: the accounts that close fast, churn faster, and poison your metrics and your roadmap. An ICP that excludes nobody isn't an ICP — it's a market description.

**Grounded in:** *Crossing the Chasm* — Geoffrey Moore: define the best-fit account by who gets the most value and retains.
**Go deeper (The Product Channel):** [How to Create a Customer Persona](https://sidsaladi.substack.com/p/how-to-create-a-customer-persona)

## When to use this
- Sales is closing logos that churn in two quarters, or win rates are sliding and you suspect mis-targeting.
- Marketing spend is spraying — high lead volume, low qualified-pipeline, rising CAC.
- You're entering a new segment and need to define who you're actually going after.
- Success is drowning because too many low-fit accounts need hand-holding to get any value.
- Annual planning: you need one shared definition of "good customer" to align GTM and roadmap.

## Before you start (gather these)
- **Customer outcome data** — your best and worst accounts by retention, expansion, and value realized (NRR, churn cohort, NPS, product usage, time-to-value). This is the ground truth the ICP is reverse-engineered from.
- **Firmographics for those accounts** — industry, size (employees/revenue), geography, tech stack, business model, GTM motion.
- **Win/loss and sales-cycle data** — who closes fast vs. stalls, deal size, who you lose to and why.
- **Your product's core value** — the specific problem you solve and the conditions under which it pays off (this defines fit at the mechanism level, not just the surface).

If you have fewer than ~10 retained accounts to learn from, or two-plus of the above are missing or vague, **ask 2–4 sharp questions first** rather than inventing a profile: e.g. "Which 5 accounts would you be most upset to lose, and why?" / "What's true about every account that gets fast value — and every account that churns?" / "What deals do you regret closing?" / "Where does the product *stop* working?" If the data is already provided, proceed and state your assumptions inline (e.g. "Assuming the 6 named accounts are representative of fit; flag if any were lighthouse deals").

**Cold start (genuine zero-data / pre-PMF).** If there are *no* retained accounts to reverse-engineer from — pre-launch, pre-PMF, or a brand-new segment — say so plainly and label the entire output **"ICP HYPOTHESIS — not evidence"** in the title and set Confidence: Low. Do not present inferred bands as measured. Then list the validation steps to convert hypothesis → evidence before GTM locks: (1) run 8–12 problem-discovery interviews against the hypothesized segment; (2) ship a small paid pilot / design-partner cohort and watch time-to-value and willingness-to-pay; (3) instrument activation + early-retention for the first cohort; (4) define the kill criteria that would falsify the hypothesis (e.g. "if pilots in segment X don't reach value in 30 days, drop X"). Revisit the ICP once ~10 accounts have real outcome data.

## Process
1. **Anchor on your best and worst accounts.** List your top retainers/expanders and your churned/regretted accounts. Don't theorize yet — just observe. The ICP lives in the *contrast* between these two sets.
2. **Extract the firmographic shape.** Find the traits the winners share and the losers don't: size band, industry, business model, tech stack, geo, growth stage. Be specific — "mid-market" is useless; "150–800 employees, Series B–C, US/EU" is targetable.
3. **Extract the behavioral and situational fit.** What's *true* about good-fit accounts beyond their stats — a trigger (just raised, new exec, regulation), a workflow they already run, a pain acute enough to pay now, the technical or organizational readiness to adopt. This is where most weak ICPs are thin; it's also where the real signal is.
4. **Name the anti-signals.** Write down who looks tempting but burns you: wrong size, wrong maturity, a use case the product half-serves, buyers with no budget authority, accounts that need heavy customization. Make these disqualifying, not "proceed with caution."
5. **Define qualifying signals you can actually observe.** For each fit trait, name the *observable proxy* a rep or marketer can check in the wild (a job posting, a funding event, a tool in their stack, a title on the buying committee). A trait you can't detect can't drive targeting.
6. **Map where they congregate.** Translate the profile into sourcing: data filters (LinkedIn/Apollo/Clearbit criteria), communities, events, integrations/marketplaces, search intent, partner channels. End on *go find them here*, not just *they look like this*.
7. **Pressure-test and bound it.** Sanity-check the profile against accounts it would wrongly include or exclude. State the addressable size implied. If the ICP describes most of your funnel, it's too loose — tighten until it excludes real, named deals.

## Output template

```
# Ideal Customer Profile — [Product / Segment]
Owner: [name/role] · Date: [date] · Based on: [N retained + N churned accounts]
Confidence: [High / Medium / Low — and why. State explicitly if any figures are
illustrative/inferred rather than measured, and name the exact dataset to validate
against before GTM filters lock — e.g. "Medium: bands inferred from 6 named accounts,
not the full book; validate against NRR-by-cohort export in [warehouse/CRM table] before
sales filters go live."]

## One-line ICP
[A targetable sentence. e.g. "Series B–C B2B SaaS companies, 150–800 employees,
US/EU, with a 3+ person data team and a modern warehouse, feeling reporting pain
acute enough to have a budgeted line item this year."]

## Why these accounts (the value mechanism)
- We create the most value when: [the condition under which the product pays off]
- Time-to-value for a good-fit account: [e.g. < 30 days]
- Unit economics: [avg ACV $___ · CAC $___ · gross margin ___% · payback ___mo · LTV:CAC ___]
  — so exclusions are defensible on margin, not just retention (a segment that retains
  but carries negative margin or a 24mo payback is still a disqualify).
- Evidence: [best accounts realize X; this trait separates retainers from churners]

## Firmographic fit
| Dimension       | Target                         | Observable signal                          |
|-----------------|--------------------------------|--------------------------------------------|
| Company size    | [150–800 employees]            | [LinkedIn headcount, Clearbit]             |
| Stage / funding | [Series B–C]                   | [Crunchbase, recent raise news]            |
| Industry        | [B2B SaaS, fintech]            | [SIC/NAICS, site, sales filter]            |
| Geography       | [US, UK, EU]                   | [HQ / billing region]                      |
| Business model  | [recurring revenue, PLG+sales] | [pricing page, motion]                     |
| Tech stack      | [uses Snowflake + dbt]         | [job posts, BuiltWith, integrations]       |

## Behavioral & situational fit
- **Trigger** — [just raised / new VP / hit a scale wall / new regulation]. Signal: [______]
- **Existing workflow** — [already runs X manually in spreadsheets]. Signal: [______]
- **Pain intensity** — [acute enough to have budget *now*, not "someday"]. Signal: [______]
- **Readiness** — [has the team/tooling/exec sponsor to adopt]. Signal: [______]
- **Buying committee** — [econ buyer: ___ · champion: ___ · user: ___]

## Anti-signals — who to AVOID (disqualifying)
| Anti-signal                        | Why it burns us                          |
|------------------------------------|------------------------------------------|
| [< 50 employees]                   | [can't realize value; churns; high touch]|
| [no in-house ___ team]             | [needs us to do the work; never adopts]  |
| [requests heavy customization]     | [drags roadmap; one-off; low margin]     |
| [no budget authority in the room]  | [long cycle, no close]                   |
| [use case we only half-serve]      | [sets false expectations; bad reviews]   |

## Qualifying checklist (rep/marketer can run this live)
- [ ] [Size in band] · [ ] [Stack present] · [ ] [Trigger fired]
- [ ] [Champion identified] · [ ] [Budget plausible] · [ ] [No disqualifying anti-signal]
→ 5+ checked = ICP. 3–4 = monitor / nurture. <3 or any anti-signal = disqualify.

## Tiers (route effort, don't just gate)
| Tier        | Definition                                  | What GTM does with them                    |
|-------------|---------------------------------------------|--------------------------------------------|
| ICP (Tier 1)| 5+ checks, no anti-signal, margin-positive  | [named sales motion, calendar time, ABM]   |
| Adjacent    | 3–4 checks, no disqualifying anti-signal    | [nurture / product-led / wait for trigger] |
| Disqualify  | <3 checks OR any anti-signal OR bad margin  | [politely decline / self-serve only]       |

## Where to find them
- **Data/filters:** [Apollo/LinkedIn Sales Nav query: ______]
- **Intent:** [keywords / G2 category / review activity: ______]
- **Communities & events:** [______]
- **Integrations / marketplaces / partners:** [______]

## Boundaries
- Implied addressable accounts: [~N]
- Deliberately excluded (and why): [______]
- Revisit when: [data refresh date / segment shift]
```

## Avoid (anti-patterns)
- **Describing your dream customer instead of your real one.** If the profile isn't reverse-engineered from accounts that actually retained, it's marketing fan-fiction. Anchor on data.
- **An ICP with no anti-signals.** If nobody is disqualified, GTM will chase everything. The exclusions are the point.
- **Traits you can't observe in the wild.** "Values data-driven decisions" can't be filtered or detected. Every trait needs an observable proxy or it's decoration.
- **Confusing the ICP (the account) with the persona (the human buyer).** This skill defines *which companies*; the buying committee inside them is a related but separate question — keep them distinct.
- **Too broad to be useful.** If your ICP matches 70% of inbound, you haven't made a decision. Tighten until it excludes named, real deals you'd otherwise have taken.

## Tips
- **The strongest evidence is your churn list.** Whatever every churned account shares — and your retainers don't — is your sharpest anti-signal. Mine the failures first.
- **Tier it, don't just gate it.** A clean "ICP / adjacent / disqualify" tiering routes effort better than a single yes/no — adjacent accounts get nurture, not sales calendar time.
- **Make it a one-liner a rep can repeat from memory.** If the ICP can't be said in a sentence on a sales floor, it won't change behavior, and behavior change is the only reason to write it.
- **Re-derive it every couple of quarters.** As the product matures and you move upmarket (or down), the accounts that fit shift. A stale ICP quietly mis-aims the whole funnel.
