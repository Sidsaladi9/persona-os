---
name: product-vision
description: Writes a product vision — the 3-5 year picture of the world your product is trying to create, and what has to become true along the way. Use when a PM or founder says "write the product vision", "what's our vision", "where is this going in three years", "the team can't see the bigger picture", or when every roadmap conversation collapses into next quarter because nothing above it exists.
tier: guided
time: 60-90 min
inputs: who you serve, what's broken for them today, and what you believe will change in your market
outputs: strategy/product-vision.md
---

# Product Vision

Writes the 3-5 year picture: the world your product is trying to create, who is better off in it, and the beliefs it rests on. Distinct from `product-strategy` — the vision is the destination, the strategy is the honest diagnosis of what's in the way and the route you've chosen through it.

**Grounded in:** *Inspired* — Marty Cagan: the vision is an inspiring, customer-centric picture of the future 3-5 years out, and its job is recruiting and alignment, not planning. It is deliberately *not* measurable — the moment you make a vision a metric you have written an OKR and lost the thing that made people care.

**The load-bearing idea:** a vision earns its keep by settling arguments you haven't had yet. If it can't tell you which of two reasonable roadmap items is more on-path, it's a mission statement wearing a vision's clothes.

## When to use this
- Every prioritization argument bottoms out in opinion because there's no shared destination above the quarter.
- Hiring senior people who ask "where is this going?" and deserve a real answer.
- After a pivot, an acquisition, or a strategy reset, when the old picture no longer describes the company.
- Before writing a multi-year roadmap or a fundraise narrative.
- When the team can recite the feature list but not the point of it.
- A new PM inherits a product with a strategy doc and no destination.

## Before you start (gather these)
- **Who you serve** — the specific person, in enough detail that a stranger could picture their day.
- **What's broken for them today** — the concrete cost of the status quo, with evidence.
- **What you believe about how the market changes** — the shifts you're betting on. This is the spine of a real vision.
- **What you will never do** — the boundaries. A vision without an edge describes everything.
- **Where you are now** — honestly, so the gap between here and there is visible.

If two or more are missing, **ask 2-4 clarifying questions before drafting.** The one that separates a real vision from a slogan: *"what do you believe about this market that most people in it don't?"* Without a contrarian belief you'll produce something true, agreeable, and useless. If `workspace/strategy/` and `memory/` already carry this, open with an Assumptions block.

## Process
1. **Start from the customer's day, not the product.** Describe a specific person's Tuesday in [year]. What do they do, what has disappeared from their week, what do they no longer think about? Concrete beats aspirational — "the Monday-morning status chase is gone" beats "empowering teams to collaborate."
2. **Name the beliefs it rests on.** Two to four things you think will be true that aren't consensus today. These are the load-bearing walls: if a belief turns out wrong, the vision changes. Write them as falsifiable statements.
3. **Draw the boundary.** What is explicitly outside this vision, permanently. The edge is what makes the vision usable for saying no.
4. **State the gap honestly.** Where you are today versus the picture. Do not soften it — the gap is what makes the vision motivating rather than complacent.
5. **Sketch the path in horizons, not dates.** Now / next / eventually, as capabilities the world gains, not features you ship. Resist putting quarters on it; a vision with a Gantt chart becomes a plan and stops doing its job.
6. **Test it against two real decisions.** Take two roadmap items you're genuinely torn between. If the vision doesn't make one more clearly on-path, it isn't specific enough — go back to step 1.
7. **Compress to something sayable.** One paragraph a new hire could repeat after hearing it once. If it needs a slide to survive, it won't.

## Output template
```markdown
# Product Vision — [product]

## The one-paragraph version
[The picture, in language a new hire repeats after hearing it once. Present tense, as if describing the future world as it already is.]

## A day in [year]
[400-600 words describing one specific person's day. Name them. What they do, what's absent that's painful today, what they no longer think about. Concrete and unglamorous — the details are what make it real.]

## What we believe (the load-bearing bets)
| # | Belief | Why we hold it | What would falsify it |
|---|---|---|---|
| 1 | [a claim about how this market changes] | [evidence or reasoning] | [the observation that would kill it] |

## Who is better off
- **[Primary person]** — [what changes for them]
- **[Secondary]** — [what changes]
- **[Who is not served by this]** — [stated plainly]

## The boundary — what this is never
- [Thing] — [why it's permanently outside, not just later]

## Where we are today
[The honest gap. Current state, in the same terms as the vision, so the distance is visible.]

## Horizons
| Horizon | What becomes true | Not yet |
|---|---|---|
| Now | [capability the world has] | |
| Next | | |
| Eventually | | |

## Decision test
Two real decisions this vision resolves:
- **[Decision A vs B]** → [which, and why the vision says so]
- **[Decision C vs D]** → [which, and why]

*If the vision doesn't resolve these, it isn't finished.*
```

## Avoid (anti-patterns)
- **A vision that's a metric.** "$100M ARR by 2029" is a goal. It tells nobody what to build and inspires no one outside the cap table.
- **Abstraction that survives find-and-replace.** If swapping your product name for a competitor's leaves it equally true, delete it and start again.
- **No contrarian belief.** A vision everyone already agrees with cannot guide a hard decision, because the hard decisions are exactly where consensus breaks.
- **Dates and quarters.** The moment a vision acquires a timeline it becomes a plan, gets missed, and stops being credible.
- **No boundary.** A vision that excludes nothing permits everything, which is how roadmaps sprawl.
- **Writing it alone and announcing it.** A vision nobody helped shape gets nodded at and ignored. Draft alone, pressure-test with three people, then publish.
- **Confusing it with strategy.** The vision says where. `product-strategy` says what's in the way and how you'll get through. Both are needed; they are not the same document.

## Tips
- 💡 **Write the "day in the life" section first and the one-paragraph version last.** The paragraph is a compression of the picture, and compressing something you haven't drawn produces platitudes.
- Read it to someone who doesn't work on the product. If they can tell you what you'd refuse to build, it's specific enough.
- For example, "teams never hold a status meeting again" is a usable vision — it immediately says yes to async digests and no to a better meeting scheduler. "Improve team communication" says nothing about either.
- Revisit annually, or whenever one of the load-bearing beliefs is falsified. A vision that never changes across a market shift wasn't making a bet.
