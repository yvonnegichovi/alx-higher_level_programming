#!/usr/bin/python3

"""This module has a class MyList that inherits from list"""


class MyList(list):
    """This class has a list"""
    def print_sorted(self):
        """This method prints the list but in ascending order"""
        sorted_list = sorted(self)
        filtered_list = [i for i in sorted_list if isinstance(i, int)]
        print(filtered_list)
