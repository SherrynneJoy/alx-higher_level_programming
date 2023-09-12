#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


"""Creating a subclass that inherits from rectangle"""


class Square(Rectangle):
    """The square is made up of sides called (size)"""
    def __init__(self, size):
        """To validate the size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """str() prints our description"""
    def __str__(self):
        """returns the printed string"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return (string)
