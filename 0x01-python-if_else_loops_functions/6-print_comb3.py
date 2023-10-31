#!/usr/bin/python3

for first_digit in range(10):
    for last_digit in range(first_digit + 1, 10):
        if first_digit != last_digit:
            if first_digit != 0 or last_digit != 1:
                print(", ", end='')
            print("{:d}{:d}".format(first_digit, last_digit), end='')
print()
