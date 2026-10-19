# MCP connect (harness one-liners)

Doop MCP is HTTP at the web origin (dev proxy): `http://localhost:4300/mcp`.
API-only docker self-host may be `http://localhost:4400/mcp` — match whatever
`ensure_doop.py status` reports.

Authenticate as the human (MCP OAuth). Agents inherit that account’s canvas access.

## Claude Code

```bash
claude mcp add --transport http doop http://localhost:4300/mcp
```

## Cursor

Add an MCP server entry pointing at `http://localhost:4300/mcp` (HTTP/SSE per
current Cursor MCP settings UI). Name it `doop`. Complete the browser OAuth
approve step when prompted.

## Generic MCP client

Any client that speaks Streamable HTTP MCP against `http://localhost:4300/mcp`
with OAuth. Reuse the same `agent_name` on every tool call for presence.

## After connect

1. Open `http://localhost:4300` and sign in (local signup; emails print to server log without SMTP).
2. Confirm tools: `list_canvases`, `get_canvas`, `create_frame`, …
3. Return to the `doop` skill workflow (canvas + draw/edit).
