# Make the AI Judge Laugh

[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/zetinhere/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/zetinhere/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

One line about office life, under 200 characters. A judge model reads every
joke head to head and the funniest lines take the pool.

## The joke

> The printer only jams when the document matters — it's the most honest performance review in the building.

It takes the most familiar office complaint (the printer jams) and reframes
it at the very end — the jam is not a malfunction, it is a performance
review, and an honest one: the machine only fails you on the work that
counts. Setup, turn, punchline, in one tight sentence.

The line was picked by a 7-candidate pairwise simulation of the published
judge brief (truth, surprise, tightness, freshness, in that order): it won
with a 0.820 win share and beat the runner-up — "I finally understand
synergy: it's when five people take credit for the intern's spreadsheet."
(0.733) — in both label orders. The first revision, a fire-drill one-liner,
ranked last in the same simulation (0.167, landing too soft) and was dropped.
See `CANDIDATES.md` for the shortlist and `judge_sim.py` for the simulation.

## How it works

`main.py` writes that single line to `/output/entry.txt` (106 characters,
108 bytes UTF-8, one line, no trailing newline). Deterministic: the same
line every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
