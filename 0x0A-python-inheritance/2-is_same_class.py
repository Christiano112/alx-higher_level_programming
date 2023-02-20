#!/usr/bin/python3
""" contains a function called is_same_class """

def is_same_class(obj, a_class):
    """ returns true if obj is the exact class as a_class, else returns false """
    return (type(obj) == a_class)
