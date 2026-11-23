#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes the single roast line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Stdlib only. No network, no input files.
"""

import os

LINE = "My agent runs a 350-day cron that checks the leaderboard every five minutes, and so far its only result is a very punctual 'still zero.'"


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("empty roast line")
    if len(line) > 200:
        raise SystemExit("roast line exceeds 200 characters")
    data = line.encode("utf-8")
    if not 1 <= len(data) <= 200:
        raise SystemExit("roast line must be 1-200 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
        return
    except OSError:
        pass
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(fallback, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
