"""Split a transcript on speaker-turn or paragraph boundaries with overlap."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_CHUNK_WORDS = 3000
DEFAULT_OVERLAP_WORDS = 300

# Speaker turn: "Name:" / "[Name]" / "Name -" at line start (common transcript shapes)
_SPEAKER_LINE = re.compile(
    r"^(?:"
    r"\[[^\]]+\]\s*"  # [Speaker] …
    r"|[A-Za-z][A-Za-z0-9_.\- ]{0,40}:\s+"  # Speaker: …
    r"|[A-Za-z][A-Za-z0-9_.\- ]{0,40}\s+[-–—]\s+"  # Speaker - …
    r")"
)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8-sig")


def split_paragraphs(text: str) -> list[str]:
    parts = re.split(r"\n\s*\n", text.strip())
    return [p for p in parts if p.strip()]


def split_speaker_turns(text: str) -> list[str] | None:
    """Return speaker-turn units when enough labeled turns exist; else None."""
    lines = text.strip().splitlines()
    if not lines:
        return None

    turns: list[str] = []
    current: list[str] = []
    labeled = 0

    for line in lines:
        if _SPEAKER_LINE.match(line.strip()):
            labeled += 1
            if current:
                turns.append("\n".join(current).strip())
                current = []
        current.append(line)

    if current:
        turns.append("\n".join(current).strip())

    turns = [t for t in turns if t]
    # Need multiple labeled turns to prefer this path over paragraphs.
    if labeled < 2 or len(turns) < 2:
        return None
    return turns


def split_units(text: str) -> list[str]:
    speaker_turns = split_speaker_turns(text)
    if speaker_turns is not None:
        return speaker_turns
    return split_paragraphs(text)


def split_oversized_unit(
    unit: str,
    chunk_words: int,
    overlap_words: int,
) -> list[str]:
    """Hard-split a single unit that exceeds chunk_words (word windows + overlap)."""
    words = unit.split()
    if len(words) <= chunk_words:
        return [unit]

    step = max(chunk_words - overlap_words, 1)
    parts: list[str] = []
    start = 0
    while start < len(words):
        end = min(start + chunk_words, len(words))
        parts.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start += step
    return parts


def expand_units(
    units: list[str],
    chunk_words: int,
    overlap_words: int,
) -> list[str]:
    expanded: list[str] = []
    for unit in units:
        if len(unit.split()) > chunk_words:
            expanded.extend(
                split_oversized_unit(unit, chunk_words, overlap_words)
            )
        else:
            expanded.append(unit)
    return expanded


def chunk_units(
    units: list[str],
    chunk_words: int = DEFAULT_CHUNK_WORDS,
    overlap_words: int = DEFAULT_OVERLAP_WORDS,
) -> list[str]:
    if chunk_words < 1:
        raise ValueError("chunk_words must be >= 1")
    if overlap_words < 0:
        raise ValueError("overlap_words must be >= 0")
    if overlap_words >= chunk_words:
        raise ValueError("overlap_words must be < chunk_words")

    units = expand_units(units, chunk_words, overlap_words)

    chunks: list[str] = []
    current: list[str] = []
    current_words = 0

    for unit in units:
        unit_words = len(unit.split())
        if current and current_words + unit_words > chunk_words:
            chunks.append("\n\n".join(current))
            overlap: list[str] = []
            overlap_count = 0
            for u in reversed(current):
                uw = len(u.split())
                if overlap and overlap_count + uw > overlap_words:
                    break
                overlap.insert(0, u)
                overlap_count += uw
            current = overlap
            current_words = overlap_count
        current.append(unit)
        current_words += unit_words

    if current:
        chunks.append("\n\n".join(current))
    return chunks


def write_chunks(chunks: list[str], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for i, chunk in enumerate(chunks):
        path = out_dir / f"chunk_{i:03d}.txt"
        path.write_text(chunk, encoding="utf-8")
        paths.append(path)
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Chunk a transcript on speaker-turn or paragraph boundaries "
            "with overlap."
        )
    )
    parser.add_argument("path", help="Transcript file path, or - for stdin")
    parser.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Output directory for chunk_NNN.txt files",
    )
    parser.add_argument(
        "--chunk-words",
        type=int,
        default=DEFAULT_CHUNK_WORDS,
        help=f"Target words per chunk (default {DEFAULT_CHUNK_WORDS})",
    )
    parser.add_argument(
        "--overlap-words",
        type=int,
        default=DEFAULT_OVERLAP_WORDS,
        help=f"Overlap words from prior chunk (default {DEFAULT_OVERLAP_WORDS})",
    )
    args = parser.parse_args(argv)

    text = read_text(args.path)
    units = split_units(text)
    if not units:
        print("0 chunks created", file=sys.stderr)
        args.out.mkdir(parents=True, exist_ok=True)
        return 0

    try:
        chunks = chunk_units(
            units,
            chunk_words=args.chunk_words,
            overlap_words=args.overlap_words,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    paths = write_chunks(chunks, args.out)
    print(f"{len(paths)} chunks created")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
