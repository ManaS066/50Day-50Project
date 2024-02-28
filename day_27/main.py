from tkinter import *

# creating window
window = Tk()

window.title("First Gui program")
window.minsize(width=500, height=500)
#adding padding
window.config(padx=200,pady=20)
# component
# label
my_label = Label(text="hi i am label", font=("Arial", 24, 'bold'))
my_label.pack(side="left")

# modify or assign of text area
# my_label['text']='NEW TEXT'
my_label.config(text="new text")
# my_label.pack(side="top")
my_label.grid(column=0 , row=0)


# Button
def button_clicked():
    a = input.get()
    my_label.config(text=a)
    my_label.grid(column=0 , row=0)


button = Button(text="click me ", command=button_clicked)  # command is used to listen the cmmand from the user .
button.grid(column=1 , row=1)
button = Button(text="click me ", command=button_clicked)  # command is used to listen the cmmand from the user .
button.grid(column=2 , row=0)
# entry component
input = Entry(width=40)
input.grid(column=3 , row=2)


# run the GUI
window.mainloop()
