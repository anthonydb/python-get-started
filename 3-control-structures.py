#!/usr/bin/env python

"""
Getting Started with Python:
Control structures
"""

# if ... then ... else
vote = 'No'

if vote == 'Yes':
    print 'The vote is Yes'
elif vote == 'No':
    print 'The vote is No'
else:
    print 'It\'s some other vote'


# while
count = 10
while (count >= 0):
    print 'The count is: ' + str(count)
    count = count - 1
print 'Liftoff!'


# for loop
car_list = ['Honda', 'Ford', 'Buick']
for car in car_list:
    print car
