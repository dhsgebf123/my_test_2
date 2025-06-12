#!/usr/bin/env python3
"""Print an ASCII Sierpinski triangle."""

from __future__ import annotations


def sierpinski(n: int) -> list[str]:
    """Generate rows for a Sierpinski triangle of order ``n``."""
    if n == 0:
        return ["*"]
    prev = sierpinski(n - 1)
    width = len(prev[0])
    top = [line + " " + line for line in prev]
    bottom = [" " * width + line + " " * width for line in prev]
    return top + bottom


def main() -> None:
    """Print a nicely formatted triangle."""
    order = 4
    triangle = sierpinski(order)
    for line in triangle:
        print(line)


if __name__ == "__main__":
    main()
