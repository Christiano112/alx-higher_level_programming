#!/usr/bin/python3
""" class Rectangle and subclass Square """

Rectangle = __import__("9-rectangle").Recatangle


class Square(Rectangle):
    """ a representation of a square """
    def __init__(self, size):
        """ instantiation of the square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
