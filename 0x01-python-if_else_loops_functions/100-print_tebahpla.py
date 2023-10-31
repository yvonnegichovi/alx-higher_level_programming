#!/usr/bin/python3

output = ""

for char_code in range(ord('z'), ord('a') - 1, -1):
    if char_code % 2 == 0:
        output += "{}".format(chr(char_code))
    else:
        output += "{}".format(chr(char_code).upper())
print("{}".format(output), end='')
