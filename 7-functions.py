# Functions


# Add two numbers   
def adder(a, b):
    result = a + b
    return result

print adder(2,1)


# test string length
def max_string_length(string):
    if len(string) > 10:
        return True
    else:
        return False

a = 'baba ghanoush'

if max_string_length(a) == True:
    print 'String is too long'
else:
    print 'OK'



