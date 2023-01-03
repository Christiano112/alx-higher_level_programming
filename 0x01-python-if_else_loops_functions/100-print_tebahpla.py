#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    if 1 % 2 == 0:
        str = 0
    else:
        str = 32
    print("{}".format(chr(i - str)), end='')
