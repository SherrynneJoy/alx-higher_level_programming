#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = list(a_dictionary.keys())
    sorted_dict.sort()
    for i in sorted_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
