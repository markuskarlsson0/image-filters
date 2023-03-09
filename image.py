"""This module contains the PILImage class."""
from PIL import Image

class PILImage:
    """This class contains methods for opening, saving and manipulating an image."""
    def __init__(self):
        self.list = []
        self.resized = None
        self.path = None
        self.current_sections = None
        self.section_count = None

    def open(self, image_path):
        """Opens an image and sets it as the current image."""
        # Try to open image and add it to list, if it fails, raise an error.
        try:
            self.list = [Image.open(image_path)]
        except IOError as exc:
            raise IOError from exc
        else:
            self.path = image_path

    def save(self, path):
        """Saves the current image to a path."""
        # Try to save current image, if it fails, raise an error.
        try:
            self.list[-1].save(path)
        except IOError as exc:
            raise IOError from exc
        except ValueError as exc:
            raise ValueError from exc

    def resize(self):
        """Resizes the current image to fit the image label."""
        image_max_width = 900
        image_max_height = 500

        # If image is wider than the max image label width,
        # resize it to the max width while keeping aspect ratio.
        if self.list[-1].width > image_max_width:
            image_width = image_max_width
            image_height = int(self.list[-1].height * image_max_width / self.list[-1].width)

            # If image now is taller than the max image label height,
            # resize it to the max height while keeping aspect ratio.
            if image_height > image_max_height:
                image_height = image_max_height
                image_width = int(self.list[-1].width * image_max_height / self.list[-1].height)

        # If image is taller than the max image label height,
        # resize it to the max height while keeping aspect ratio.
        elif self.list[-1].height > image_max_height:
            image_height = image_max_height
            image_width = int(self.list[-1].width * image_max_height / self.list[-1].height)

            # If image now is wider than the max image label width,
            # resize it to the max width while keeping aspect ratio.
            if image_width > image_max_width:
                image_width = image_max_width
                image_height = int(self.list[-1].height * image_max_width / self.list[-1].width)

        # If image fits in image label max dimensions
        else:
            image_width = self.list[-1].width
            image_height = self.list[-1].height

        # Image dimensions can't be 0
        image_width = max(image_width, 1)
        image_height = max(image_height, 1)

        # Resizes image
        self.resized = self.list[-1].resize((image_width, image_height))

    def crop(self):
        """Crops the current image into sections."""
        image_sections = []
        image_section_width = self.list[-1].width // self.section_count

        for index in range(0, self.section_count - 1):
            image_sections.append(self.list[-1].crop((image_section_width * index, 0,
                image_section_width * (index + 1), self.list[-1].height)))

        image_sections.append(self.list[-1].crop(
            (image_section_width * (self.section_count - 1), 0,
            self.list[-1].width, self.list[-1].height)))

        self.current_sections = image_sections

    def merge(self):
        """Merges the current image sections into one image."""
        if self.list[-1].mode == 'RGB':
            new_image = Image.new(mode='RGB', size=self.list[-1].size)
        elif self.list[-1].mode == 'RGBA':
            new_image = Image.new(mode='RGBA', size=self.list[-1].size)

        for index, new_image_section in enumerate(self.current_sections):
            new_image.paste(new_image_section, (new_image_section.width * index, 0))

        current_sections_length = len(self.current_sections) - 1
        new_image.paste(self.current_sections[current_sections_length],
            (self.current_sections[0].width * current_sections_length, 0))

        self.list.append(new_image)
