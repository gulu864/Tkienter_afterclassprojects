from tkinter import *
from datetime import date

window = Tk()

window.title("Age calculator app")
window.geometry('400x400')

label = Label(text = "Enter your Name:", fg = 'red', bg = 'blue')
lbl = Entry()
label4 = Label(text = "Enter your birthyear:", fg = 'red', bg = 'blue')
lbl4 = Entry()

def begin():

    name = lbl.get()
    by = lbl4.get()
    
    global Message
    Message = "Hello " + name + "!" + "Welcome to the application!"
    var1 = "\n I guess your age is ", (date.today().year - int(by))
    text_box.insert(END, Message)
    text_box.insert(END, var1)

text_box = Text(height = 3)
btn1 = Button(text = "Click me", fg = 'black', bg = 'red', command = begin)

label.pack()
lbl.pack()
label4.pack()
lbl4.pack()
btn1.pack()
text_box.pack()
window.mainloop()