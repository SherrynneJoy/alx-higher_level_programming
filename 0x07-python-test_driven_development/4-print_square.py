#!/usr/bin/python3

def print_square(size):
    """prints a square with the # symbol.
    size is the size length of the square.
    If size is not an integer a TypeError is raised.
    If size is less than zero, a ValueError is raised.
    If size is a float and less than 0, a TypeError is raised."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print('#', end="")for j in range(size)]
        print("")
