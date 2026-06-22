---
name: triage-requests
description: Sorts a pile of inbound feature requests from sales, support, and users into themes, quantifies demand behind each, and recommends build / watch / decline with a templated reply for every requester. Use when you say "I have 40 requests to go through," "what are people actually asking for," "triage this feedback dump," "theme these tickets," or "should we build this or say no?"
---

# Triage Requests

Demand intake and theming: turn a noisy stream of individual asks into a small set of weighted themes, then make an explicit build / watch / decline call on each — so the loud minority doesn't set your roadmap.

**Grounded in:** *Escaping the Build Trap* — Melissa Perri: tie every request to an outcome and say no to output-chasing.
**Go deeper (The Product Channel):** [Effective Prioritization](https://sidsaladi.substack.com/p/week-11-effective-prioritization)

## When to use this
- You've collected a quarter's worth of feature requests across sales notes, support tickets, and user feedback and need to make sense of them.
- A single big customer (or a loud Slack channel) is pushing a request and you need to size whether the demand is real and broad.
- Leadership asks "what are customers asking for?" and you only have a messy spreadsheet.
- You keep getting the same ask in different words and want to collapse it into one theme with a count.
- You need to close the loop with requesters — tell sales/support/users what you decided and why — without writing each reply from scratch.

## Before you start (gather these)
- **The raw requests** — pasted tickets, sales notes, survey rows, quotes. Each ideally with: who asked, what they asked for, source (sales/support/user), and any account/revenue/segment tag.
- **Strategy filter** — your current product strategy, theme, or "what we're NOT doing this year." Without this, every triage drifts into a popularity contest.
- **A demand denominator** — total accounts, MRR, or active users, so a "12 requests" means something relative to the base.

If 2+ of these are missing or vague, ASK 2-4 sharp questions before triaging: *What's the source breakdown — are these from sales, support, or users? Is there account/revenue data attached to any? What's your strategy theme this quarter so I can filter against it? Roughly how big is the customer base these came from?* If the data is already pasted and rich enough, proceed and state your assumptions inline (e.g., "Assuming all requests carry equal weight since no revenue tags were provided").

## Process
1. **Normalize.** Read every request and restate it as a neutral *job/problem*, not the requester's proposed solution. "Add a Salesforce sync button" and "I have to copy-paste deals into the CRM" are the same theme.
2. **Deduplicate / merge.** Before counting anything, collapse near-identical asks into a single canonical request and **sum their counts** (and their revenue/account tags). Three tickets saying "export to CSV," "let me download my data," and "bulk export button" are one ask with a count of 3, not three asks — keep the merged count and the distinct-account tally so volume and reach stay honest.
3. **Cluster into themes.** Group jobs into 5-12 themes. Name each theme after the problem ("Manual CRM data entry"), not a feature. Keep a one-off "Long tail / single asks" bucket — don't force fits.
4. **Quantify demand per theme.** Count requests, but weight them: a request tagged to a $200K account or asked by 8 distinct users outweighs one anonymous ticket. Compute three signals per theme — *volume* (count), *reach* (% of base or revenue touched), and *intensity* (workaround pain / churn-or-deal risk language).
   - **Precedence for small or revenue-heavy piles:** when the pile is small (N < 20) or any requests carry revenue/account tags, lead the ranking with *revenue-at-risk × strategic fit*, not volume. With few data points or real dollars attached, raw count is noise — a single $200K deal-blocker outranks a theme with 8 anonymous tickets. Treat volume as a tiebreaker between themes of comparable revenue and fit, not the driver.
5. **Score against strategy.** For each theme, rate strategic fit (does this advance the current theme?) and effort (rough T-shirt). High demand + high fit + low effort rises; high demand + low fit is a *watch* or a *decline-with-reason*, not an automatic build.
   - **Effort rubric (T-shirt):** **S** = less than one sprint. **M** = 1-2 sprints. **L** = more than a quarter or requires cross-team work.
   - **Revenue-blocking but off-strategy asks:** if a theme is gating real revenue (a $X deal stalls or an account threatens churn) but is genuinely off-strategy, name the dollar figure explicitly, still rate the verdict **Watch** or **Decline** on its merits — do not let revenue pressure bend it into a Build — and route the revenue risk to a sales/exec escalation (a deal-desk call, a one-off commitment, a pricing or partner workaround) rather than absorbing it into the roadmap. The roadmap stays strategy-driven; the dollar risk goes to whoever owns that deal.
6. **Make the call.** Assign each theme one verdict: **Build** (commit, route to roadmap), **Watch** (real but not now — set a re-trigger threshold), **Decline** (explicitly not doing — say why). Force a decision on every theme; "TBD" is not allowed.
7. **Write the loop-closing replies.** Draft a templated response per verdict, with source-aware variants (sales / support / user) so requesters hear back. Closing the loop is what keeps the intake pipe full and trusted.

## Output template

```markdown
# Request Triage — [Period / Source]
**Inputs:** [N] requests across [sales / support / users] · base = [X accounts / $Y MRR / Z users]
**Strategy filter:** [current theme — what we ARE and ARE NOT prioritizing]
**Assumptions:** [e.g., requests weighted equally; no revenue tags provided]

## Demand summary
| Theme (problem, not feature) | Requests | Reach (% base / $) | Intensity | Strat fit | Effort | Verdict |
|---|---|---|---|---|---|---|
| [Manual CRM data entry] | [14] | [22% of accts] | High (churn risk x3) | High | M | **Build** |
| [Bulk export of reports] | [9] | [11% of accts] | Med | Med | S | **Watch** |
| [Custom theming / white-label] | [6] | [4% / 1 acct] | Low | Low | L | **Decline** |
| [Long tail — single asks] | [11] | — | — | — | — | Park |

**Reading:** Intensity = workaround pain + deal/churn language. Reach = distinct accounts or revenue touched, not raw count.

## Verdicts in detail

### ▶ BUILD — [Theme name]
- **Job to be done:** [neutral problem statement]
- **Demand:** [N] requests · [reach] · [who: e.g., 3 enterprise accts named X-risk]
- **Why now:** [advances strategy theme + size of pain]
- **Next step:** [route to spec / roadmap Now-Next-Later slot]
- **Open question:** [what we still need to learn]

### ⏸ WATCH — [Theme name]
- **Demand:** [N] requests · [reach]
- **Why not now:** [lower fit / higher effort / not enough reach yet]
- **Re-trigger threshold:** [e.g., "revisit if this passes 20 distinct accounts or a $100K deal blocks on it"]

### ✕ DECLINE — [Theme name]
- **Demand:** [N] requests · [reach]
- **Why we're saying no:** [off-strategy / serves <X% / better solved by Y / niche]
- **Alternative offered:** [workaround, partner, or "tracked but not planned"]

## Templated requester replies

Pick the variant that matches who raised the ask. Sales wants deal-impact and timing; support wants something to relay to a ticket; users want plain, human acknowledgement.

**Build replies:**
> **→ Sales:** [theme] is now on the roadmap, targeting [Now/Next/Later]. You can tell [account] we're building it. I'll ping you the moment there's something to demo — flag if a deal timeline hinges on a specific date.
> **→ Support:** Good news on [theme] — it's on the roadmap for [Now/Next/Later]. You can let the reporters know it's coming and close the loop. I'll update you when it ships so you can follow up.
> **→ User:** Thanks for flagging [theme]. We're hearing this from enough of you that it's now on our roadmap — targeting [Now/Next/Later]. I'll follow up when there's something to test. Anything specific about [the workflow] you want me to keep in mind?

**Watch replies:**
> **→ Sales:** [theme] is real and tracked, but not in the current cycle — we're focused on [strategy theme]. We'll revisit when [re-trigger threshold]. If a deal or churn risk hinges on it, send me the account and $ and I'll re-weigh it now.
> **→ Support:** We're tracking [theme] but it's not scheduled yet. You can tell reporters it's logged and on the watch list — no timeline. Keep tagging tickets to it so we see if volume climbs toward [re-trigger threshold].
> **→ User:** Appreciate the request on [theme]. It's real and we're tracking it, but it's not in the current cycle — we're focused on [strategy theme] right now. We'll revisit when [re-trigger threshold]. If a deal or churn risk hinges on it, tell me and I'll re-weigh it.

**Decline replies:**
> **→ Sales:** Straight answer on [theme]: we're not planning to build it, because [reason — off-strategy / niche]. For [account], here's the workaround/alternative: [alternative]. If it's blocking real revenue, loop in [deal desk / exec] — let's solve it as a deal, not a roadmap item.
> **→ Support:** We're declining [theme] — not on the plan, because [reason]. You can tell reporters honestly it's not coming, and offer [alternative/workaround]. I'll keep it logged so we'd notice if demand shifts.
> **→ User:** Thanks for raising [theme]. Being straight with you: this isn't something we plan to build, because [reason — off-strategy / serves a small slice]. In the meantime, [alternative/workaround]. I'll keep it logged so we'd notice if demand shifts.

## What changed / next
- [Themes routed to roadmap, declines communicated, watch thresholds set]
- [Open: which requesters still need a reply]
```

## Avoid (anti-patterns)
- **Theming by feature, not problem.** "Add export button" and "let me pull my data into Excel" get split into two themes and demand looks half as big. Always normalize to the job first.
- **Counting raw tickets as demand.** Ten tickets from one angry account isn't ten units of demand. Weight by distinct accounts and revenue, or one loud customer hijacks the roadmap.
- **Letting volume override strategy.** The most-requested theme is often a *decline* — high count, low strategic fit. Don't auto-build the top of the list.
- **Leaving themes as "TBD."** A triage with no verdicts is just a sorted spreadsheet. Force build/watch/decline on every theme.
- **Skipping the reply.** Not closing the loop teaches sales and users to stop sending requests — and the intake dries up.

## Tips
- A clean *decline* with a reason builds more trust than a vague "we'll consider it." Saying no is the highest-leverage output of triage.
- Tag every request with its source — sales and support skew toward different asks (deal-blockers vs. friction), and the mix tells you what kind of pain you're really seeing.
- If a connector is available (Linear, Jira, Intercom, a CRM), pull requests straight from it — but this skill works entirely from pasted data, so a copied spreadsheet is enough.
- Set numeric re-trigger thresholds on every *Watch* ("revisit at 20 accounts or one $100K block"). It turns "not now" into a real decision instead of a soft maybe.
