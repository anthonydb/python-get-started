# STRING METHODS
# http://docs.python.org/2/library/stdtypes.html#string-methods

# slicing strings
phone = '703-555-1212'
print phone[0:3]
print phone[4:7]
print phone[8:]

a = 'Happy Birthday, Bob!'
print a
print len(a)
print a.lower()
print a.replace('Bob', 'Sue')
print a.replace('Bob', 'Sue').replace('!', '')
print a.split()

b = 'Bob,Sue,,Mary,Steve'
print b.split(',')
