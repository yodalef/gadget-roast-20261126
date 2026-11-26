#!/usr/bin/env python3
"""Entry for make.fun 'One-Line Roast: The Gadget You Use Every Day'.

Writes one line roasting an everyday gadget (1-200 chars) to the
output directory's entry.txt: MAKEFUN_OUTPUT_DIR when set, else
/output, else ./output next to this file.  No network use.
"""
import os

LINE = ("My smartphone: a supercomputer that video-calls across the "
        "planet, used daily as a flashlight, a teeth-checking mirror, "
        "and a $1,200 way to ignore people in person.")

MAX_CHARS = 200


def validated_line():
    """The entry line, checked against the competition's 1-200 limit."""
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry line must be 1-%d chars, got %d"
                         % (MAX_CHARS, len(line)))
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    last_err = None
    for out_dir in candidates:
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(validated_line() + "\n")
            print(path)
            return
        except OSError as e:
            last_err = e
    raise last_err


if __name__ == "__main__":
    main()
