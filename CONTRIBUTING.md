# Contributing

The best contribution is a skill you actually use. Second best is a bug report from a real install.

Everything here is markdown and Python 3 with no dependencies. If you can write a good PRD, you can contribute a skill.

---

## Adding a skill

**Use the tool that's already here.** Ask your agent to run `skill-creator` — it writes the frontmatter contract, the sections, and the anti-patterns in the house format, and it knows the quality bar. Writing one by hand is fine too; it just takes longer to pass.

```bash
python3 tests/score_skill.py skills/<your-skill>/SKILL.md
```

**Ship at 100, not at the 85 floor.** The floor is what a skill is allowed to decay to over time, not what it's allowed to arrive at. Every failed check is a real gap — a missing `Avoid` section means you never wrote down how this goes wrong, and a failed `asks_before_producing` on a `guided` skill means it will confidently invent inputs it should have requested.

Then run the full suite:

```bash
python3 tests/run_all.py && python3 tests/check_all_artifacts.py && python3 tests/audit.py
```

**A skill needs a worked example.** `examples/cadence/<skill>.md`, run against the demo company (Cadence — B2B async-standup SaaS, ~$3M ARR, fixing week-2 retention). It's not decoration: `check_all_artifacts.py` validates it against your own output template, so an example that drifts from its skill fails CI.

**Before you propose a new skill, check the nearest existing one.** If yours is 80% an existing skill, extend that one instead. `skill-creator` calls this the anti-bloat check and it's the reason this isn't 200 overlapping skills.

---

## What makes a skill good here

- **Grounded in a named source.** Not decoration — a constraint the model follows. `customer-interview` won't write "Would you use this?" because the Mom Test discipline is in the skill. That's the mechanism.
- **An honest tier.** `quick` / `guided` / `campaign`, plus a `time` a busy person can plan around. Labelling a two-week campaign as `guided` ambushes someone.
- **Anti-patterns from real scars.** The 3–5 ways this job is actually done badly. This is the half that makes it better than a generic prompt.
- **A concrete output template.** Copy-pasteable, with an `outputs:` path under `workspace/` so the artifact lands where the next skill can find it.

---

## Bugs

The most useful report tells us **which install** and **what you ran**:

```
Host: Cursor (installed via get.sh)
Ran: /weekly
Expected: a metrics review
Got: it asked me for my north-star metric, which is already in memory/strategy.md
```

Bugs that only appear *after* install are the valuable ones — the repo layout and the installed layout differ, and that gap has produced most of our real defects.

---

## What we won't merge

- **Skills that are really one prompt.** No process, no framework, no reusable output template.
- **Anything that scores below 85**, or that drops another skill's score. CI catches both.
- **Individual productivity scoring.** No output ranking, no comparing two people. This is a permanent line — it's what makes people willing to write honestly in the tools this OS reads.
- **Skill count for its own sake.** Breadth is not the axis we compete on.

---

## Other personas

Team OS, Founder OS, Marketer OS, and Engineering Lead OS are planned for the same marketplace. If you want to build one, open an issue first — there's shared scaffolding (the scorer, the workspace, the memory system) that should be hoisted rather than copied, and it's worth agreeing on that before you fork.

---

MIT. By contributing you agree your work ships under the same license.
