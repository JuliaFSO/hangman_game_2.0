from generate_csv import generate_csv
from utils import random_word, get_cat
from frames import create_main_window

def main():
    generate_csv()
    word = random_word()
    category = get_cat(word)
    print(word)
    print(category)
    root = create_main_window(word)
    root.mainloop()


main()
