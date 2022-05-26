from dataclasses import dataclass


@dataclass
class ImageException():
    pass


def generate_thumbnail(image_media, max_size):
    """Resize the supplied image so that neither width nor height exceeds max_size (in pixels).Pass in an anvil.Media
    object representing the image. """
    pass


def get_dimensions(image_media):
    """Get the dimensions of an image (width, height).Pass in an anvil.Media object representing the image."""
    pass


def rotate(image_media, angle):
    """Rotate the supplied image clockwise by the given number of degrees.Pass in an anvil.Media object representing
    the image. """
    pass
