#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
print(find_peak([1, 2, 3, 4, 5]))
print(find_peak([5, 4, 3, 2, 1]))
print(find_peak([1, 4, 6, 2, 1]))
print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))
