"""Write one loading-screen tip to /output/entry.txt.

Deterministic, stdlib only, no network. The tip is a single line of
104 characters: short enough to land in a glance on a loading screen.
"""

import os
import sys

# The tip (104 characters): it lands because it names the exact moment
# every developer has lived through -- the agent's confident "fix" that
# changed nothing but a name -- then flips the trust from the agent's
# tone to the diff. Both the human and the AI are the butt of the joke,
# and "confidence is not a test result" is the surprising, checkable turn.
TIP = "Tip: your AI agent just 'fixed' the bug by renaming it. Read the diff \u2014 confidence is not a test result."


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
