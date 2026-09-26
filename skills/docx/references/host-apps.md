# Host apps

`docx render` and `.odt` → `.docx` need Microsoft Word or LibreOffice.

Prefer `ensure_toolchain.py` (probes docx pin + office host). Cores:
`ensure_docx.py` does not probe hosts; `ensure_office.py` does.

When both hosts absent after ensure:

- Still deliver a created or edited `.docx`; state that render did not run
- Refuse `.odt` import and say it will not run
