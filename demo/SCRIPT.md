# The 60-second demo

The single highest-converting asset for this launch. One take, no editing beyond trimming the ends.

**The story in one line:** it installs in seconds, it already knows your product, and by the end of the week it has written you a skill you didn't ask for.

**Don't demo the skill count.** Everyone has skills. Demo the loop — it's the only thing in the video a competitor can't screenshot back at you.

---

## Before you hit record

```bash
bash demo/setup-demo-env.sh ~/demo-cadence
```

That creates a clean folder with the OS installed and a **seeded activity log** — because `/tune-up` needs a 3× pattern to propose anything, and a fresh install has none. Without it the ending doesn't happen.

- Terminal at **~16pt**, plain prompt, light or dark but high contrast
- Window ~1280×800, nothing else on screen
- `cd ~/demo-cadence` and clear the scrollback before recording

---

## The shots

### 0:00–0:10 — Install

Type it, don't paste. People need to see it's one line.

```bash
claude plugin marketplace add Sidsaladi9/persona-os && claude plugin install product-manager-os@persona-os
```

**On screen:** the install completing.
**Caption:** *One command. 53 skills, free, open source.*

---

### 0:10–0:22 — It learns your product

```
/setup
```

Choose **"bootstrap from a doc"** and paste `demo/sample-prd.md`. It reads the PRD and fills `memory/` — product, users, stage, north star — without asking you to type any of it.

**On screen:** memory files being written.
**Caption:** *Paste one real doc. It never asks you the basics again.*

> This is the beat most people skip in demos and it's the one that separates you from a prompt pack. Let it breathe for two full seconds.

---

### 0:22–0:42 — Do actual work

Type this exactly — it's a real PM request, not a prompt:

```
Sales keeps asking for bulk CSV export. I think the real problem is
they can't get data out at all. Turn it into a spec.
```

**On screen:** `write-spec` fires without being named. Then — and this is the shot — the file appearing at `workspace/projects/csv-export/spec.md`.

Show the file. Two seconds is enough.

**Caption:** *You never name a skill. The artifact lands on disk, not in a chat window.*

---

### 0:42–0:58 — The part nobody else has

```
/tune-up
```

**On screen:** it reports that you've hand-rolled three launch emails with no skill firing, checks the nearest existing skill, and proposes building you a `launch-email` skill drafted from your own three examples — accept / tweak / reject.

**Caption:** *It watches the work you repeat and builds you the skill for it.*

---

### 0:58–1:00 — Card

> **Product Manager OS** — free, open source
> `github.com/Sidsaladi9/persona-os`

---

## What to cut if you run long

In order: the install caption, the file-open shot, the `/setup` path choice. **Never cut `/tune-up`** — it's the whole reason the video exists.

## What not to do

- **No voiceover.** Captions only. It gets watched on mute.
- **No slides, no logo animation.** The terminal is the product.
- **Don't speed up the typing.** Fake-fast typing reads as fake.
- **Don't stage a failure recovery.** Cute, and it costs you the 60 seconds you have.
