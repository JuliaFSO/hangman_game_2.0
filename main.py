from generate_csv import generate_csv
from utils import random_word
from frames import create_main_window

def main():
    generate_csv()
    word = random_word()
    print(word)
    root = create_main_window(word)
    root.mainloop()


main()
