#!/usr/bin/python3

def add_integer(a, b=98):
    """Returns the sum of a and b
    Float type arguments are cast into integer type
    If a and b are nither float nor integer, a TypeError occurs"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
