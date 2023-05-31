from tkinter import *
from password_manager import PasswordManager
from password_generator import PasswordGenerator
import os

# Environmental variable to pull in email address

DEFAULT_EMAIL = os.environ["EMAIL"]

# Pulling in modules for functionality

password_generator = PasswordGenerator()
password_manager = PasswordManager()

# Defining button functions


def generate_password():
    password_generator.generate_password(pass_input=pass_input,
                                         end=END)


def save_password():
    password_manager.save(website_input=website_input,
                          email_input=email_input,
                          pass_input=pass_input,
                          end=END)


def find_password():
    password_manager.find_password(website_input=website_input)

# UI Setup


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=50)
email_input.insert(0, DEFAULT_EMAIL)
email_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=32)
pass_input.grid(column=1, row=3)

# Generate password button and command function

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

# Save password button and command function

add_button = Button(text="Add",
                    width=43,
                    command= save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Search for password button and command function

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
