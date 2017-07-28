'''
dictionaries are another data structure.

a dictionary is like a list, except that it 
is made of key:value pairs
'''

aDict = {"firstKey":1}

#you can add an item or overwrite an existing item
#like this:

aDict["newItem"] = 3

print aDict

#note: dictionaries are NOT ordered! this is because their
#guts are different than lists. this makes them faster
#to search and iterate through.

aListDictionary = [["renay", "the land that is all things wonderful"], ["ben", "a boy in love"]]

print aListDictionary