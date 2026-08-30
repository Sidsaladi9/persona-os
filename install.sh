#!/usr/bin/env bash
# Product Manager OS — file installer. No plugin marketplace, no Python required.
#
#   bash install.sh                              # Claude Code, into the current dir
#   bash install.sh ~/code/my-project            # Claude Code, into that dir
#   bash install.sh --target cursor ~/code/app   # Cursor / Codex / Gemini / any agent
#   bash install.sh --list                       # what targets exist
#   bash install.sh --force ...                  # overwrite files that collide
#
# Everything it copies is already built and committed under dist/ — this script
# just puts the right bundle in the right place and refuses to clobber your work.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$REPO/plugins/product-manager-os/dist"
TARGET_HOST="claude-code"
DEST=""
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET_HOST="${2:?--target needs a value}"; shift 2 ;;
    --force) FORCE=1; shift ;;
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

COLLIDE=""
ENTRY_PRE="$(ls "$SRC" | grep -E '^(CLAUDE|AGENTS|GEMINI)\.md$' | head -1)"
if [ -f "$DEST/$ENTRY_PRE" ] \
   && ! head -1 "$DEST/$ENTRY_PRE" | grep -qF "# Product Manager OS" \
   && ! cmp -s "$SRC/$ENTRY_PRE" "$DEST/$ENTRY_PRE"; then
  : # someone else's brief — handled below by writing ours beside it, not a collision
fi
for item in "$SRC"/*/ "$SRC"/.claude "$SRC"/.cursor; do
  [ -d "$item" ] || continue
  name="$(basename "$item")"
  case "$name" in memory|workspace) continue ;; esac
  [ -d "$DEST/$name" ] || continue
  while IFS= read -r rel; do
    [ -f "$DEST/$name/$rel" ] || continue
    cmp -s "$item/$rel" "$DEST/$name/$rel" && continue   # identical: a re-install
    COLLIDE="$COLLIDE  $name/$rel
"
  done <<EOF
$(cd "$item" && find . -type f | sed 's|^\./||')
EOF
done

if [ -n "$COLLIDE" ] && [ "$FORCE" != "1" ]; then
  printf '\n✗ Stopped. These files already exist here and differ from what the OS ships:\n\n'
  printf '%s' "$COLLIDE"
  printf '\nNothing was written. Your files are untouched.\n\n'
  printf 'Pick one:\n'
  printf '  • install into a folder of its own    (recommended)\n'
  printf '  • bash install.sh --force --target %s %s   (overwrites the files above)\n\n' "$TARGET_HOST" "$DEST"
  exit 1
fi


# The operating brief — never clobber someone else's, but do update our own.
# Re-running the installer to upgrade is the common case; without the identity
# check below it left the user with two brains, both loaded, both ~8k tokens,
# neither obviously authoritative.
ENTRY="$(ls "$SRC" | grep -E '^(CLAUDE|AGENTS|GEMINI)\.md$' | head -1)"
BRAIN_MARK="# Product Manager OS"
if [ ! -f "$DEST/$ENTRY" ]; then
  cp "$SRC/$ENTRY" "$DEST/$ENTRY"
  echo "• $ENTRY → project root"
elif head -1 "$DEST/$ENTRY" | grep -qF "$BRAIN_MARK"; then
  # It's ours from a previous install. Upgrade in place.
  if cmp -s "$SRC/$ENTRY" "$DEST/$ENTRY"; then
    echo "• $ENTRY → already current"
  else
    cp "$SRC/$ENTRY" "$DEST/$ENTRY"
    echo "• $ENTRY → updated in place (it was a previous version of the OS brain)"
  fi
  # Clean up the redundant sidecar an older installer may have left behind.
  SIDE="$DEST/${ENTRY%.md}-product-manager-os.md"
  if [ -f "$SIDE" ] && head -1 "$SIDE" | grep -qF "$BRAIN_MARK"; then
    rm -f "$SIDE"
    echo "• removed the duplicate ${ENTRY%.md}-product-manager-os.md left by an earlier install"
  fi
else
  # Someone else's brief. Leave it completely alone.
  cp "$SRC/$ENTRY" "$DEST/${ENTRY%.md}-product-manager-os.md"
  echo "• You already have $ENTRY — wrote the OS brain to ${ENTRY%.md}-product-manager-os.md."
  echo "  Append it into yours, or reference it with: @${ENTRY%.md}-product-manager-os.md"
fi

# Everything else the bundle ships. memory/ and workspace/ hold YOUR content and
# are only ever seeded. The rest are OS-owned — but "OS-owned" is a claim about
# OUR files, not about the folder. On the codex/gemini/generic bundles the OS
# writes a top-level skills/, and plenty of people already have one of their own
# there. A plain `cp -R` would overwrite a same-named file without a word.
# So: find the collisions first, and refuse rather than clobber.
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
# $REPO may be a throwaway temp dir when we were fetched by get.sh, so point at
# the canonical URL — a path that stops existing the moment the script ends is
# worse than no path at all.
if [ -f "$REPO/INSTALL.md" ] && [ -d "$REPO/.git" ]; then
  echo "   Full guide: $REPO/INSTALL.md"
else
  echo "   Full guide: https://github.com/Sidsaladi9/persona-os/blob/main/INSTALL.md"
fi
