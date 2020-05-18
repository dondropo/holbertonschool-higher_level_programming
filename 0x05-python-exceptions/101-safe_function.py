#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        var = fct(*args)
    except Exception as identifier:
        var = "Exception: " + str(identifier) + '\n'
        stderr.write(var)
        return None
    return var
