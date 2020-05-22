"""
File: move_square.py
--------------------
This program moves a square block to center.
"""

import tkinter
import time

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SQUARE_SIZE = 100


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Move square to center')
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    end_y = start_y + SQUARE_SIZE
    rect = canvas.create_rectangle(0, start_y, SQUARE_SIZE, end_y, fill='black')

    while not is_past_center(canvas, rect):
        canvas.move(rect, 1, 0)
        canvas.update()

        time.sleep(1/50.)

    canvas.mainloop()


def is_past_center(canvas, shape):
    max_x = CANVAS_WIDTH / 2 - SQUARE_SIZE / 2
    corr_x = get_left_x(canvas, shape)

    return max_x < corr_x

def get_left_x(canvas, shape):
    # returns the x location of the shape
    return canvas.coords(shape)[0]

def get_top_y(canvas, shape):
    # returns the y location of the shape
    return canvas.coords(shape)[1]

def make_canvas(width, height, title):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas





if __name__ == '__main__':
    main()