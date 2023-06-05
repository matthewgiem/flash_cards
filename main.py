from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Import data as a PD dataframe
data = pd.read_csv("data/french_words.csv")
list_of_words = data.to_dict(orient="records")

# Logic
def change_word():
    current_card = random.choice(list_of_words)
    canvas.itemconfig(card_word, text=current_card["French"])

# Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
front_flash_card_image = PhotoImage(file="images/card_front.png")
back_flash_card_image = PhotoImage(file="images/card_back.png")
correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
canvas.create_image(400, 263, image=front_flash_card_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60 ,"bold"))

# Buttons
unknown_button = Button(image=wrong)
unknown_button.grid(row=1, column=0)
unknown_button.config(highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)

correct_button = Button(image=correct)
correct_button.grid(row=1, column=1)
correct_button.config(highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)


print(list_of_words)
window.mainloop()