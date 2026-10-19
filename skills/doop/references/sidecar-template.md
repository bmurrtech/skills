# Sidecar: `.scratch/doop/<slug>.md`

Default on every session that creates or reuses a canvas. Untracked (under
`.scratch/`). Append a dated section on later invokes for the same slug.

```markdown
# <Title — process / architecture session>

- **Canvas id:** `<id>`
- **URL:** `http://localhost:4300/c/<id>`
- **Mode:** process | architecture | both
- **Forms:** pipeline, topology, …
- **Doop home:** `~/.doop` (or path used)
- **Created:** <yyyy-MM-dd>

## Notes

<Stakeholder confirmations, open questions, next tweaks>

## Capture <yyyy-MM-dd>

<Append-only meeting deltas>
```

Do not store API keys. Do not copy Doop `data/` into the consumer repo.
