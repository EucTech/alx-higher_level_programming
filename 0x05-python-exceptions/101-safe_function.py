#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception as e:
        print("Execption: {}".format(e), file=sys.stderr)
        return None
