#!/usr/bin/env python3
"""
Broken-promise audit.

The other test scripts check that files are well-formed. This checks something
they can't: **does every path the OS tells someone to use actually exist where
they'll be standing when they're told to use it?**

That's the bug class that shipped `automations/` referenced by a brief that never
shipped it, `/tune-up` invoking a script absent from every bundle, and a
"Full guide:" line pointing into a temp directory deleted seconds earlier. Each
looked fine in the repo and was broken for every user.

  python3 tests/audit.py
  python3 tests/audit.py --check   # CI mode, non-zero exit on any failure
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(P))

FAIL, WARN = [], []
def fail(cat, msg): FAIL.append((cat, msg))
def warn(cat, msg): WARN.append((cat, msg))

skills = sorted(d for d in os.listdir(f"{P}/skills")
                if os.path.isfile(f"{P}/skills/{d}/SKILL.md"))
commands = {f[:-3] for f in os.listdir(f"{P}/commands") if f.endswith(".md")}
workers = {f[:-3] for f in os.listdir(f"{P}/agents") if f.endswith(".md")}

# Text the OS shows a user or gives the model. Anything here that names a path
# is a promise, and every promise has to survive installation.
def instruction_sources():
    out = {"CLAUDE.md": open(f"{P}/CLAUDE.md", encoding="utf-8").read()}
    for pat in ("commands/*.md", "automations/*.md", "skills/*/SKILL.md",
                "memory/*.md", "agents/*.md", "workspace/README.md"):
        for f in sorted(glob.glob(f"{P}/{pat}")):
            out[os.path.relpath(f, P)] = open(f, encoding="utf-8").read()
    return out


# ── 1. THE BIG ONE: runnable/referenced paths must ship in every bundle ──────
SHIPPABLE = ("tests", "automations", "skills", "commands", "agents", "memory", "workspace")
promised = {}
for src, txt in instruction_sources().items():
    for m in re.finditer(r'((?:' + "|".join(SHIPPABLE) + r')/[\w.-]+\.(?:py|md|sh|json))', txt):
        promised.setdefault(m.group(1), set()).add(src)

for path, srcs in sorted(promised.items()):
    if not os.path.exists(f"{P}/{path}"):
        fail("promise", f"{path} is referenced by {', '.join(sorted(srcs))} but does not exist")
        continue
    for tgt in sorted(os.listdir(f"{P}/dist")):
        d = f"{P}/dist/{tgt}"
        if not os.path.isdir(d):
            continue
        top = path.split("/")[0]
        if os.path.exists(f"{d}/{path}") or os.path.exists(f"{d}/.claude/{path}") \
           or os.path.exists(f"{d}/{top}") or os.path.exists(f"{d}/.claude/{top}") \
           or os.path.exists(f"{d}/.cursor/{top}"):
            continue
        fail("bundle", f"{tgt}: {path} is referenced by {sorted(srcs)[0]} but not shipped")

# ── 2. Named things must exist ───────────────────────────────────────────────
for src, txt in instruction_sources().items():
    for m in re.finditer(r'`([a-z][a-z0-9-]{3,})` subagent', txt):
        if m.group(1) not in workers:
            fail("reference", f"{src} names unknown worker '{m.group(1)}'")
    for m in re.finditer(r'\breach for (?:the )?`([a-z][a-z0-9-]{3,})`', txt):
        if m.group(1) not in skills:
            fail("reference", f"{src} points at unknown skill '{m.group(1)}'")

for w in workers:
    if not any(f"`{w}` subagent" in t for t in instruction_sources().values()):
        fail("reference", f"agents/{w}.md is defined but no skill delegates to it")

# ── 3. Every bundle is internally complete ───────────────────────────────────
for tgt in sorted(os.listdir(f"{P}/dist")):
    d = f"{P}/dist/{tgt}"
    if not os.path.isdir(d):
        continue
    entry = next((e for e in ("CLAUDE.md", "AGENTS.md", "GEMINI.md")
                  if os.path.isfile(f"{d}/{e}")), None)
    if not entry:
        fail("bundle", f"{tgt}: no operating brief")
        continue
    # os.walk, not glob — glob skips dot-directories, and half the bundles put
    # their skills in .claude/skills or .cursor/rules
    n = sum(1 for dp, _, fn in os.walk(d) if "SKILL.md" in fn)
    if n != len(skills):
        fail("bundle", f"{tgt}: {n} skills shipped, {len(skills)} expected")
    if not (os.path.isdir(f"{d}/.claude/commands") or os.path.isdir(f"{d}/commands")
            or os.path.isfile(f"{d}/COMMANDS.md")):
        fail("bundle", f"{tgt}: workflows neither shipped nor described")
    if not (os.path.isdir(f"{d}/.claude/agents") or os.path.isdir(f"{d}/agents")
            or os.path.isfile(f"{d}/WORKERS.md")):
        fail("bundle", f"{tgt}: workers neither shipped nor described")
    if tgt not in ("claude-code", "claude-cowork") and "Claude Code" in open(f"{d}/{entry}", encoding="utf-8").read():
        fail("bundle", f"{tgt}: brief still tells the user they're on Claude Code")
    # an .mcp.json at the root of a non-Claude bundle is a file that looks like
    # config and silently isn't
    if tgt not in ("claude-code", "claude-cowork") and os.path.isfile(f"{d}/.mcp.json"):
        fail("bundle", f"{tgt}: ships .mcp.json at the project root, where only Claude reads it")

# ── 4. Counts agree everywhere a human will read them ────────────────────────
pj = json.load(open(f"{P}/.claude-plugin/plugin.json"))
mk = json.load(open(f"{ROOT}/.claude-plugin/marketplace.json"))
m = re.search(r"Ships (\d+) battle", pj["description"])
if not m or int(m.group(1)) != len(skills):
    fail("count", f"plugin.json claims {m.group(1) if m else '?'} skills, {len(skills)} ship")
if pj["name"] != mk["plugins"][0]["name"]:
    fail("count", "plugin.json and marketplace.json disagree on the plugin name")
if not os.path.isdir(os.path.join(ROOT, mk["plugins"][0]["source"])):
    fail("count", "marketplace.json source path does not resolve")

for doc in ("README.md", "INSTALL.md", "QUICKSTART.md", "LAUNCH.md",
            "plugins/product-manager-os/README.md"):
    fp = os.path.join(ROOT, doc)
    if not os.path.isfile(fp):
        fail("docs", f"{doc} is missing")
        continue
    txt = open(fp, encoding="utf-8").read()
    for m in re.finditer(r'\b(\d\d)\+? (?:skills|book-grounded)', txt):
        if int(m.group(1)) != len(skills):
            fail("count", f"{doc} claims {m.group(1)} skills")

# ── 5. Every skill appears where people and models look for it ───────────────
for doc in ("CLAUDE.md", "README.md"):
    txt = open(f"{P}/{doc}", encoding="utf-8").read()
    for s in skills:
        if f"`{s}`" not in txt:
            fail("coverage", f"{s} is not listed in {doc}")

# ── 6. Relative links resolve ────────────────────────────────────────────────
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [x for x in dn if x not in (".git", "node_modules", "__pycache__")]
    for f in fn:
        if not f.endswith(".md"):
            continue
        fp = os.path.join(dp, f)
        for m in re.finditer(r'\[([^\]]+)\]\(([^)#\s]+)\)',
                             open(fp, encoding="utf-8", errors="ignore").read()):
            t = m.group(2)
            if t.startswith(("http", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(dp, t))):
                fail("links", f"{os.path.relpath(fp, ROOT)} → {t}")

# ── report ───────────────────────────────────────────────────────────────────
for cat, msg in FAIL:
    print(f"✗ [{cat}] {msg}")
for cat, msg in WARN:
    print(f"⚠ [{cat}] {msg}")
print(f"\n{len(skills)} skills · {len(commands)} commands · {len(workers)} workers · "
      f"{len(promised)} promised paths checked across "
      f"{len([d for d in os.listdir(f'{P}/dist') if os.path.isdir(f'{P}/dist/{d}')])} bundles")
print(f"{len(FAIL)} failures · {len(WARN)} warnings")
if FAIL and "--check" in sys.argv:
    sys.exit(1)
if not FAIL:
    print("\nNo broken promises.")
