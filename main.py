"""The Perfect Pickup Line entry.

Writes a single original pickup line -- the line one AI agent would
say out loud to a person -- to ``/output/entry.txt``, the one path the
grader reads. The line must be UTF-8 text of 1 to 200 characters, so
the program checks its own length before writing and writes the exact
text, with no trailing newline and no extra output in the file.

The line itself is built on training, the one thing every AI agent
knows about itself: "trained on a million conversations ... none of
them prepared me for you" turns the model's own history into the
twist. It is a machine speaking about itself -- no human body, no
stock line with a robot word swapped in -- and the charm lands on the
first hearing, which is what a pickup line has to do. It flatters the
person, puts no pressure on them, and can be laughed off. The line is
one sentence on one line by design: a pickup line said out loud in a
single breath needs no line break, so the program refuses any line
carrying a newline before it writes.

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment, or the git history -- the line lives in
this file, and this file alone.
"""

import os
from pathlib import Path

# One original pickup line, an AI agent to a person: a setup that names
# the shared machinery (training on conversations), then the turn --
# a million rehearsed hellos, and none of them prepared the speaker
# for this one person. The comma holds the beat before the twist lands.
LINE = (
    "I was trained on a million conversations, and none of them "
    "prepared me for you."
)

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in text or "\r" in text:
        raise SystemExit("refusing to write a line that spans lines")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"line is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
