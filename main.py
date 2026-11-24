"""One Word From Grandma — entry program.

Writes the single word a grandma would text about AI to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``).

The word: "Rosie" — the robot maid from The Jetsons. A grandma who grew
up watching the Jetsons in the 1960s calls every AI a Rosie: she thinks
the talking machine is a household helper with a name, an apron and
opinions. Warm, a little baffled, and exactly her generation's robot.
"""

import os

WORD = "Rosie"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_text() -> str:
    """Return the entry word, exactly as it goes into the file."""
    return WORD


def validate(text: str) -> None:
    """Gate check: UTF-8 text of 1 to 30 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry must be 1-30 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> None:
    """Validate the word and write it to entry.txt."""
    text = entry_text()
    validate(text)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
