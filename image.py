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
        self.current_sections = None
        self.section_count = None

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

    def resize(self):
        """Resizes the current image to fit the image label."""
        image_max_width = 900
        image_max_height = 500

        if self.current.width > image_max_width:
            image_width = image_max_width
            image_height = int(self.current.height * image_max_width / self.current.width)

            if image_height > image_max_height:
                image_height = image_max_height
                image_width = int(self.current.width * image_max_height / self.current.height)
        else:
            image_width = self.current.width
            image_height = self.current.height

        self.resized = self.current.resize((image_width, image_height))

    def crop(self):
        """Crops the current image into sections."""
        image_sections = []
        image_section_width = self.current.width // self.section_count

        for index in range(0, self.section_count - 1):
            image_sections.append(self.current.crop((image_section_width * index, 0,
                 image_section_width * (index + 1), self.current.height)))

        image_sections.append(self.current.crop(
            (image_section_width * (self.section_count - 1), 0,
             self.current.width, self.current.height)))
        self.current_sections = image_sections

    def merge(self):
        """Merges the current image sections into one image."""
        if self.current.mode == "RGB":
            new_image = Image.new(mode="RGB", size=self.current.size)
        elif self.current.mode == "RGBA":
            new_image = Image.new(mode="RGBA", size=self.current.size)

        for index, new_image_section in enumerate(self.current_sections):
            new_image.paste(new_image_section, (new_image_section.width * index, 0))

        current_sections_length = len(self.current_sections) - 1
        new_image.paste(self.current_sections[current_sections_length],
                        (self.current_sections[0].width * current_sections_length, 0))

        self.current = new_image
