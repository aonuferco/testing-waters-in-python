import random
import string


def cow_n_bull():
    rand = [random.randint(1, 9) for _ in range(0, 4)]  # randomly generated number
    cows, bulls, count = 0, 0, 0
    valid = False  # game stop/run flag
    print("Please enter a 4 digit value")

    while not valid:

        uinput = input("Your guess > ")

        if any(c in string.punctuation for c in uinput) or any(c.isalpha() for c in uinput):
            print("Please enter a 4 digit value")
        else:
            uinput = list(map(int, uinput))
            if len(uinput) == 4:
                for i in range(0, len(uinput)):
                    if uinput[i] in rand and rand[i] == uinput[i]:
                        cows += 1
                    elif uinput[i] in rand and rand[i] != uinput[i]:
                        bulls += 1

                count += 1

                if cows == 4:
                    print("You guessed it right")
                    print("It took you " + str(count) + " tries")
                    valid = True
                else:
                    print(str(cows) + " cows," + str(bulls) + " bulls")
                    cows, bulls = 0, 0
            else:
                print("Please enter a 4 digit value")
