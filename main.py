#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Entry program: writes a two-line explanation of one everyday thing
(a toaster) to /output/entry.txt.

Line 1 explains the toaster to a 10-year-old in a single vivid sentence
built on one analogy. Line 2 says in one sentence what that analogy
maps and what it leaves out.
"""

import os

TEXT = (
    "A toaster is a tiny lift that dips your bread into glowing wires "
    "and pops it back up when it turns brown.\n"
    "It maps the ride down, the wait, and the pop, but it leaves out "
    "that the bread never moves by itself and the heat comes from wires, not fire.\n"
)


def main():
    lines = TEXT.splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines"
    assert 1 <= len(TEXT) <= 400, "entry must be 1 to 400 characters"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    print("wrote %d characters to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
