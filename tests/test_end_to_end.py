import subprocess
import sys
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
ROOT = TESTS_DIR.parent
FIXTURES = TESTS_DIR / "fixtures"


def run_program(input_file):
    return subprocess.run(
        [sys.executable, "-B", str(ROOT / "analyze_network.py"), str(input_file)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class EndToEndTests(unittest.TestCase):
    def test_fixtures(self):
        """Run every fixtures/<name>.txt against fixtures/<name>.expected.txt.

        Success cases must exit 0 and print exactly the expected lines. Cases
        named error_<name> must exit non-zero with each expected line in stderr.
        """
        inputs = sorted(
            path
            for path in FIXTURES.glob("*.txt")
            if not path.name.endswith(".expected.txt")
        )
        self.assertTrue(inputs, "no fixtures found")

        for input_file in inputs:
            with self.subTest(fixture=input_file.stem):
                expected_file = input_file.with_suffix(".expected.txt")
                expected = expected_file.read_text().splitlines()
                result = run_program(input_file)

                if input_file.stem.startswith("error_"):
                    self.assertNotEqual(result.returncode, 0)
                    for line in expected:
                        self.assertIn(line, result.stderr)
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stdout.splitlines(), expected)


if __name__ == "__main__":
    unittest.main()
