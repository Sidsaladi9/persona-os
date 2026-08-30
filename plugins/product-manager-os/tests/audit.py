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

for doc in ("README.md", "INSTALL.md",
            "plugins/product-manager-os/README.md"):
    fp = os.path.join(ROOT, doc)
    if not os.path.isfile(fp):
        fail("docs", f"{doc} is missing")
        continue
    txt = open(fp, encoding="utf-8").read()
    for m in re.finditer(r'\b(\d\d)\+? (?:skills|book-grounded)', txt):
        if int(m.group(1)) != len(skills):
            fail("count", f"{doc} claims {m.group(1)} skills")

# ── 5. Every user-facing component is documented ─────────────────────────────
# A feature nobody can find is a feature nobody uses. The brain needs the skills;
# the README needs everything a person could reach for.
brain_txt = open(f"{P}/CLAUDE.md", encoding="utf-8").read()
readme_txt = open(f"{P}/README.md", encoding="utf-8").read()

for s in skills:
    if f"`{s}`" not in brain_txt:
        fail("coverage", f"skill {s} is not listed in CLAUDE.md")
    if f"`{s}`" not in readme_txt:
        fail("coverage", f"skill {s} is not listed in README.md")

for c in sorted(commands):
    if f"/{c}" not in readme_txt:
        fail("coverage", f"command /{c} is not explained in README.md")

for a in sorted(f[:-3] for f in os.listdir(f"{P}/automations")
                if f.endswith(".md") and f != "README.md"):
    if f"`{a}`" not in readme_txt:
        fail("coverage", f"automation {a} is not explained in README.md")

for m in sorted(f for f in os.listdir(f"{P}/memory") if f.endswith(".md")):
    if f"`{m}`" not in readme_txt:
        fail("coverage", f"memory file {m} is not explained in README.md")

for w in sorted(d for d in os.listdir(f"{P}/workspace")
                if os.path.isdir(os.path.join(P, "workspace", d))):
    if f"`{w}/" not in readme_txt and f"{w}/`" not in readme_txt:
        fail("coverage", f"workspace/{w} is not explained in README.md")

for wk in sorted(workers):
    if f"`{wk}`" not in readme_txt:
        fail("coverage", f"worker {wk} is not explained in README.md")

# the tools the OS tells a user to run must be findable in the README
USER_TOOLS = ("relevance_report.py", "score_skill.py", "run_all.py",
              "check_artifact.py", "index_workspace.py")
for t in USER_TOOLS:
    if t not in readme_txt:
        fail("coverage", f"tests/{t} is something the OS asks users to run, "
                         f"but the README never mentions it")

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

# ── 7. The plugin install path actually delivers the OS ──────────────────────
# A plugin cannot ship a CLAUDE.md that Claude reads — only the project's own
# CLAUDE.md is loaded. So on `/plugin install` the brain reaches the session
# ONLY through the SessionStart hook. If that breaks, the plugin still installs,
# still lists 53 skills, and silently becomes a prompt pack: no bootstrap, no
# memory, no workspace, no activity log. Nothing else in this suite sees it.
import subprocess

hooks_json = f"{P}/hooks/hooks.json"
hook_sh = f"{P}/hooks/session-start.sh"

if not os.path.isfile(hooks_json):
    fail("plugin", "hooks/hooks.json is missing — the operating brain will not "
                   "load on a /plugin install")
elif not os.path.isfile(hook_sh):
    fail("plugin", "hooks/session-start.sh is missing")
else:
    try:
        hj = json.load(open(hooks_json, encoding="utf-8"))
    except Exception as e:
        hj = None
        fail("plugin", f"hooks/hooks.json does not parse: {e}")
    if hj is not None:
        starts = hj.get("hooks", {}).get("SessionStart")
        if not starts:
            fail("plugin", "hooks.json declares no SessionStart hook")
        else:
            cmds = [h.get("command", "") for g in starts for h in g.get("hooks", [])]
            if not any("session-start.sh" in c for c in cmds):
                fail("plugin", "SessionStart hook does not invoke session-start.sh")
            if not any("${CLAUDE_PLUGIN_ROOT}" in c for c in cmds):
                fail("plugin", "SessionStart command must go through "
                               "${CLAUDE_PLUGIN_ROOT} — a relative path breaks "
                               "once the plugin is installed from a cache")

    if not os.access(hook_sh, os.X_OK):
        warn("plugin", "hooks/session-start.sh is not executable")

    # Run it the way Claude Code will, from a directory that is not the plugin.
    for label, cwd, setup in (("cold", "/tmp", False), ("set-up", None, True)):
        import tempfile
        d = tempfile.mkdtemp()
        if setup:
            os.makedirs(f"{d}/memory", exist_ok=True)
            open(f"{d}/memory/MEMORY.md", "w").write("# Memory Index\n")
        env = dict(os.environ, CLAUDE_PLUGIN_ROOT=P)
        try:
            r = subprocess.run(["bash", hook_sh], cwd=d, env=env,
                               capture_output=True, text=True, timeout=15)
        except Exception as e:
            fail("plugin", f"session-start.sh ({label}) failed to run: {e}")
            continue
        if r.returncode != 0:
            fail("plugin", f"session-start.sh ({label}) exited {r.returncode}")
        out = r.stdout
        if not out.strip():
            fail("plugin", f"session-start.sh ({label}) produced no context")
        # SessionStart context is truncated at ~2KB, in every output form we
        # tried (plain stdout AND hookSpecificOutput.additionalContext). Going
        # over the cap is the worst failure mode available: the plugin looks
        # installed and behaves like a prompt pack. See hooks/README.md.
        if len(out.encode()) > 2048:
            fail("plugin", f"session-start.sh ({label}) emits "
                           f"{len(out.encode())} bytes; SessionStart context is "
                           f"capped at ~2048 and the remainder is dropped "
                           f"silently")
        if "CLAUDE.md" not in out:
            fail("plugin", f"session-start.sh ({label}) never points the model "
                           f"at the operating brain")
        if setup is False and "memory/" not in out:
            fail("plugin", "session-start.sh (cold) does not mention bootstrapping "
                           "memory/ — a fresh install has nowhere to put anything")

    # Docs must teach the namespaced form. On a plugin install the commands are
    # /product-manager-os:setup, not /setup, and every doc said /setup.
    for doc, path in (("plugin README", f"{P}/README.md"),
                      ("INSTALL.md", f"{ROOT}/INSTALL.md"),
                      ("root README", f"{ROOT}/README.md")):
        if "product-manager-os:setup" not in open(path, encoding="utf-8").read():
            fail("plugin", f"{doc} never shows the namespaced command form "
                           f"(/product-manager-os:setup) — it is what a plugin "
                           f"user actually has to type")

    # The install that bit a real user: the marketplace is a cached clone, so a
    # second `install` reinstalls the cached version and reports an old number.
    # Both front doors have to say how to refresh it.
    for doc, path in (("root README", f"{ROOT}/README.md"),
                      ("INSTALL.md", f"{ROOT}/INSTALL.md")):
        if "marketplace update" not in open(path, encoding="utf-8").read():
            fail("plugin", f"{doc} never mentions `claude plugin marketplace update` "
                           f"— without it a returning user silently reinstalls the "
                           f"cached version and sees a stale version number")

    # get.sh can now refuse (ambiguous host, colliding files). A refusal a user
    # cannot interpret is worse than the guess it replaced.
    readme_root = open(f"{ROOT}/README.md", encoding="utf-8").read().lower()
    if "more than one tool" not in readme_root or "--force" not in readme_root:
        fail("plugin", "root README does not explain the two cases where get.sh "
                       "stops instead of installing (ambiguous host, colliding "
                       "files) — the user is left at a dead end")

# ── 8. Shipped assets are reachable in the bundle that ships them ────────────
# WORKERS.md shipped into all four non-subagent bundles with NOTHING pointing at
# it: the nine worker skills still opened "Delegate to the `critic` subagent",
# naming a thing those hosts do not have. The README meanwhile promised the
# skill "says plainly that the result is a self-review". It didn't.
for tgt in sorted(os.listdir(f"{P}/dist")):
    d = f"{P}/dist/{tgt}"
    if not os.path.isdir(d):
        continue
    # claude-code nests these at .claude/agents/, cowork at agents/ — just look.
    has_agents = any("critic.md" in fs for _, _, fs in os.walk(d))
    workers_md = os.path.join(d, "WORKERS.md")
    skills = [os.path.join(dp, "SKILL.md")
              for dp, _, fs in os.walk(d) if "SKILL.md" in fs]
    if has_agents:
        if os.path.isfile(workers_md):
            fail("bundles", f"{tgt} ships real subagents AND WORKERS.md — pick one")
        continue
    if not os.path.isfile(workers_md):
        fail("bundles", f"{tgt} has no subagents and no WORKERS.md — nine skills "
                        f"reference a worker this host cannot provide")
        continue
    pointing = [f for f in skills
                if "WORKERS.md" in open(f, encoding="utf-8", errors="ignore").read()]
    if not pointing:
        fail("bundles", f"{tgt} ships WORKERS.md but no skill points at it — the "
                        f"asset is orphaned")
    for f in skills:
        s = open(f, encoding="utf-8", errors="ignore").read()
        if "subagent" in s and "WORKERS.md" not in s:
            fail("bundles", f"{tgt}/{os.path.basename(os.path.dirname(f))} names a "
                            f"subagent on a host that has none, without pointing at "
                            f"WORKERS.md")
    # the honesty rule is the whole reason WORKERS.md exists
    for f in pointing:
        if "self-review" not in open(f, encoding="utf-8", errors="ignore").read():
            fail("bundles", f"{tgt}/{os.path.basename(os.path.dirname(f))} uses a "
                            f"worker brief without telling the model to label the "
                            f"result a self-review")

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
