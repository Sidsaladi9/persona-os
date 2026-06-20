Run the weekly OS tune-up. This is how the Product Manager OS improves itself from the work I actually do. Be concise and **never apply anything without my explicit yes** — you only propose.

## 1. Read the signal
Read `memory/activity-log.md` (the `## Log` section only — ignore the example block) and `memory/os-suggestions.md` (so you don't re-propose something already pending or rejected).

If the log has fewer than ~5 real entries, say so and stop — there isn't enough signal yet. Don't invent patterns.

## 2. Detect patterns (threshold: 3×)
Look only for these, and only when they repeat **3 or more times**:

- **Missing skill** — the same *kind of job* done with `skill: none` 3+ times. (e.g. three hand-rolled launch emails.)
- **Skill needs tuning** — the same skill with the *same correction* 3+ times. (e.g. `prioritize` + "changed RICE weights" three times.)
- **Stale/contradicted memory** — a knowledge file that the recent work shows is now wrong (only if obvious).

Be ruthless: a vague resemblance is not a pattern. If nothing clears 3×, report "nothing to propose this week" and stop.

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
