# Automations — Product Manager OS

These are **ready-to-wire routines** for a standard PM week. Each one is a prompt you can run on a schedule so Claude does the prep before you ask.

You don't need any of them to use the OS — they're leverage on top. Pick the ones that fit your week and wire them up.

## How to schedule them

You have three options, easiest first:

### 1. Claude Code scheduled tasks / routines (recommended)
If you're on Claude Code, ask Claude:

> "Schedule the Friday metrics review automation in `automations/weekly-metrics-review.md` to run every Friday at 9am."

Claude will set up a recurring cloud agent that runs the prompt on schedule. Manage them anytime with `/schedule`.

### 2. cron (any machine with the Claude CLI)
Each automation file is a self-contained prompt. Run it headless:

```bash
claude -p "$(cat automations/weekly-metrics-review.md)"
```

Then add a cron entry (`crontab -e`):

```cron
# Friday 9am — weekly metrics scorecard + stakeholder draft
0 9 * * 5  cd /path/to/your/project && claude -p "$(cat automations/weekly-metrics-review.md)" >> logs/metrics-review.log 2>&1
```

### 3. Manual (no setup)
Just paste the contents of any automation file into Claude when you want it. The schedule is optional — the prompt is the value.

## The routines

| File | Cadence | What it does |
|---|---|---|
| `sprint-kickoff.md` | Start of each sprint | Pulls the backlog, drafts a sprint plan with a goal, flags risks. |
| `weekly-metrics-review.md` | Weekly (e.g. Friday) | Builds a metrics scorecard and a leadership update draft. |
| `daily-standup.md` | Daily | Summarizes what moved into a standup-ready update. |
| `weekly-os-tuneup.md` | Weekly (e.g. Sunday) | Reads your activity log, finds work you repeat, and proposes new/tuned skills for you to accept or reject. This is how the OS improves itself. Also runnable on demand with `/tune-up`. |

> Tip: connectors make these auto-magic. With Linear/Jira connected, sprint-kickoff pulls real issues. With Amplitude/Mixpanel connected, the metrics review pulls real numbers. Without them, the routine will ask you to paste the data — still useful, just not hands-free.
