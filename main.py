#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten, in the dog's own voice. Standard library only.
"""

import os

ENTRY = "The homework barked first, so I ate the witness."


def main() -> None:
    # Gate: exactly one line, 1-200 characters, non-empty (not only whitespace).
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be empty or only whitespace"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    assert len(lines) == 1, "output must be exactly one line"
    assert lines[0] == ENTRY, "output must match the entry"
    assert 1 <= len(lines[0]) <= 200, "output line must be 1-200 characters"


if __name__ == "__main__":
    main()
