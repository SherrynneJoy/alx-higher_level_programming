#!/usr/bin/python3
"""Creates the base class for all other classes"""
import json


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

    """JSON library functions"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return json.dumps(list_dictionaries)
