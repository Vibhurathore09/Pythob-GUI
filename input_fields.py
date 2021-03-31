from tkinter import *
r = Tk()

e = Entry(r,width = 50)
e.pack()
e.insert(0,"Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    mylabel = Label(r, text=hello)
    mylabel.pack()


myButton = Button(r,text="click me!",padx=50,pady=50,command = myClick,fg = "#ffffff",bg ="#000000")
myButton.pack()
#state = DISABLED
##ffffff is a hexcolor code for white and #000000 us a hexcolour code for black

r.mainloop()