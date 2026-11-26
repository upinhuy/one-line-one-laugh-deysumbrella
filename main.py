"""One Line, One Laugh — entry program.

Reads the single funny line from entry.txt (shipped in this repository)
and writes it to /output/entry.txt, where the make.fun gate and judge
read it. The line is one sentence pair, 1-140 characters, plain UTF-8.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        line = f.read().strip()
    # The gate accepts UTF-8 text of 1 to 140 characters, not only
    # whitespace. Refuse to write anything outside that window so a
    # bad line fails loudly here instead of silently at the gate.
    if not line or len(line) > 140:
        print(f"entry must be 1-140 characters, got {len(line)}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
