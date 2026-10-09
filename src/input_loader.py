"""Takes arguments from the command line using argparse library and reads the content of the provided input file."""

import argparse
from pathlib import Path


def load_input() -> str:
    parser = argparse.ArgumentParser(
        description="Analyze partner relationships from an input text file."
    )
    parser.add_argument(
        "infile",
        type=Path,
        help="Path to the input text file (based on the current working directory)",
    )
    args = parser.parse_args()

    # ensure that the input file exists and is a file that is readable
    if not args.infile.is_file():
        parser.error(f"input file does not exist or is not a file: {args.infile}")

    # attempt to read the content of the input file, throw error if failure
    try:
        return args.infile.read_text()
    except OSError as e:
        raise SystemExit(f"could not read {args.infile}: {e}") from e
