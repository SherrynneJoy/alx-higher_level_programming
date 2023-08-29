#!/usr/bin/python3
"""Creating a square object"""


class Square:
    """creating a private instance attribute of size"""
    def __init__(self, size=0):
        """To check if the size is valid"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """Creating a public instance of attribute area"""
    def area(self):
        return (self.__size * self.__size)
