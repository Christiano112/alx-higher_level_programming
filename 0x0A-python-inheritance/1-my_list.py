#!/usr/bin/python3
""" a class called MyList """


class MyList(list):
    """ a subclass of list """
    def __init__(self):
        """ initialize theobject """
        super().__init__()

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
