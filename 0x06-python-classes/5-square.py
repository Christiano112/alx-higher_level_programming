#!/usr/bin/python3
""" A class that defines a square """


class Square:
    """ Representation of the square class """

    def __init__(self, size=0):
        """ Initializing this square class
        Args:
            size: stands for the size of the square defined
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(slef):
        """ Retrieves size of square """

        return self.__size

    @size.setter
    def size(slef, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square
        Returns: the current areabof the square size
        """

        return (self.__size ** 2)

    def my_print(self):
        """ print the square as # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.size)
