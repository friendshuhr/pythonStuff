'''this is a gui, which simply means a non-console application

GRAPHICAL USER INTERFACE

one new thing that I use here is a CLASS

a class is an OBJECT, and a GUI is a perfect use for a class

OBJECTS have ATTRIBUTES and METHODS, just like in real life...

TREES, in the general sense are GREEN and BROWN
a TREE method could be tree.loseLeaves()

all of these ATTRIBUTES and METHODS are contained in a CLASS

in python, a class' ATTRIBUTES are called INSTANCE VARIABLES

they are defined in method called '__init__'

each METHOD is a function with a parameter called "self", which
denotes that it is a CLASS METHOD.

'''

from Tkinter import *
import ttk

class gooey:
    def __init__(self, master):
        self.master = master
        master.title("basic gui")
        
        self.mainFrame = ttk.Frame(self.master)
        self.mainFrame.grid()
        
        self.hW = ttk.Label(self.mainFrame, text = "hello, world!")
        self.hW.grid()
        
if __name__ == "__main__":
    root = Tk()
    gui = gooey(root)
    root.mainloop()