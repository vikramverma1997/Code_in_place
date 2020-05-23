"""
File: bounce_ball.py
--------------------
This program creates a ball and bounce it off when it touches the boundary.
"""

import tkinter
import time
import random


CANVAS_WIDTH = 1000      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 1000     # Height of drawing canvas in pixels
Ball_SIZE = 70


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Bounce ball')
    start_y = 0
    end_y = start_y + Ball_SIZE
    ball = canvas.create_oval(0, start_y, Ball_SIZE, end_y, fill='black')
    change_x = 3
    change_y = 1

    while True:
        canvas.move(ball, change_x, change_y)

        if get_bottom_x(canvas, ball) >= CANVAS_WIDTH or get_left_x(canvas, ball) <= 0:
            change_x *= -1
        if get_top_y(canvas, ball) <= 0 or get_bottom_y(canvas, ball) >= CANVAS_HEIGHT:
            change_y *= -1

        canvas.update()
        time.sleep(1/400)

    canvas.mainloop()



def get_left_x(canvas, shape):
    # returns the x location of the shape
    return canvas.coords(shape)[0]

def get_top_y(canvas, shape):
    # returns the y location of the shape
    return canvas.coords(shape)[1]

def get_bottom_y(canvas, shape):
    return canvas.coords(shape)[3]


def get_bottom_x(canvas, shape):
    return canvas.coords(shape)[2]


def make_canvas(width, height, title):
   """
   DO NOT MODIFY
   Creates and returns a drawing canvas
   of the given int size with a blue border,
   ready for drawing.
   """
   top = tkinter.Tk()
   top.minsize(width=width, height=height)
   top.title(title)
   canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
   canvas.pack()
   return canvas


if __name__ == '__main__':
    main()