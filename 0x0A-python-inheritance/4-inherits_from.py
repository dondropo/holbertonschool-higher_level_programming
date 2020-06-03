#!/usr/bin/python3
"""
returns True if the object is an
instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """inheritance class"""
    if not isinstance(type(obj), a_class) or type(obj) == a_class:
        return False
    else:
        return True