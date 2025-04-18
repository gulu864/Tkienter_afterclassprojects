from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x400')
window.title('Password checker app')

tkl = Label(text = "Enter a password", bg = 'red', fg = 'blue')
tklentry = Entry()
symbols = "!@#$%^&*()"

def check():

    password = tklentry.get()
    score = 0

    if any(char.islower() for char in password):
        score = score + 2

    if any(char.isupper() for char in password):
        score = score + 2

    if any(char.isdigit() for char in password):
        score = score + 2
    
    if any(char in symbols for char in password):
        score = score + 2

    if len(password) > 8:
        score = score + 2

    text_box.insert(END, score)


text_box = Text(height = 5)
lbl = Label(text = "if score = 2 its a weak password,if score = 6 its a medium password,if score = 8 its a strong password")

btn = Button(text = "check", fg = 'black', bg = 'blue', command= check)

tkl.pack()
tklentry.pack()
lbl.pack()
btn.pack()
text_box.pack()

window.mainloop()