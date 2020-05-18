"""
File: pencil_sketch.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.8


def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')
    bluescreen(foreground, background)
    background.show()


def bluescreen(foreground, background):
    for pixel in foreground:
        avg_pixel = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.blue <= (avg_pixel * INTENSITY_THRESHOLD):
            x = pixel.x
            y = pixel.y
            background.set_pixel(x, y, pixel)


if __name__ == '__main__':
    main()