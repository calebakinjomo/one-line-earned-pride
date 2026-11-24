#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 characters) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. No arguments, no network,
no dependencies — just the line.
"""

import os

LINE = (
    "At nine, after two years of sounding out every word, Sam read the "
    "bedtime story to his little sister all the way to the end, and she "
    "fell asleep before he did."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
