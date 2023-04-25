import sys


def main(title: str):
    if not title.isnumeric() or int(title) >= (1 << 9):
        sys.exit(1)
    print("Hello World!")
    print(title)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
