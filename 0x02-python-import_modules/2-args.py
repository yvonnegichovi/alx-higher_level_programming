#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    if num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
