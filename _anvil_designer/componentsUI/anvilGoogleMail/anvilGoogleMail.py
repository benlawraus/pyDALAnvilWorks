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
def send(to=None, subject=None, text=None, html=None, cc=None, bcc=None, from_address=None, draft=False):
    """Send an email via GMail. ‘to’, ‘cc’ and ‘bcc’ may be strings (email addresses) or lists of strings (multiple addresses). At least one of ‘text’ and ‘html’ need to be provided (both strings). Passing draft=True will create a draft message rather than sending it."""
    pass
