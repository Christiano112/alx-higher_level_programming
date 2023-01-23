#!/usr/bin/python3
def safe_print_integer(x):
    try:
        print("{:d}".format(x))
        return True
    except (ValueError, TypeError):
        return False
