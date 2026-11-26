import os

LINE = "I can freeze time, but only for objects that are already perfectly still."


def entry_text():
    return LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
