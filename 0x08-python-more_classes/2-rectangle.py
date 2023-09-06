#!/usr/bin/python3
"""Creating a rectangle"""


class Rectangle:
    """Defines an empty class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Getter and setter methods to update and retrieve data"""
    @property
    def width(self):
        return (self.__width)

    """Private instance for width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Private instance for height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Public instance to calculate the area of the rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """Public instance to calculate the perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return ((self.__width * 2) + (self.__height * 2))
