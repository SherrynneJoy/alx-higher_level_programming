#!/usr/bin/python3

def max_integer(list=[]):
    """checks for maximum integer in a list.
    If list is empty, the function returns None."""

    if len(list) == 0:
        return None
    res = list[0]
    j = 1
    while j < len(list):
        if list[j] > res:
            res = list[j]
        j += 1
    return res
