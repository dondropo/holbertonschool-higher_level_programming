#!/usr/bin/python3
"""
Module for that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a text inside a file"""
    writer = 0
    with open(filename, mode='w', encoding='UTF-8') as file:
        writer = file.write(text)
        return writer
