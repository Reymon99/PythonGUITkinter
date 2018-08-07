from tkinter import *

def hola():
    print("Hi!")

f=Frame(cursor="mouse")
f.pack(padx=15,pady=15)

logoimg=PhotoImage(file="431280.png")

logo=Label(f,image=logoimg)
logo.pack(side=TOP,padx=10,pady=10)

titulo=Label(f,text="Agenda Telefónica",fg="blue",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

autor=Label(f,text="Sergio Majé")
autor.pack(side=TOP,padx=10,pady=10)

button1=Button(f,text="Listar elementos de la agenda",command=hola)
button1.pack(side=BOTTOM,padx=10,pady=10)

f.mainloop()