#!/usr/bin/python3

def element_at(my_list, idx):
    if idx <= -1:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
