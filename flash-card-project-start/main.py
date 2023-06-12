from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}

# ================ data csv ================================
try:
    data = pandas.read_csv(
        "D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/data/words_to_learn.csv")
except:
    original = pandas.read_csv(
        "D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/data/french_words.csv")
    learn = original.to_dict(orient="record")

else:
    learn = data.to_dict(orient="record")


def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(learn)

    canvas_front.itemconfig(image_bg, image=card_front)
    canvas_front.itemconfig(language, text="French", fill="black")
    canvas_front.itemconfig(word, text=current_card['French'], fill="black")
    flip = window.after(3000, func=back_card)


def back_card():
    canvas_front.itemconfig(image_bg, image=card_back)
    canvas_front.itemconfig(language, text="English", fill="white")
    canvas_front.itemconfig(word, text=current_card['English'], fill="white")


def words_to_learn():
    learn.remove(current_card)
    pandas.DataFrame(learn).to_csv("D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/data/words_to_learn.csv", index=False)

    next_card()

# ============================= front =======================================
window = Tk()
window.title("Flashy")
window.config(padx=120, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, func=back_card)

# ============ get images' path============
image_wrong = PhotoImage(
    file="D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/images/wrong.png")
image_right = PhotoImage(
    file="D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/images/right.png")
card_back = PhotoImage(
    file="D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/images/card_back.png")
card_front = PhotoImage(
    file="D:/Mine/Programming/Python/CourseUdemy/projects/flash-card-project-start/images/card_front.png")

canvas_front = Canvas(width=800, height=556, bg=BACKGROUND_COLOR, highlightthickness=0)
image_bg = canvas_front.create_image(400, 280, image=card_front)
language = canvas_front.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas_front.create_text(400, 263, text=f"", font=("Ariel", 60, "bold"))
canvas_front.grid(columnspan=2, row=1)

wrong_button = Button(image=image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2)

right_button = Button(image=image_right, highlightthickness=0, command=words_to_learn)
right_button.grid(column=1, row=2)
next_card()

window.mainloop()
