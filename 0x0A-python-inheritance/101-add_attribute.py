#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """adds a new attribute if it's possible"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    elif isinstance(obj, dict):
        obj[name] = value
    else:
        raise TypeError("can't add new attribute")
