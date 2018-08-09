from tkinter import *

root=Tk()

frame=Frame(root)
frame.pack(padx=7,pady=7)

label_1=Label(frame,text="User")
label_2=Label(frame,text="Password")
entry_1=Entry(frame)
entry_2=Entry(frame)
c=Checkbutton(frame,text="Keep me logged in")

label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
c.grid(columnspan=2)

root.mainloop()
