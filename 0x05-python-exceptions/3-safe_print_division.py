#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, TypeError, FloatingPointError):
        div = None
    finally:
        print("Inside results: {}".format(div))
    return div
