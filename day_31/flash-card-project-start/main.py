from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Data manipulation
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# UI Setup
window = Tk()
window.title("Language Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(old_image, image=background_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(old_image, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data1 = pd.read_csv("data/words_to_learn.csv")
    data1.to_csv("data/words_to_learn.csv")
    next_card()


flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
background_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
old_image = canvas.create_image(400, 263, image=background_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 130, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 260, text="word", font=("Arial", 60, "bold"))

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
tick_img = PhotoImage(file="images/right.png")
known_button = Button(image=tick_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
