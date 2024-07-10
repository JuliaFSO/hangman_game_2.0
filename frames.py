import tkinter as tk
from PIL import Image, ImageTk
from utils import *

tries = 0
hangman_image_label = None
great_job_image_label = None
play_again_image_label = None
better_luck_image_label = None
result_label = None

def create_buttons(letters_frame, word, track_label, result_frame, category_label, category_frame):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    buttons = []
    for i, letter in enumerate(letters):
        row = i // 6
        col = i % 6
        btn = tk.Button(letters_frame, image=letters_frame.button_image, compound='center', text=letter,
                        font=('Verdana', 18))
        btn.grid(row=row, column=col, sticky='nsew')
        btn.config(command=lambda b=btn: button_state(b, word, track_label, result_frame, category_label, letters_frame,
                                                      category_frame))
        buttons.append(btn)
    letters_frame.buttons = buttons


def disable_buttons(letters_frame):
    for btn in letters_frame.buttons:
        btn.config(state=tk.DISABLED)


def button_state(b, word, track_label, result_frame, category_label, letters_frame, track_frame):
    global tries, hangman_image_label, result_label
    b.config(state=tk.DISABLED)
    letter = button_clicked(b)

    if find_letter(letter, word):
        current_track = track_label['text']
        new_track = update_track(current_track, word, letter)
        track_label.config(text=new_track)
        if word == new_track.replace(' ', ''):
            category_label.config(text=f"The word is:", font=('Verdana', 25, 'bold'), padx=30)
            formatted_word = format_word(word)
            track_label.config(text=formatted_word, font=('Verdana', 25, 'bold'), fg='#9E4250', padx=30)
            display_great_job(result_frame)
            display_play_again_button(track_frame, root, word)
            disable_buttons(letters_frame)
        else:
            result_label.config(text=f"Yeah, '{letter}' is in.", font=('Verdana', 30, 'bold'), fg='#498563', padx=50, pady=50)
    else:
        if tries < 9:
            tries += 1
            if tries == 9:
                result_label.config(text=f"\nONE MORE TRY!\n", font=('Verdana', 30, 'bold'), fg='#9E4250', padx=50, pady=50)
            else:
                result_label.config(text=f"Nope. No '{letter}'.", font=('Verdana', 30, 'bold'), fg='#9E4250', padx=50, pady=50)
            update_hangman_image()
        else:
            tries += 1
            category_label.config(text=f"The word was:", font=('Verdana', 25, 'bold'), padx=30)
            formatted_word = format_word(word)
            track_label.config(text=formatted_word, font=('Verdana', 25, 'bold'), fg='#9E4250', padx=30)
            update_hangman_image()
            display_better_luck(result_frame)
            display_play_again_button(track_frame, root, word)
            disable_buttons(letters_frame)


def create_frames(root, word):
    global hangman_image_label, great_job_image_label, play_again_image_label, better_luck_image_label, \
        result_frame, result_label

    # Logo frame
    logo_frame = tk.Frame(root, bg="#FFDDC1", bd=2)
    logo_frame.grid(row=0, column=0, padx=15, columnspan=2, sticky='nsew')

    logo_image = Image.open("./images/hangman_logo.png")
    logo_tk_image = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(logo_frame, image=logo_tk_image, bg="#FFDDC1")
    logo_label.image = logo_tk_image
    logo_label.grid(row=0, column=0)

    # Category and Track frames
    category_track_frame = tk.Frame(root)
    category_track_frame.configure(bg="#FFDDC1")
    category_track_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky='nsew')

    category_frame = tk.LabelFrame(category_track_frame)
    category_frame.configure(bg="#FFDDC1", bd=0)
    category_frame.grid(row=0, column=0, padx=20, pady=10, sticky='nsew')

    category_label = tk.Label(category_frame, text=f"Guess the {get_cat(word)}",
                              font=('Verdana', 25, 'bold'), fg='#34A0A4', bg='#FFDDC1', padx=30)
    category_label.grid(row=0, column=0)

    track_frame = tk.LabelFrame(category_track_frame)
    track_frame.configure(bg="#FFDDC1", bd=0)
    track_frame.grid(row=1, column=0, sticky='nsew', ipadx=80)

    track_label = tk.Label(track_frame, text=init_track(word), font=('Verdana', 25, 'bold'), bg='#FFDDC1', padx=30)
    track_label.grid(row=0, column=0, padx=20, pady=10)

    # Image frame
    image_frame = tk.LabelFrame(root)
    image_frame.configure(bg="#FFDDC1", bd=0)
    image_frame.grid(row=2, column=0, sticky='nsew')

    tk_image = update_hangman_image()
    hangman_image_label = tk.Label(image_frame, image=tk_image, bg="#FFDDC1")
    hangman_image_label.image = tk_image
    hangman_image_label.grid(row=0, column=0, pady=10, padx=30)

    # Result frame
    result_frame = tk.LabelFrame(root)
    result_frame.configure(bg="#FFDDC1", bd=0)
    result_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    result_label = tk.Label(result_frame, text="", font=('Verdana', 18, 'bold'), bg='#FFDDC1')
    result_label.grid(row=0, column=0)

    # Letters frame
    letters_frame = tk.LabelFrame(root, bg="#FFDDC1", bd=0)
    letters_frame.grid(row=0, column=1, padx=40, pady=40, sticky='nsew')
    letters_frame.button_image = tk.PhotoImage(file="./images/button_small.png")
    create_buttons(letters_frame, word, track_label, result_label, category_label, category_track_frame)


def update_hangman_image():
    global hangman_image_label, tries
    image_path = f"images/hangman{tries}_bg.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if hangman_image_label is not None:
        hangman_image_label.config(image=tk_image)
        hangman_image_label.image = tk_image

    return tk_image


def display_great_job(result_frame):
    global great_job_image_label
    image_path = "./images/great_job.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if great_job_image_label is not None:
        great_job_image_label.grid_forget()

    great_job_image_label = tk.Label(result_frame, image=tk_image, bg="#FFDDC1")
    great_job_image_label.image = tk_image
    great_job_image_label.grid(row=0, column=0)


def display_better_luck(result_frame):
    global better_luck_image_label
    image_path = "./images/better_luck.png"
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)

    if better_luck_image_label is not None:
        better_luck_image_label.grid_forget()

    better_luck_image_label = tk.Label(result_frame, image=tk_image, bg="#FFDDC1")
    better_luck_image_label.image = tk_image
    better_luck_image_label.grid(row=0, column=0)


def display_play_again_button(track_frame, root, word):
    global play_again_image_label
    play_again = "./images/play_again_small.png"
    play_image = Image.open(play_again)
    tk_image = ImageTk.PhotoImage(play_image)

    if play_again_image_label is not None:
        play_again_image_label.grid_forget()

    play_again_image_label = tk.Button(track_frame, image=tk_image, bg="#FFDDC1", command=lambda: reset_game(root),
                                       bd=0, relief=tk.FLAT, highlightthickness=0)
    play_again_image_label.image = tk_image
    play_again_image_label.grid(row=1, column=1, stick="e")


def create_main_window(word):
    global root
    root = tk.Tk()
    root.geometry("875x875")
    root.title("Hangman Game")
    root.configure(bg="#FFDDC1")
    root.resizable(False, False)
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
