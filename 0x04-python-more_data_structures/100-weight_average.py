#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    x = 0
    y = 0

    for my_tuple in my_list:
        x += my_tuple[0] * my_tuple[1]
        y += my_tuple[1]

    return (x / y)
