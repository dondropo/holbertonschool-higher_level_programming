#!/usr/bin/python3
"""Creates a rectangle class that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize rectangle weight and height"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width.
        check if value is an int an if value < 0
        """
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height
        check if value is an int an if value < 0
        """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """calculate area"""

        return self.__height * self.__width

    def perimeter(self):
        """Calculate perimeter"""

        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with '#'"""

        var = ''
        if self.__width is 0 or self.__height is 0:
            return var
        for i in range(self.__height):
            for j in range(self.__width):
                var += str(self.print_symbol)
            if i != self.__height - 1:
                var += '\n'
        return var

    def __repr__(self):
        """Print rectangle's value"""

        w = str(self.__width)
        h = str(self.__height)
        var = "Rectangle(" + w + ", " + h + ")"
        return var

    def __del__(self):
        """Print bye rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
