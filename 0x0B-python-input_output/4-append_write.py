#!/usr/bin/python3
"""
Module for function that appends a string at
the end of a text file (UTF8) and returns the
number of characters added
"""


def append_write(filename="", text=""):
    """Append a text inside a file"""
    a = 0
    with open(filename, mode='a', encoding='UTF-8') as file:
        a = file.write(text)
        return a
