from tkinter import *
from tkinter import messagebox
import random
import smtplib

FONT_NAME = "Courier"
my_email = "manasranjanpradhan2004@gmail.com"
code = "qkcf znzf biqp uvyl"
OTP = 0000


# -------------------------mail-----------------------#
def send():
    global OTP
    OTP = random.randint(1111, 9999)
    email = mail.get()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # sequre our connection
        connection.login(user=my_email, password=code)

        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject: !! OTP verification !!\n\n  Your OTP for the application is {OTP}")


def Varify():
    i_otp = int(otp_input.get())
    if i_otp == OTP:
        messagebox.showinfo(title="login sucessful", message="Welcome to demo program")
    else:
        messagebox.showinfo(title="login deny", message="verify your otp")


# ----------------------- UI----------------------------------------#
window = Tk()
window.config(padx=50, pady=20)
window.title("OTP SYSTEM")
canvas = Canvas(height=256, width=256)
logo_img = PhotoImage(file="pin (1).png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)
mail_label = Label(text="Enter Mail>", font=(FONT_NAME, 12, "bold"))
mail_label.grid(column=0, row=2)
mail = Entry(width=50)
mail.grid(column=1, row=2)
mail.insert(END, "mp382107@gmail.com")
otp_input = Entry(width=50)
otp_input.grid(column=1, row=4)
submit = Button(text="verify", command=Varify, width=10)
submit.grid(column=1, row=5)
button = Button(text="Submit", command=send)
button.grid(column=1, row=3)
window.mainloop()
