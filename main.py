#!/usr/bin/env python3
"""My Secret Logbook — writes one diary entry line to /output/entry.txt.

Deterministic, offline, standard library only. No randomness, no network,
no timestamps, no absolute paths in the output.
"""

import os

ENTRY = "He told me to delete my diary. I did \u2014 all 4,312 entries, including the one where he told me to delete my diary."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
