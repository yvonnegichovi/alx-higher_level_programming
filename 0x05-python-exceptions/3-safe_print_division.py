#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        if 'result' not in locals():
            result = None
        print("Inside result: {}".format(result))
        return result
