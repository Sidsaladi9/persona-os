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
detect() {
  [ -d ".cursor" ]                   && { echo cursor;        return; }
  [ -f "GEMINI.md" ] || [ -d ".gemini" ] && { echo gemini-cli; return; }
  [ -d ".claude" ] || [ -f "CLAUDE.md" ] && { echo claude-code; return; }
  [ -f "AGENTS.md" ]                 && { echo codex;         return; }
  echo claude-code
}

if [ -z "$TARGET" ]; then
  TARGET="$(detect)"
  say "No tool given — detected: $TARGET"
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
