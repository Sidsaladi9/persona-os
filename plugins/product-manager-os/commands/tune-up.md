---
description: Improve the OS from my recent work — propose new/tuned skills from patterns in my activity log
---

Run the OS tune-up now (the on-demand version of the weekly self-improvement pass). **Propose only — never apply anything without my explicit yes.**

1. **Read the signal.** `memory/activity-log.md` (the `## Log` section only) and `memory/os-suggestions.md` (skip anything already pending or rejected). If there are fewer than ~5 real entries, tell me there isn't enough signal yet and stop.

2. **Detect patterns at a 3× threshold** — and nothing weaker:
   - **Missing skill:** same kind of job with `skill: none` 3+ times.
   - **Skill needs tuning:** same skill + same `correction` 3+ times.
   - **Stale memory:** a knowledge file the recent work shows is now wrong (only if obvious).

3. **Anti-bloat:** before proposing any *new* skill, find the nearest existing skill in `skills/` and prefer tuning/extending it. Only propose new if nothing covers the job; say which skill you checked.

4. **Queue + present.** Append each surviving pattern as a `[PENDING]` entry in `memory/os-suggestions.md`, then show me the batch for **accept / tweak / reject**.
   - Accept a *new skill* → use `skill-creator`, ground it in my last ~3 examples of that job, and mark it `status: draft`.
   - Accept a *tune* → make the specific change to the skill (or to `house-style.md` if it's formatting).
   - Reject → move it to `## Resolved` with the date so it's not re-proposed.

5. **Graduate drafts:** any `status: draft` skill used 3× with no correction → promote to permanent and tell me.

Keep it tight. End with: proposals made / accepted / drafts graduated.
