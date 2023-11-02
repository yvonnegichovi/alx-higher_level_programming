#!/usr/bin/python3
import functools
print(functools.reduce(lambda a, b: a + b, [chr(c) for c in range(65, 91)]))
