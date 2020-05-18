#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as exon:
        print("Exception: {}", exon, file=stderr)
        return False
    return True
