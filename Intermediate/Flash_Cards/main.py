from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
new_card = ""

def words_to_learn():
    unknown_words = pandas.DataFrame(to_learn)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)

def next_card_cross():
    global timer, new_card
    window.after_cancel(timer)
    new_card = random.choice(to_learn)
    words_to_learn()

    canvas.itemconfig(bg_image, image=cardfront_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_card["French"], fill="black")

    timer = window.after(3000, card_back, new_card)
    
def next_card_check():
    global new_card
    to_learn.remove(new_card)
    next_card_cross()

def card_back(card):
    canvas.itemconfig(bg_image, image=cardback_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")

# --------------------------------------------------

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, IndexError) as error:
    data = pandas.read_csv("data/french_words.csv")
   
to_learn = data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, card_back)

cardfront_image = PhotoImage(file="images/card_front.png")
cardback_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
bg_image = canvas.create_image(410, 270, image=cardfront_image)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card_check)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness=0, command=next_card_cross)
wrong_button.grid(column=0, row=1)

next_card_cross()

window.mainloop()


