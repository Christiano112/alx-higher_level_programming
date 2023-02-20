#!/usr/bin/python3
""" contains a function called is_kind_of_class """

def is_kind_of_class(obj, a_class):
    """ true if obj is an instance or inherited, else false """
    return (isinstance(obj, a_class))
