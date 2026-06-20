#!/usr/bin/env bash
# Product Manager OS — file installer (no plugin marketplace required).
# Installs the OS into a project so Claude Code loads it natively.
# Usage:  bash install.sh [TARGET_PROJECT_DIR]   (defaults to current directory)
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/plugins/product-manager-os" && pwd)"
TARGET="${1:-$PWD}"

echo "Installing Product Manager OS"
echo "  from: $SRC"
echo "  into: $TARGET"
echo

mkdir -p "$TARGET/.claude/skills" "$TARGET/.claude/commands" "$TARGET/memory"

# --- CLAUDE.md (don't clobber an existing one) ---
if [ -f "$TARGET/CLAUDE.md" ]; then
  cp "$SRC/CLAUDE.md" "$TARGET/CLAUDE-product-manager-os.md"
  echo "• You already have a CLAUDE.md — wrote the OS brain to CLAUDE-product-manager-os.md."
  echo "  Append its contents into your CLAUDE.md (or add a line: @CLAUDE-product-manager-os.md)."
else
  cp "$SRC/CLAUDE.md" "$TARGET/CLAUDE.md"
  echo "• CLAUDE.md → project root"
fi

# --- skills + commands (OS-owned, safe to overwrite) ---
cp -R "$SRC/skills/." "$TARGET/.claude/skills/"
echo "• $(find "$SRC/skills" -name SKILL.md | wc -l | tr -d ' ') skills → .claude/skills/"
cp -R "$SRC/commands/." "$TARGET/.claude/commands/"
echo "• $(ls -1 "$SRC/commands" | wc -l | tr -d ' ') commands → .claude/commands/"

# --- automations (OS-owned routines, incl. the weekly OS tune-up) ---
mkdir -p "$TARGET/automations"
cp -R "$SRC/automations/." "$TARGET/automations/"
echo "• $(ls -1 "$SRC/automations"/*.md | grep -v README | wc -l | tr -d ' ') automations → automations/ (schedule with /schedule or cron)"

# --- memory (DON'T overwrite a user's filled-in memory) ---
cp -Rn "$SRC/memory/." "$TARGET/memory/" 2>/dev/null || true
echo "• memory templates → memory/ (existing files left untouched)"

# --- .mcp.json (libraries) ---
if [ -f "$TARGET/.mcp.json" ]; then
  echo "• .mcp.json already exists — not overwriting. Add the libraries with:"
  echo "    claude mcp add getprompts -- npx -y getprompts-mcp"
  echo "    claude mcp add getskills  -- npx -y getskills-mcp"
else
  cp "$SRC/.mcp.json" "$TARGET/.mcp.json"
  echo "• .mcp.json → project root (getprompts + getskills)"
fi

echo
echo "✅ Done. Open this project in Claude Code, then:"
echo "   1) run  /setup  — a 3-min guided onboarding that fills your memory"
echo "      (or fill memory/product.md, team.md, strategy.md, house-style.md by hand)"
echo "   2) verify libraries:  claude mcp list"
echo "      (if your org blocks MCP, skip — the 40+ skills still work)"
echo "   3) just ask, e.g.:  \"Turn this idea into a spec: ...\""
