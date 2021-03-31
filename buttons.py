from tkinter import *
r = Tk()
def myClick():
    mylabel = Label(r,text="Look! I clicked  a button!")
    mylabel.pack()
myButton = Button(r,text="click me!",padx=50,pady=50,command = myClick,fg = "#ffffff",bg ="#000000")
myButton.pack()
#state = DISABLED
##ffffff is a hexcolor code for white and #000000 us a hexcolour code for black

r.mainloop()