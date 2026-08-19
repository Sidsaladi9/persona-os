#!/usr/bin/env bash
# Product Manager OS — file installer. No plugin marketplace, no Python required.
#
#   bash install.sh                              # Claude Code, into the current dir
#   bash install.sh ~/code/my-project            # Claude Code, into that dir
#   bash install.sh --target cursor ~/code/app   # Cursor / Codex / Gemini / any agent
#   bash install.sh --list                       # what targets exist
#
# Everything it copies is already built and committed under dist/ — this script
# just puts the right bundle in the right place and refuses to clobber your work.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$REPO/plugins/product-manager-os/dist"
TARGET_HOST="claude-code"
DEST=""

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET_HOST="${2:?--target needs a value}"; shift 2 ;;
    --list)
      echo "Targets:"
      for d in "$DIST"/*/; do echo "  $(basename "$d")"; done
      exit 0 ;;
    -h|--help) sed -n '2,10p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) DEST="$1"; shift ;;
  esac
done

DEST="${DEST:-$PWD}"
SRC="$DIST/$TARGET_HOST"

if [ ! -d "$SRC" ]; then
  echo "Unknown target '$TARGET_HOST'. Run: bash install.sh --list" >&2
  exit 1
fi

echo "Installing Product Manager OS ($TARGET_HOST)"
echo "  from: $SRC"
echo "  into: $DEST"
echo

mkdir -p "$DEST"

# The operating brief — never clobber an existing one.
ENTRY="$(ls "$SRC" | grep -E '^(CLAUDE|AGENTS|GEMINI)\.md$' | head -1)"
if [ -f "$DEST/$ENTRY" ]; then
  cp "$SRC/$ENTRY" "$DEST/${ENTRY%.md}-product-manager-os.md"
  echo "• You already have $ENTRY — wrote the OS brain to ${ENTRY%.md}-product-manager-os.md."
  echo "  Append it into yours, or reference it with: @${ENTRY%.md}-product-manager-os.md"
else
  cp "$SRC/$ENTRY" "$DEST/$ENTRY"
  echo "• $ENTRY → project root"
fi

# Everything else the bundle ships. OS-owned dirs are safe to overwrite;
# memory/ and workspace/ hold YOUR content, so never overwrite those.
for item in "$SRC"/*/ "$SRC"/.claude "$SRC"/.cursor; do
  [ -d "$item" ] || continue
  name="$(basename "$item")"
  case "$name" in
    memory|workspace)
      mkdir -p "$DEST/$name"
      cp -Rn "$item/." "$DEST/$name/" 2>/dev/null || true
      echo "• $name/ → seeded (your existing files left untouched)" ;;
    *)
      mkdir -p "$DEST/$name"
      cp -R "$item/." "$DEST/$name/"
      echo "• $name/ → installed" ;;
  esac
done

for f in COMMANDS.md WORKERS.md MCP-SETUP.md; do
  [ -f "$SRC/$f" ] && cp "$SRC/$f" "$DEST/$f" && echo "• $f → project root"
done

# MCP config goes where THIS host reads it, and never overwrites an existing one.
if [ -f "$SRC/.mcp.json" ]; then
  if [ -f "$DEST/.mcp.json" ]; then
    echo "• .mcp.json exists — not overwriting. Add the libraries with:"
    echo "    claude mcp add getprompts -- npx -y getprompts-mcp"
    echo "    claude mcp add getskills  -- npx -y getskills-mcp"
  else
    cp "$SRC/.mcp.json" "$DEST/.mcp.json"
    echo "• .mcp.json → project root (getprompts + getskills)"
  fi
elif [ -f "$SRC/.cursor/mcp.json" ] && [ ! -f "$DEST/.cursor/mcp.json" ]; then
  mkdir -p "$DEST/.cursor"
  cp "$SRC/.cursor/mcp.json" "$DEST/.cursor/mcp.json"
  echo "• .cursor/mcp.json → getprompts + getskills"
fi

N_SKILLS="$(find "$SRC" -name SKILL.md | wc -l | tr -d ' ')"
echo
echo "✅ Done — $N_SKILLS skills installed for $TARGET_HOST."
echo
echo "   1) Open this project in your agent, then run  /setup  (or just ask it to"
echo "      \"set me up\") — a 3-minute onboarding that fills memory/ so it stops"
echo "      asking you the basics. Skip it and it resumes later; nothing is lost."
echo "   2) Just describe the work:  \"Turn this idea into a spec: ...\""
echo
[ -f "$SRC/.mcp.json" ] && echo "   Optional: verify the libraries with  claude mcp list  (needs Node 18+)."
echo "   Full guide: $REPO/QUICKSTART.md"
