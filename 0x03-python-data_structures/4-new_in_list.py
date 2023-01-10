#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)

    if idx < 0:
        return(my_list)

    if idx > len(my_list) - 1:
        return(my_list)

    for x in range(len(new_list)):
        if x == idx:
            new_list[x] = element

    return(new_list)
