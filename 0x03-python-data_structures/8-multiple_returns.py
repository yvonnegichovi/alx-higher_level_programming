#!/usr/bin/python3

def multiple_returns(sentence):
    result = ""
    if len(sentence) == 0:
        return (0, None)
    result = len(sentence), sentence[0]
    return result
