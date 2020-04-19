from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    while front_is_clear():
        repair_all_arches()
        move_to_another_arch()
    repair_all_arches()


def repair_all_arches():
    repair_one_arch()
    return_back()


def repair_one_arch():
    turn_left()
    while front_is_clear():
        check_beeper()
    if no_beepers_present():
        put_beeper()


def check_beeper():
    if beepers_present():
        move()
    else:
        put_beeper()
        move()


def return_back():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_to_another_arch():
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
