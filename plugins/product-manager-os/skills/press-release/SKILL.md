---
name: press-release
description: Writes the Amazon-style working-backwards press release and FAQ for a product or feature before it's built. Use when a PM says "write the press release", "PR/FAQ", "working backwards doc", "let's write the launch announcement first", "what would we say when this ships", or wants to pressure-test whether an idea is worth building by trying to make it sound compelling to a customer.
tier: guided
time: 45-60 min
inputs: the idea, who it's for, and what they can do after it exists that they couldn't before
outputs: projects/<project>/press-release.md
---

# Press Release (Working Backwards)

Writes the announcement *first*, as if the thing already shipped, then the FAQ that survives a skeptical room. The output is a decision instrument, not marketing copy: if you cannot write a compelling press release, that is the finding.

**Grounded in:** *Working Backwards* — Colin Bryar & Bill Carr: start from the customer announcement and the FAQ, and let a weak press release kill a weak idea before it consumes a roadmap. The rule that does the work is the constraint — one page, customer language, no internal jargon, benefits stated as what the customer can now do.

## When to use this
- At the *start* of a significant bet, before a spec exists and before engineering estimates anchor the conversation.
- When a proposal keeps getting described in internal terms and nobody can say what changes for a customer.
- To force a decision between three competing ideas — write all three, and the weak ones become obvious.
- Before a roadmap review where you need one page an exec can read cold.
- When an idea feels exciting but you suspect the excitement is internal, not customer-side.

## Before you start (gather these)
- **The customer** — a specific segment or role, not "users". The press release is written to them.
- **What they can do afterwards that they can't today** — stated as a capability, not a feature.
- **The evidence the problem is real** — a number, a quote, a support volume, a lost deal.
- **The hardest question a skeptic will ask** — you'll need it for the FAQ, and if you don't know it, find it first.
- **What already exists** — the alternative the customer uses today, including doing nothing.

If two or more are missing, **ask 2-4 sharp clarifying questions before writing.** The one that matters most: *"what can they do the day after this ships that they can't do today?"* If the answer is a feature description rather than a capability, stay there until it isn't. When you already have the context, state an explicit Assumptions block up top so it can be corrected in one line.

## Process
1. **Write the headline as the customer would repeat it.** One line, plain language, no product name games. If a customer wouldn't say it out loud to a colleague, rewrite it.
2. **Write the sub-head: who it's for and the single benefit.** One sentence. This is the piece that most often exposes a fuzzy target segment.
3. **Write the problem paragraph in the customer's words.** Use the actual language from tickets or interviews. Internal framing ("our activation funnel underperforms") is a tell that you're writing for yourself.
4. **Write the solution paragraph as capability, not mechanism.** What they can now do. Mechanism belongs in the FAQ, not here.
5. **Add the two quotes.** An internal leader quote that states *why this matters strategically*, and a customer quote that states *what changed for them*. Write the customer quote as if transcribed — if it sounds like marketing, the benefit isn't concrete enough yet.
6. **Write the FAQ, hardest question first.** Customer FAQ and internal FAQ separately. The internal FAQ is where cost, risk, what-we're-not-doing, and the thing you're least sure about live. **An FAQ with no uncomfortable question in it is not finished.**
7. **Apply the kill test.** Read the whole page as someone with no context. If it isn't compelling, say that plainly and recommend not building it — that is the skill working, not failing.

## Output template
```markdown
# [Headline — what the customer would say, one line]
### [Sub-head — who it's for and the one benefit, one sentence]

**[CITY] — [Month Day, Year]** — [Company] today announced [thing], which lets [specific customer] [do the new capability]. [One sentence on availability and price.]

## The problem
[2-4 sentences, in the customer's language. Lead with the evidence: the number, the volume, the quote. State what it costs them today.]

## What we built
[2-4 sentences. What the customer can now do, in order of how they'd experience it. Capability, not architecture. No internal terms.]

## What people are saying
> "[Internal leader quote — why this matters strategically, not how clever the tech is.]"
> — [Name, role]

> "[Customer quote — a concrete before-and-after in their own voice. Should sound transcribed, not written.]"
> — [Name, role, company]

## How to get started
[The first step a customer takes, in one or two sentences. If this is complicated, that's a product finding.]

---

# FAQ

## Customer questions
**[The question a real customer asks first]**
[Straight answer. No deflection.]

**What does it cost?**
[Answer, or state explicitly that pricing is undecided and when it will be.]

**What if [the obvious failure case]?**
[Answer.]

## Internal questions
**Why are we the right ones to build this?**

**What's the biggest risk, and what would we do if it happens?**

**What are we explicitly NOT building in v1?**

**What has to be true for this to work?** *(the riskiest assumption — name it, and the cheapest test of it)*

**What does this cost to build and run?** *(rough order of magnitude, stated as a range)*

**What are we saying no to by doing this?**

**What's the thing we're least sure about?** *(answer honestly — this is the most valuable line on the page)*

---

## Verdict
**Compelling? [yes / no / not yet]** — [one paragraph. If "not yet", say exactly what would have to change: a sharper segment, a bigger benefit, or better evidence the problem is real.]
```

## Avoid (anti-patterns)
- **Writing it after the spec.** The whole value is that it comes first, when it can still change what you build. Written afterwards, it's a press release.
- **Internal language in the customer section.** "Leveraging our unified data layer" tells a customer nothing. If a term wouldn't survive being read to a customer, cut it.
- **A fabricated customer quote that sounds like a brochure.** Real people say concrete things: *"I used to spend Monday morning chasing six people for updates. Now I read one digest."*
- **An FAQ of soft questions.** If nothing in the FAQ is uncomfortable, you skipped the point of the exercise.
- **Refusing to fail the kill test.** A press release that can't be made compelling is the cheapest possible "no". Say so.
- **Feature lists.** Three benefits stated as capabilities beat ten features every time.
- **Vague availability.** "Coming soon" in a working-backwards doc hides the scoping conversation you need to have.

## Tips
- 💡 **Write the customer quote first.** It's the hardest line on the page, and if you can't make it concrete, nothing downstream will be either.
- Read it out loud to someone outside the team. Watch where they look confused — that's the paragraph to rewrite.
- For example, if the headline needs a clause explaining what the product category is, your positioning isn't settled — run `positioning` before finishing this.
- Keep the whole thing to one page for the release plus two for the FAQ. The constraint is the mechanism; a three-page release proves nothing.
- Revisit it at launch. The gap between what you promised here and what actually shipped is the most honest retro input you'll get — feed it to `spec-vs-shipped`.
