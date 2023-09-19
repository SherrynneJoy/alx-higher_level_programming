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

    """args and kwargs"""
    def update(self, *args, **kwargs):
        """updates the rectangle using args"""
        if args and len(args) != 0:
            num_args = 0
            for arg in args:
                if num_args == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num_args == 1:
                    self.size = arg
                elif num_args == 2:
                    self.x = arg
                elif num_args == 3:
                    self.__y = arg
                num_args += 1
        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id":
                    if n is None:
                        self.__init__(self.size, self.x, self.__y)
                    else:
                        self.id = n
                elif m == "size":
                    self.size = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.__y = n

    """a dictionary function"""
    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
