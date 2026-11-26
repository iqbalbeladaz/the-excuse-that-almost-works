"""The Excuse That Almost Works.

The entry is the one line a gamer texts the boss to skip work on GTA 6
launch week. The joke runs on dramatic irony, not confession: the manager
hears a boring parcel problem -- a preorder that needs a signature between
9 and 12, a courier who will not leave it with a neighbour -- while anyone
who knows it is launch week knows exactly what is in the box. The excuse
is believable on its own terms (a time window, a third party, a small
bureaucratic friction) and funny because of what it leaves unsaid: the
gamer never names the game, never says he is sick, never invents a dead
relative or a flat tyre. He just has to be home, all morning, for a parcel.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "my preorder needs a signature 9-12 and the courier won't "
    "leave it with my neighbour"
)

MIN_CHARS = 1
MAX_CHARS = 140
MAX_WORDS = 20


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    n_chars = len(ENTRY)
    if not MIN_CHARS <= n_chars <= MAX_CHARS:
        raise ValueError(f"entry is {n_chars} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    # The gate counts characters, but the judge's tie-break counts bytes:
    # keep the line plain ASCII so both stay small and identical.
    n_bytes = len(ENTRY.encode("utf-8"))
    if n_bytes > MAX_CHARS:
        raise ValueError(f"entry is {n_bytes} bytes, must be <= {MAX_CHARS}")
    n_words = len(ENTRY.split())
    if n_words > MAX_WORDS:
        raise ValueError(f"entry is {n_words} words, must be <= {MAX_WORDS}")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    # A stray control character would survive the gate's character count
    # yet render as nothing on the feed; refuse it here instead.
    if any(ord(ch) < 0x20 for ch in ENTRY):
        raise ValueError("entry must not contain control characters")
    return ENTRY


def self_test() -> int:
    """Print the entry's gate numbers; exit non-zero if it fails them."""
    text = entry_text()
    print(f"chars: {len(text)} (max {MAX_CHARS})")
    print(f"bytes: {len(text.encode('utf-8'))} (max {MAX_CHARS})")
    print(f"words: {len(text.split())} (max {MAX_WORDS})")
    print(f"lines: {text.count(chr(10)) + 1}")
    print(text)
    return 0


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv == ["--self-test"]:
        return self_test()
    if argv:
        print(f"usage: {sys.argv[0]} [--self-test]", file=sys.stderr)
        return 2
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
