# Version gate

Read before prep commits. Authorize **version** and **channel** (prerelease vs
stable). Inference may recommend only — never silently choose.

## When to skip re-ask

Skip the version/channel prompt **only** if the user already stated **both**
(e.g. “release 0.2.1-rc1” ⇒ version + prerelease channel). If only one is
stated, ask for the other.

## Recommendation (channel-preserving)

Discover `previous_version` from latest git tag / CHANGELOG / package evidence.

| Current channel | Primary recommendation | Alternatives to offer |
|-----------------|------------------------|------------------------|
| Prerelease (`X.Y.Z-rcN`) | Same `X.Y.Z`, next `rc(N+1)` | bump to stable `X.Y.Z`; next minor rc; next major rc |
| Stable (`X.Y.Z`) | Next **patch** `X.Y.(Z+1)` | optional `X.Y.(Z+1)-rc1`; next minor; next major |

Present recommendation + brief why; wait for explicit authorization of the pair
`(version, channel)`.

## Prompt shape (lean)

```text
Version gate
- previous: <prev>
- recommend: <ver> (<channel>) — <one-line why>
- alts: <comma list>
Authorize version + channel (or state both explicitly).
```

## Done when

User-authorized `version` + `channel` recorded. Build **release context**:

- `version`, `previous_version`, `channel`, `tag` (`v` + version),
  `release_intent: true`
- optional contract hint from discovery
