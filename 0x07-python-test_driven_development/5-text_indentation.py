#!/usr/bin/python3

def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :.
    text must be a string or a TypeError will be
    raised.
    There shouldn't be s[aces at the start or end of a line."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    m = 0
    while m < len(text) and text[m] == '':
        m += 1

    while m < len(text):
        print(text[m], end="")
        if text[m] == "\n" or text[m] in ".?:":
            if text[m] in ".?:":
                print("\n")
            m += 1
            while m < len(text) and text[m] == '':
                m += 1
            continue
        m += 1
