from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

def default_val(val):
    return lambda: val
String = str
Number = float
Integer = int
Color = str
Boolean = bool
Themerole = str
Object = object
Seconds = float
Items = List[Dict]
Datagridcolumns = List[str]
Pixels = int
Uri = str
Html = str
Icon = str
Form = object

@dataclass
class TempFile():
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
