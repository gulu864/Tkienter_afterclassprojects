from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Length Converter")
window.geometry('400x400')

lbl1 = Label(text = "Enter an inch", fg = 'black', bg = 'red')
lbl1text = Entry()

def convert():

    var1 = int(lbl1text.get())
    value = "Centimeter of " + str(var1) + "=" + str(var1/2)

    messagebox.showinfo("result", value)

btn = Button(text = "convert", fg = 'black', bg = 'red' ,command = convert)

lbl1.pack()
lbl1text.pack()
btn.pack()

window.mainloop()