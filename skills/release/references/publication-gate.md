# Publication gate

Read after local validation passes, **before** creating or pushing any tag.

## Confirm exactly

- Annotated tag name (`v…`)
- Commit SHA to tag
- Branch / HEAD relationship (canonical release SHA)
- Validation summary (commands + pass)

## Affirmative enough

After version was authorized at the version gate, a clear affirmative (“yes” /
“proceed” / “LGTM” / “ship it”) is enough. Re-state the exact tag + SHA in the
prompt so affirmation binds to those values.

## Prompt shape (lean)

```text
Publication gate
- tag: v<version>
- sha: <full-or-short>
- branch: <name>
- validated: <one-line summary>
Push this annotated tag? (yes / proceed / LGTM)
```

## Hard stops

- Do not create the tag before affirmation.
- Do not push the tag before affirmation.
- Do not treat branch push as publication.
- If SHA moved since validation → re-validate; do not carry old authorization.
