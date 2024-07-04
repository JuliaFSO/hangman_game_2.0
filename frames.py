import tkinter as tk
from PIL import Image, ImageTk
from utils import init_track, update_track


def create_buttons():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, letter in enumerate(letters):
        row = i // 6
        col = i % 6
        btn = tk.Button(letters_frame, image=button, compound='center', text=letter, font=('Verdana', 18))
        btn.grid(row=row, column=col)
        btn.config(command=lambda b=btn: button_state(b))
    return btn


def button_state(b):
    b.config(state=tk.DISABLED)


# Main window
root = tk.Tk()
root.geometry("875x500")
root.title("Hangman Game")
root.configure(bg="white")

# Image frame
image_frame = tk.LabelFrame(root)
image_frame.configure(bg="white", bd=0)
image_frame.grid(row=0, column=0, padx=10, pady=20, sticky='nsew')

image_path = "images/hangman_image2.png"
image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(image)

label = tk.Label(image_frame, image=tk_image, bg="white")
label.image = tk_image
label.grid(row=2, column=0, pady=10, padx=30)

# Letters frame
letters_frame = tk.LabelFrame(root)
letters_frame.configure(bg="white", bd=0)
letters_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

button = tk.PhotoImage(file="./images/button_small.png")

create_buttons()

# Category frame
category_frame = tk.LabelFrame(root)
category_frame.configure(bg="white", bd=0)
category_frame.grid(row=5, column=0, columnspan=2)

categoryLabel = tk.Label(category_frame, text="Guess the 'Instrument'", font=('Verdana', 18, 'bold', 'bold'), bg='white')
categoryLabel.grid(row=0, column=0)


# Track frame
track_frame = tk.LabelFrame(root)
track_frame.configure(bg="white", bd=0)
track_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

trackLabel = tk.Label(track_frame, text=init_track('guitar'), font=('Verdana', 18, 'bold', 'bold'), bg='white')
trackLabel.grid(row=0, column=0, pady=10, padx=10)

root.mainloop()
