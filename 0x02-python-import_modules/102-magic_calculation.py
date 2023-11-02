#!/usr/bin/python3

def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return __import__('magic_calculation_102').sub(a, b)
