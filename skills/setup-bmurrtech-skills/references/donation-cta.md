# Donation CTA (optional)

Read during **Present and confirm** and **Write** when offering funding
surfaces. Glossary: **Donation CTA** / **FUNDING.yml** in consumer
`CONTEXT.md` (and library [CONTEXT.md](../../../CONTEXT.md)).

## Prompt shape

Always re-ask on every setup run (default **no** — like docx). After the
scaffold table + PRD A/B (+ docx if offered):

```text
**Want to add donation CTAs (Ko-fi, Buy Me a Coffee, or similar)?**

Default **no**. Yes → paste usernames or full URLs for each platform you want
(Ko-fi, Buy Me a Coffee, GitHub Sponsors, and/or custom links).
```

No reply / LGTM / bare affirmatives on the overall setup confirm **without** an
explicit yes on this question → **skip** (do not invent funding files).

## Target files (only when yes + URLs given)

| File | Role |
|------|------|
| `.github/FUNDING.yml` | GitHub Sponsors sidebar — fill only platforms the user supplied; leave others as commented stubs |
| `README.md` | Section **Support this Repo** (badges + links). Create section if missing; ask before replacing a different existing Support heading |
| `CONTEXT.md` | Short **Donation CTA** / **FUNDING.yml** glossary entries (stub create or confirmed edit only) |

Do **not** use the heading “Support open source” in consumers — that wording is
for OSS libraries that choose it; consumers get **Support this Repo**.

## Write matrix

1. Ensure `.github/` exists.
2. Write or merge `.github/FUNDING.yml`:
   - `ko_fi: <username>`
   - `buy_me_a_coffee: <username>`
   - `github: [<user>]` when Sponsors username given
   - `custom: [<url>, …]` for other URLs
3. README section (append if no Support heading):

```markdown
## Support this Repo

- ☕ **[Buy Me a Coffee](https://www.buymeacoffee.com/<user>)** or **[Ko-fi](https://ko-fi.com/<user>)**

<p align="center">
  <a href="https://www.buymeacoffee.com/<user>" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20the%20project-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a><!--
  --><a href="https://ko-fi.com/<user>" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/Ko--fi-Support%20the%20project-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi"></a>
</p>
```

Adapt bullets/badges to only the platforms supplied. For custom URLs, link text
= hostname or label the user gave.

4. CONTEXT glossary (when stubbing or user confirmed edit):

```markdown
**Donation CTA**:
Optional funding surfaces: `.github/FUNDING.yml`, README **Support this Repo**,
and these glossary links. Platforms: <list URLs>.
_Avoid_: inventing CTAs without operator opt-in; “Support open source” heading
in non-OSS scaffolds

**FUNDING.yml**:
GitHub funding file at `.github/FUNDING.yml` for the Sponsors sidebar.
```

## Boundaries

- Never invent usernames or URLs.
- Never overwrite a non-empty FUNDING.yml / Support section without ask.
- Skip entirely when the answer is no / silent on this optional question.
