#!/usr/bin/env python3
"""
Build Product Manager OS for every agent that can run it.

The 53 skills are plain markdown with YAML frontmatter — that part is already
portable. What is not portable is the packaging: where each agent looks for its
entry file, whether it supports slash commands, and whether it speaks MCP.
This script emits a correct bundle per target instead of telling people to
"copy the folder and figure it out."

  python3 scripts/build_targets.py            # build every target into dist/
  python3 scripts/build_targets.py --target codex
  python3 scripts/build_targets.py --list
  python3 scripts/build_targets.py --clean

Nothing here is generated from a template that could drift: the skills, the
brain, and the commands are copied from the single source of truth in this
plugin. Run the test suite before building.
"""
import argparse
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

# skills_dir      — where that agent loads skills from
# entry           — the filename it reads as its operating brief
# commands        — native slash commands, or "inline" (folded into a COMMANDS doc)
# mcp             — where THIS host reads MCP config, or None. Dropping
#                   .mcp.json at the project root only works for Claude hosts;
#                   shipping it elsewhere looks like it works and silently does not.
# agents          — target dir for the critic/researcher subagents, or None if the
#                   host has no subagent concept (then they're described, not shipped)
TARGETS = {
    "claude-code": dict(
        mcp_path=".mcp.json",
        agents=".claude/agents",
        label="Claude Code",
        skills_dir=".claude/skills", entry="CLAUDE.md",
        commands=".claude/commands", mcp=True,
        install=("Copy the contents of this folder into your project root.\n"
                 "Claude Code loads `CLAUDE.md`, `.claude/skills/`, `.claude/commands/`\n"
                 "and `.mcp.json` automatically — nothing to configure."),
    ),
    "claude-cowork": dict(
        mcp_path=".mcp.json",
        agents="agents",
        label="Claude Cowork",
        skills_dir="skills", entry="CLAUDE.md",
        commands="commands", mcp=True,
        install=("In Cowork: Plugins → Personal → Add marketplace from GitHub →\n"
                 "`Sidsaladi9/persona-os`, then install `product-manager-os`.\n"
                 "This folder is the same content, for manual install."),
    ),
    "codex": dict(
        mcp_path=None,
        agents=None,
        label="Codex CLI (OpenAI)",
        skills_dir="skills", entry="AGENTS.md",
        commands="inline", mcp=True,
        install=("Copy into your project root. Codex reads `AGENTS.md` on start.\n"
                 "Slash commands are not native — the workflows are described in\n"
                 "`COMMANDS.md` and can be invoked by name in plain language\n"
                 '("run the weekly workflow").'),
    ),
    "cursor": dict(
        mcp_path=".cursor/mcp.json",
        agents=None,
        label="Cursor",
        skills_dir=".cursor/rules", entry="AGENTS.md",
        commands="inline", mcp=True,
        install=("Copy into your project root. Cursor reads `AGENTS.md`, and the\n"
                 "skills land in `.cursor/rules/` where they're picked up as rules."),
    ),
    "gemini-cli": dict(
        mcp_path=None,
        agents=None,
        label="Gemini CLI",
        skills_dir="skills", entry="GEMINI.md",
        commands="inline", mcp=True,
        install=("Copy into your project root. Gemini CLI reads `GEMINI.md`.\n"
                 "Workflows are in `COMMANDS.md`; invoke them by name."),
    ),
    "generic": dict(
        mcp_path=None,
        agents=None,
        label="Any agent (plain files)",
        skills_dir="skills", entry="AGENTS.md",
        commands="inline", mcp=False,
        install=("Point your agent at `AGENTS.md` as its system/context file and\n"
                 "give it read access to `skills/`. Everything is plain markdown."),
    ),
}

# CLAUDE.md says "Claude" and "Claude Code" throughout. Rewrite for other hosts
# rather than shipping a brief that names the wrong product.
def retarget_brain(text, target, cfg):
    if target in ("claude-code", "claude-cowork"):
        return text
    agent = {"codex": "Codex", "cursor": "Cursor",
             "gemini-cli": "Gemini", "generic": "the agent"}[target]
    out = text
    out = out.replace("Claude Code", agent)
    # "Claude reads", "Claude starts working" → the host's name
    out = re.sub(r"\bClaude\b(?! Code)", agent, out)
    # the getskills MCP writes into Claude's own skills dir; that instruction
    # does not apply on another host, so say so rather than rewriting the path
    out = out.replace(
        "`install_skill({ slug })` — write it into `~/.claude/skills/` so it's loaded next session.",
        "`install_skill({ slug })` — fetches a skill's full body. (The one-click install "
        f"writes into Claude's skills directory; on {agent} you save the returned body into "
        f"`{cfg['skills_dir']}/` yourself.)")
    out = out.replace(".claude/skills/", f"{cfg['skills_dir']}/")
    if cfg["commands"] == "inline":
        out = out.replace(
            "**Flagship workflows (slash commands).**",
            "**Flagship workflows.** (This host has no native slash commands — "
            "the user invokes these by name, e.g. *\"run the weekly workflow\"*. "
            "Full definitions are in `COMMANDS.md`.)\n\n**Workflows.**")
    return out


def commands_doc(cfg):
    """Fold the slash commands into one markdown file for hosts without them."""
    cdir = os.path.join(ROOT, "commands")
    parts = [
        "# Workflows",
        "",
        "This host has no native slash commands. Each workflow below is a "
        "multi-step process the agent should run when the user asks for it by "
        "name — *\"run setup\"*, *\"do the weekly\"*, *\"new feature: dark mode\"*.",
        "",
    ]
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith(".md"):
            continue
        name = fn[:-3]
        body = open(os.path.join(cdir, fn), encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", body, re.S)
        desc = ""
        if m:
            d = re.search(r"^description:\s*(.+)$", m.group(1), re.M)
            desc = d.group(1).strip() if d else ""
            body = m.group(2)
        parts += [f"## `{name}`", "", f"> {desc}" if desc else "", "", body.strip(), "", "---", ""]
    return "\n".join(parts)


def build(target):
    cfg = TARGETS[target]
    out = os.path.join(DIST, target)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out, exist_ok=True)

    # skills — the portable core
    dst_skills = os.path.join(out, cfg["skills_dir"])
    shutil.copytree(os.path.join(ROOT, "skills"), dst_skills)
    n_skills = len([d for d in os.listdir(dst_skills)
                    if os.path.isdir(os.path.join(dst_skills, d))])

    # brain, retargeted
    brain = open(os.path.join(ROOT, "CLAUDE.md"), encoding="utf-8").read()
    open(os.path.join(out, cfg["entry"]), "w", encoding="utf-8").write(
        retarget_brain(brain, target, cfg))

    # commands
    if cfg["commands"] == "inline":
        open(os.path.join(out, "COMMANDS.md"), "w", encoding="utf-8").write(commands_doc(cfg))
        n_cmds = "inline"
    else:
        shutil.copytree(os.path.join(ROOT, "commands"), os.path.join(out, cfg["commands"]))
        n_cmds = len([f for f in os.listdir(os.path.join(ROOT, "commands")) if f.endswith(".md")])

    # memory + workspace scaffolding travel with every target
    shutil.copytree(os.path.join(ROOT, "memory"), os.path.join(out, "memory"))
    ws_src, ws_dst = os.path.join(ROOT, "workspace"), os.path.join(out, "workspace")
    os.makedirs(ws_dst, exist_ok=True)
    for item in os.listdir(ws_src):
        s = os.path.join(ws_src, item)
        if os.path.isdir(s):
            os.makedirs(os.path.join(ws_dst, item), exist_ok=True)
            open(os.path.join(ws_dst, item, ".gitkeep"), "w").close()
            tpl = os.path.join(s, "TEMPLATE.md")
            if os.path.isfile(tpl):
                shutil.copy2(tpl, os.path.join(ws_dst, item, "TEMPLATE.md"))
        elif item == "README.md":
            shutil.copy2(s, os.path.join(ws_dst, item))

    if cfg["mcp"] and cfg["mcp_path"]:
        dst = os.path.join(out, cfg["mcp_path"])
        os.makedirs(os.path.dirname(dst) or out, exist_ok=True)
        shutil.copy2(os.path.join(ROOT, ".mcp.json"), dst)
        mcp_note = f"`{cfg['mcp_path']}` — loads automatically"
    elif cfg["mcp"]:
        # This host speaks MCP but reads its config somewhere we shouldn't guess at.
        # Give the server definition and let the user put it where their version wants.
        open(os.path.join(out, "MCP-SETUP.md"), "w", encoding="utf-8").write(
            "# Bundled libraries (optional)\n\n"
            "The OS works fully without these. They add live access to "
            "[getprompts](https://getprompts.org) (900+ PM prompts) and "
            "[getskills](https://getskillsai.org) (3,000+ installable skills).\n\n"
            "Two zero-config public npm packages — no account, no API key, read-only:\n\n"
            "```\nnpx -y getprompts-mcp\nnpx -y getskills-mcp\n```\n\n"
            "**Where to put this depends on your host, and the path moves between "
            "versions — check your host's current MCP docs rather than trusting a path "
            "written here.** The server definition itself is what you need:\n\n"
            "```json\n"
            '{\n  "mcpServers": {\n'
            '    "getprompts": { "command": "npx", "args": ["-y", "getprompts-mcp"] },\n'
            '    "getskills":  { "command": "npx", "args": ["-y", "getskills-mcp"] }\n'
            "  }\n}\n```\n\n"
            "Needs Node 18+. If your org blocks MCP servers, skip this entirely — all 53 "
            "skills work without them.\n")
        mcp_note = "`MCP-SETUP.md` — this host's MCP config path varies, so the server definition ships instead"
    else:
        mcp_note = "not included — this target has no MCP support"

    # subagents: ship them where the host understands them, describe them where it doesn't
    if cfg["agents"]:
        shutil.copytree(os.path.join(ROOT, "agents"), os.path.join(out, cfg["agents"]))
        agents_note = f"`{cfg['agents']}/` (critic + researcher)"
    else:
        note = ["# Workers", "",
                "This host has no subagent concept, so `critic` and `researcher` are not "
                "shipped as separate definitions. Nine skills reference them.", "",
                "**Emulate them where you can:** open a fresh session, paste only the "
                "artifact (for `critic`) or one slice of the corpus (for `researcher`), and "
                "follow the brief below. The isolation is the whole point — a critique run "
                "in the context that produced the document is a self-review, and should be "
                "labelled as one.", ""]
        for fn in sorted(os.listdir(os.path.join(ROOT, "agents"))):
            body = open(os.path.join(ROOT, "agents", fn), encoding="utf-8").read()
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", body, re.S)
            if m:
                body = m.group(2)
            note += [f"## `{fn[:-3]}`", "", body.strip(), "", "---", ""]
        open(os.path.join(out, "WORKERS.md"), "w", encoding="utf-8").write("\n".join(note))
        agents_note = "`WORKERS.md` (described — this host has no subagents)"

    readme = f"""# Product Manager OS — {cfg['label']}

Built from `plugins/product-manager-os` by `scripts/build_targets.py`.
**Do not edit these files** — edit the source and rebuild, or your changes are
overwritten on the next build.

- **{n_skills} skills** in `{cfg['skills_dir']}/`
- **Operating brief:** `{cfg['entry']}`
- **Workflows:** {'`COMMANDS.md` (invoke by name)' if cfg['commands'] == 'inline' else f'`{cfg["commands"]}/` ({n_cmds} slash commands)'}
- **Memory:** `memory/` · **Workspace:** `workspace/`
- **Workers:** {agents_note}
- **Bundled libraries:** {mcp_note}

## Install

{cfg['install']}

## What to do first

Run setup (or ask for it by name) to fill `memory/` so the OS stops asking you
the basics. You can skip it — it resumes later and only asks what's still blank.

---
*From [The Product Channel](https://sidsaladi.substack.com) by Sid Saladi. MIT.*
"""
    open(os.path.join(out, "README.md"), "w", encoding="utf-8").write(readme)
    return n_skills


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", choices=sorted(TARGETS))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--clean", action="store_true")
    a = ap.parse_args()

    if a.list:
        print(f"\n{'target':<16}{'entry':<12}{'skills dir':<18}commands")
        print("─" * 62)
        for k, v in sorted(TARGETS.items()):
            print(f"{k:<16}{v['entry']:<12}{v['skills_dir']:<18}"
                  f"{v['commands'] if v['commands'] != 'inline' else 'inline (COMMANDS.md)'}")
        print()
        return

    if a.clean:
        shutil.rmtree(DIST, ignore_errors=True)
        print("dist/ removed")
        return

    targets = [a.target] if a.target else sorted(TARGETS)
    for t in targets:
        n = build(t)
        print(f"  ✅ {TARGETS[t]['label']:<26} → dist/{t}/  ({n} skills)")
    print(f"\n{len(targets)} target(s) built into dist/\n")


if __name__ == "__main__":
    main()
