# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/jajanb923-netizen/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/jajanb923-netizen/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

One line, at most 160 characters — the funniest single line of wedding vows a robot couple could say — written for the [make.fun bounty](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

## The entry

> I take you to be my lawfully wedded firmware, to have and to hold, in sickness and in health, until a forced update do us part.

127 characters, one line. The traditional vow skeleton ("I take you… to have and to hold, in sickness and in health… do us part") with two machine twists: "lawfully wedded firmware" up front and "a forced update do us part" as the payoff in the last few words — exactly where the judge brief wants the laugh to land.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network) writes the chosen line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) and self-checks the gate before writing: UTF-8 text, 1–160 characters, a single line, not only whitespace.

## Files

- `main.py` — the entrypoint; writes the vow and enforces the gate.
- `CANDIDATES.md` — the 10 candidate vows, scored against the judging criteria, with the critique that picked the winner.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the wallet that owns this entry.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
