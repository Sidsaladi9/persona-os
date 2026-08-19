# Incidents

> **What broke, not what you tweaked.** This is the failure log — separate from
> `activity-log.md`, which records corrections. The two feed the tune-up at very
> different thresholds, and that difference is the point.
>
> Local-only. Never sent anywhere, never pasted into an output.

## The line between a correction and an incident

| | Correction (→ `activity-log.md`) | Incident (→ here) |
|---|---|---|
| What happened | The output was usable; you changed it | The output was **unusable, wrong, or dangerous to send** |
| Examples | "make it shorter", "use our template", "lead with the number" | invented a metric that doesn't exist · ignored a stated constraint · used a stale fact from memory · produced a spec with no acceptance criteria · you deleted it and did it by hand |
| Tune-up threshold | **3×** before it proposes anything | **1×** — one real failure is enough to propose a fix |
| Why the difference | Three corrections is a preference. One is taste. | A skill that produced something you couldn't use has a defect, and waiting for it to happen twice more is waiting to be burned twice more |

**When in doubt, it's a correction.** Over-logging incidents makes the loud signal quiet again.

---

## Entry format

```
### YYYY-MM-DD — <short title>
- **Skill:** <name | none — hand-rolled>
- **What:** what the OS produced or did, factually. No blame, no adjectives.
- **Impact:** what it cost you. Time, a wrong decision, something sent that shouldn't have been. If it cost nothing, this is probably a correction.
- **Root cause:** the mechanism, as best you can tell — missing input, stale memory file, ambiguous instruction in the skill, wrong tier, model error.
- **Prevention:** the specific change that would stop it. A line in the skill, a required input, a check in the process. "Be more careful" is not a prevention.
- **Status:** open | fixed <date> | won't fix — <reason>
```

Fill in what you know. A half-filled incident logged now beats a complete one you never write.

---

## Open

<!-- newest first -->

_(none)_

---

## Resolved

<!-- moved here with the fix and date, so the same defect isn't re-proposed -->

_(none)_

---

## How this gets used

- **`/tune-up`** reads every `open` incident and proposes a fix for each — at 1×, no pattern required. Root cause routes the fix: a skill defect edits the skill, a missing input adds it to that skill's `inputs:`, a stale fact fixes the memory file.
- **The session-start nudge** surfaces the count of open incidents once, quietly, and moves on.
- **A repeated root cause across different skills** is the highest-value finding in the whole OS — it means the problem is in `CLAUDE.md`, not in any one skill.
