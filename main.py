from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

words_data = pd.read_csv('data/french_words.csv')
words_dict = words_data.to_dict(orient='records')

def known_word():
    new_word = random.choice(words_data['French'])
    canvas.itemconfig(word_text, text=new_word)
    canvas.itemconfig(language_text, text='French')

def unknown_word():
    new_word = random.choice(words_data['French'])
    canvas.itemconfig(word_text, text=new_word)
    canvas.itemconfig(language_text, text='French')

window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image=PhotoImage(file='images\card_front.png')
canvas.create_image(400,263, image=card_image)
language_text = canvas.create_text(400,150, text='French', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400,263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image=PhotoImage(file='images/right.png')
right_button=Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

wrong_image=PhotoImage(file='images/wrong.png')
wrong_button=Button(image=wrong_image, highlightthickness=0, command=unknown_word)
wrong_button.grid(column=0, row=1)


#words_dict = {row['French']:row['English'] for (index,row) in words_data.iterrows()}


window.mainloop()