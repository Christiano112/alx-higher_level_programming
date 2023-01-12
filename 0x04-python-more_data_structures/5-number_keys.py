#!/usr/bin/python3
def number_keys(a_dictionary):
    x = 0
    new_list = list(a_dictionary.keys())

    for i in new_list:
        x += i

    return (x)
