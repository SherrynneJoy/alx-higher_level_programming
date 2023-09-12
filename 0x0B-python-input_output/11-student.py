#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """defines a student by first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """a public method to retrieves a dictionary representation of Student"""
    def to_json(self, attrs=None):
        """using the dict method"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)

    """method that replaces all attributes of the Student instance"""
    def reload_from_json(self, json):
        """assumes json will always be a dictionary"""
        for k, v in json.items():
            setattr(self, k, v)
