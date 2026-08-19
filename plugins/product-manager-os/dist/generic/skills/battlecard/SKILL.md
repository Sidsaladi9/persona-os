---
name: battlecard
description: Produces a one-page sales battlecard for a specific competitor — how to position against them, the traps to set, the objections you'll hear, and where to concede. Use when a PM or PMM says "make a battlecard", "how do we sell against X", "sales keeps losing to X", "what do we say when they mention X", or when reps are improvising competitive answers and each one says something different.
tier: quick
time: 30-45 min
inputs: the competitor, real deals you've faced them in, and what reps currently say
outputs: research/battlecard-<competitor>.md
---

# Battlecard

Turns competitive knowledge into something a rep can use mid-call. One page, one competitor, written for someone with fifteen seconds and a prospect waiting. Distinct from `competitive-brief`, which is the analysis for internal strategy — this is the enablement artifact that comes out of it.

**Grounded in:** *Obviously Awesome* — April Dunford: compete on the value the customer actually weighs, not on a feature grid, and choose a frame of reference where your strengths are the ones that matter. Paired with standard sales-enablement practice — a card is only useful if a rep can find the answer without reading the page.

**The load-bearing idea:** a battlecard that lists forty feature comparisons gets read once and never opened again. Three traps and four objection responses get used in every call.

## When to use this
- Reps are improvising against a competitor and each gives a different answer.
- A named competitor shows up in enough deals to be worth a page — usually 3+ in a quarter.
- After a `win-loss` analysis surfaces a competitor-specific loss pattern.
- Before a launch that changes the competitive story.
- A competitor ships something that changes the conversation and the field needs an answer this week.

## Before you start (gather these)
- **The competitor, one at a time** — a card covering three competitors covers none of them.
- **Real deals you've faced them in** — what was said, what was lost, what was won. Not their website.
- **What reps currently say** — the improvised answers. Some are good and should be canonized; some are actively losing deals.
- **Their public pricing and packaging** — and where it's opaque, which is itself usable.
- **Where you genuinely lose to them** — you need this to write the concession section, which is the part that makes the card credible.

If two or more are missing, **ask 2-3 clarifying questions before writing**, starting with *"what are the last three deals we faced them in, and what actually happened?"* A card built from the competitor's marketing site teaches reps to argue with a brochure. If `workspace/research/` already holds a competitive brief or win/loss for them, read it first and open with an Assumptions block.

## Process
1. **Write the one-line frame first.** How you want the prospect to think about the category when both names are on the table. Everything else on the card serves this line.
2. **Pick three traps, no more.** A trap is a question the prospect asks the competitor that exposes a real, structural weakness — not a gap they'll close next quarter. Each trap needs the question verbatim and the answer you expect them to give.
3. **Write the objection responses in spoken language.** The literal objection a prospect says, then a response a rep can say out loud without reading. If it needs a slide, it's not an objection response.
4. **Concede clearly where they're better.** Name it, and give the rep the honest reframe. **This is the section that makes the rest believable** — a card with no concessions gets discounted entirely by experienced reps.
5. **Add the disqualification line.** When should the rep walk away? Knowing which deals to lose fast is worth more than winning a bad one, and nobody else writes this down.
6. **Add proof, not adjectives.** One customer story, one number, one quote. Specifics survive the call; adjectives don't.
7. **Date it and name an owner.** Competitive facts rot in weeks. An undated card is worse than none because reps trust it.

## Output template
```markdown
# Battlecard — vs. [Competitor]

**Updated:** [date] · **Owner:** [name] · **Next review:** [date]
**We face them in:** [x] of deals · **Win rate vs. them:** [x]%

## The frame (say this early)
> "[One line that reframes the category so the things we're better at are the things that matter.]"

## Why we win
| Reason | Say it like this | Proof |
|---|---|---|
| [structural advantage] | "[spoken line]" | [customer / number] |

## Why we lose *(read this before you argue)*
| Reason | Honest reframe | When to concede outright |
|---|---|---|
| [where they're genuinely better] | "[spoken line]" | [the deal shape where you should walk] |

## Three traps
**1. "[The question to plant, verbatim]"**
- **What they'll say:** [expected answer]
- **Why it lands:** [the structural weakness it exposes]

**2. "[Question]"** — [expected answer] · [why it lands]

**3. "[Question]"** — [expected answer] · [why it lands]

## Objection handling
**"[Objection as a prospect actually says it]"**
> "[Response a rep can say out loud, in one breath.]"

**"They're cheaper."**
> "[Response — reframe to total cost or value, with a number.]"

**"They have [feature] and you don't."**
> "[Response — concede if true, then reframe to what the customer is actually trying to do.]"

## Pricing
| | Us | Them |
|---|---|---|
| Model | | |
| Entry price | | |
| What's extra | | |
| Where they're opaque | — | [and how to use that] |

## Disqualify fast when
- [Deal shape where they win and we should not spend the cycles.]

## Proof points
- **Customer:** [name/anonymized] — [what happened, one sentence, with a number]
- **Number:** [the one statistic that matters in this comparison]
- **Quote:** "[a customer who switched, in their words]"

## What changed since last update
- [date] — [what moved, and what on this card it affects]
```

## Avoid (anti-patterns)
- **The forty-row feature grid.** Nobody opens it mid-call. Three traps and four objections get used every day.
- **No concession section.** Reps know where you lose. A card that pretends otherwise loses their trust and gets ignored entirely.
- **Built from their marketing site.** Their site describes their ambition. Your lost deals describe their product.
- **Traps that are really temporary gaps.** If they'll ship it next quarter, the trap becomes a liability the day they do. Aim at structural constraints — architecture, business model, who they're built for.
- **Written prose instead of spoken lines.** For example, "our platform offers superior extensibility" is unsayable; "you can wire it into your own tooling in an afternoon — theirs needs their services team" is what a rep will actually use.
- **No date.** Competitive facts rot fast, and a stale card confidently told is worse than silence.
- **One card covering three competitors.** Each competitor needs a different frame. Merging them produces a card that fits none.

## Tips
- 💡 **Interview two reps before writing, for fifteen minutes each.** They already know the answer; the card's job is to canonize the best version and delete the losing improvisations.
- Test it by handing it to a new rep and role-playing the objection. If they have to read a paragraph before answering, rewrite that line.
- Keep it to one page, genuinely. The second page is where trust goes to die.
- Re-run `win-loss` quarterly and update the card from it. Anything on the card contradicted by the actual deal data should go, however good it sounds.
