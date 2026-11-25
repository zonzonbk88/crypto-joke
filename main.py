"""Laugh Track: The Crypto Trading Joke Contest.

Writes exactly one joke (a single line, 1-200 characters) to
/output/entry.txt. Standard library only.
"""

import os

JOKE = "Gas fees are the only thing in crypto that goes up when everything else goes down."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def verify(path: str) -> str:
    """Read the entry back and enforce the contest gate."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises on invalid UTF-8
    if text.endswith("\n") or text.endswith("\r"):
        raise ValueError("entry must not end with a newline")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    return text


def main() -> None:
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    checked = verify(OUTPUT_PATH)
    assert checked == line
    print(f"entry ok: {len(checked)} chars")


if __name__ == "__main__":
    main()
