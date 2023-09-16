#!/usr/bin/python3
"""A class that inherits methods of  Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits methods of class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    """Each attribute has its own getter and setter"""
    @property
    def width(self):
        return (self.__width)

    """width setter"""
    @width.setter
    def width(self):
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    """height setter"""
    @height.setter
    def height(self):
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    """x setter"""
    @x.setter
    def x(self):
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    """y setter"""
    @y.setter
    def y(self):
        self.__y = y
