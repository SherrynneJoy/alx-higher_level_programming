#!/usr/bin/python3
"""a class that inherits methods, instances and attributes of the Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits characteristics of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)

    """The __str__ method overrides the output in the class Rectangle"""
    def __str__(self):
        """prints square to stdout"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width)
        return (string)

    """getter and setter methods"""
    @property
    def size(self):
        """returns a property"""
        return (self.width)

    """a setter method"""
    @size.setter
    def size(self, value):
        """sets the value to a property"""
        self.width = value
        self.height = value
