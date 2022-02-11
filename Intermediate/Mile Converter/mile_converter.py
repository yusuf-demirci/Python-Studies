from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string=0)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(padx=15, pady=5)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label2.config(padx=15, pady=5)

label3 = Label()
label3.config(text=0)
label3.grid(column=1, row=1)
label3.config(padx=15, pady=5)

label4 = Label()
label4.config(text="Km")
label4.grid(column=2, row=1)
label4.config(padx=15, pady=5)

def calculate():
    km = round(int(entry.get())*1.609344, 2)
    label3.config(text=km)

button = Button()
button.config(text="Calculate", command=calculate)
button.config(padx=15, pady=5)
button.grid(column=1, row=2)

window.mainloop()