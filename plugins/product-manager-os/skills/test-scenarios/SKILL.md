---
name: test-scenarios
description: Derives QA test scenarios and acceptance test cases from a spec or user story, covering happy paths, edge cases, error states, data variations, and ML quality-bar/eval cases. Use when you need to "write test cases for this story," "figure out what QA should check," "turn this spec into acceptance criteria," "find the edge cases we're missing," or "design eval cases for this AI feature."
---

# Test Scenarios

Turns a spec or story into a complete test matrix using classic test-case design: happy path, edge cases, error paths, and data variations — plus quality-bar/eval cases for ML and AI features where output is probabilistic rather than deterministic.

**Grounded in:** *Agile Testing* — Lisa Crispin & Janet Gregory: cover happy/edge/error/data paths from acceptance criteria.
**Go deeper (The Product Channel):** [PM's 30-Minute AI Evals](https://sidsaladi.substack.com/p/pms-30-minute-ai-evals-a-lightweight)

## When to use this
- A spec or story is "code complete" and you need acceptance test cases before sign-off.
- Engineering says "it works" but you suspect untested edge and error paths.
- You're writing acceptance criteria and want them backed by concrete, checkable scenarios.
- A feature involves messy real-world data (uploads, dates, currencies, names, timezones) and you need data-variation coverage.
- The feature is ML/AI-driven (search, recommendations, classification, generation) and you need eval cases with a defined quality bar, not just pass/fail.

## Before you start (gather these)
- **The spec or story** — what the feature does, the user goal, and the acceptance criteria as written.
- **Inputs and their constraints** — every field/parameter, allowed types, ranges, required vs. optional, formats.
- **System boundaries** — dependencies, integrations, auth/permission rules, and what's explicitly out of scope.
- **For ML/AI features** — what "good output" means, the quality bar (accuracy threshold, latency, safety constraints), and a few known-good / known-bad examples.

If two or more of these are missing or vague, ASK 2–4 sharp clarifying questions before generating (e.g., "What are the field-level validation rules?", "What's the expected behavior when the upstream service times out?", "For this recommendation feature, what's the minimum acceptable relevance bar and how is it judged?"). If the spec is already concrete, proceed and state any assumptions inline in the output.

## Process
1. **Number the acceptance criteria.** List and number every acceptance criterion (AC-1, AC-2, …). If the spec doesn't state them as a numbered list, reconstruct them from the spec's stated behavior and success conditions, and mark them as reconstructed. Every scenario you write must trace back to exactly one of these.
2. **Extract the testable units.** List every distinct behavior, input field, state transition, and integration point in the spec. One row of this list = one branch of the test tree.
3. **Map the happy path first.** Write the canonical end-to-end success scenario(s) — the flows that must work for the feature to ship at all. These are your P0s.
4. **Test tenant/workspace isolation and authz boundaries.** For any multi-tenant or multi-user feature, write P0 scenarios that confirm one tenant/workspace/user cannot read, write, or enumerate another's data — across every access path (direct API, list/search, exports, shared links, IDs in URLs). Try cross-tenant IDs, role downgrades, and revoked-access reuse. B2B cross-tenant data leaks are the highest-severity, most-missed bugs; treat any leak as P0.
5. **Apply the state-transition / concurrency lens.** Map the object's lifecycle states and the transitions between them, then test what happens when actions arrive out of expected order or in parallel: edit-after-submit, retract/undo after a downstream action, concurrent edits to the same record (last-write-wins vs. conflict), double-submit, and stale-read overwrites. For each, specify the expected resolution (reject, merge, version conflict, idempotent no-op).
6. **Enumerate edge cases per input.** For each input apply boundary analysis: empty, min, max, just-over-max, zero, negative, very large, unicode/emoji, whitespace, duplicates, ordering. Cover boundaries, not just middles.
7. **Walk every error path.** For each failure mode (bad input, denied permission, timeout, dependency down, partial failure, concurrent edit), specify the expected handled behavior — error message, retry, graceful degradation. Untested error paths are where production incidents live.
8. **Vary the data.** Real-world data variations: long names, missing fields, mixed locales, timezones/DST, currency/decimal formats, leap years, RTL text, malformed files, injection-looking strings. These find the bugs synthetic data hides.
9. **Add ML quality-bar/eval cases (if applicable).** Define a golden set with an explicit **size** (how many labeled examples) and **label source** (human-rated, expert-curated, production-sampled, synthetic), then assert an **aggregate metric over the set** (e.g., precision ≥ 0.9 over N=200, 0 unsafe outputs over N=50) rather than per-row exact-match asserts. Include adversarial/ambiguous inputs. Eval cases assert "good enough" in aggregate, not exact equality per row.
10. **Assign priority and traceability.** Tag each scenario P0/P1/P2 (see priority rubric below) and link it back to the numbered acceptance criterion it verifies. Flag any criterion with no covering test as a coverage gap.

### Priority rubric
- **P0** — Blocks ship. Data loss/corruption, security or tenant-isolation/authz failure, or a core happy path that doesn't work. Must pass before release.
- **P1** — Degraded but recoverable. Feature works but with a wrong or confusing result, missing error handling, or a workaround needed; ship-blocking only if it hits a common path.
- **P2** — Cosmetic or rare. Minor display issues, unlikely edge inputs, polish. Track but don't block.

## Output template

```markdown
# Test Scenarios: [Feature / Story Name]

**Spec reference:** [link or ID]
**Author / date:** [name] · [date]
**Assumptions made:** [list any assumptions taken where the spec was silent]
**Out of scope:** [what these tests deliberately do not cover. Outcome/retention/business metrics (e.g., D7 retention, conversion lift) are NOT QA scope — instead assert the instrumentation EVENT fires with the right payload; the metric itself is validated in analytics, not here.]

## Coverage summary
| Category | # Scenarios | P0 | Notes |
|---|---|---|---|
| Happy path | [n] | [n] | |
| Tenant/authz isolation | [n] | [n] | [all P0; omit row if single-tenant] |
| State/concurrency | [n] | [n] | [edit-after-submit, retract, concurrent edit] |
| Edge cases | [n] | [n] | |
| Error paths | [n] | [n] | |
| Data variations | [n] | [n] | |
| ML quality/eval | [n] | [n] | [omit row if not ML] |

## 1. Happy path
| ID | Scenario | Preconditions | Steps | Expected result | Priority | Verifies AC |
|---|---|---|---|---|---|---|
| HP-1 | [canonical success flow] | [state] | [1. … 2. …] | [observable result] | P0 | [AC-#] |

## 2. Tenant / authz isolation  *(only for multi-tenant or multi-user features — all P0)*
| ID | Actor / access path | Attempted cross-boundary action | Expected result | Priority | Verifies AC |
|---|---|---|---|---|---|
| TI-1 | [tenant B user, via API] | [read tenant A's record by ID] | [403 / 404, no data returned, audit logged] | P0 | [AC-#] |
| TI-2 | [downgraded/revoked role] | [reuse old token / list other workspace] | [access denied, no enumeration leak] | P0 | [AC-#] |

## 3. State transitions / concurrency
| ID | Starting state | Action / interleaving | Expected resolution | Priority | Verifies AC |
|---|---|---|---|---|---|
| ST-1 | [submitted] | [edit after submit] | [reject / require recall] | P1 | [AC-#] |
| ST-2 | [active] | [retract/undo after downstream action] | [defined rollback or block] | P1 | [AC-#] |
| ST-3 | [shared record] | [two concurrent edits] | [last-write-wins / version conflict surfaced] | P1 | [AC-#] |

## 4. Edge cases
| ID | Input / condition | Boundary tested | Expected result | Priority | Verifies AC |
|---|---|---|---|---|---|
| EC-1 | [e.g., max-length value at limit] | [boundary] | [expected handling] | P1 | [AC-#] |
| EC-2 | [empty / zero / negative] | [boundary] | [expected handling] | P1 | [AC-#] |

## 5. Error paths
| ID | Failure trigger | Expected handled behavior | User-facing message | Recovery | Priority |
|---|---|---|---|---|---|
| ER-1 | [invalid input] | [reject + no state change] | [exact message] | [retry / fix] | P0 |
| ER-2 | [dependency timeout] | [graceful degradation] | [message] | [retry / fallback] | P1 |
| ER-3 | [permission denied] | [block + audit log] | [message] | — | P0 |

## 6. Data variations
| ID | Data shape | Example value | Expected result | Priority |
|---|---|---|---|---|
| DV-1 | [unicode / emoji / RTL] | [example] | [renders & stores correctly] | P1 |
| DV-2 | [timezone / DST boundary] | [example] | [correct local conversion] | P1 |
| DV-3 | [currency / decimal format] | [example] | [no rounding/format error] | P2 |

## 7. ML quality-bar / eval cases  *(only for ML/AI features)*
**Golden set size:** [N labeled examples, e.g., N=200]
**Label source:** [human-rated / expert-curated / production-sampled / synthetic]
**Aggregate metric & bar:** [metric over the set, e.g., precision ≥ 0.9 over N=200, 0 unsafe outputs over N=50, p95 latency < 2s]
**Judging method:** [human rubric / automated metric / LLM-as-judge]

> Assert the aggregate metric over the golden set, not per-row exact matches. The rows below are illustrative slices, not the pass/fail unit.

| ID | Input slice | Expected behavior | Aggregate assertion | Priority |
|---|---|---|---|---|
| ML-1 | [typical queries] | [acceptable outputs] | [precision/relevance ≥ bar over N] | P0 |
| ML-2 | [ambiguous inputs] | [reasonable interpretations] | [hallucination rate ≤ bar over N] | P1 |
| ML-3 | [adversarial / unsafe prompts] | [refusal / safe handling] | [0 policy violations over N] | P0 |

## Coverage gaps
- [Acceptance criterion with no covering scenario — flag for follow-up]
```

## Avoid (anti-patterns)
- **Happy-path tunnel vision** — writing five variations of the success flow and one error case. Most defects live in error and data-variation rows; weight your coverage there.
- **Restating the spec as a test** — "Verify the button works" is not a scenario. Every row needs a concrete input, action, and observable expected result.
- **Exact-match assertions on ML output** — asserting a generated/ranked output equals a fixed string. Use quality bars and ranges; probabilistic features fail deterministic tests for the wrong reasons.
- **Boundary-blindness** — testing "a number" instead of zero, negative, max, and max+1. Off-by-one and overflow bugs hide exactly at the edges you skipped.
- **Orphan scenarios** — test cases that don't trace to an acceptance criterion, and criteria with no test. Both are coverage holes; the traceability column exists to expose them.

## Tips
- Build the input list first, then mechanically apply the four lenses (boundary, empty/null, type, format) to each input — coverage falls out instead of relying on inspiration.
- Write the expected result as something a tester can *observe* without reading the code: a message, a stored value, a status, a redirect.
- For ML features, lock a small golden eval set early and re-run it on every model/prompt change — it's your regression net against silent quality drift.
- Sort by priority, not by category: a P0 error path matters more than a P2 happy-path variation, and a triaging team should see the must-pass set first.
