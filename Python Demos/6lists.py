'''Listas... and string adding

Lists are a great data structure to contain multiple items

in many programming languages, lists can only contain one type, say integers
or strings, but in python, you can put anything you want into a list

cue the examples!!

'''
#made an empty list...
aList = [] # a list
#notice that the word 'list' is a word you can't use as a variable name
#notice also that I capitalized the second word in the variable name e.g.
# 'renayIsBeautiful'. this is called camel casing, and while it's not 
#a rule per se, it makes variable names easier to read, and is nice
#etiquette

anotherList = [0,1,2,3,4]

stringList = ['renay', 'is', 'beautiful']

'''
here is a time when for loops come in handy, because lists
are iterable.
'''

for i in anotherList:#range(0,5)
    print i
    

aString = ""

for s in stringList:
    aString += s
    #aString = aString + s
    aString += " "
print aString

"""adding and removing items... list operations"""

aList.append("adding")
aList.append("items")
aList = aList + ["is", "easy"]
print aList

aList.append(["as", "pie"])
print aList

print aList[4]