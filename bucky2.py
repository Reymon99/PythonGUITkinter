from tkinter import *

def printName(event):
    print("Hi my name is Bucky2!")

root=Tk()

button=Button(root,text="Print my name",bg="green")
button.bind("<Button-1>",printName)
button.pack(padx=5,pady=5)

root.mainloop()