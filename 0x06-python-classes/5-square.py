#!/usr/bin/python3
"""Creating a square object"""


class Square:
    def __init__(self, size=0):
        self.size = size

    """Getter and setter method to retrieve and update the object"""
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

    """Creating public instance methods"""
    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character"""
        for i in range(0, self.__size):
            [print("#", end="")for j in range(self.__size)]
            print("")
        """to check if size is zero"""
        if self.__size == 0:
            print("")


