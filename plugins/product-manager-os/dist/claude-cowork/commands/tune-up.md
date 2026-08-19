---
description: Improve the OS from my recent work — propose new/tuned skills from patterns in my activity log
---

Run the OS tune-up now (the on-demand version of the weekly self-improvement pass). **Propose only — never apply anything without my explicit yes.**

1. **Read the three signals.**
   - `memory/incidents.md` → the `## Open` section. **Every open incident gets a proposal, at 1×.** No pattern required — a defect that produced unusable output does not need to recur to be worth fixing. Do these first; they outrank everything below.
   - `memory/activity-log.md` → the `## Log` section only, for 3× patterns.
   - `python3 tests/relevance_report.py` → skills whose artifacts are never referenced or revisited.
   - Skip anything already `[PENDING]` or rejected in `memory/os-suggestions.md`.

   If there are no open incidents **and** fewer than ~5 real log entries **and** no relevance flags, say there isn't enough signal yet and stop. Don't invent patterns to have something to say.

2. **Detect, at the right threshold for each source:**
   - **Incident → 1×.** Route the fix by root cause: a skill defect edits the skill; a missing input adds it to that skill's `inputs:`; a stale fact fixes the memory file; a wrong tier corrects the frontmatter. **A root cause that repeats across *different* skills is the highest-value finding available** — it means the problem is in `CLAUDE.md`, not in any one skill. Say so explicitly when you see it.
   - **Missing skill → 3×.** Same kind of job with `skill: none` 3+ times.
   - **Skill needs tuning → 3×.** Same skill + same `correction` 3+ times.
   - **Dead output → ≥3 artifacts, ≥2/3 never revisited.** The skill runs and the user never comes back to what it made. Propose a change to *what* it produces or *when* it fires — not a new skill. This is usually a wrong output template or a wrong tier.
   - **Stale memory:** a knowledge file the recent work shows is now wrong (only if obvious).

3. **Anti-bloat:** before proposing any *new* skill, find the nearest existing skill in `skills/` and prefer tuning/extending it. Only propose new if nothing covers the job; say which skill you checked.

4. **Queue + present.** Append each surviving pattern as a `[PENDING]` entry in `memory/os-suggestions.md`, then show me the batch for **accept / tweak / reject**.
   - Accept a *new skill* → use `skill-creator`, ground it in my last ~3 examples of that job, and mark it `status: draft`.
   - Accept a *tune* → make the specific change to the skill (or to `house-style.md` if it's formatting).
   - Reject → move it to `## Resolved` with the date so it's not re-proposed.

5. **Graduate drafts:** any `status: draft` skill used 3× with no correction **and no incident** → promote to permanent and tell me. An incident resets the count; a draft that failed once has not proven out.

6. **Close incidents you fixed.** When I accept a fix, move that incident to `## Resolved` in `memory/incidents.md` with the date and what changed. An open incident that's been fixed will keep generating the same proposal every week.

Keep it tight. End with: **open incidents / proposals made / accepted / drafts graduated / incidents closed.** If nothing cleared a threshold, say that in one line — a quiet week is a real result, not a failure to report.
