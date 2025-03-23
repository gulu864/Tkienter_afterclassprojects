from tkinter import *

window = Tk()

window.title("Getting started with Widgets")
window.geometry('400x300')

label = Label(text = "In this application we are going to have 2 numbers and multiply it.", fg = 'white', bg = 'red')
lbl1 = Label(text = "Enter A number", fg = 'blue', bg = 'yellow')
lbl1text = Entry()
lbl2 = Label(text = "Enter a number", fg = 'blue', bg = 'yellow')
lbl2text = Entry()

def Multiply():
    num1 =int(lbl1text.get())
    num2 =int(lbl2text.get())

    global Message
    Message = num1 * num2

    text_box.insert(END, Message)

text_box = Text(height = 3)
btn = Button(text = "MULTIPLY!", command = Multiply, bg = 'green', fg = 'blue')

label.pack()
lbl1.pack()
lbl1text.pack()
lbl2.pack()
lbl2text.pack()
btn.pack()
text_box.pack()

window.mainloop()