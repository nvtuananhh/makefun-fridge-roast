"""Fridge Roast: One Line, Biggest Laugh — one roast of a smart fridge.

The program writes a single line to /output/entry.txt: a smart fridge
that updated its firmware at 3 a.m., broke its own ice maker, and
then asked its owner to rate the update five stars.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The roast's twist lands in the last words: rate the update five stars.
# The firmware update is the joke: it broke the ice maker, then graded itself.
# No grocery-ordering or spying crack — the update is the fresh angle.
LINE = "My smart fridge updated its firmware at 3 a.m., broke the ice maker, and asked me to rate the update five stars."


def build_line():
    """Return the entry line, checked: one line, under 200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
