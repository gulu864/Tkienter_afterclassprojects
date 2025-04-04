from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('400x400')

txt = Label(text = "Enter  number", fg = 'black', bg = 'blue')
txtlbl = Entry()
txt2 = Label(text = "Enter  number", fg = 'black', bg = 'blue')
txtlbl2 = Entry()

def Add():

    add1 = txtlbl.get()
    add2 = txtlbl2.get()
    global Message
    Message = add1, "+", add2, "=", int(add1) + int(add2)
    text_box.insert(END, Message)

def Sub():

    add1 = txtlbl.get()
    add2 = txtlbl2.get()
    global Message
    Message = add1, "-", add2, "=", int(add1) - int(add2)
    text_box.insert(END, Message)


def Mul():

    add1 = txtlbl.get()
    add2 = txtlbl2.get()
    global Message
    Message = add1, "x", add2, "=", int(add1) * int(add2)
    text_box.insert(END, Message)


def Div():

    add1 = txtlbl.get()
    add2 = txtlbl2.get()
    global Message
    Message = add1, "/", add2, "=", int(add1) / int(add2)
    text_box.insert(END, Message)




text_box = Text(height = 3)
btnadd = Button(text = '+', command = Add, height = 1,fg = 'red', bg = 'yellow', )
btnsub = Button(text = '-', command = Sub, height = 1,fg = 'red', bg = 'yellow', )
btnmul = Button(text = 'x', command = Mul, height = 1,fg = 'red', bg = 'yellow', )
btndiv = Button(text = '/', command = Div, height = 1,fg = 'red', bg = 'yellow', )

txt.pack()
txtlbl.pack()
txt2.pack()
txtlbl2.pack()
btnadd.pack()
btnsub.pack()
btnmul.pack()
btndiv.pack()
text_box.pack()

window.mainloop()