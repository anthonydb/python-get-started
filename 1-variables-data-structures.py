# Basic data types
# ----------------

# integer
a = 1
print a

# decimal
pi = 3.14159
print pi

# string
guy = 'Fred'
print guy

# Variables of different types can be
# concatenated if cast as strings
print guy + ' has ' + str(pi) + ' days to eat ' + str(a) + ' donut.'


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