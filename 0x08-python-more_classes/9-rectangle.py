#!/usr/bin/python3
"""Creating a rectangle"""


class Rectangle:
    """Public class attribute to count number of instances"""
    number_of_instances = 0
    """Public class attribute used as a symbol for string repr"""
    print_symbol = "#"
    """Defines an empty class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    """Static method to compare rectangle sizes"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)

    """Class method that returns a new rectangle instance"""
    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    """Methods to print the rectangle using the # symbol"""
    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns a printable representaion of the rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    """Deleting an instance of the rectangle object"""
    def __del__(self):
        """Prints a message for every instance deletion"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
