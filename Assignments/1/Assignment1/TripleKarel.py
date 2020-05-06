from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
# karel paints the three buildings
    for i in range(3):
        paint_one_box()


"""
Karel paints one building
Pre: None
Post: Karel is facing south
"""
def paint_one_box():
    for i in range(2):
        paint_one_line()
        turn_left()
        move()
    paint_one_line()
    turn_right()

"""
Karel paints one side of a building
Pre: None
Post: None
"""
def paint_one_line():
    while left_is_blocked():
        put_beeper()
        move()

"""
Karel turns right by moving left three times
Pre: None
Post: None
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
