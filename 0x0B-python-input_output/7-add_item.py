#!/usr/bin/python3
"""a script that adds all arguments to a Python list, and then
save them to a file"""
import json
import sys
import os


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    if os.path.exists("add_item.json"):
        elements = load_from_json_file("add_item.json")
    else:
        elements = []

    #adding command line args to the list
    for arg in sys.argv[1:]:
        elements.append(arg)

    #save the list in a file called add_item.json
    save_to_json_file(elements, "add_item.json")
