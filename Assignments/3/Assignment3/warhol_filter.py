"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for rows in range(N_ROWS):
        for cols in range(N_COLS):
            patch = make_recolored_patch(0.5 * (cols+1) * (rows + 0.1), cols * 1.2, 0.8 * (cols + 1))
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    pixel = patch.get_pixel(x, y)
                    final_image.set_pixel(x + (cols * PATCH_SIZE), y + (rows* PATCH_SIZE), pixel)
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

if __name__ == '__main__':
    main()