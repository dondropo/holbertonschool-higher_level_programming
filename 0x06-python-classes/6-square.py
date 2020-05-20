#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Square class with a construction method"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with size and area attribute"""

        self.__size = size

    def area(self, area=0):
        """defines area and makes the square operation into return"""

        return(self.__size * self.__size)

    def my_print(self):
        """print all the square with #"""

        if self.size == 0:
            print()
            return

        for i in range(self.size):
            print('#' * self.size)

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(' ', end='')
                else:
                    print('#', end='')
            print()

    @property
    def size(self):
        """getter of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
