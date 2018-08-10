from tkinter import *

def doNothing():
    print("ok ok I won't...")

root=Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...",command=doNothing)
subMenu.add_command(label="Now...",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=root.quit)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

#Toolbar

toolbar=Frame(root,bg="blue")

insertButt=Button(toolbar,text="Insert Image",command=doNothing)
insertButt.pack(side=LEFT,padx=2,pady=2)
printButt=Button(toolbar,text="Print",command=doNothing)
printButt.pack(side=LEFT,padx=1,pady=1)

toolbar.pack(side=TOP,fill=X)

#Statusbar

status=Label(root,text="Preparing to do nothing...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()