#!/usr/bin/python3
""" class myInt """


class MyInt(int):
    """ MyInt class is a rebel """
    def __new__(cls, *args, **kwargs):
        """ create a new instance of the class """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ not equals to is now equals to """
        return int(self) != other

    def __ne__(self, other):
        """ equals to is now not eqauls to """
        return int(self) == other
