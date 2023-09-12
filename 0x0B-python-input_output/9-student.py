#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """defines a student by first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """a public method to retrieves a dictionary representation of Student"""
    def to_json(self):
        """using the dict method"""
        return (self.__dict__)
