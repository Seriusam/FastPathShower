from Tkinter import *
import os
import sys

root = Tk()
root.title("Fast File URL Shower")

l = Label(root, text=str(sys.argv[1:][0]))
l.pack()

root.mainloop()

