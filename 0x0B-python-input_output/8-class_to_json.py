#!/usr/bin/python3
"""a function that returns the dictionary description with simple data
structure(list, dictionary, string, integer and boolean) for JSON
serialization of an object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    serial = {}

    for attr_name in dir(obj):
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)

            if isinstance(attr_value, (list, dict, str, int, bool)):
                serial[attr_name] = attr_value

    return (serial)
