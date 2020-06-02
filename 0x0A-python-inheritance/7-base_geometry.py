#!/usr/bin/python3
"""
Write a BaseGeometry class
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """exception raiser"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """conditions"""

        if type(value) is not int:
            raise TypeError(str(name) + " <name> must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " <name> must be greater than 0")
