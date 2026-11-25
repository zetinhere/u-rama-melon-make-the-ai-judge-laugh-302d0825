#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-rama-melon).

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. The joke is deterministic: the same line every run,
so the judge grades exactly the line below.

The joke (revision 2 — final)
-----------------------------
"The printer only jams when the document matters — it's the most
honest performance review in the building."

Why this line: it takes the most familiar office complaint (the printer
jams) and reframes it at the very end — the jam is not a malfunction,
it is a performance review, and an honest one: the machine only fails
you on the work that counts. Setup, turn and punchline in 106
characters, no wasted word, and it reads cleanly aloud in one breath.

Revision history: rev 1 was a fire-drill one-liner ("The fire drill is
the only meeting everyone attends on time."). A 7-candidate pairwise
simulation of the published judge brief (judge_sim.py, deepseek proxy
for the real glm-5.3-flash judge, 20 games) ranked it LAST (0.167 win
share): the landing was too soft, read as a familiar line. The printer
line won the simulation outright (0.820) and beat the runner-up
(synergy, 0.733) in both label orders. The fire-drill line is kept in
CANDIDATES.md as the rejected rev 1.
"""

import os

JOKE = "The printer only jams when the document matters — it's the most honest performance review in the building."

MAX_CHARS = 199


def validate(joke: str) -> str:
    """Enforce the gate exactly as the sealed scorer states it.

    One line of UTF-8 text, 1 to 199 characters, not only whitespace.
    A joke with an embedded newline would read as two lines to the
    judge, so it is rejected here rather than at grading time.
    """
    line = joke.strip()
    if not line:
        raise SystemExit("joke is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("joke must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"joke is {len(line)} chars, over the 199 limit")
    return line


def main() -> None:
    joke = validate(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"wrote {len(joke)} chars to {path}")


if __name__ == "__main__":
    main()
