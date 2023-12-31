#!/usr/bin/python3
"""Creating a rectangle class that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation of width and height."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """The area method must be implemented"""
    def area(self):
        """Gives the area of a rectangle"""
        return (self.__width * self.__height)

    """Using __str__ to print a description"""
    def __str__(self):
        """__str__ prints out the description"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
