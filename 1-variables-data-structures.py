#!/usr/bin/env python

"""
Getting Started with Python:
Variables and Data Structures
"""

# Basic data types
# ----------------

# string
nation = 'Portugal'

# integer
year = 2012

# decimal
birth_rate = 1.28

# Variables of different types can be
# concatenated if cast as strings
sentence = nation + ' had a birth rate of ' + str(birth_rate) + \
    ' children per woman in ' + str(year) + '.'
print sentence


# Data structures
# -----------------


# Lists (are mutable)

# Create a list:
car_list = ['Honda', 'Ford', 'Buick']

# Retrieve the first item:
print car_list[0]

# Sort the list, then print
car_list.sort()
print car_list

# Retrieve the first two items (slicing)
print car_list[0:2]

# Add and remove items from the list
car_list.append('Kia')
car_list.remove('Honda')
print car_list


# Tuples (are immutable)

# Create a tuple
cars_tuple = ('Honda', 'Ford', 'Buick')

# Retrieve the third item (note zero index)
print cars_tuple[2]


# Dictionaries

# Create a dictionary
cars_dict = {'make': 'Honda', 'year': 2010, 'color': 'Silver'}

# Retrieve the value for the key 'year'
print cars_dict['year']

# Set a new value for the key 'year'
cars_dict['year'] = 2013
print cars_dict['year']
