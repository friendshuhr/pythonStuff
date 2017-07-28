'''woot woot miscellany!'''

'''part 1: getting user input! yayyy about time...'''

#to prompt specifically and INTEGER or DOUBLE(decimal number, float):

num = input("Enter a number: ")

#to prompt a non-specified type which will be PROCESSED AS A STRING:

rawInput = raw_input("Enter anything! yay: ")

print "the number you entered is: "+str(num)
print "the string you entered is: "+rawInput




'''part 2: funny string tricks'''

#escape characters...

#this is cool!!! "\n" creates a line break in a string ex below:

print "up\ndown"


'''importing modules'''

#have you ever wanted to calculate something with a square root?
#have you ever wanted to get a psuedo-random number?

#importing a module can make that easier!

#most modules are part of what's called the 'standard python library,'
#which means that you don't need to install anything new on your
#computer to use them.

#here's how it's done:

import math
#math is a standard python module that contains math functions
#it's not imported automatically with every file because it's not always
#needed.

#with math you can do this:
x = input("Enter a number: ")
print "Its square root is: "+str(math.sqrt(x))
