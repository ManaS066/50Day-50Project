THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score", fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(text="Some Question ")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()
