#!/usr/bin/python3
""" A module that defines a square """


class Square:
    """ A class representation of a square class"""

    def __init__(self, size=0):
        """ Initializing this square class
        Args:
            size: stands for the size of the square defined
        """

        if not isinstance(size, int):
            raise TypeError('size mustbe an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """ Retrieves size of a square """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: the current area of the square
        """

        return (self.__size ** 2)
