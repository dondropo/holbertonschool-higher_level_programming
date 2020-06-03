#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """find the square area, with the inheritance of rectangle"""

        return self.__size * self.__size
