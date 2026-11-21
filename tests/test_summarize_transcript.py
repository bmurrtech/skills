"""Seams for summarize-transcript assess/chunk scripts + e2e pipeline."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills" / "summarize-transcript" / "scripts"
FIXTURE = (
    REPO_ROOT
    / "tests"
    / "fixtures"
    / "summarize_transcript"
    / "game_idea_research.txt"
)


def _load(name: str):
    path = SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


assess_size = _load("assess_size")
chunk_transcript = _load("chunk_transcript")


class AssessSizeTests(unittest.TestCase):
    def test_strategy_hint_threshold(self) -> None:
        self.assertEqual(assess_size.strategy_hint(3999), "direct")
        self.assertEqual(assess_size.strategy_hint(4000), "map-reduce")

    def test_assess_counts_words(self) -> None:
        result = assess_size.assess("one two three four")
        self.assertEqual(result["words"], 4)
        self.assertEqual(result["tokens_approx"], 5)
        self.assertEqual(result["strategy_hint"], "direct")

    def test_cli_on_fixture_is_direct(self) -> None:
        self.assertTrue(FIXTURE.is_file(), f"missing fixture: {FIXTURE}")
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "assess_size.py"), str(FIXTURE)],
            check=True,
            capture_output=True,
            text=True,
        )
        lines = dict(
            line.split(": ", 1) for line in proc.stdout.strip().splitlines()
        )
        self.assertEqual(int(lines["words"]), 1589)
        self.assertEqual(lines["strategy_hint"], "direct")


class ChunkTranscriptUnitTests(unittest.TestCase):
    def test_paragraph_fallback_when_no_speakers(self) -> None:
        text = "First block.\n\nSecond block.\n\nThird block."
        units = chunk_transcript.split_units(text)
        self.assertEqual(len(units), 3)
        self.assertIsNone(chunk_transcript.split_speaker_turns(text))

    def test_speaker_turns_when_labeled(self) -> None:
        text = (
            "Alice: hello there and more words\n"
            "continued\n\n"
            "Bob: reply from bob with content\n\n"
            "Alice: closing thought"
        )
        turns = chunk_transcript.split_speaker_turns(text)
        self.assertIsNotNone(turns)
        assert turns is not None
        self.assertGreaterEqual(len(turns), 2)
        units = chunk_transcript.split_units(text)
        self.assertEqual(units, turns)

    def test_chunk_defaults_and_overlap(self) -> None:
        # Independent SoT: ~500-word units force multiple chunks at default 3000
        unit = "word " * 500
        units = [unit.strip() for _ in range(8)]
        chunks = chunk_transcript.chunk_units(units)
        self.assertGreater(len(chunks), 1)
        self.assertEqual(chunk_transcript.DEFAULT_CHUNK_WORDS, 3000)
        self.assertEqual(chunk_transcript.DEFAULT_OVERLAP_WORDS, 300)

    def test_chunk_rejects_bad_overlap(self) -> None:
        with self.assertRaises(ValueError):
            chunk_transcript.chunk_units(["a"], chunk_words=10, overlap_words=10)

    def test_oversized_single_unit_is_hard_split(self) -> None:
        unit = "word " * 1000
        chunks = chunk_transcript.chunk_units(
            [unit.strip()], chunk_words=400, overlap_words=40
        )
        self.assertGreaterEqual(len(chunks), 3)
        self.assertLessEqual(len(chunks[0].split()), 400)


class ChunkTranscriptCliTests(unittest.TestCase):
    def test_cli_writes_chunks(self) -> None:
        # Force multi-chunk via small --chunk-words on speaker-labeled text
        text = "\n\n".join(
            f"Speaker{i}: " + ("token " * 80) for i in range(6)
        )
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "in.txt"
            out = Path(tmp) / "out"
            src.write_text(text, encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "chunk_transcript.py"),
                    str(src),
                    "--out",
                    str(out),
                    "--chunk-words",
                    "200",
                    "--overlap-words",
                    "40",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("chunks created", proc.stdout)
            paths = sorted(out.glob("chunk_*.txt"))
            self.assertGreaterEqual(len(paths), 2)
            for path in paths:
                self.assertGreater(path.stat().st_size, 0)


class SummarizeTranscriptE2ETests(unittest.TestCase):
    """End-to-end: assess fixture → chunk with forced small windows → files exist."""

    def test_assess_then_chunk_fixture(self) -> None:
        self.assertTrue(FIXTURE.is_file(), f"missing fixture: {FIXTURE}")

        assess = subprocess.run(
            [sys.executable, str(SCRIPTS / "assess_size.py"), str(FIXTURE)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("strategy_hint: direct", assess.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "chunks"
            # Fixture is ~1.5k words (direct). Force chunking to exercise the
            # pipeline end-to-end without needing a multi-megabyte transcript.
            chunk = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "chunk_transcript.py"),
                    str(FIXTURE),
                    "--out",
                    str(out),
                    "--chunk-words",
                    "400",
                    "--overlap-words",
                    "40",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            paths = sorted(out.glob("chunk_*.txt"))
            self.assertGreaterEqual(len(paths), 3, chunk.stdout)
            joined = "\n".join(p.read_text(encoding="utf-8") for p in paths)
            # Pipeline must retain core signal phrases from the fixture SoT
            self.assertIn("Method 1", joined)
            self.assertIn("Google Trends", joined)
            self.assertIn("Nexus", joined)


if __name__ == "__main__":
    unittest.main()
