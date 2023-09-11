#!/usr/bin/python3
"""A class that inherits from list."""


class MyList(list):
    """list the superclass whereas MyList is the subclass."""
    def print_sorted(self):
        sorted_l = sorted(self)
        for element in sorted_l:
  #          print(element, end=' ')
        print()
