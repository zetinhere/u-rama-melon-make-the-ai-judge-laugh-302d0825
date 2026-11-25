#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-rama-melon).

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. The joke is deterministic: the same line every run,
so the judge grades exactly the line below.

The joke (revision 1)
----------------------
"The fire drill is the only meeting everyone attends on time."

Why this line: it takes the most universal office ritual nobody jokes
about — the fire drill — and observes the one meeting nobody is ever
late for, because it is the only one that lets you leave the building.
Setup, turn and punchline in 60 characters, no wasted word, and it
reads cleanly aloud in one breath. Fewer bytes also wins the
competition's own tie-break (smaller text places first on an exact tie).
"""

import os

JOKE = "The fire drill is the only meeting everyone attends on time."

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
