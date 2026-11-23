"""One-Line Laugh Sprint.

Writes a single original funny line to /output/entry.txt.
Deterministic: stdlib only, no network, no clock, no randomness.
"""

import os

JOKE = "My Wi-Fi only drops during important meetings, which is how I learned my router has a better sense of drama than I do."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

