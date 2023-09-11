#!/usr/bin/python3
"""A class that inherits from list."""


class MyList(list):
    """list the superclass whereas MyList is the subclass."""
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
