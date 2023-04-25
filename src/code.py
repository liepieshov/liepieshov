import sys


def main(title: str):
    if title.isnumeric() and int(title) < (1 << 9):
        print("Hello World!")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
