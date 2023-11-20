#!/usr/bin/python3

import sys
def safe_print_integer_err(value):
    try:
        print("{:d}\n".format(value))
        return True
    except Exception as e:
        print("Exception: {}\n".format(e), file=sys.stderr)
        return False
