#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line — the funniest one-line review of my own Monday —
to /output/entry.txt. No title, no explanation, just the line.

Revision notes (second write, in-session): the first draft was a flat
list of complaints with no turn. The revised line keeps the concrete
details (9 a.m. "quick sync", triple-digit inbox) but frames it as an
actual review — star rating included — and lands the joke at the end:
the commute home, the worst part of most days, was the highlight.
Deadpan, repeatable to a coworker, no wasted words.
"""

import os

LINE = (
    "Monday, reviewed: my 9 a.m. 'quick sync' ran 90 minutes, my inbox "
    "hit triple digits before lunch, and the commute home was the "
    "highlight \u2014 one star, would not recommend."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
