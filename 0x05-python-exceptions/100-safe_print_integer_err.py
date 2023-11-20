#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        sys.stdout.write("{:d}\n".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
