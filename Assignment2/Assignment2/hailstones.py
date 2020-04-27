"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""

STOP_NUMBER = 1


def check_num(num):
    remainder = num % 2
    if remainder == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    return even_or_odd


def main():
    count = 0
    num = int(input("Enter a positive integer: "))
    while num < 0:
        num = int(input("Please enter a positive integer: "))

    while num != STOP_NUMBER:
        even_or_odd = check_num(num)
        if even_or_odd == "even":
            num1 = int(num / 2)
            print(str(num) + " is even, so I take half: " + str(num1))
        else:
            num1 = int((3 * num) + 1)
            print(str(num) + " is odd, so I take 3n + 1: " + str(num1))
        num = num1
        count += 1

    print("The process took " + str(count) + " steps to reach 1")








# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
