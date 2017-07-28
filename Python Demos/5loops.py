'''LOOPPPPPSSSies!

in python there are 2 kinds of loops(3, but the third
isn't really looping, it's called recursion, more on that later)

there are while loops and for loops

while loops are like conditionals. they are executed while a condition is met'''

print "while"
x = 0
while x < 5:
    print x
    x = x + 1
    
''' for loops iterate through a range. they can iterate through a range of numbers
or a range of items in a list. Anything that python deems "iterable" can be used for
a for loop. We'll  start with numbers.'''

print "for"
for i in range(6):
    print i