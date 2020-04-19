from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    make_row_black()
    while corner_color_is(BLACK):
        extreme_corners_white()
    put_beeper()

"""
Karel makes the extreme two corners white
Pre: Karel is facing west and standing on black
Post: Karel is facing east and standing on black
"""
def extreme_corners_white():
    paint_corner(BLANK)
    move()
    while corner_color_is(BLACK):
        move()
    paint_corner(BLANK)
    turn_around()
    move()

"""
Karel makes the whole row black except the first block
Pre: karel is facing east
Post: karel is facing west
"""
def make_row_black():
    while front_is_clear():
        move()
        paint_corner(BLACK)
    turn_around()


def turn_around():
    turn_left()
    turn_left()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
