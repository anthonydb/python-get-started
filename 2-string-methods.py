#!/usr/bin/env python

"""
Getting Started with Python:
String Methods

https://docs.python.org/2/library/stdtypes.html#string-methods
https://docs.python.org/3/library/stdtypes.html#string-methods
"""

# modifying strings
# -----------------

a = 'Happy Birthday, Bob!'
print a

# how long is the string?
print len(a)

# lowercase the string
print a.lower()

# replace Bob with Sue
print a.replace('Bob', 'Sue')

# chain replacements
print a.replace('Sue', 'Bob').replace('!', '')

# split the string on spaces
print a.split()

# split a string on commas
b = 'Bob,Sue,,Mary,Steve'
print b.split(',')


# slicing strings
# ---------------

phone = '703-555-1212'
print phone[0:3]
print phone[4:7]
print phone[8:]
