#!/usr/bin/env python3
"""Print an ASCII Sierpinski triangle."""

from __future__ import annotations


def sierpinski(n: int) -> list[str]:
    """Generate rows for a Sierpinski triangle of order ``n``."""
    if n < 0:
        raise ValueError("order must be non-negative")
    if n == 0:
        return ["*"]
    prev = sierpinski(n - 1)
    pad = " " * (2 ** (n - 1))
    top = [pad + line + pad for line in prev]
    bottom = [line + " " + line for line in prev]
    return top + bottom


def main() -> None:
    """Print a Sierpinski triangle to stdout."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--order",
        type=int,
        default=3,
        help="triangle order (non-negative integer)",
    )
    args = parser.parse_args()

    triangle = sierpinski(args.order)
    for line in triangle:
        print(line)


if __name__ == "__main__":
    main()
