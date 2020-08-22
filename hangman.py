"""
SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example). It is the combination
of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.

In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The
player guesses one letter at a time until the entire word has been guessed. 
"""

import random

# global vars
COUNT, GAMEOVER, WON = 0, False, False


def hangman():
    global COUNT, GAMEOVER, WON
    dict = {}

    word = random.choice(open("sowpods.txt", "r").read().split("\n"));
    letter_list = list(word)
    guessed_letter_list = list("_" * len(word))
    print("Welcome to Hangman. Please enter a letter at a time. You have 6 incorrect guesses.")
    print("_ " * len(word))

    while not GAMEOVER:
        if COUNT == 5:
            GAMEOVER = True

        print("Guess your letter: ")
        letter = input().upper()

        if letter in letter_list:
            temp = [i for i in range(len(letter_list)) if letter_list[i] == letter]
            for i in temp:
                dict[i] = letter
            for key, value in dict.items():
                guessed_letter_list[key] = value
            print(*guessed_letter_list)
            if guessed_letter_list == letter_list:
                GAMEOVER = True
                WON = True
        else:
            COUNT += 1
            print("Incorrect. You have " + str(6 - COUNT) + " incorrect guesses left."
                  if 6 - COUNT > 1 else "Incorrect. You have 1 incorrect guess left.")

    if WON:
        print("Congratulations! You've won!")
    else:
        print("You've lost. The word was ", *letter_list)
