#!/usr/bin/pyhton3
import random
number = random.randint(-10000, 10000)
# num = int(repr(number)[-1])
if number >= 0:
    num = number % 10
else:
    num = number % -10
if num > 5:
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
if num == 0:
    print(f"Last digit of {number:d} is {num:d} and is 0")
if num < 6 and num != 0:
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
