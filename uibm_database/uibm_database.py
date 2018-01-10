#!/usr/bin/python3
# coding=latin-1

import sys
import sqlite3
import os
import tkinter

def main():
 
    print("hello world")

    a = app()
    a.run4()


class app:

    def __init__(self):
        self.data=[]    

    def run(self):

        root = tkinter.Tk()
        w = tkinter.Label(root, text="hello world")
        w.pack()
        root.mainloop()
	
    def run2(self):
        root = tkinter.Tk()
        msgstr = "hello world"
        msg = tkinter.Message(root, text=msgstr)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        root.mainloop()


    def run3(self):
        root = tkinter.Tk()
        frame = tkinter.Frame(root)
        frame.pack()
        button = tkinter.Button(frame, text="Quit", fg="red",command=quit)
        button.pack(side=tkinter.LEFT)
        slogan = tkinter.Button(frame, text="Hello", command=self.write_slogan)
        slogan.pack(side=tkinter.LEFT)
        root.mainloop()

    def run4(self):
        root = tkinter.Tk()
        tkinter.Label(root, text="name").grid(row=0)
        tkinter.Label(root, text="amount").grid(row=1)

        e1 = tkinter.Entry(root)
        e2 = tkinter.Entry(root)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        root.mainloop()

    def write_slogan(self):
        print("Tkinter is about to be used")

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    main()
