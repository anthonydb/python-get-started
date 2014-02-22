# STRING METHODS
# http://docs.python.org/2/library/stdtypes.html#string-methods


# slicing strings
#------------------------

phone = '703-555-1212'
print phone[0:3]
print phone[4:7]
print phone[8:]


# modifying strings
#-------------------------

a = 'Happy Birthday, Bob!'
print a

# how long is the string?
print len(a)

# lowercase the string
print a.lower()

# replace Bob with Sue
print a.replace('Bob', 'Sue')

# chain replacements
print a.replace('Bob', 'Sue').replace('!', '')

# split the string on spaces
print a.split()

# split a strong on commas
b = 'Bob,Sue,,Mary,Steve'
print b.split(',')
