import tkinter as tk
from PIL import Image, ImageTk
from utils import *

tries = 0
hangman_image_label = None


def create_buttons(letters_frame, word, trackLabel, resultLabel):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, letter in enumerate(letters):
        row = i // 6
        col = i % 6
        btn = tk.Button(letters_frame, image=letters_frame.button_image, compound='center', text=letter, font=('Verdana', 18))
        btn.grid(row=row, column=col)
        btn.config(command=lambda b=btn: button_state(b, word, trackLabel, resultLabel))
    return btn


def button_state(b, word, trackLabel, resultLabel):
    global tries, hangman_image_label
    b.config(state=tk.DISABLED)
    letter = button_clicked(b)

    if find_letter(letter, word):
        current_track = trackLabel['text']
        new_track = update_track(current_track, word, letter)
        trackLabel.config(text=new_track)
        resultLabel.config(text=f"Good guess! The word has '{letter}'.")
    else:
        if tries < 9:
            tries += 1
            if tries == 9:
                resultLabel.config(text=f"JUST ONE MORE TRY!")
            else:
                resultLabel.config(text=f"Nope. No '{letter}'. Try again.")
            update_hangman_image()
        else:
            tries += 1
            resultLabel.config(text=f"You ran out of tries! \nThe correct word was '{word}'.")
            update_hangman_image()

def create_frames(root, word):
    global tries, hangman_image_label
    # Image frame
    image_frame = tk.LabelFrame(root)
    image_frame.configure(bg="white", bd=0)
    image_frame.grid(row=0, column=0, padx=10, pady=20, sticky='nsew')
    root.rowconfigure(0, weight=1)

    tk_image = update_hangman_image()
    hangman_image_label = tk.Label(image_frame, image=tk_image, bg="white")
    hangman_image_label.image = tk_image
    hangman_image_label.grid(row=2, column=0, pady=10, padx=30)

    # Track frame
    track_frame = tk.LabelFrame(root)
    track_frame.configure(bg="white", bd=0)
    track_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
    root.rowconfigure(1, weight=0)

    trackLabel = tk.Label(track_frame, text=init_track(word), font=('Verdana', 18, 'bold', 'bold'), bg='white')
    trackLabel.grid(row=0, column=0, pady=10, padx=10)

    # Category frame
    category_frame = tk.LabelFrame(root)
    category_frame.configure(bg="white", bd=0)
    category_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

    categoryLabel = tk.Label(category_frame, text=f"Guess the {get_cat(word)}",
                             font=('Verdana', 18, 'bold', 'bold'), bg='white')
    categoryLabel.grid(row=0, column=0, padx=10, pady=10)

    # Result frame
    result_frame = tk.LabelFrame(root)
    result_frame.configure(bg="white", bd=0)
    result_frame.grid(row=3, rowspan=3, column=1, padx=10, pady=10, sticky='nsew')
    root.rowconfigure(2, weight=1)

    resultLabel = tk.Label(result_frame, text=f"", font=('Verdana', 18, 'bold', 'bold'), bg='white')
    resultLabel.grid(row=0, rowspan=3, column=0, padx=10, pady=10)

    # Letters frame
    letters_frame = tk.LabelFrame(root, bg="white", bd=0)
    letters_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
    letters_frame.button_image = tk.PhotoImage(file="./images/button_small.png")
    create_buttons(letters_frame, word, trackLabel, resultLabel)

    return root


def update_hangman_image():
    global hangman_image_label, tries
    image_path = f"images/hangman{tries}.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if hangman_image_label is not None:
        hangman_image_label.config(image=tk_image)
        hangman_image_label.image = tk_image

    return tk_image


def create_main_window(word):
    root = tk.Tk()
    root.geometry("875x580")
    root.title("Hangman Game")
    root.configure(bg="white")
    create_frames(root, word)
    return root
