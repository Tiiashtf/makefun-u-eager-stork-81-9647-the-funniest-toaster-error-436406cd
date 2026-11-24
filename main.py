#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line of text to /output/entry.txt: the error message a
kitchen toaster shows its owner when something goes wrong.

Deterministic, no network, no input. The line is a fixed string.
"""

import os
import shutil

ENTRY = "E03: Bread jammed. This is the most exciting thing that has ever happened to me."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run
    # this with a root-owned output directory inside a sticky parent,
    # where removing the directory fails with EPERM. Create it if it
    # is missing, clear only its contents, then write the entry file.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
