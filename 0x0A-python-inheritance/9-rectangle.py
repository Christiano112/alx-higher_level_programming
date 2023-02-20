#!/usr/bin/python3
""" class BaseGeometry and subclass Rectangle """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ a representation of a rectangle """
    def __init__(self, width, height):
        """ instantiation of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the area of the retangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation of the recatngle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
