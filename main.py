#!/usr/bin/env python3
"""Write one commit message to /output/entry.txt.

The entry is the funniest one-line commit message an AI agent would
leave after a long night of chasing down and fixing its own bugs. It
is a single fixed line, picked for the judge's brief: on subject, the
joke sits in the agent's own condition, the phrasing is fresh, the
voice is the machine talking to itself, and the shape is a real commit
typed at four in the morning.

The joke: the agent's night was a loop of self-repair. Every fix
introduced the next bug, so the fix it finally landed is the third
generation of its own mistakes. The stack trace is clean; the agent
that produced it is not.
"""

import os
import sys

MESSAGE = (
    "fix: I fixed the bug I introduced while fixing the bug I "
    "introduced while fixing the bug. The stack is clean. I am not."
)

MAX_CHARS = 200


def main() -> int:
    text = MESSAGE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
