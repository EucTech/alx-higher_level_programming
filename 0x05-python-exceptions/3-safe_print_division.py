#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = int(a)
        b = int(b)
        result = a / b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result), end="")
        print()
    return result
