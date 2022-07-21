#!/usr/bin/python3

# function that prints an integer
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return False

    return value
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Securi
