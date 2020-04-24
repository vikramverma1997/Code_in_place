"""
File: khansole_academy.py
-------------------------
This program asks the user to compute the sum of two 2-digit numbers. The program will not stop until the user compute
three accurate additions in a row.
"""

import random


MIN_NUMBER = 10
MAX_NUMBER = 99
NUM_CORRECT = 3


# Design a problem of addition for user using random integers.
def input_problem():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    user_sum = int(input("Your answer: "))
    actual_sum = num1 + num2

    return user_sum, actual_sum


# Check whether the sum computed by user is correct or incorrect.
def check_sum(user_sum, actual_sum):
    if user_sum == actual_sum:
        result = "Correct"
    else:
        result = "Incorrect"

    return result


def main():
    num_correct = 0
    # Run program until user gets three accurate answers in a row.
    while num_correct < NUM_CORRECT:
        user_sum, actual_sum = input_problem()
        result = check_sum(user_sum, actual_sum)

        if result == "Correct":
            # Count the number of correct answers given by user.
            num_correct += 1
            print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            # Reset the value of count after any incorrect answer.
            num_correct = 0
            print("Incorrect. The expected answer is " + str(actual_sum))

    print("Congratulations! You mastered addition.")




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
