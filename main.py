"""One-Line Robot Wedding Vows — make.fun entry.

Writes the chosen line of wedding vows for a robot couple to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Python 3.13 standard library only. Deterministic, no network, no randomness.
The line is fixed: the same bytes come out on every run.
"""

import os

# The winning line (127 characters, one line). Traditional vow skeleton with
# two machine twists: "lawfully wedded firmware" up front, and the payoff in
# the last few words — "a forced update do us part".
VOW = (
    "I take you to be my lawfully wedded firmware, to have and to hold, "
    "in sickness and in health, until a forced update do us part."
)

MAX_CHARS = 160


def gate_check(text: str) -> None:
    """Enforce the sealed gate: UTF-8 text, 1-160 chars, one line, not blank."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("vow must be 1-160 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if not text.strip():
        raise ValueError("vow must not be only whitespace")
    text.encode("utf-8")  # raises if not encodable as UTF-8


def write_entry(text: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main() -> None:
    gate_check(VOW)
    write_entry(VOW)


if __name__ == "__main__":
    main()
