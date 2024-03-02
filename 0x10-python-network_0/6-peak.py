#!/usr/bin/python3
"""This module finds the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Prototype for this sorting"""
    if len(list_of_integers) is 0:
        return None
    else:
        max = list_of_integers[0]
        for i in list_of_integers:
            if max < list_of_integers[i]:
                list_of_integers[i] = max
            return max
