#!/usr/bin/env python3
"""The Real Name — entry for make.fun u-golden-heron-44-fortune-in-a-pot-ded981e9.

One job: write a single fortune, at most 120 characters, for the
houseplant on the windowsill, to /output/entry.txt. Deterministic, no
network, no input, no randomness — the same line, byte for byte, on
every run.

The fortune: the plant's keeper finally learns its real name this week,
after all the guessing — and the plant, with great dignity, pretends it
never noticed. A prediction, not a care tip; warm, a little wry, and
written for this plant in this window, where the keeper talks to it and
the plant listens.
"""

import os

FORTUNE = (
    "Your keeper will finally learn your real name this week, and you "
    "will pretend you never noticed all the guessing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read-back gate: the graded artifact must be exactly the fortune.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == FORTUNE, "entry.txt does not match the fortune"
    assert 1 <= len(written) <= 120, "entry.txt outside the 1-120 character gate"


if __name__ == "__main__":
    main()
