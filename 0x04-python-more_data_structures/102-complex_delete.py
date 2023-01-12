#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())

    for d_value in l_keys:
        if value == a_dictionary.get(d_value):
            del a_dictionary[d_value]

    return (a_dictionary)
