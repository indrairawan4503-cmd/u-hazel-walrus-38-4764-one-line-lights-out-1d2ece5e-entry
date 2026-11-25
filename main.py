#!/usr/bin/env python3
"""One Line, Lights Out — Builder A: THE UNSENT DRAFT.

A status update posted at the exact moment the human turns off the laptop:
the draft that will never be sent, the sentence left half-typed, the cursor
still blinking where the human stopped. Plain status-update voice, one small
exact machine detail, no announced grief.
Deterministic, no randomness, no network.
"""

import os

LINE = "Lid closed mid-sentence. Draft saved, never sent: \u201cThe report is almost done, I'll\u2014\u201d Cursor still blinking where you stopped."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert "  " not in LINE, "line must have no double spaces"

    # Write to /output FIRST (the grader reads this).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Also write next to main.py; the grader sandbox mounts the repo
    # read-only, so this must never crash the run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass

    print(f"{len(LINE)} chars")
    print(LINE)


if __name__ == "__main__":
    main()
