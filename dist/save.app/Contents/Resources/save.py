from Tkinter import *
import os
import sys

root = Tk()
root.title("Fast File Path Shower")


l = Label(root, text="PATH: "+str(sys.argv[1:][0]))
l.pack()

root.mainloop()

