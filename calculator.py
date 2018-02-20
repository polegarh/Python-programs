#calculator
'''
want a calculator to be a wisget
give it a parent and pack it (or grid it)
inherit from Frame all the time - like a window
but doesnt have to be top level, can be packed/gridded

'''
from math import *
from tkinter import *

class Calculator(Frame):
    #have to accept a parent argument
    def __init__(self,parent=None):
        #first always calla a frame constructor
        Frame.__init__(self,parent=None)
        # constructor will layout all its subwidgets
        self.entry = Entry(self)
        self.entry.grid(row=0,column=0,columnspan=4)
        btns = "0123456789+-/*().%=C"
        for i in range(len(btns)):
            def cmd(key=btns[i]):
                self.click(key)
            b = Button(self,text=btns[i],width=3, command=cmd)
            b.grid(row=i//4+1,column=i%4)
    def click(self,key):
        if key == 'C':
            self.entry.delete(0,END)
        elif key == '=':
            try:
                answer = eval(self.entry.get())
            except:
                ans = 'ERROR'
            self.entry.delete(0,END)
            self.entry.insert(END,answer)
        else: #just write the key into the entry
            self.entry.insert(END,key)


# create a widget and make it visible
Calculator().pack()
