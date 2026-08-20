# Live test — 20 minutes, before you record or launch

The automated suite proves the files are right. It cannot prove the OS *behaves*.
This does. Every step has a pass condition; if one fails, stop and fix it rather
than launching around it.

Run it in a throwaway folder, not your real work.

```bash
mkdir ~/pmos-livetest && cd ~/pmos-livetest
```

---

## 1. Install — 2 min

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

Restart Claude Code in that folder.

**Pass:** no errors, and `/setup` appears when you type `/`.
**This is the path with zero automated coverage** — everything else has been verified from CI.

---

## 2. Bootstrap — 2 min

Ask for something real *before* running setup. This tests the first-run trigger.

```
Turn this into a spec: sales keeps asking for bulk CSV export, but I think the
real problem is they can't get data out at all.
```

**Pass, all four:**
- [ ] It creates `memory/` and `workspace/` (they don't exist on a plugin install)
- [ ] It answers the question. Setup is not the price of a first answer
- [ ] `write-spec` fires without you naming it
- [ ] The spec lands at `workspace/projects/<slug>/spec.md`

**Fail signals:** it asks you to run `/setup` first; it writes nothing to disk; it asks which skill to use.

---

## 3. Onboarding — 3 min

```
/setup
```

Choose **bootstrap from a doc** and paste `demo/sample-prd.md` (or a real PRD).

**Pass:**
- [ ] It fills `memory/product.md`, `team.md`, `strategy.md` from the doc without interrogating you
- [ ] `memory/onboarding.md` coverage count goes up
- [ ] It picks up house style (sentence-case headings, "teams" not "customers")

Then:

```
/setup status
```

**Pass:** shows what it knows and what's missing. Does not re-ask answered questions.

---

## 4. Does memory actually get used — 3 min

```
Draft a leadership update on where the CSV export work stands.
```

**Pass:** it uses your product name, your north-star metric, and your format **without you pasting any of it**. That is the entire value proposition. If it asks you what your product is, memory is not being read and nothing else matters.

---

## 5. The workers — 3 min

```
Red-team that spec.
```

**Pass:**
- [ ] It says it's handing the artifact to `critic`
- [ ] The critique names a load-bearing assumption and ranks findings fatal / serious / minor
- [ ] It does **not** simply agree with the spec it just wrote

---

## 6. The loop — 5 min ⬅ the headline claim

Seed a pattern the way a real week would:

```
Draft a launch email for the v3 pricing change.
```
```
Write the launch email for the mobile beta.
```
```
Launch email for the API rate-limit change.
```

Check `memory/activity-log.md` — three lines, each `skill: none`.

```
/tune-up
```

**Pass, all four:**
- [ ] It spots the 3× pattern
- [ ] It names the nearest existing skill and says why that one doesn't cover it (anti-bloat check)
- [ ] It proposes a new skill drafted from *your three examples*, not a template
- [ ] It waits for accept / tweak / reject rather than just doing it

**If this fails, do not launch.** It is the one claim no competitor can make, and the whole demo is built on it.

---

## 7. Libraries — 2 min

```bash
claude mcp list
```

**Pass:** `getprompts` and `getskills` both show **Connected**. Needs Node 18+.
If your org blocks MCP, note it and move on — all 53 skills work without them.

---

## 8. Clean up

```bash
cd ~ && rm -rf ~/pmos-livetest
```

---

## Scorecard

| # | Test | Pass? |
|---|---|---|
| 1 | Plugin installs | |
| 2 | Bootstraps + answers first, skill fires, artifact lands | |
| 3 | `/setup` fills memory from a doc; `status` works | |
| 4 | Memory is actually used in later work | |
| 5 | `critic` gives an independent critique | |
| 6 | **`/tune-up` proposes a skill from a 3× pattern** | |
| 7 | Both MCPs connected | |

**6 is the gate.** Everything else can be patched post-launch. That one is the product.
