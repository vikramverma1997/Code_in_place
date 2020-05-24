"""
File: brickbreaker.py
---------------------
This program is a game known as brick breaker. In this game, we bounce the ball with the help of a rectangular paddle.
"""

import tkinter
import time
import random

# How big is the playing area?
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 1000     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 10              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_Y = 50      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING) / N_COLS
BRICK_COLORS = ['red', 'orange', 'yellow', 'green', 'cyan']

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 120
CHANGE_X_START = 10
CHANGE_Y_START = 7


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')
    bricks = create_bricks(canvas)
    ball = create_ball(canvas)
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, PADDLE_Y + 20, fill='black')
    dx = CHANGE_X_START
    dy = CHANGE_Y_START

    while True:
        # update world
        mouse_x = canvas.winfo_pointerx()
        canvas.move(ball, dx, dy)
        canvas.moveto(paddle, mouse_x, PADDLE_Y)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1
        if hit_paddle(canvas, paddle):
            dy *= -1
        for brick in bricks:
            if hit_brick(canvas, brick):
                canvas.moveto(brick, CANVAS_WIDTH + 10, CANVAS_HEIGHT + 10)
                bricks.remove(brick)
                dy *= -1
                break
        if hit_bottom_wall(canvas, ball):
            ball = create_ball(canvas)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1/70)

    canvas.mainloop()


def hit_brick(canvas, object):
    x_1 = get_left_x(canvas, object)
    y_1 = get_top_y(canvas, object)
    x_2 = get_right_x(canvas, object)
    y_2 = get_bottom_y(canvas, object)
    colliding_list = canvas.find_overlapping(x_1, y_1, x_2, y_2)
    return len(colliding_list) > 1


def hit_paddle(canvas, object):
    x_1 = get_left_x(canvas, object)
    y_1 = get_top_y(canvas, object)
    x_2 = get_right_x(canvas, object)
    y_2 = get_bottom_y(canvas, object)
    colliding_list = canvas.find_overlapping(x_1, y_1, x_2, y_2)
    return len(colliding_list) > 1


def create_ball(canvas):
    start_x = CANVAS_WIDTH / 2 - BALL_SIZE / 2
    end_x = start_x + BALL_SIZE
    start_y = CANVAS_HEIGHT / 2 - BALL_SIZE / 2
    end_y = start_y + BALL_SIZE
    ball = canvas.create_oval(start_x, start_y, end_x, end_y, fill='black')
    return ball


def create_bricks(canvas):
    bricks = []
    choose_color = -1

    for y in range(N_ROWS):
        # choose one color for 2 rows
        if (y % 2) == 0:
            choose_color += 1
            # if we increase N_ROWS, then colors are repeated
            if choose_color > (len(BRICK_COLORS) - 1):
                choose_color = 0
        color = BRICK_COLORS[choose_color]
        for x in range(N_COLS):
            start_x = ((x + 1) * SPACING) + (x * BRICK_WIDTH)
            end_x = start_x + BRICK_WIDTH
            start_y = BRICK_START_Y + (y * (SPACING + BRICK_HEIGHT))
            end_y = start_y + BRICK_HEIGHT
            brick = canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color, outline=color)
            bricks.append(brick)
    return bricks


def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0


def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0


def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT + BALL_SIZE


def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_right_x(canvas, object):
    return canvas.coords(object)[2]


def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


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
