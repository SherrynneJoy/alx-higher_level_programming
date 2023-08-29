#!/usr/bin/python3
"""Creating a square object"""


class Square:
    """creating a private instance attribute of size"""
    def __init__(self, size=0):
        self.size = size

    """Getter and setter methods to retrieve and update objects"""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """Creating a pulic instance attribute"""
    def area(self):
        return (self.__size * self.__size)
