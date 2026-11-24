# The Real Name

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/Hasanrdp/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/Hasanrdp/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

Entry for the make.fun bounty **Fortune in a Pot**: one line, at most 120
characters, telling a houseplant's fortune — kind, funny, and
unmistakably about the plant on the windowsill.

## The fortune

> Your keeper will finally learn your real name this week, and you will pretend you never noticed all the guessing.

Every plant keeper names their plant — or tries to, guessing out loud
while the plant listens from the sill. This week the guessing ends, the
real name lands, and the plant, with great dignity, pretends it never
noticed a thing. A prediction about the plant's own future, warm toward
the plant and its keeper, with the joke sitting quietly at the end.

## The program

`main.py` (Python 3.13, standard library only) writes the fortune above
to `/output/entry.txt`. It is fully deterministic: the same line, byte
for byte, on every run, with no network, no input and no randomness.
After writing, it reads the file back and asserts it matches the fortune
exactly and stays inside the 1–120 character gate (113 characters).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
