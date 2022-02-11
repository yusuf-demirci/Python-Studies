from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website:{
        "email": email,
        "password": password
        }
    }

    if not website or not email or not password:
        messagebox.showwarning(title="Warning", message="Please fill all information!")
    else:
        try:
            with open("Data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)           
                # updating old data with new data
                data.update(new_dict)
        except (FileNotFoundError, JSONDecodeError) as error:
                data = new_dict
        
        with open("Data.json", "w") as data_file:
            # saving updated to file
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("Data.json") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, JSONDecodeError) as error :
        data = {}

    if website in data:
        messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                   f"Password: {data[website]['password']}")
    else:
        messagebox.showinfo(title="Error", message=f"No details found for {website}.")

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(500, 400)
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=160, height=200)
canvas.create_image(105, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)
website_entry = Entry(width=26)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0,row=2)
email_entry = Entry(width=45)
email_entry.insert(0, "email@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()