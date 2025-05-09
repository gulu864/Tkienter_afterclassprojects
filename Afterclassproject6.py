from tkinter import *
import random

window = Tk()
window.title("Rock,Paper,Sciccors Machine")
window.geometry('400x400')
msg = Label(text = "rock,paper,scissors")
msgen = Entry()
choices = ["rock","paper","scissors"]
computer = ""
def Go():
    computer = random.choice(choices)
    player = msgen.get() 

    if player == "rock":
        if computer == "rock":
            msg.config(text = "tie")
        elif computer == "paper":
            msg.config(text = "computer won!")
        elif computer == "scissors":
            msg.config(text = "player won!")

    if player == "scissors":
        if computer == "scissors":
            msg.config(text = "tie")
        elif computer == "rock":
            msg.config(text = "computer won!")
        elif computer == "paper":
            msg.config(text = "player won!")

    if player == "paper":
        if computer == "paper":
            msg.config(text = "tie")
        elif computer == "scissors":
            msg.config(text = "computer won!")
        elif computer == "rock":
            msg.config(text = "player won!")

    text_box.insert(END, f"player chosen {player}")
    text_box.insert(END, f"\n computer chosen {computer}")

text_box = Text(height = 5)
btn = Button(text = "GO!", bg = "blue", fg = "red", command = Go)

msg.pack()
msgen.pack()
btn.pack()
text_box.pack()

window.mainloop()