#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueErro('size must be >= 0')

        self.__size = size
