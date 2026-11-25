#!/usr/bin/env python3
"""Write the single-line excuse to /output/entry.txt.

Deterministic, standard library only, no network. The output is exactly
one line with no trailing newline, inside the gate: 1-140 characters
and at most 20 words.
"""

import os

ENTRY = "Sorry, my boiler burst overnight and the emergency plumber says I can't leave the flat until it's fixed"


def main():
    # Guard the gate so a future edit to ENTRY cannot silently break it.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert len(ENTRY.split()) <= 20, "entry must be at most 20 words"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # newline="" keeps the write byte-exact: no trailing newline is added.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
