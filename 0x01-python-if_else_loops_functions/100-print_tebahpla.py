#!/usr/bin/python3
chan = False
dif = ord('A') - ord('a')
for i in range(ord('z'), ord('a') - 1, -1):
    if chan:
        i += dif
    chan = not chan
    a = chr(i)
    print("{}".format(a), end='')
