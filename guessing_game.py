"""
In a previous exercise, we've written a program that 'knows' a number and asks a user to guess it.
This time, we're going to do exactly the opposite.
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.
"""

VALID, NUM, LOW, HIGH, COUNT = False, 0, 0, 0, 0


def ask():
    global VALID, NUM, COUNT, LOW, HIGH

    COUNT = COUNT + 1
    print("Is", NUM, "your number?")
    uinput = input("Y/N > ")
    if uinput.lower() == "y":
        VALID = True
    else:
        print("Is", NUM, "too HIGH or too LOW?")
        uinput = input("H/L > ")
        if uinput.lower() == "h":
            HIGH = NUM - 1
        else:
            LOW = NUM + 1
        NUM = int((LOW + HIGH) / 2)


def guessing_game():
    global NUM, LOW, HIGH, COUNT

    print("Is your number between 50 and 100?")
    uinput = input("Y/N > ")

    if uinput.lower() == "y":
        LOW, HIGH, NUM = 50, 100, 75
        while not VALID:
            ask()
        print("It took", COUNT, "tries for me to guess your number")
    else:
        LOW, HIGH, NUM = 1, 50, 25
        while not VALID:
            ask()
        print("It took", COUNT, "tries for me to guess your number")


guessing_game()

