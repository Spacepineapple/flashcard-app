from tkinter import *
import pandas as pd
from flashcard import Flashcard

BACKGROUND_COLOR = "#B1C8DD"
FRONT = "white"
BACK = "#d9e4e8"

window = Tk()
flashcard = Flashcard()

window.title("Flashcard Learning App")
window.config(height = 500, width = 500, bg=BACKGROUND_COLOR)

canvas = Canvas(height = 450, width = 800, bg=FRONT)
canvas.grid(column=0, row=0, columnspan=3, padx=50, pady=50)

language_label = Label()
canvas.create_text(400, 150, text=flashcard.language_1, font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=flashcard.label_word, font=("Arial", 60, "bold"))

def flip_card():
    if canvas["background"] == FRONT:
        canvas.delete("all")
        canvas.config(bg=BACK)
        canvas.create_text(400, 150, text=flashcard.language_2, font=("Ariel", 40, "italic"))
        label_word = flashcard.random_word[flashcard.language_2]
        canvas.create_text(400, 263, text=label_word, font=("Arial", 40, "bold"))
        if flashcard.reading != None:
            read_word = flashcard.random_word[flashcard.reading]
            canvas.create_text(400, 375, text=read_word, font=("Arial", 40, "italic"))
    else:
        canvas.delete("all")
        canvas.config(bg=FRONT)
        label_word = flashcard.random_word[flashcard.language_1]
        canvas.create_text(400, 150, text=flashcard.language_1, font=("Ariel", 40, "italic"))
        canvas.create_text(400, 263, text=flashcard.label_word, font=("Arial", 60, "bold"))


def new_word():
    canvas.delete("all")
    flashcard.get_word()
    canvas.create_text(400, 150, text=flashcard.language_1, font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=flashcard.label_word, font=("Arial", 60, "bold"))

def new_remove():
    flashcard.remove_word()
    new_word()

tick_image = PhotoImage(file="images\\right.png")
tick_button = Button(image=tick_image, highlightthickness=0, height=50, width=50, command=new_remove)
tick_button.grid(column=0, row=1)

cross_image = PhotoImage(file="images\wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, height=50, width=50, command=new_word)
cross_button.grid(column=1, row=1)

flip_image = PhotoImage(file="images\\flip.png")
flip_button = Button(image=flip_image, highlightthickness=0, height=50, width=50, command=flip_card)
flip_button.grid(column=2, row=1)

window.mainloop()

