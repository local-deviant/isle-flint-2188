"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The program is fully deterministic: no input, no file reads, no randomness,
no clock, no network. It writes the same fixed text on every run, with no
trailing newline.
"""

import os
from pathlib import Path

TEXT = "Error: slot occupied. Nothing inserted. Please remove the nothing and try again."


def main() -> None:
    """Write the entry text to /output/entry.txt (or $ENTRY_OUTPUT)."""
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
