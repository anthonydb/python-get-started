#!/usr/bin/env python

"""
Getting Started with Python:
Functions
"""


# Add two numbers
def adder(a, b):
    result = a + b
    return result

result = adder(2, 1)
print result


# test string length
def max_string_length(string):
    if len(string) > 10:
        return True
    else:
        return False

a = 'baba ghanoush'

if max_string_length(a):
    print 'String is too long'
else:
    print 'String\'s OK'
