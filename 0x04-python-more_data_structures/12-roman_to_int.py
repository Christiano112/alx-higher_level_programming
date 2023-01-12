#!/usr/bin/python3
def to_subtract(l_num):
    to_s = 0
    max_list = max(l_num)

    for i in l_num:
        if max_list > i:
            to_s += i

    return (max_list - to_s)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l_keys = list(rom.keys())

    num = 0
    l_rom = 0
    l_num = [0]

    for x in roman_string:
        for r_rum in l_keys:
            if r_rum == x:
                if rom.get(x) <= l_rom:
                    num += to_subtract(l_num)
                    l_num = [rom.get(x)]
                else:
                    l_num.append(rom.get(x))

                l_rom = rom.get(x)

    num += to_subtract(l_num)

    return (num)
