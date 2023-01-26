"""This module contains the PILImage class."""
from PIL import Image

class PILImage:
    """This class contains methods for opening, saving and manipulating an image."""
    def __init__(self):
        self.current = None
        self.original = None
        self.last = None
        self.resized = None
        self.path = None

    def open(self, image_path):
        """Opens an image and sets it as the current image."""
        try:
            self.current = Image.open(image_path)
        except IOError:
            raise IOError
        else:
            self.original = self.current
            self.last = self.current
            self.path = image_path

    def save(self, path):
        """Saves the current image to a path."""
        try:
            self.current.save(path)
        except IOError:
            raise IOError
        except ValueError:
            raise ValueError

    def resize(self, image):
        """Resizes an image to fit the image label."""
        image_max_width = 900
        image_max_height = 500

        if image.width > image_max_width:
            image_width = image_max_width
            image_height = int(image.height * image_max_width / image.width)

            if image_height > image_max_height:
                image_height = image_max_height
                image_width = int(image.width * image_max_height / image.height)
        else:
            image_width = image.width
            image_height = image.height

        image_resized = image.resize((image_width, image_height))
        return image_resized
