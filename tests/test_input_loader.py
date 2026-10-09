import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.input_loader import load_input


def run_load_input(path):
    with patch.object(sys, "argv", ["network_analyzer.py", str(path)]):
        return load_input()


class InputLoaderTests(unittest.TestCase):
    def test_reads_input_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "input.txt"
            input_file.write_text("Partner Chris\n")
            self.assertEqual(run_load_input(input_file), "Partner Chris\n")

    def test_rejects_missing_file_and_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            for path in (Path(temp_dir) / "missing.txt", Path(temp_dir)):
                with self.subTest(path=path.name):
                    stderr = io.StringIO()
                    with (
                        contextlib.redirect_stderr(stderr),
                        self.assertRaises(SystemExit) as error,
                    ):
                        run_load_input(path)
                    self.assertEqual(error.exception.code, 2)
                    self.assertIn("does not exist or is not a file", stderr.getvalue())

    def test_reports_file_read_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "unreadable.txt"
            input_file.write_text("Partner Chris\n")
            with (
                patch.object(Path, "read_text", side_effect=OSError("read failed")),
                self.assertRaisesRegex(SystemExit, "could not read .*unreadable"),
            ):
                run_load_input(input_file)


if __name__ == "__main__":
    unittest.main()
