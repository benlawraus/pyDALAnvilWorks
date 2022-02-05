from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from ...common_structures import ClassDict


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
Items = list
Datagridcolumns = list
Pixels = int
Uri = str
Html = str
Icon = str
Form = object
