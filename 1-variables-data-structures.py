# Basic data types
# ----------------

# integer
a = 1
print a

# decimal
pi = 3.14
print pi

# string
guy = 'Fred'
print guy

# You can concatenate these if you cast as strings
print guy + ' has ' + str(pi) + ' days to eat ' + str(a) + ' donut.'


# Data structures
# -----------------

# Lists (mutable)
car_list = ['Honda', 'Ford', 'Buick']
print car_list[0]
print car_list[0:2]
car_list.append('Kia')
car_list.remove('Honda')
print car_list

# Tuples (immutable)
cars_tuple = ('Honda', 'Ford', 'Buick')
print cars_tuple[2]

# Dictionaries
cars_dict = {'make': 'Honda', 'year': 2010, 'color': 'Silver'}
print cars_dict['year']
cars_dict['year'] = 2013
print cars_dict['year']