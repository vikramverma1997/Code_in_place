"""
File: pencil_sketch.py
----------------
This program takes an rgb image and convert it into a pencil sketch.
"""


from simpleimage import SimpleImage

PADDING = 5

def main():
    original = SimpleImage('Images/vikram.png')
    original.show()
    copy_img = make_copy(original)
    img_gray = grayscale(copy_img)
    img_inverted = inversion(img_gray)
    img_blurred = blur(img_inverted)
    img_blurred.show()


# blurs the input image
def blur(image):
    copy_image_padded = add_padding(image, PADDING)
    for y in range(PADDING, copy_image_padded.height - PADDING):
        for x in range(PADDING, copy_image_padded.width - PADDING):
            blur_pixel(copy_image_padded, x, y, 11)

    return copy_image_padded


def blur_pixel(image, x_index, y_index, blur_size):
    red = 0
    blue = 0
    green = 0
    for y in range(x_index - PADDING, x_index - PADDING + blur_size):
        for x in range(y_index - PADDING, y_index - PADDING + blur_size):
            pixel = image.get_pixel(x, y)
            red += pixel.red
            blue += pixel.blue
            green += pixel.green
    for pixel in image:
        pixel.red = red / (blur_size ** 2)
        pixel.blue = blue / (blur_size ** 2)
        pixel.green = green / (blur_size ** 2)


def add_padding(image, padding):
    copy_image = SimpleImage.blank(image.width + (2 * padding), image.height + (2 * padding))
    for pixel in copy_image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            copy_image.set_pixel(x + padding, y + padding, pixel)

    return copy_image


# invert the input image
def inversion(image):
    copy_image = make_copy(image)
    for pixel in copy_image:
        pixel.red = 255 - pixel.red
        pixel.green = 255 - pixel.green
        pixel.blue = 255 - pixel.blue

    return copy_image


# convert the copy of the original image into grayscale
def grayscale(image):
    copy_image = make_copy(image)
    for pixel in copy_image:
        value = 0.299 * pixel.red + 0.587 * pixel.green + 0.114 * pixel.blue
        pixel.red = value
        pixel.green = value
        pixel.blue = value

    return copy_image


# makes a copy of the original image
def make_copy(original_image):
    copy_image = SimpleImage.blank(original_image.width, original_image.height)
    for pixel in original_image:
        copy_image.set_pixel(pixel.x, pixel.y, pixel)

    return copy_image






if __name__ == '__main__':
    main()
