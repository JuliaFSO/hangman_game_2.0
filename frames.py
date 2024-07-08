import tkinter as tk
from PIL import Image, ImageTk
from utils import *

tries = 0
hangman_image_label = None
great_job_image_label = None
try_again_image_label = None
play_again_image_label = None
better_luck_image_label = None
result_label = None

def create_buttons(letters_frame, word, track_label, result_label):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, letter in enumerate(letters):
        row = i // 13
        col = i % 13
        btn = tk.Button(letters_frame, image=letters_frame.button_image, compound='center', text=letter,
                        font=('Comic Sans MS', 18))
        btn.grid(row=row, column=col)
        btn.config(command=lambda b=btn: button_state(b, word, track_label, result_label))
    return btn

def button_state(b, word, track_label, result_label):
    global tries, hangman_image_label
    b.config(state=tk.DISABLED)
    letter = button_clicked(b)

    if find_letter(letter, word):
        current_track = track_label['text']
        new_track = update_track(current_track, word, letter)
        track_label.config(text=new_track)
        if word == new_track.replace(' ', ''):
            result_label.config(text=f"")
            display_great_job(result_frame)
            display_play_again_button(result_frame, root, word)
        else:
            result_label.config(text=f"Yeah, '{letter}' is in.", font=('Comic Sans MS', 18, 'bold'))
    else:
        if tries < 9:
            tries += 1
            if tries == 9:
                result_label.config(text=f"ONE MORE TRY!", font=('Comic Sans MS', 18, 'bold'))
            else:
                result_label.config(text=f"Nope. No '{letter}'.", font=('Comic Sans MS', 18, 'bold'))
            update_hangman_image()
        else:
            tries += 1
            result_label.config(text=f"The word was '{word}'.", font=('Comic Sans MS', 18, 'bold'))
            update_hangman_image()
            display_better_luck(result_frame)
            display_play_again_button(result_frame, root, word)

def create_frames(root, word):
    global hangman_image_label, great_job_image_label, try_again_image_label, play_again_image_label, better_luck_image_label, category_label, result_frame

    # Category and Track frames
    category_track_frame = tk.Frame(root)
    category_track_frame.configure(bg="white", bd=0)
    category_track_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    category_frame = tk.LabelFrame(category_track_frame)
    category_frame.configure(bg="white", bd=0)
    category_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    category_label = tk.Label(category_frame, text=f"Guess the {get_cat(word)}",
                              font=('Comic Sans MS', 18, 'bold'), bg='white')
    category_label.grid(row=0, column=0, padx=10, pady=10)

    track_frame = tk.LabelFrame(category_track_frame)
    track_frame.configure(bg="white", bd=0)
    track_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    track_label = tk.Label(track_frame, text=init_track(word), font=('Comic Sans MS', 18, 'bold'), bg='white')
    track_label.grid(row=0, column=0, pady=10, padx=10)

    # Image frame
    image_frame = tk.LabelFrame(root)
    image_frame.configure(bg="white", bd=0)
    image_frame.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

    tk_image = update_hangman_image()
    hangman_image_label = tk.Label(image_frame, image=tk_image, bg="white")
    hangman_image_label.image = tk_image
    hangman_image_label.grid(row=0, column=0, pady=10, padx=30)

    # Result frame
    result_frame = tk.LabelFrame(root)
    result_frame.configure(bg="white", bd=0)
    result_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    result_label = tk.Label(result_frame, text="", font=('Comic Sans MS', 18, 'bold'), bg='white')
    result_label.grid(row=0, column=0, padx=10, pady=10)

    # Letters frame
    letters_frame = tk.LabelFrame(root, bg="white", bd=0)
    letters_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')
    letters_frame.button_image = tk.PhotoImage(file="./images/button_small.png")
    create_buttons(letters_frame, word, track_label, result_frame)

def update_hangman_image():
    global hangman_image_label, tries
    image_path = f"images/hangman{tries}.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if hangman_image_label is not None:
        hangman_image_label.config(image=tk_image)
        hangman_image_label.image = tk_image

    return tk_image

def display_great_job(result_frame):
    global great_job_image_label
    image_path = "./images/great_job_small.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if great_job_image_label is not None:
        great_job_image_label.grid_forget()

    great_job_image_label = tk.Label(result_frame, image=tk_image, bg="white")
    great_job_image_label.image = tk_image
    great_job_image_label.grid(row=0, column=0, pady=10, padx=30)

def display_better_luck(result_frame):
    global better_luck_image_label
    image_path = "./images/better_luck_small.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if better_luck_image_label is not None:
        better_luck_image_label.grid_forget()

    better_luck_image_label = tk.Label(result_frame, image=tk_image, bg="white")
    better_luck_image_label.image = tk_image
    better_luck_image_label.grid(row=0, column=0, pady=10, padx=30)

def display_play_again_button(result_frame, root, word):
    global play_again_image_label
    play_again = "./images/play_again_small.png"
    play_image = Image.open(play_again)
    tk_image = ImageTk.PhotoImage(play_image)

    if play_again_image_label is not None:
        play_again_image_label.grid_forget()

    play_again_image_label = tk.Button(result_frame, image=tk_image, bg="white", command=lambda: reset_game(root),
                                       bd=0, relief=tk.FLAT, highlightthickness=0)
    play_again_image_label.image = tk_image
    play_again_image_label.grid(row=1, column=0, pady=10, padx=30)

def create_main_window(word):
    global root
    root = tk.Tk()
    root.geometry("875x875")
    root.title("Hangman Game")
    root.configure(bg="white")
    create_frames(root, word)
    return root

def reset_game(root):
    global tries, hangman_image_label, great_job_image_label, try_again_image_label, play_again_image_label, \
        better_luck_image_label, category_label, result_frame,  result_label

    tries = 0
    hangman_image_label = None
    great_job_image_label = None
    try_again_image_label = None
    play_again_image_label = None
    better_luck_image_label = None
    category_label = None
    result_label = None

    for child in root.winfo_children():
        child.destroy()

    word = random_word()
    print(word)
    create_frames(root, word)
