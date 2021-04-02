from tkinter import*
root = Tk()
root.title("Simple Calculator")

e = Entry(root,width = 70, borderwidth = 5)
e.grid(row = 0 , column = 0, columnspan = 5 ,padx = 20 , pady = 13)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "additon"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
 
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



button_1 = Button(root, text = "1",padx=50,pady = 20,command =lambda : (button_click(1))).grid(row = 3 ,column = 0)

button_2 = Button(root, text = "2",padx=50,pady = 20,command =lambda : (button_click(2))).grid(row = 3 ,column = 1)

button_3 = Button(root, text = "3",padx=50,pady = 20,command =lambda : (button_click(3))).grid(row = 3 ,column = 2)

button_4 = Button(root, text = "4",padx=50,pady = 20,command =lambda : (button_click(4))).grid(row = 2 ,column = 0)

button_5 = Button(root, text = "5",padx=50,pady = 20,command =lambda : (button_click(5))).grid(row = 2 ,column = 1)

button_6 = Button(root, text = "6",padx=50,pady = 20,command =lambda : (button_click(6))).grid(row = 2 ,column = 2)

button_7 = Button(root, text = "7",padx=50,pady = 20,command =lambda : (button_click(7))).grid(row = 1 ,column = 0)

button_8 = Button(root, text = "8",padx=50,pady = 20,command =lambda : (button_click(8))).grid(row = 1 ,column = 1)

button_9 = Button(root, text = "9",padx=50,pady = 20,command =lambda : (button_click(9))).grid(row = 1 ,column = 2)

button_0 = Button(root, text = "0",padx=50,pady = 20,command =lambda : (button_click(0))).grid(row = 4 ,column = 1)

button_add=Button(root, text = "+",padx=50,pady = 20,command =button_add).grid(row = 3 ,column = 4)

button_subtract = Button(root, text = "-",padx=50,pady = 20,command =button_subtract).grid(row = 2 ,column = 4)

button_multiply = Button(root, text = "*",padx=50,pady = 20,command =button_multiply).grid(row = 1 ,column = 4)

button_clear = Button(root, text = "CLEAR",padx=37,pady = 20,command = button_clear).grid(row = 4 ,column = 4)

button_divide = Button(root, text = "/",padx=51,pady = 20,command =button_divide).grid(row = 4 ,column = 0)

button_equal = Button(root, text = "=",padx=49,pady = 20,command =button_equal).grid(row = 4 ,column = 2)


root.mainloop()
