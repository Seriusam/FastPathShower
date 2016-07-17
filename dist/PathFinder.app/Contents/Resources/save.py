from Tkinter import *
import os
import sys

root = Tk()
root.title("Fast File Path Shower")


l = Label(root,width=30, text="PATH: ")
l.pack()

T = Text(root, width=50, height=1, highlightbackground="grey")
if(len(sys.argv[1:]) > 0):
	T.insert(END, str(sys.argv[1:][0]))
else:
	T.insert(END, "D&Drop the file to the app icon")
T.pack()

root.mainloop()

