"""
File: learn_algebra.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""

import random

MIN_NUMBER = 10
MAX_NUMBER = 99
NUM_CORRECT = 3


def input_problem(learn_what):
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    if learn_what == "a":
        print("What is " + str(num1) + " + " + str(num2) + "?")
        actual_result = num1 + num2
    elif learn_what == "b":
        print("What is " + str(num1) + " - " + str(num2) + "?")
        actual_result = num1 - num2
    elif learn_what == "c":
        print("What is " + str(num1) + " * " + str(num2) + "?")
        actual_result = num1 * num2
    elif learn_what == "d":
        print("What is " + str(num1) + " / " + str(num2) + "?")
        actual_result = num1 / num2

    user_result = float(input("Your answer: "))

    return user_result, actual_result


def check_sum(user_result, actual_result):
    if user_result == actual_result:
        result = "Correct"
    else:
        result = "Incorrect"

    return result


def learn_algebra(learn_what):
    num_correct = 0

    # Run program until user gets three accurate answers in a row.
    while num_correct < NUM_CORRECT:
        user_result, actual_result = input_problem(learn_what)
        result = check_sum(user_result, actual_result)

        if result == "Correct":
            # Count the number of correct answers given by user.
            num_correct += 1
            print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            # Reset the value of count after every incorrect answer.
            num_correct = 0
            print("Incorrect. The expected answer is " + str(actual_result))

    if learn_what == "a":
        print("Congratulations! You mastered addition.")
    elif learn_what == "b":
        print("Congratulations! You mastered subtraction.")
    elif learn_what == "c":
        print("Congratulations! You mastered multiplication.")
    elif learn_what == "d":
        print("Congratulations! You mastered division.")


def main():
    learn_what = input("What would you like to learn? \n a. Addition \n b. Subtraction \n c. Multiplication \n d. Division \n Give your answer (a, b, c or d): ")
    learn_algebra(learn_what)






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
