Run the weekly OS tune-up. This is how the Product Manager OS improves itself from the work I actually do. Be concise and **never apply anything without my explicit yes** — you only propose.

## 1. Read the three signals
- **`memory/incidents.md`** → the `## Open` section. Every open incident gets a proposal at **1×**, before anything else. A defect that produced unusable output does not need to repeat to be worth fixing.
- **`memory/activity-log.md`** → the `## Log` section only (ignore the example block), for 3× patterns.
- **`python3 tests/relevance_report.py`** → skills whose artifacts are never referenced or revisited after they're written.

Also read `memory/os-suggestions.md` so you don't re-propose something already pending or rejected.

If there are no open incidents, fewer than ~5 real log entries, and no relevance flags, say so and stop — there isn't enough signal yet. Don't invent patterns.

## 2. Detect, at the threshold that fits each source

**At 1× — incidents.** Every open incident. Route the fix by its root cause: skill defect → edit the skill; missing input → add it to that skill's `inputs:`; stale fact → fix the memory file; wrong tier → fix the frontmatter. **If the same root cause appears under two different skills, the problem is in `CLAUDE.md`** — call that out first, it's the most valuable thing you'll find all week.

**At 3× — behaviour patterns.** Only when they genuinely repeat:
- **Missing skill** — the same *kind of job* done with `skill: none` 3+ times. (e.g. three hand-rolled launch emails.)
- **Skill needs tuning** — the same skill with the *same correction* 3+ times. (e.g. `prioritize` + "changed RICE weights" three times.)
- **Stale/contradicted memory** — a knowledge file that recent work shows is wrong (only if obvious).

**At ≥3 artifacts, ≥2/3 dead — relevance.** A skill that runs and produces things nobody revisits. Propose a change to *what* it produces or *when* it fires, not a new skill — it's usually a wrong output template or a wrong tier.

Be ruthless on the 3× rules: a vague resemblance is not a pattern. Be the opposite on incidents — those are already evidence.

## 3. Anti-bloat check (required before proposing a new skill)
For each missing-skill candidate, search `skills/` for the nearest existing skill. **Prefer tuning or extending an existing skill over creating a new one.** Only propose a brand-new skill if no existing skill reasonably covers the job. State the nearest skill and why it's not a fit.

## 4. Write proposals to the queue
For each surviving pattern, append a `[PENDING]` entry to `memory/os-suggestions.md` in the file's format (kind, signal, proposal, overlap check, status).

## 5. Present for accept / tweak / reject
Show me each proposal as a short batch — *"here's how I'd improve myself this week."* For each, I reply accept / tweak / reject.

- **Accept (new skill):** use the `skill-creator` skill to write it, **grounded in my last ~3 examples of that job** from our history (my format, my tone), and mark it a **draft** (`status: draft` in the frontmatter — see skill-creator). It fires normally but stays provisional.
- **Accept (tune skill):** make the specific change to the existing skill, or to `memory/house-style.md` if it's a formatting correction.
- **Accept (fix memory):** update the knowledge file.
- **Reject:** move the entry to `## Resolved` in `os-suggestions.md` with "rejected <date>" so it's not proposed again.

## 6. Graduate drafts
Check any existing `status: draft` skills: if one has been used **3 times without a correction** (per the activity log), promote it to permanent (remove the draft flag) and tell me. This is the only step that changes a skill without asking — and it only *removes* a provisional flag on something already accepted.

End with a one-line summary: proposals made, accepted, drafts graduated.
