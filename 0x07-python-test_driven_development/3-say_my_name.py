#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """prints a name where first_name and last_name
    are strings. If not a TypeError is raised."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
