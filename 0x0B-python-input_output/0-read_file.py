#!/usr/bin/python3
"""
module for read a text file (UTF8)
"""


def read_file(filename=""):
    """Open a file and print its text inside"""
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end='')
