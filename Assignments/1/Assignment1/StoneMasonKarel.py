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


# Karel repairs all the arches of the building
def repair_all_arches():
    repair_one_arch()
    return_back()


"""
Karel repairs one arch of all the arches
Pre: Karel is facing east
Post: Karel is facing north
"""
def repair_one_arch():
    turn_left()
    while front_is_clear():
        check_beeper()
    if no_beepers_present():
        put_beeper()


"""
Karel check whether a beeper is present or not. 
If not present, karel puts one beeper.
Pre: None
Post: None
"""
def check_beeper():
    if beepers_present():
        move()
    else:
        put_beeper()
        move()


"""
Karel returns back to its initial position
Pre: Karel is facing North
Post: Karel is facing east
"""
def return_back():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


"""
Karel rotates 180 degree
Pre: None
Post: None
"""
def turn_around():
    turn_left()
    turn_left()


"""
Karel moves to another arch to repair
Pre: Karel is facing east
Post: Karel is facing east
"""
def move_to_another_arch():
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
