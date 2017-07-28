'''
functions: a pythonic way of programming

functions are snippets of code that you can call with a command.

python has many built-in functions, just like the "LIST.append(ITEM)" and the

"PRINT" function
'''

#here is a simple function:

def printHello():
    print "hello!"
    
#   functions are started with the statement 'def'
#   after the name of the function there are parentheses
#   after that, there is a colon, and every line in the function
#   is indented

#this is how you call a function
printHello()

#here is a function with a parameter and a return value
#parameters are values that the function uses
#when you give a function a VARIABLE as a parameter,
#that VARIABLE is NOT changed, however, you can set
#that variable to the RETURN VALUE.

def addMe(x,y):
    return x*2+y
num = 5
print
addMe(num,6)

print num
