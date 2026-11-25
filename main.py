#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline
(1-200 characters, one line) to /output/entry.txt.
Python 3, standard library only. No network, no reads outside this file.
"""

import sys
from pathlib import Path

JOKE = "I finished it in my head three days ago; unfortunately, my hands were on holiday."
OUT = Path("/output/entry.txt")
LIMIT = 200


def check(text: str) -> str | None:
    if not text.strip():
        return "entry must not be blank"
    if text != text.strip():
        return "entry must not have leading or trailing whitespace"
    if len(text) > LIMIT:
        return f"entry must be at most {LIMIT} characters (got {len(text)})"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    # The judge brief wants one sentence: a second sentence-terminator
    # anywhere except the very end means the line is two sentences.
    body = text.rstrip(".!?")
    if any(mark in body for mark in ".!?"):
        return "entry must be a single sentence"
    return None


def main() -> int:
    problem = check(JOKE)
    if problem:
        print(problem, file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
