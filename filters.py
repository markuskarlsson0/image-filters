"""This module contains the filters that can be applied to an image."""
from PIL import Image

def invert_filter(current_image):
    """Inverts the color channels of an image."""
    new_image = Image.new(mode="RGB", size=current_image.size)

    for x_pixel in range(current_image.width):
        for y_pixel in range(current_image.height):
            red_channel, green_channel, blue_channel = current_image.getpixel((x_pixel, y_pixel))
            new_image.putpixel((x_pixel, y_pixel), (green_channel, blue_channel, red_channel))

    return new_image