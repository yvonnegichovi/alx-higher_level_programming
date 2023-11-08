#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_intergers = set(map(lambda x: x, my_list))
    result = sum(uniq_intergers)
    return result
