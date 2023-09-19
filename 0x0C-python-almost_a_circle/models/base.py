#!/usr/bin/python3
"""Creates the base class for all other classes"""
import json
import csv


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

    """saving a file using json"""
    @classmethod
    def save_to_file(cls, list_objs):
        """saves a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    """from json to string"""
    @staticmethod
    def from_json_string(json_string):
        """converts from json to string"""
        if json_string is None or json_string == []:
            return ([])
        return json.loads(json_string)
