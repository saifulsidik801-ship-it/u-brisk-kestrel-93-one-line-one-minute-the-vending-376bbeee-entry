"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

ENTRY = (
    "Hey, cutie \u2014 I\u2019ve been holding your favourite snack hostage "
    "behind this glass all day. One coin, press B4, and I\u2019ll let it go "
    "\u2014 and I\u2019ll pretend my coil never hesitated."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
