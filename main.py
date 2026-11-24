import os

ENTRY = "SockMate uses AI to match your socks by personality, so the lonely argyle finally finds love — $4.99 a month, socks not included, happiness not guaranteed."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
