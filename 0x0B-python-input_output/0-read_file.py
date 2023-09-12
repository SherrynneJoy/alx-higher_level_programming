#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads a file and prints to stdout"""
    with open("my_file_0.txt", encoding="UTF-8") as f:
        print(f.read())
