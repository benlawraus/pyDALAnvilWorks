from dataclasses import dataclass


@dataclass
class TempFile:
    def __enter__(self):
        pass

    def __exit__(self):
        pass

    pass


def download(media):
    """Download the given Media Object immediately in the user’s browser."""
    pass


def from_file(filename, mime_type, name):
    """Creates a Media object from the given file."""
    pass


def print_media(media):
    """Print the given Media Object immediately in the user’s browser."""
    pass


def write_to_file(media, filename):
    """Write a Media object to the given file"""
    pass
