"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


# constants
COUNTDOWN_NUM = 10
COUNTDOWN_START = 10


def main():

    # print countdown from 10 to 1
    for i in range(COUNTDOWN_NUM):
        print(COUNTDOWN_START - i)

    print("Liftoff!")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
