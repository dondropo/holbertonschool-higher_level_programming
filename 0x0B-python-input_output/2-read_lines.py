#!/usr/bin/python3
"""
Module that reads n lines of a text file
(UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """Read and print nb lines of a file"""
    line_count = 0
    with open(filename, encoding='UTF-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')
        for i in file:
            if line_count < nb_lines:
                print(i, end='')
                line_count += 1
