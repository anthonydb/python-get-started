# FILE Input/Output
# 'r' is reading, 'w' is writing (overwrites), 'a' is append


# open a file for writing
# creates a file with some text
with open('myfile.txt', 'a') as f:
    f.write('Hello there.\n')
    f.write('This is the second line.')


# open a file for reading; print all lines
with open('gettysburg.txt', 'r') as f:
    print f
    for line in f:
        print line


# open a file for reading; print first line
with open('gettysburg.txt', 'r') as f:
    line = f.readline()
    print line


# read a line and split it into a list
with open('gettysburg.txt', 'r') as f:
    line = f.readline().split()
    print line


# get all the words into a list
words_list = []
with open('gettysburg.txt', 'r') as f:
    for line in f:
        for x in line.split():
            words_list.append(x.lower())
    print words_list


# Bonus! Count word frequency.
# (Please, though, no word clouds ...)
from collections import Counter

words_list = []
#with open('gettysburg.txt', 'r') as f:
with open('SOTU_2013.txt', 'r') as f:
    for line in f:
        for x in line.split():
            if len(x) >= 4:
                words_list.append(x.lower().replace('.', '').replace(',', ''))
    # print Counter(words_list).most_common(20)
    counts = Counter(words_list).most_common()

with open('word-count.txt', 'w') as f:
    for pair in counts:
        out = pair[0] + ': ' + str(pair[1]) + '\n'
        f.write(out)
