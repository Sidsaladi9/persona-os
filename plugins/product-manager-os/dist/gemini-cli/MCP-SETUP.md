# Bundled libraries (optional)

The OS works fully without these. They add live access to [getprompts](https://getprompts.org) (900+ PM prompts) and [getskills](https://getskillsai.org) (3,000+ installable skills).

Two zero-config public npm packages — no account, no API key, read-only:

```
npx -y getprompts-mcp
npx -y getskills-mcp
```

**Where to put this depends on your host, and the path moves between versions — check your host's current MCP docs rather than trusting a path written here.** The server definition itself is what you need:

```json
{
  "mcpServers": {
    "getprompts": { "command": "npx", "args": ["-y", "getprompts-mcp"] },
    "getskills":  { "command": "npx", "args": ["-y", "getskills-mcp"] }
  }
}
```

Needs Node 18+. If your org blocks MCP servers, skip this entirely — all 53 skills work without them.
