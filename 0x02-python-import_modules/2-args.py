#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args_list = argv[1:]
    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(args_list, start=1):
            print("{}: {}".format(i, arg))
