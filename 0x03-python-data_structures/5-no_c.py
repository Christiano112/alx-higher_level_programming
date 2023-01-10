#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in len(my_string):
        if x != 'c' and x != "C":
            new_string = new_string + my_string[x]

    return (new_string)
