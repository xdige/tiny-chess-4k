# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/xdige/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/xdige/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python: alpha-beta search with a transposition table, quiescence over captures and check evasions, piece-square-table evaluation, and repetition-aware scoring, packed as an lzma payload in a single `main.py`. It plays the make.fun house gauntlet through the env at `MAKEFUN_ENV_URL`, searching to a fixed node budget — never a clock — so every replay matches move for move.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=3a39fjze&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
