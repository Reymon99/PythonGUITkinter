from tkinter import *

def leftClick(event):
    print("Left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("Right")

root=Tk()

frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)
frame.pack()

root.mainloop()