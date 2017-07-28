from Tkinter import *
import ttk

class GalleryGui:
    def __init__(self, master):
        self.master = master
        
        self.mainFrame = ttk.Frame(self.master)
        self.mainFrame.grid()
        
        self.entryFrame = ttk.Frame(self.mainFrame)
        self.entryFrame.grid(row = 0, column = 0)
        
        self.buttonFrame = ttk.Frame(self.mainFrame)
        self.buttonFrame.grid(row = 1, column = 0, sticky = N+S+E+W)
        #image url
        self.l1 = ttk.Label(self.entryFrame, text = "Enter Image URL:")
        self.l1.grid(row = 0, column = 0)
        
        self.e1 = ttk.Entry(self.entryFrame)
        self.e1.grid(row = 0, column = 1)
        #caption
        self.l2 = ttk.Label(self.entryFrame, text = "Enter Caption:")
        self.l2.grid(row = 1, column = 0)
        
        self.e2 = ttk.Entry(self.entryFrame)
        self.e2.grid(row = 1, column = 1)
        #link--> destination
        self.l3 = ttk.Label(self.entryFrame, text = "Enter Destination Link:")
        self.l3.grid(row = 2, column = 0)
        
        self.e3 = ttk.Entry(self.entryFrame)
        self.e3.grid(row = 2, column = 1)
        
        self.genButton = ttk.Button(self.buttonFrame, text = "Generate Code!")
        self.genButton.grid(row = 0, column = 0, sticky = N+S+E+W)
        
        self.results = Text(self.buttonFrame, height = 4)
        self.results.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        
if __name__ == "__main__":
    root = Tk()
    gui = GalleryGui(root)
    root.mainloop()


def addGallery(imgSrc, caption, link):
    firstSection = '''<div style="float:left; padding:5px;"><a href="'''
    secondSection = '''"><img src="'''
    thirdSection = '''" alt="" width="225" height="300" class="alignnone size-medium wp-image-150" /><p>'''
    fourthSection = '''</p></a></div>'''
    
    shortCode = firstSection+link+secondSection+imgSrc+thirdSection+caption+fourthSection
    
    return shortCode
src = '''http://dostortugas.net/wp-content/uploads/2017/07/P1000624-225x300.jpeg'''
link = '''http://dostortugas.net/?page_id=47'''
caption = '''Views around Dos Tortugas'''
print addGallery(src, caption, link)