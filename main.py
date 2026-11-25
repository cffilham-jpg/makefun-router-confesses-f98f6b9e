"""Write one router excuse to entry.txt in the output directory."""

import os
import tempfile


LINE = "The toaster bet me you'd scream."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("Excuse must not be empty or whitespace-only.")
    if len(text) > CHAR_LIMIT:
        raise ValueError(f"Excuse must be at most {CHAR_LIMIT} characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(LINE)


if __name__ == "__main__":
    main()
