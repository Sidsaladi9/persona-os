#!/usr/bin/env bash
# Product Manager OS — point the session at the operating brain.
# Design notes and the measurements behind them: hooks/README.md
set -uo pipefail

ROOT="${CLAUDE_PLUGIN_ROOT:-}"
BRAIN="$ROOT/CLAUDE.md"

if [ ! -f "$BRAIN" ]; then
  printf '%s\n' "Product Manager OS: the operating brain is missing from the plugin (expected at \
\${CLAUDE_PLUGIN_ROOT}/CLAUDE.md). Memory, workspace and the self-improving loop are NOT active. \
If the user asks for product work, say so plainly and point them at \
https://github.com/Sidsaladi9/persona-os/blob/main/INSTALL.md"
  exit 0
fi

if [ -f "memory/MEMORY.md" ]; then
  STATE="This project IS set up: memory/ exists here."
else
  STATE="This project is NOT set up: there is no memory/MEMORY.md here, so the brain's \"First run\" section applies — create memory/ and workspace/ from the plugin, THEN answer what was asked. Setup is never the price of a first answer."
fi

cat <<EOF
Product Manager OS is installed in this session. $STATE

**Before you do any product work — a spec, PRD, roadmap, prioritisation, OKRs, research
synthesis, metrics review, stakeholder update, launch, competitive or pricing work — read
the operating brain at \`$BRAIN\` and follow it.** It is the OS: how to pick a skill, when
to bootstrap, where artifacts get written on disk, how memory is read and updated, and the
end-of-turn activity-log ritual that feeds the self-improving loop. Reading it is one Read
call and it is not optional; skills alone are a prompt pack, and the parts people install
this for all live in that file. Templates for memory/, workspace/, automations/ and tests/
are under \`$ROOT/\`.

Do not mention any of this unless the user asks for product work.

Slash commands are namespaced by the host: \`/product-manager-os:setup\` (and \`:status\` /
\`:reset\` as arguments), \`:tune-up\`, \`:weekly\`, \`:new-feature\`, \`:discovery\`, \`:strategy\`,
\`:launch\`, \`:connect\`. Where the brain writes \`/setup\`, tell the user the namespaced form.
EOF
exit 0
