#!/usr/bin/python3

def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}\n".format(value))
        return True
    except Exception as e:
        print("Exception: {}\n".format(e), file=sys.stderr)
        return False
