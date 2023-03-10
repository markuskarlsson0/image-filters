"""This module contains the filters that can be applied to an image."""
from PIL import Image

def grayscale_filter(current_image, intensity):
    """Makes image grayscale."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                average_channel = (red_channel + green_channel + blue_channel) // 3

                # Put average channel into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (average_channel, average_channel, average_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                average_channel = (red_channel + green_channel + blue_channel) // 3

                # Put average channel into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (average_channel, average_channel, average_channel, alpha_channel))

    return new_image

def invert_filter(current_image, intensity):
    """Makes image colors inverted."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # Put inverted channels into new image
                new_image.putpixel((x_pixel, y_pixel), (green_channel, blue_channel, red_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # Put inverted channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (green_channel, blue_channel, red_channel, alpha_channel))

    return new_image

def black_and_white_filter(current_image, intensity):
    """Makes image black and white."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # If pixel is more light than dark, make it white
                if red_channel + green_channel + blue_channel > 382.5:
                    red_channel = 255
                    green_channel = 255
                    blue_channel = 255
                # If pixel is more dark than light, make it black
                else:
                    red_channel = 0
                    green_channel = 0
                    blue_channel = 0

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # If pixel is more light than dark, make it white
                if red_channel + green_channel + blue_channel > 382.5:
                    red_channel = 255
                    green_channel = 255
                    blue_channel = 255
                # If pixel is more dark than light, make it black
                else:
                    red_channel = 0
                    green_channel = 0
                    blue_channel = 0

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image

def sepia_filter(current_image, intensity):
    """Makes image sepia toned."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                new_red_channel = int((red_channel * 0.393) + (green_channel * 0.769) + \
                    (blue_channel * 0.189))
                new_green_channel = int((red_channel * 0.349) + (green_channel * 0.686) + \
                    (blue_channel * 0.168))
                new_blue_channel = int((red_channel * 0.272) + (green_channel * 0.534) + \
                    (blue_channel * 0.131))

                # Pixel values can't be higher than 255
                new_red_channel = min(new_red_channel, 255)
                new_green_channel = min(new_green_channel, 255)
                new_blue_channel = min(new_blue_channel, 255)

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (new_red_channel, new_green_channel, new_blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                new_red_channel = int((red_channel * 0.393) + (green_channel * 0.769) + \
                    (blue_channel * 0.189))
                new_green_channel = int((red_channel * 0.349) + (green_channel * 0.686) + \
                    (blue_channel * 0.168))
                new_blue_channel = int((red_channel * 0.272) + (green_channel * 0.534) + \
                    (blue_channel * 0.131))

                # Pixel values can't be higher than 255
                new_red_channel = min(new_red_channel, 255)
                new_green_channel = min(new_green_channel, 255)
                new_blue_channel = min(new_blue_channel, 255)

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (new_red_channel, new_green_channel, new_blue_channel, alpha_channel))

    return new_image

def cold_filter(current_image, intensity):
    """Makes image cold toned."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel * 0.9)
                green_channel = int(green_channel * 0.9)
                blue_channel = int(blue_channel * 1.1)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel * 0.9)
                green_channel = int(green_channel * 0.9)
                blue_channel = int(blue_channel * 1.1)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image

def warm_filter(current_image, intensity):
    """Makes image warm toned."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel * 1.2)
                green_channel = int(green_channel * 1.05)
                blue_channel = int(blue_channel * 0.9)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel * 1.2)
                green_channel = int(green_channel * 1.05)
                blue_channel = int(blue_channel * 0.9)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image

def colorful_filter(current_image, intensity):
    """Makes image colorful."""
    # This filter does not use the intensity slider
    if intensity != 1:
        return False

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # Makes channel with highest value the only active channel
                if red_channel > green_channel and red_channel > blue_channel:
                    red_channel = 255
                    green_channel = 0
                    blue_channel = 0
                elif green_channel > red_channel and green_channel > blue_channel:
                    red_channel = 0
                    green_channel = 255
                    blue_channel = 0
                elif blue_channel > red_channel and blue_channel > green_channel:
                    red_channel = 0
                    green_channel = 0
                    blue_channel = 255
                else:
                    red_channel = 255
                    green_channel = 255
                    blue_channel = 255

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                # Makes channel with highest value the only active channel
                if red_channel > green_channel and red_channel > blue_channel:
                    red_channel = 255
                    green_channel = 0
                    blue_channel = 0
                elif green_channel > red_channel and green_channel > blue_channel:
                    red_channel = 0
                    green_channel = 255
                    blue_channel = 0
                elif blue_channel > red_channel and blue_channel > green_channel:
                    red_channel = 0
                    green_channel = 0
                    blue_channel = 255
                else:
                    red_channel = 255
                    green_channel = 255
                    blue_channel = 255

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image

def lighter_filter(current_image, intensity):
    """Makes image lighter."""
    intensity *= 10

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel + intensity)
                green_channel = int(green_channel + intensity)
                blue_channel = int(blue_channel + intensity)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel + intensity)
                green_channel = int(green_channel + intensity)
                blue_channel = int(blue_channel + intensity)

                # Pixel values can't be higher than 255
                red_channel = min(red_channel, 255)
                green_channel = min(green_channel, 255)
                blue_channel = min(blue_channel, 255)

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image

def darker_filter(current_image, intensity):
    """Makes image darker."""
    intensity *= 10

    # If RGB image, apply filter to all channels
    if current_image.mode == 'RGB':
        # Create new RGB image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGB', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel - intensity)
                green_channel = int(green_channel - intensity)
                blue_channel = int(blue_channel - intensity)

                # Pixel values can't be lower than 0
                red_channel = max(red_channel, 0)
                green_channel = max(green_channel, 0)
                blue_channel = max(blue_channel, 0)

                # Put modified channels into new image
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel))

    # If RGBA image, apply filter to all channels except alpha
    elif current_image.mode == 'RGBA':
        # Create new RGBA image with same size as current image where changes can be saved
        new_image = Image.new(mode='RGBA', size=current_image.size)

        for x_pixel in range(current_image.width):
            for y_pixel in range(current_image.height):
                # Get channels of current pixel
                red_channel, green_channel, blue_channel, alpha_channel = current_image.getpixel(
                    (x_pixel, y_pixel))

                red_channel = int(red_channel - intensity)
                green_channel = int(green_channel - intensity)
                blue_channel = int(blue_channel - intensity)

                # Pixel values can't be lower than 0
                red_channel = max(red_channel, 0)
                green_channel = max(green_channel, 0)
                blue_channel = max(blue_channel, 0)

                # Put modified channels into new image except alpha
                new_image.putpixel((x_pixel, y_pixel),
                    (red_channel, green_channel, blue_channel, alpha_channel))

    return new_image
