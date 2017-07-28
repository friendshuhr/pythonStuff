'''
reading a writing files!

this section is a basic introduction to reading and writing
text files(.txt)

the syntax for reading a file is as follows:

'''

#the file I have included in this directory is a copy-paste from a wikipedia article
#about the carribean 2005 football championship

fileName = "example.txt"
mode = "r"#r = read, w = write(with overwrite), a = append

with open(fileName, mode) as infile:
    text = infile.read()
    
print text

#writing a file:

s = raw_input("Enter the name of the file you want to create: ")
t = raw_input("Enter some text that you want to put in the file: ")

with open(s, "w") as w:
    w.write(t)