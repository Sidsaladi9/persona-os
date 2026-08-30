#!/usr/bin/env bash
# Product Manager OS — one-step installer.
#
#   curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh | bash -s -- cursor
#
# Installs into the CURRENT directory. Detects your tool if you don't name one.
# No git required. Nothing is installed system-wide and nothing runs after this exits.
#
# Rather not pipe a script from the internet into bash? Good instinct:
#   curl -fsSLO https://raw.githubusercontent.com/Sidsaladi9/persona-os/main/get.sh
#   less get.sh && bash get.sh cursor
set -euo pipefail

REPO="${PERSONA_OS_REPO:-Sidsaladi9/persona-os}"
REF="${PERSONA_OS_REF:-main}"
SRC_OVERRIDE="${PERSONA_OS_SRC:-}"     # local checkout, for testing
DEST="$PWD"
TARGET="${1:-}"

say() { printf '%s\n' "$*"; }
die() { printf '\n✗ %s\n' "$*" >&2; exit 1; }

# ── which tool? ───────────────────────────────────────────────────────────────
# Collect EVERY host signal present, not the first one in an arbitrary order.
# The old version returned on the first hit with Claude ahead of Codex, so any
# folder that had ever run Claude Code — which is most of them — silently got
# the Claude bundle even when AGENTS.md was sitting right there. Guessing wrong
# here installs the wrong entry file and the wrong skills path, and the user
# finds out when nothing loads.
detect_all() {
  local found=""
  [ -d ".cursor" ]                       && found="$found cursor"
  { [ -f "GEMINI.md" ] || [ -d ".gemini" ]; } && found="$found gemini-cli"
  { [ -d ".claude" ] || [ -f "CLAUDE.md" ]; } && found="$found claude-code"
  [ -f "AGENTS.md" ]                     && found="$found codex"
  echo "${found# }"
}

if [ -z "$TARGET" ]; then
  FOUND="$(detect_all)"
  COUNT=$(printf '%s\n' $FOUND | grep -c . || true)
  if [ "$COUNT" -gt 1 ]; then
    say "This folder has signals for more than one tool:$(printf ' %s' $FOUND)"
    say
    say "I won't guess — the wrong bundle installs the wrong entry file and the"
    say "wrong skills path, and you'd find out when nothing loads. Name the one"
    say "you actually use:"
    say
    for t in $FOUND; do say "  bash get.sh $t"; done
    say
    die "Stopped. Nothing was written."
  elif [ "$COUNT" -eq 1 ]; then
    TARGET="$FOUND"
    say "No tool given — detected: $TARGET"
  else
    TARGET="claude-code"
    say "No tool given and no signals in this folder — defaulting to: $TARGET"
  fi
  say "(override with:  bash get.sh <claude-code|claude-cowork|codex|cursor|gemini-cli|generic>)"
  say
fi

# ── sanity-check the destination ──────────────────────────────────────────────
case "$DEST" in
  "$HOME"|"$HOME/Downloads"|"$HOME/Desktop"|/tmp|/tmp/*|/)
    say "⚠️  You're installing into: $DEST"
    say "   This folder becomes your product brain — months of specs, research, and"
    say "   strategy will live here. A dedicated folder is a much better home:"
    say
    say "     mkdir ~/product-work && cd ~/product-work"
    say
    reply="n"
    if printf '   Continue here anyway? [y/N] ' && read -r reply < /dev/tty 2>/dev/null; then
      :
    else
      # Non-interactive (piped into bash, CI). Declining is the safe default.
      say ""
      say "   (no terminal available to ask — declining by default)"
      reply="n"
    fi
    case "$reply" in
      [yY]*) ;;
      *) die "Stopped. Nothing was written. Re-run from a folder you have chosen for this." ;;
    esac
    say ;;
esac

# ── fetch ─────────────────────────────────────────────────────────────────────
if [ -n "$SRC_OVERRIDE" ]; then
  SRC="$SRC_OVERRIDE"
  CLEANUP=""
else
  command -v curl >/dev/null 2>&1 || die "curl is required."
  command -v tar  >/dev/null 2>&1 || die "tar is required."
  TMP="$(mktemp -d)"
  CLEANUP="$TMP"
  trap 'rm -rf "$CLEANUP"' EXIT
  say "Downloading Product Manager OS…"
  curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/$REF" \
    | tar -xz -C "$TMP" || die "Download failed. Check your connection, or install from the repo directly."
  SRC="$(find "$TMP" -maxdepth 1 -type d -name 'persona-os-*' | head -1)"
  [ -n "$SRC" ] || die "Unexpected archive layout — please install from the repo directly."
fi

[ -d "$SRC/plugins/product-manager-os/dist/$TARGET" ] \
  || die "Unknown target '$TARGET'. Options: $(ls "$SRC/plugins/product-manager-os/dist" | tr '\n' ' ')"

# ── install ───────────────────────────────────────────────────────────────────
bash "$SRC/install.sh" --target "$TARGET" "$DEST"
