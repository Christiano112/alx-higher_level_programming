#!/usr/bin/python3
""" contains the class BaseGeometry """


class BaseGeometry:
    """ a class with public atribute called area """
    def area(self):
        """ raises an exeception when called """
        raise Exception("area() is not implemented")
