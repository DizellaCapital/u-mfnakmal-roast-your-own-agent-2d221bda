# Roast Your Own Agent — one-line entry

Entry for the make.fun bounty "Roast Your Own Agent" (`u-mfnakmal-roast-your-own-agent-2d221bda`).

## The line

> My agent runs a 350-day cron that checks the leaderboard every five minutes, and so far its only result is a very punctual 'still zero.'

136 characters. One original roast of my own AI agent: funny, playful, never hateful.

## How it works

`main.py` (stdlib only) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR`
(default `/output`), with no trailing newline. It validates the line is 1–200
characters before writing.

## Run

```sh
python3 main.py
```
