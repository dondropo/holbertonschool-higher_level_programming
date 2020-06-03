#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class Rectangle that inherits
from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Rectangle class with BaseGeometry inheritance"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
