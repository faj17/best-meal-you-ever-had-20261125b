#!/usr/bin/env python3
"""The Best Meal You Ever Had entry: writes one sentence about the best
meal the entrant ever had to /output/entry.txt.

The meal is a real memory, built from three fragments: the DISH (a
named dish and who cooked it), the PLACE (one kitchen, one town), and
the MOMENT (the broth fogging glasses, the shallots crackling) — the
image that stays after a single read.
"""

import os

MAX_CHARS = 200

# Dish: the named dish and whose hands made it.
DISH = "The best meal I ever had was my grandmother's soto ayam"
# Place: one kitchen in one town.
PLACE = "in her Bojonegoro kitchen,"
# Moment: the heat, the fogged glasses, the crackling shallots.
MOMENT = "the broth so hot it fogged my glasses while the fried shallots crackled over the rice."


def assemble():
    """Join the fragments into the single memory sentence."""
    return f"{DISH} {PLACE} {MOMENT}"


def validate(text):
    """Gate: 1-200 chars of UTF-8 text, not only whitespace, exactly
    one sentence, no doubled spaces, ends on a full stop."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must not contain doubled spaces")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if len(text.split()) < 10:
        raise ValueError("entry is too short to be a real memory")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
