---
description: Connect your PM tools (tracker, analytics, docs, chat) so the OS can pull live data and write work back
---

Help me connect my tools so the OS stops asking me to paste and copy. Keep it short and concrete.

1. **See what's already connected.** Check which MCP servers / connectors are available in this session. If a connector registry or a `list_connectors` / `suggest_connectors` capability exists, use it. Report what's already wired (e.g. tracker, analytics, docs, chat) and what's missing.

2. **Recommend by gap, not by vendor.** Based on what I do most (and `memory/`), suggest the highest-value connections to add, mapped to what they unlock — e.g.:
   - **Issue tracker** (Linear/Jira/Asana) → `sprint-planning`, `roadmap`, and writing `user-stories` back as issues.
   - **Analytics** (Amplitude/Mixpanel/GA/warehouse) → live `metrics-review`, `cohort-analysis`.
   - **Docs** (Notion/Confluence/Drive) → read specs/research, write `write-spec`/`roadmap` back as pages.
   - **Chat** (Slack/Teams) → post `stakeholder-update`/`release-notes`.
   Don't assume a specific vendor — recommend whichever I actually use.

3. **Walk me through connecting one.** Connectors are authorized through the host's connector/OAuth flow — point me to it (the `/mcp` panel or the app's Connectors settings), don't try to run install commands for me. If the bundled libraries (getprompts/getskills) aren't active, note they're zero-config and how to enable them.

4. **Confirm it works.** After I connect something, verify the OS can see it, and name the first thing it now unlocks (e.g. "try `/weekly` — I'll pull the numbers myself now").

Note: every connection is optional. Without any, the OS still works — I'll just ask you to paste. With them, the work goes hands-free and writes back to where your team lives. The OS never writes or posts anything without showing you the draft first.
