from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Window Title","Monkeys can live up 300 years.")

answer=tkinter.messagebox.askquestion("Question I","Do you like silly faces?")

if answer=='yes':
    print("8===D~")

root.mainloop()