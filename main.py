from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    words_data = pd.read_csv('data/words_to_learn.csv')
    words_dict = words_data.to_dict(orient='records')
except FileNotFoundError:
    words_data = pd.read_csv('data/french_words.csv')
    words_dict = words_data.to_dict(orient='records')

card_words = {}

def flip_card():    
    canvas.itemconfig(language_text, fill='white', text='English')
    canvas.itemconfig(word_text, fill='white', text = card_words['English'])
    canvas.itemconfig(card_image, image = card_back_image)

def new_card_known():
    words_dict.remove(card_words)
    unknown_words_df = pd.DataFrame.from_dict(words_dict)
    unknown_words_df.to_csv('data/words_to_learn.csv', index=False)
    new_card()

def new_card():
    global card_words
    global timer
    window.after_cancel(timer)
    card_words = random.choice(words_dict)
    canvas.itemconfig(word_text, fill='black', text=card_words['French'])
    canvas.itemconfig(language_text,fill='black', text='French')
    canvas.itemconfig(card_image, image = card_front_image)
    timer = window.after(3000, flip_card)

window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image=PhotoImage(file='images\card_front.png')
card_back_image=PhotoImage(file='images\card_back.png')
card_image = canvas.create_image(400,263, image=card_front_image)
language_text = canvas.create_text(400,150, text='French', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400,263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image=PhotoImage(file='images/right.png')
right_button=Button(image=right_image, highlightthickness=0, command=new_card_known)
right_button.grid(column=1, row=1)

wrong_image=PhotoImage(file='images/wrong.png')
wrong_button=Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

timer = window.after(3000, flip_card)
new_card()

window.mainloop()