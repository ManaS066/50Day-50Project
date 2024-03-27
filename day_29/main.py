import sys
from tkinter import *
import random
import json

from PyInstaller.building.api import EXE, PYZ
from PyInstaller.building.build_main import Analysis

FONT_NAME = "Courier"
from tkinter import messagebox, simpledialog
import pyperclip
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
import os
import sys
# hiddenimports = ["C:/Users/MANAS/AppData/Local/Temp/_MEI143402/logo.png"]


# myscript.spec

# # -*- mode: python ; coding: utf-8 -*-
#
# block_cipher = None
#
# added_files = [
#     ('dist/logo.png', 'logo.png')  # Adjust the paths as necessary
# ]
#
# a = Analysis(['main.py'],
#              pathex=['D:\\study meterial\\codes\\100days or python\\day_29'],
#              binaries=[],
#              datas=added_files,
#              hiddenimports=[],
#              hookspath=[],
#              runtime_hooks=[],
#              excludes=[],
#              win_no_prefer_redirects=False,
#              win_private_assemblies=False,
#              cipher=block_cipher,
#              noarchive=False)
#
# pyz = PYZ(a.pure, a.zipped_data,
#           cipher=block_cipher)
# exe = EXE(pyz,
#           a.scripts,
#           [],
#           exclude_binaries=True,
#           name='main',
#           debug=False,
#           bootloader_ignore_signals=False,
#           strip=False,
#           upx=True,
#           console=True)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEI PASS2'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    password_list += [random.choice(symbols) for n in range(nr_symbols)]
    password_list += [random.choice(letters) for n in range(nr_letters)]
    password_list += [random.choice(numbers) for n in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)
    pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    insert = False
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if website == "" or email == "" or password == "":
        insert = False
    else:
        # messagebox.showinfo(title="conform your detail",message="are u want to continue")
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the detail for the website : "
                                               f"{website} with \n email/email  : {email} and password is {password}")
        if is_ok:
            try:
                with open(resource_path("data.json"), mode="r") as data:
                    # write data inside json file
                    # json.dump(new_data,data,indent=4)
                    # read data from json file
                    data1 = json.load(data)
                    # modify the data
                    data1.update(new_data)

                    with open(resource_path("dist/data.json"), mode="w") as data:
                        json.dump(data1, data, indent=4)

                        # data.write(f"{website} :\n")
                        # data.write(f"{email} :")
                        # data.write(f"{password}\n")
                        insert = True
            except:
                with open(resource_path("data.json"), "w") as data:
                    json.dump(new_data, data, indent=4)
                    insert = True

    if insert:

        conform_label = Label(text="Password saved successfully !!", font=(FONT_NAME, 12, "italic"), fg="green")
        conform_label.grid(column=1, row=5)

    else:
        conform_label = Label(text="Please fill all the box !! again", font=(FONT_NAME, 12, "italic"), fg="red")
        conform_label.grid(column=1, row=5)

    web_input.delete(0, END)
    # email_input.delete(0, END)
    password_input.delete(0, END)


# ------------------------------SEARCH _--------------------------------------#
def search():
    with open(resource_path("data.json"), "r") as data:
        data1 = json.load(data)
        website = web_input.get()
        try:
            search_data = data1[website]

        except:
            messagebox.showinfo(title="NOT found ", message="website data /ac not found")
        else:
            messagebox.showinfo(title="Searched Item",
                                message=f"Email:{search_data["email"]}\n Password :{search_data["password"]}")
            messagebox.askquestion(title="you want to continue", message="perss yes ", )


# ---------------------------- UI SETUP ------------------------------- #


# Check if the user entered a password

window = Tk()
window.config(pady=20, padx=20)
window.title("Password manager ")
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage("logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
web_label = Label(text="Website:    ", font=(FONT_NAME, 12, "bold"))
web_label.grid(column=0, row=2)

web_input = Entry(width=40)
web_input.xview_moveto(1.5)
web_input.focus()

web_input.grid(column=1, row=2, columnspan=2)

email_label = Label(text="Email/Username:    ", font=(FONT_NAME, 12, "bold"))
email_input = Entry(width=60)
email_label.grid(column=0, row=3)
# email_input.insert(0,"enter mail: ")
email_input.insert(END, "manasranjanpradhan2004@gmail.com")
email_input.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_input = Entry(width=50)

generate_password = Button(text="Generate", command=generate, width=10)
password_label.grid(column=0, row=4)
password_input.grid(column=1, row=4, columnspan=2)
generate_password.grid(column=2, row=4)

add_password = Button(text="Add", command=add_pass, width=55)
add_password.grid(column=1, row=6, columnspan=2)

add_search = Button(text="Search", command=search, width=9)
add_search.grid(column=2, row=2)
window.mainloop()
