'''conditionals make branches in programs.
the first three programs in this folder were
linear; each line was evaluated, then executed.
with conditional statements, different lines can be executed
or skipped'''
#variable declaration
x = 5
print "if elif else"
if x < 5:
    print "not high enough!"
    print "go higher"
elif x == 5:
        print "wow!"
else:
    print "too high!"
    
#   notice!!!
#   each conditional statement ends in a ':'
#   the commands that are executed by each condition are indented
#   when you compare or check that something is equal, you use '=='
#   elif stands for else if, in other words, elif will only execute if
#   the if its conditions are met AND the previous conditions are false


''' 
conditional/logic expressions in python:

==      is equal
<       less than
>       greater than
!=      not equal
<=      less than or equal
>=       greater than or equal

and     and(notice that you need 'expression x' AND 'expression y')
or      or
not     not
is in   to check it an item is contained in another
'''