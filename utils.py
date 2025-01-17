import random
import csv


def random_word():
    words_list = []
    with open('hangman_words.csv', 'r') as words_file:
        data = csv.reader(words_file)
        next(data)
        for row in data:
            words_list.append(row[0])
        random_index = random.randint(0, len(words_list)-1)
        return words_list[random_index]


def get_cat(word):
    with open('hangman_words.csv', 'r') as words_file:
        data = csv.reader(words_file)
        for row in data:
            if word == row[0]:
                category = row[1]
                return category
    return None


def init_track(word):
    dash = ' _ '
    track = dash*len(word)
    return track


def update_track(track, word, letter):
    new_track = ''
    letter = letter.upper()
    for i in range(len(word)):
        if word[i] == letter:
            new_track += f' {letter} '
        else:
            new_track += track[i*3:i*3+3]
    return new_track


def button_clicked(btn):
    return btn['text']


def format_word(word):
    formatted_word = ''
    for letter in word:
        formatted_word += f' {letter} '
    return formatted_word


def find_letter(letter, word):
    if letter in word:
        return True
    else:
        return False
