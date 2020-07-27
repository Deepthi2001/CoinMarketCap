from tkinter import *
import requests # helps us to get the data
import json # helps us to pass the data

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")

name = Label(pycrypto, text="Bitcoin", bg="black", fg="white", font=("Arial Bold", 10))
bt = Button(pycrypto, text="enter", bg="orange", fg="red")
name.grid(row=0, column=0)
bt.grid(row=0, column=1)
'''txt = Entry(pycrypto, width=10)
txt.grid(column=1, row=0)'''
'''def clicked():
    res = "welcome to " + txt.get()
    l1.configure(text=res)
bt = Button(pycrypto, text="enter",command=clicked)'''


pycrypto.mainloop()