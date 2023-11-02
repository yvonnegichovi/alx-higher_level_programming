#!/usr/bin/python3
start, end = ord('A'), ord('Z')
print(*[chr(x) for x in range(start, end + 1)], sep='', end='\n')
