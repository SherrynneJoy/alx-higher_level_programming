#!/usr/bin/python3
"""Creating a class called Base"""


class Base:
    """This will be the base of all other classes"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
