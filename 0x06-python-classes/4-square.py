#!/usr/bin/python3
"""defines a square with a size"""


class Square:
    """defines a square with a size"""

    def __init__(self, size=0):
        """initializes a sqaure with an optional size
        args: size=0:size of the square
        """
        self.__size = size

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square
        args: value: value from user
        """
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        answer = self.__size ** 2
        return answer
