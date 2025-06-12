#!/usr/bin/env python3
"""Print the 9x9 multiplication table."""


def main() -> None:
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} * {i} = {i * j}", end="\t")
        print()


if __name__ == "__main__":
    main()
