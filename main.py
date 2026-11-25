#!/usr/bin/env python3
"""The 3AM Fridge Text — a smart fridge texts its owner at 3am.

Writes one line to /output/entry.txt.
"""

import os

ENTRY = "3am. Third snack tonight. I'm not storing your food anymore, I'm storing evidence."


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    if not 1 <= len(value) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_fridge_voice(value):
    lowered = value.lower()
    if "3am" not in lowered:
        raise ValueError("entry must say 3am")
    if "i'm" not in lowered and "i am" not in lowered:
        raise ValueError("entry must speak in the fridge's first-person voice")


def check_no_cliche(value):
    lowered = value.lower()
    for cliche in ("milk", "ice cream", "door left open", "door open"):
        if cliche in lowered:
            raise ValueError("entry must avoid the obvious angle: %s" % cliche)


def check_no_joke_explaining_words(value):
    lowered = value.lower()
    for word in ("funny", "joke", "haha", "lol", "hilarious"):
        if word in lowered:
            raise ValueError("entry must not explain its own joke: %s" % word)


def check_no_control_chars(value):
    for ch in value:
        if ord(ch) < 32:
            raise ValueError("entry must not contain control characters")


def check_utf8(value):
    value.encode("utf-8")


def validate(value):
    for check in (
        check_is_text,
        check_not_blank,
        check_length,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_spaces,
        check_terminal_punctuation,
        check_fridge_voice,
        check_no_cliche,
        check_no_joke_explaining_words,
        check_no_control_chars,
        check_utf8,
    ):
        check(value)


def choose_output_path():
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    validate(ENTRY)
    path = choose_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
