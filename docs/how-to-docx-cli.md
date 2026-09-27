# Install docx-cli (operator)

Human install for the library **`docx`** skill. Agents **probe** `docx --version`
against the skill pin; they do **not** download or `--install` the CLI
([ADR 0011](adr/0011-ADR-skill-scanner-posture-prereqs.md)).

**Pin for this library:** `0.26.0` (`skills/docx/scripts/ensure_docx.py`). Prefer
that release tag over floating `latest` when following these steps. Expected
SHA-256 digests for release assets live in `skills/docx/scripts/DIGESTS`
(operator verify only).

Upstream: [kklimuk/docx-cli](https://github.com/kklimuk/docx-cli) (MIT).

## npm / Bun (simplest)

Requires Bun >= 1.3:

```sh
bun add -g bun-docx
# or run without installing:
bunx bun-docx --version
```

Confirm the version matches the skill pin (`0.26.0`). If the package tracks a
newer release, either wait for a library pin bump or use the standalone path
below with `VERSION=0.26.0`.

## Standalone binary

Every release publishes prebuilt binaries, `install.sh`, and `SHA256SUMS`. The
installer verifies SHA-256 before installing. Prefer the **pinned** tag:

```sh
VERSION=0.26.0
BASE="https://github.com/kklimuk/docx-cli/releases/download/v${VERSION}"

curl -fsSLO "${BASE}/install.sh"
curl -fsSLO "${BASE}/SHA256SUMS"
shasum -a 256 -c SHA256SUMS --ignore-missing   # or: sha256sum -c …
# optional: also match skills/docx/scripts/DIGESTS for your platform asset
sh install.sh
```

Honors `PREFIX` (default `$HOME/.local/bin`) and `VERSION`. Platforms:
linux/x64, linux/arm64, darwin/x64, darwin/arm64, windows/x64.

Ensure `PREFIX` is on `PATH` (`export PATH="$HOME/.local/bin:$PATH"`).

Once installed, `docx upgrade --to v0.26.0` updates a standalone binary with the
same verify path. On an npm/bun install, use the package manager instead.

### Manual binary (skip install.sh)

Download `docx-<platform>` + `SHA256SUMS` from the
[v0.26.0 release](https://github.com/kklimuk/docx-cli/releases/tag/v0.26.0),
verify, `chmod +x`, put on `PATH`. Cross-check digests against
`skills/docx/scripts/DIGESTS` when using this library’s pin.

## Office host (render / `.odt` import)

`docx render` and `.odt` → `.docx` need Microsoft Word or LibreOffice. Everything
else works on the `.docx` zip alone. Install Word or LibreOffice yourself; the
skill’s `ensure_office.py` only probes and prints hints — it never runs package
managers. See [`skills/docx/references/host-apps.md`](../skills/docx/references/host-apps.md).

## After install

```sh
docx --version   # expect 0.26.0 for this library pin
# from the skill folder (or with scripts on PYTHONPATH):
python3 scripts/ensure_toolchain.py
```

Re-run the **`docx`** skill once the probe exits 0.
