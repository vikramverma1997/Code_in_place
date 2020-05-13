"""
File: guess_game.py
------------------
This program is a simple guessing game in which user have to guess the correct number.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    count = 1
    print("Hello! Let's play a number guessing game.\nPress ctrl-c to quit.")
    user_name = input("Please enter your name: ")

    while True:
        print(user_name + ", I'm thinking of an integer in the interval [" + str(MIN_NUMBER) + ", " + str(MAX_NUMBER) + "]")
        guessed_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        user_guess = int(input("Please enter your guess: "))

        while user_guess != guessed_number:
            if user_guess < guessed_number:
                print(user_name + ", your guess was too low!")
                user_guess = int(input("Please enter your guess: "))
                count += 1
            elif user_guess > guessed_number:
                print(user_name + ", your guess was too high!")
                user_guess = int(input("Please enter your guess: "))
                count += 1

        print("Congratulations " + user_name + ", you got it!")
        print("You took " + str(count) + " guesses.")










if __name__ == '__main__':
    main()