#!/usr/bin/python3
"""Creates the base class for all other classes"""


class Base:
    """a class object"""
    __nb_objects = 0

    """Instantiation"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects