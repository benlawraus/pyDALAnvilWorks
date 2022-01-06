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
def plot_image(dpi=None, facecolor=None, edgecolor=None, format=None, transparent=None, frameon=None, bbox_inches=None, pad_inches=None, filename=None):
    """Return the current Matplotlib figure as an PNG image. Returns an Anvil Media object that can be displayed in Image components.Optional arguments have the same meaning as for ‘savefig()’"""
    pass
