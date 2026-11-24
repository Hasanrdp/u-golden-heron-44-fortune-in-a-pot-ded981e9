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

import hashlib
import os
import sys

FORTUNE = (
    "Your keeper will finally learn your real name this week, and you "
    "will pretend you never noticed all the guessing."
)

OUTPUT_PATH = "/output/entry.txt"

# Pinned digest of the exact bytes this program must write: the 113-char
# fortune encoded as UTF-8 (113 bytes, pure ASCII).
EXPECTED_SHA256 = "da13a0ab4af5c5515fcf4fdf17de2584cb96ba692faba7de4f1ca209e3c5769d"
EXPECTED_BYTES = 113


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read-back gate: what landed on disk must match the fortune exactly —
    # exact bytes, exact length (113), and the pinned sha256 digest.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != FORTUNE.encode("utf-8"):
        print("error: read-back mismatch: output differs from the fortune",
              file=sys.stderr)
        return 1
    if len(raw) != EXPECTED_BYTES:
        print(f"error: read-back length: found {len(raw)} bytes, "
              f"expected {EXPECTED_BYTES}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"error: read-back sha256: found {digest}, "
              f"expected {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    if not 1 <= len(raw) <= 120:
        print("error: entry.txt outside the 1-120 character gate",
              file=sys.stderr)
        return 1
    print(f"verified: {len(FORTUNE)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
