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
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    """height setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    """x setter"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    """y setter"""
    @y.setter
    def y(self, value):
        if not isinstance(int, value):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """a public method that returns the area of the rectangle"""
    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    """a publlic method to print the rectanglee in stdout"""
    def display(self):
        """prints the rectangle using the '#' symbol"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    """the __str__ method"""
    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)

    """the args and kwargs functions"""
    def update(self, *args, **kwargs):
        """updates the rectangle using args"""
        if args and len(args) != 0:
            num_args = 0
            for arg in args:
                if num_args == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                self.__y)
                    else:
                        self.id = arg
                elif num_args == 1:
                    self.__width = arg
                elif num_args == 2:
                    self.__height = arg
                elif num_args == 3:
                    self.__x = arg
                elif num_args == 4:
                    self.__y = arg
                num_args += 1
        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id":
                    if n is None:
                        self.__init__(self.__width, self.__height, self.__x,
                                self.__y)
                    else:
                        self.id = n
                elif m == "width":
                    self.__width = n
                elif m == "height":
                    self.__height = n
                elif m == "x":
                    self.__x = n
                elif m == "y":
                    self.__y = n
