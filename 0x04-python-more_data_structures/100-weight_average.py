#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = sum(map(lambda x: x[0] * x[1], my_list))
    total_weight = sum(map(lambda x: x[1], my_list))
    return weighted_sum / total_weight if total_weight != 0 else 0
