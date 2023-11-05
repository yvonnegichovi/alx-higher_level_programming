#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for a in my_list:
        result.append(a % 2 == 0)
    return result
