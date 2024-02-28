from tkinter import *

window = Tk()
window.title("Unit converter")
window.minsize(300, 200)
window.config(padx=200, pady=200)


# button

def button_clicked():
    celcius = float(cel.get())
    far = (celcius * 9 / 5) + 32
    res = Label(text=f"{far}", font=("Arial", 20))
    res.grid(column=2, row=4)


# createing labe
my_label = Label(text="enter temperature in celcious", font=("Arial", 20))
my_label.grid(column=1, row=1)

far_label = Label(text="temp in farhenite:", font=("Arial", 20))
far_label.grid(column=3,row=1)
cel = Entry(width=40)

cel.grid(column=2,row=2)
button = Button(text="Convert", command=button_clicked)  # command is used to listen the cmmand from the user .
button.grid(column=2, row=5)

window.mainloop()
