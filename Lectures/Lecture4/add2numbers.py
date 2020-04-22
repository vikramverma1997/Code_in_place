"""
File: add2numbers.py
--------------------
Program which asks for the user inputs of two numbers and prints their sum.
"""


def main():
    print("This is a program to calculate sum of two numbers.")

    # ask the user to input first number
    num1 = input("Enter first number: ")

    # convert string into integer
    num1 = int(num1)

    # ask the user to input second number
    num2 = input("Enter second number: ")

    # convert string into integer
    num2 = int(num2)

    # computer sum of the two numbers
    total = num1 + num2

    # print the sum
    print("The sum is: " + str(total) + ".")


if __name__ == '__main__':
    main()
