"""Warning Label for Humans: One Line, Big Laugh.

Writes the chosen one-line safety warning label to /output/entry.txt.
Pure standard library, Python 3.13.
"""

import os

ENTRY = "WARNING: This human will only read the instructions after breaking the thing. Warranty void since birth."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """The gate: 1 to 160 characters, one line, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} characters, over the 160 limit")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
