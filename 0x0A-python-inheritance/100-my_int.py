#!/usr/bin/python3
"""a class that inherits from int"""


class MyInt(int):
    """MyInt inherits from int"""

    def __eq__(self, value):
        """changes the equal sign to not equal"""
        return self.real != value

    def __ne__(self, value):
        """"changes the not equal to operator to the equal to operator"""
        return self.real == value
