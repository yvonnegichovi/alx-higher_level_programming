#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    def value_by_two(value):
        return value * 2
    new_value = list(map(value_by_two, a_dictionay))
    print("
