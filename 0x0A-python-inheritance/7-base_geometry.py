#!/usr/bin/python3
"""an empty class BaseGeometry"""


class BaseGeometry:
    """Creates an empty class"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.".format(name))
