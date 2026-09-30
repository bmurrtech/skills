# Version gate

Read before prep commits. Authorize **version** and **channel** (prerelease vs
stable). Inference computes a **primary recommendation** from prior release —
it does **not** invent outside the table below. The primary recommendation is
the **default action** when the user does not override it.

## When to skip re-ask

Skip the version/channel prompt **only** if the user already stated **both**
(e.g. “release 0.2.1-rc1” ⇒ version + prerelease channel). If only one is
stated, ask for the other.

## Recommendation (channel-preserving)

Discover `previous_version` from latest git tag / CHANGELOG / package evidence
(prefer newest semver tag that matches a CHANGELOG dated heading).

| Current channel | Primary recommendation (➡️ default) | Alternatives to offer |
|-----------------|--------------------------------------|------------------------|
| Prerelease (`X.Y.Z-rcN`) | Same `X.Y.Z`, next `rc(N+1)` | bump to stable `X.Y.Z`; next minor rc; next major rc |
| Stable (`X.Y.Z`) | Next **patch** `X.Y.(Z+1)` | optional `X.Y.(Z+1)-rc1`; next minor; next major |

Present recommendation + brief why. Wait for authorization of the pair
`(version, channel)` — either an **override** (user states both / picks an alt)
or **accept default** (below).

## Default action (no other guidance)

When the user did **not** state a different version/channel, treat acceptance of
the gate as authorization of the **primary recommendation**:

- No reply / LGTM / affirmatives / “go with recommended” / “proceed” / “ship it”
  after the lean prompt → authorize **recommend** + its channel
- Explicit alt or explicit version+channel → use that instead
- Never invent a version outside the table; never skip the gate prompt unless
  both were already stated up front

## Prompt shape (lean)

```text
Version gate
- previous: <prev>
- recommend: <ver> (<channel>) — <one-line why>
- alts: <comma list>
➡️ authorize recommend (default; no reply / LGTM / affirmatives → recommend)
  or state version + channel / pick an alt
```

## Done when

Authorized `version` + `channel` recorded (default-accept or override). Build
**release context**:

- `version`, `previous_version`, `channel`, `tag` (`v` + version),
  `release_intent: true`
- optional contract hint from discovery
