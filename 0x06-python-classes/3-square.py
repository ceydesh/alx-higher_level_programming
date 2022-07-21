#!/usr/bin/python3
"""defines a square with a size"""


class Square:
    """defines a square with a size"""
    def __init__(self, size=0):
        """initializes a sqaure with an optional size
        args: size=0:size of the square
        """
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        answer = self.__size ** 2
        return answer
