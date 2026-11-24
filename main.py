#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry generator.

Deterministic, no network. Writes exactly one line (the entry) to
/output/entry.txt, creating /output if needed.
"""

import os

ENTRY = (
    "Texted my boss 'sorry, running late' \u2014 autocorrect sent "
    "'sorry, running naked.' HR ticket #4821 was opened before I "
    "even parked the car."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
