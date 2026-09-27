# Host apps

`docx render` and `.odt` → `.docx` need Microsoft Word or LibreOffice.

Prefer `ensure_toolchain.py` (probes docx pin + office host). Cores:
`ensure_docx.py` probes PATH for the library pin and prints a short manual
hint (see [docs/how-to-docx-cli.md](../../../docs/how-to-docx-cli.md));
`ensure_office.py` probes only and prints LibreOffice/Word install hints — it
never runs brew/winget/apt/`sudo` and never downloads the CLI.

When both hosts absent after ensure:

- Still deliver a created or edited `.docx`; state that render did not run
- Refuse `.odt` import and say it will not run
- Point the operator at the printed LibreOffice/Word install hint; do not escalate privileges
