#!/usr/bin/env python3
"""
Regenerate workspace/INDEX.md — a map of everything the OS has produced.

Run it any time:  python3 tests/index_workspace.py

Why this exists: after a few months the workspace is the most valuable thing in
the repo and the hardest to see. The index gives Claude one file to read at
session start to know what already exists, so it stops re-asking for context
that's sitting on disk.
"""
import os
import re
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WS = os.path.join(ROOT, "workspace")

ORDER = ["projects", "strategy", "research", "metrics", "decisions", "meetings", "comms"]
BLURB = {
    "projects":  "one folder per named piece of work",
    "strategy":  "the slow-changing calls",
    "research":  "what we learned about users and the market",
    "metrics":   "numbers and what they meant",
    "decisions": "calls that would be expensive to relitigate",
    "meetings":  "notes and retros",
    "comms":     "anything that went to other humans",
}


def title_of(path):
    """First markdown H1, else the filename."""
    try:
        with open(path, encoding="utf-8") as fh:
            for _ in range(40):
                line = fh.readline()
                if not line:
                    break
                m = re.match(r"^#\s+(.+?)\s*$", line)
                if m:
                    return m.group(1)
    except (OSError, UnicodeDecodeError):
        pass
    return os.path.splitext(os.path.basename(path))[0]


def walk(folder):
    base = os.path.join(WS, folder)
    if not os.path.isdir(base):
        return []
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in sorted(dirnames) if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.startswith(".") or fn == "TEMPLATE.md":
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, WS)
            out.append((rel, title_of(full), os.path.getmtime(full)))
    return out


def main():
    lines = [
        "# Workspace Index",
        "",
        f"_Generated {date.today().isoformat()} by `python3 tests/index_workspace.py`. "
        "Do not hand-edit — regenerate instead._",
        "",
    ]
    total = 0
    for folder in ORDER:
        items = walk(folder)
        if not items:
            continue
        total += len(items)
        lines += [f"## `{folder}/` — {BLURB[folder]}  ({len(items)})", ""]
        for rel, title, mtime in sorted(items, key=lambda x: -x[2]):
            when = date.fromtimestamp(mtime).isoformat()
            lines.append(f"- [{title}]({rel}) · `{rel}` · {when}")
        lines.append("")

    if total == 0:
        lines += [
            "_Nothing here yet._",
            "",
            "The workspace fills up as you work — every skill writes its artifact to the "
            "path declared in its `outputs:` frontmatter. Run `/weekly` or ask for a spec "
            "and the first files appear.",
            "",
        ]
    else:
        lines.insert(3, f"**{total} artifacts.**")
        lines.insert(4, "")

    open(os.path.join(WS, "INDEX.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"workspace/INDEX.md regenerated — {total} artifacts")


if __name__ == "__main__":
    main()
