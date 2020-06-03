#!/usr/bin/python3
"""
Module for look at the number
of lines of a text file
"""


def number_of_lines(filename=""):
    """Count the lines"""
    with open(filename, encoding='UTF-8') as file:
        line_count = 0
        for i in file:
            line_count += 1
            if not line_count:
                break
        return line_count
