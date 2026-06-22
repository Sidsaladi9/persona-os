---
name: visualize
description: Turns a PM artifact into a clean, self-contained HTML visual you can open and screenshot — a RICE/Kano prioritization matrix, a Now/Next/Later roadmap board, an OKR tree, a metrics scorecard, or a journey-map swimlane. Use when you say "make this visual", "turn this into a board / matrix / chart", "render the roadmap", "show me a scorecard", "visualize this", "I want to screenshot this", or after any skill produces a structured artifact and a picture would land harder than text.
---

# Visualize

Turns the structured output of a PM skill into a **single self-contained HTML file** — no server, no build, no external fonts or CDNs — that opens in any browser and is built to be screenshotted into a deck, a Slack post, or a doc. Text artifacts inform; a clean visual *persuades* and travels. This is the skill that makes the work shareable.

It renders five PM artifacts, each with a purpose-built layout:

| Artifact | Visual | Comes from |
|---|---|---|
| Prioritization | **RICE / Kano matrix** (impact × effort quadrant, or ranked bars) | `prioritize` |
| Roadmap | **Now / Next / Later board** (3 columns of cards) | `roadmap` |
| OKRs | **Objective → Key Result tree** with progress bars | `okrs` |
| Metrics | **Scorecard** of KPI cards with trend arrows + 🟢🟡🔴 status | `metrics-review` |
| Journey | **Swimlane** (stages × actions / thoughts / pains / opportunities) | `journey-map` |

## When to use this
- A skill just produced a prioritization, roadmap, OKR set, metrics review, or journey map and you want a picture, not a table.
- You're prepping a deck, a leadership update, or a Slack/Notion post and need a screenshot-ready visual.
- Someone says "can you make this a board / matrix / scorecard / chart" or "visualize this."
- You want the artifact to travel — a RICE matrix lands in a planning review far harder than a markdown table.

## Before you start (gather these)
- **The artifact + its data** — the prioritized list (with RICE/Kano scores), the roadmap items by horizon, the OKRs with progress, the metrics with current/prior/target, or the journey stages. If a sibling skill just produced it, use that output directly.
- **Which visual** — infer it from the artifact type; if genuinely ambiguous, ask once. Don't render a roadmap as a matrix.
- **House style** — if `memory/house-style.md` defines brand colors/fonts, use them via the CSS variables below so the visual looks like the company's, not generic.

If you have the structured data, **proceed and render** — don't make the user reformat it for you. If the data is missing scores/values a widget needs (e.g. RICE numbers), fill what you can and clearly mark gaps in the visual rather than inventing numbers.

## Process
1. **Pick the widget** from the artifact type (table above). One artifact → one focused visual; don't cram two.
2. **Map the data into the widget's structure** — e.g. for the matrix, each item needs an x (effort) and y (impact); for the board, each card needs a title, horizon, and one-line why.
3. **Build ONE self-contained `.html` file** using the design system and the matching template below. Inline every style. No `<script src>`, no Google Fonts, no CDN — it must render offline and survive being emailed.
4. **Apply house style** if defined — override the CSS variables only; keep the structure.
5. **Write it to the project** at `./<artifact>-<slug>.html` (e.g. `roadmap-q3.html`), then tell the user the path and that they can open it in a browser and screenshot it. Offer to adjust colors/labels.
6. **Never invent data to fill the picture.** A visual makes numbers look authoritative — only render what's real; mark estimates with a `~` and unknowns as `—`.

## Design system (use for every widget)
Put this in a `<style>` block; override the `:root` variables from `house-style.md` if it defines brand colors.
```css
:root{
  --ink:#0f172a; --muted:#64748b; --line:#e2e8f0; --bg:#ffffff; --surface:#f8fafc;
  --accent:#4f46e5; --good:#16a34a; --warn:#d97706; --bad:#dc2626;
  --radius:12px; --shadow:0 1px 3px rgba(15,23,42,.08),0 1px 2px rgba(15,23,42,.04);
  --font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);
  line-height:1.45;padding:32px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1040px;margin:0 auto}
h1{font-size:22px;margin:0 0 4px} .sub{color:var(--muted);font-size:13px;margin:0 0 24px}
.foot{color:var(--muted);font-size:12px;margin-top:28px;border-top:1px solid var(--line);padding-top:12px}
.card{background:var(--bg);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow)}
```
Every file: a `.wrap` container, an `<h1>` title + `.sub` line (artifact + date + product), the widget, and a `.foot` credit line ("Product Manager OS · The Product Channel"). Keep it calm and uncluttered — whitespace is the point.

## Output template (worked: Now / Next / Later board)
This is the reference build — the other widgets follow the same shell, swapping the widget block. Fill `[brackets]`.
```html
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>[Product] — Roadmap</title>
<style>
:root{--ink:#0f172a;--muted:#64748b;--line:#e2e8f0;--bg:#fff;--surface:#f8fafc;--accent:#4f46e5;--good:#16a34a;--warn:#d97706;--bad:#dc2626;--radius:12px;--shadow:0 1px 3px rgba(15,23,42,.08),0 1px 2px rgba(15,23,42,.04);--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);line-height:1.45;padding:32px}
.wrap{max-width:1040px;margin:0 auto}h1{font-size:22px;margin:0 0 4px}.sub{color:var(--muted);font-size:13px;margin:0 0 24px}
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.col h2{font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid var(--line)}
.col.now h2{color:var(--accent);border-color:var(--accent)}
.item{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.item .t{font-weight:600;font-size:14px}.item .w{color:var(--muted);font-size:12.5px;margin-top:3px}
.tag{display:inline-block;font-size:11px;color:var(--accent);background:#eef2ff;border-radius:6px;padding:2px 7px;margin-top:8px}
.foot{color:var(--muted);font-size:12px;margin-top:28px;border-top:1px solid var(--line);padding-top:12px}
</style></head><body><div class="wrap">
<h1>[Product] — Roadmap</h1><p class="sub">Now / Next / Later · [date]</p>
<div class="board">
  <div class="col now"><h2>Now</h2>
    <div class="item"><div class="t">[Item]</div><div class="w">[why it's now]</div><span class="tag">[outcome]</span></div>
  </div>
  <div class="col"><h2>Next</h2>
    <div class="item"><div class="t">[Item]</div><div class="w">[why]</div></div>
  </div>
  <div class="col"><h2>Later</h2>
    <div class="item"><div class="t">[Item]</div><div class="w">[why]</div></div>
  </div>
</div>
<p class="foot">Product Manager OS · The Product Channel</p>
</div></body></html>
```

### The other four widgets (same shell, swap the block)
- **RICE/Kano matrix** — a `position:relative` square plot (`.plot{aspect-ratio:1;border-left:2px solid var(--line);border-bottom:2px solid var(--line)}`); place each item as an absolutely-positioned dot (`left:%effort`, `bottom:%impact`) with a label; axis captions "Effort →" / "Impact ↑"; top-left quadrant tinted as "quick wins." Fallback when no x/y: horizontal **ranked bars** of RICE score.
- **OKR tree** — each Objective is a `.card` with its title, then nested Key Results as rows, each with a label and a progress bar (`.bar{height:8px;background:var(--line);border-radius:4px} .bar>i{display:block;height:100%;background:var(--accent);border-radius:4px;width:[pct]%}`) and a `[current]/[target]` value. Color the bar `--good/--warn/--bad` by pace.
- **Metrics scorecard** — a responsive grid (`grid-template-columns:repeat(auto-fit,minmax(180px,1fr))`) of `.card`s: metric name, big current value, a trend chip (`▲`/`▼` colored by good direction) vs prior, target underneath, and a left border in `--good/--warn/--bad` for 🟢/🟡/🔴 status.
- **Journey swimlane** — a CSS grid: columns = stages, rows = "Doing / Thinking / Feeling / Pain / Opportunity." First column is sticky row labels. Put an emoji emotion (😀😐😣) in the Feeling row; tint Pain cells faint red and Opportunity cells faint green so the problem areas pop.

## Avoid (anti-patterns)
- **External dependencies.** A Google-Fonts link or a Chart.js CDN means it breaks offline and on a plane and behind a firewall. Inline everything — the file must work double-clicked from a USB stick.
- **Inventing data to make it look complete.** A blank cell is honest; a made-up RICE score in a polished matrix is a lie with a nice font. Mark gaps `—`.
- **Cramming two artifacts into one file.** A roadmap *and* a scorecard in one page reads as a cluttered dashboard. One artifact, one focused visual; render two files if asked.
- **Chartjunk.** Gradients, drop shadows on everything, 3D, rainbow categorical colors. The design system is deliberately calm — restraint is what makes it look senior.
- **Wrong widget for the data.** A roadmap is a board, not a matrix; OKRs are a tree, not a bar chart. Match the structure to the artifact.

## Tips
- **Build for the screenshot.** Keep it to one viewport-ish height where you can, generous margins, big readable type — assume it ends up cropped into a slide.
- **Lead the eye.** Accent-color only the one thing that matters (the "Now" column, the quick-wins quadrant, the red metric); everything else stays neutral.
- **Reuse the shell.** Title + sub + widget + foot is constant; only the middle block changes. That consistency is what makes a deck of these look like one product.
- **Offer the follow-up.** After rendering, ask if they want it in brand colors (pull from `house-style.md`) or a second view — a screenshot beats a paragraph in 90% of PM comms.
