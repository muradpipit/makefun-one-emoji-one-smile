#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty entry.

The task: send exactly one emoji, the one most likely to make a stranger
smile. This program writes that emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and nothing else.

The emoji is the hugging face. Open arms, a warm welcome, readable at a
glance by a stranger of any age or background: friendly without being
intimate, chosen rather than the first default smiley, and impossible to
read as sarcasm. A hug is the warmest thing one emoji can offer a stranger.

The program is fully deterministic: no randomness, no clock, no network,
no input. Every run writes the same single emoji, byte for byte.
"""

import os

EMOJI = "🤗"  # U+1F917 HUGGING FACE

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

    # Read it back and check the gate ourselves: exactly one character,
    # UTF-8, not whitespace. If anything is off, fail loudly instead of
    # handing the grader a bad file.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        print(f"ERROR: entry.txt holds {len(written)} characters, expected 1")
        return 1
    if written != EMOJI:
        print("ERROR: entry.txt does not match the chosen emoji")
        return 1
    print(f"Wrote one emoji to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
