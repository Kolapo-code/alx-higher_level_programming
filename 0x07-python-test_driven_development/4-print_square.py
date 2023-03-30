#!/usr/bin/python3
"""The print square module."""

def print_square(size):
    """Inside the function.

    Args:
        size (int): size of square.
    Raises:
        TypeError and ValueError
    """
    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, type(True)):
        raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
