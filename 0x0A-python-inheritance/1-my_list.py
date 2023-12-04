#!/usr/bin/python3

"""This module has a class MyList that inherits from list"""


class MyList(list):
    """This class has a list"""
    def print_sorted(self):
        """This method prints the list but in ascending order"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
