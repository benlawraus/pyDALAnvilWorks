from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from ..._anvil_designer.common_structures import ClassDict


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


@dataclass
class PDFRenderer():
    def render_form(self, form_name, *args, **kwargs):
        """Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to pass to its constructor.Returns a PDF as an Anvil Media object.		"""
        pass

    pass


def render_form(form_name, *args, **kwargs):
    """Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to pass to its constructor.Returns a PDF as an Anvil Media object."""
    pass
