#!/usr/bin/python3
"""This module finds the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Prototype for this sorting"""
    max = list_of_integers[0]
    if len(list_of_integers) is 0:
        return None
    else:
        for i in list_of_integers:
            if max < list_of_integers[i]:
                list_of_integers[i] = max
            return max
