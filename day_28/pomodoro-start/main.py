from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_tim=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_tim)
    canvas.itemconfig(time_text,text="00:00")
    Timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it is the 1/3/5/7 th rep
    if reps % 8 == 0:
        Timer_label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:

        Timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        countdown(work_sec)
        Timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    m = int(count / 60)
    s = int(count % 60)
    if s < 10:
        s = f"0{s}"
    canvas.itemconfig(time_text, text=f"{m}:{s}")
    if count > 0:
        global  my_tim
        my_tim=window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark=""
        for _ in range(int(reps/2)):
            mark+=" ?"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoor clock")

window.config(padx=50, pady=50, bg=YELLOW)

Timer_label = Label(text='Timer', font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
Timer_label.grid(column=1, row=0)


def button_clicked():
    pass


start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.config(padx=0, pady=0)
reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)
checkmark = Label(text="?", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)

time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
