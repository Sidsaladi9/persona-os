#!/usr/bin/env bash
# Build a clean, recordable demo environment.
#
#   bash demo/setup-demo-env.sh ~/demo-cadence
#
# Why this exists: /tune-up only proposes something when it finds a 3x pattern in
# the activity log, and a fresh install has an empty one. Without a seeded log the
# closing shot — the part of the demo that matters — simply doesn't happen.
#
# The seeded log is clearly labelled as demo data. It represents a real usage
# pattern (three hand-rolled launch emails); it is not a fabricated result.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-$HOME/demo-cadence}"

if [ -e "$DEST" ]; then
  printf 'Destination exists: %s\nDelete it and start clean? [y/N] ' "$DEST"
  read -r r; case "$r" in [yY]*) rm -rf "$DEST" ;; *) echo "Stopped."; exit 1 ;; esac
fi

mkdir -p "$DEST"
bash "$REPO/install.sh" --target claude-code "$DEST" > /dev/null
echo "• OS installed"

# --- memory left INTENTIONALLY EMPTY: /setup filling it is shot 2 -------------

# --- the activity log, seeded so /tune-up has something true to find ----------
cat > "$DEST/memory/activity-log.md" <<'LOG'
# Activity Log

> One line per meaningful task. Read by `/tune-up`, never sent anywhere.
>
> ⚠️ DEMO DATA — seeded by demo/setup-demo-env.sh so `/tune-up` has a pattern to
> find on camera. Delete this file before using this folder for real work.

## Log
- 2026-08-04 · asked: "draft the launch email for the v3 pricing change" · skill: none · correction: none
- 2026-08-05 · asked: "prioritize the Q3 backlog against retention" · skill: prioritize · correction: none
- 2026-08-07 · asked: "summarize the customer advisory board call" · skill: meeting-notes · correction: "shorter, decisions only"
- 2026-08-11 · asked: "write the launch email for the mobile beta" · skill: none · correction: none
- 2026-08-12 · asked: "why did activation drop last week" · skill: metrics-review · correction: none
- 2026-08-14 · asked: "cohort read on the March signups" · skill: cohort-analysis · correction: none
- 2026-08-18 · asked: "launch email for the API rate-limit change" · skill: none · correction: none
LOG
echo "• activity log seeded — 3x 'launch email' with no skill firing"

# --- a real-looking PRD to paste into /setup ---------------------------------
cp "$REPO/demo/sample-prd.md" "$DEST/sample-prd.md"
echo "• sample-prd.md placed (paste this into /setup)"

cat <<DONE

Ready. Before you record:

  cd $DEST
  clear

Shot 1   claude plugin marketplace add ... (or note it's already installed here)
Shot 2   /setup  → "bootstrap from a doc" → paste sample-prd.md
Shot 3   "Sales keeps asking for bulk CSV export. I think the real problem is
          they can't get data out at all. Turn it into a spec."
Shot 4   /tune-up   ← the seeded log makes this land

Full shot list: demo/SCRIPT.md
DONE
