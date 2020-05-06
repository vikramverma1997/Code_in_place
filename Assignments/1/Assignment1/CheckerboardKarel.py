from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    checkboard_pattern()


def checkboard_pattern():
    if front_is_clear():
        place_all_beepers()
    else:
        turn_left()
        if  front_is_clear():
            place_all_beepers()
        else:
            put_beeper()


def place_all_beepers():
    while front_is_clear():
        place_one_row()


def place_one_row():
    while front_is_clear():
        put_beeper()
        move()
        beeper_at_extreme_corner()
    # return_back()
    check_beeper()


def beeper_at_extreme_corner():
    if front_is_clear():
        move()
        if front_is_blocked():
            put_beeper()


def check_beeper():
    if beepers_present():
        align()
        if front_is_clear():
            move()
    else:
        align()


def align():
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

    """
def return_back():
    turn_around()
       while front_is_clear():
         move()
    check_beeper()

def turn_around():
    turn_left()
    turn_left()
    """

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
