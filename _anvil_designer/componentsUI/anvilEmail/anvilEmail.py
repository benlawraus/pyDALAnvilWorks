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
class DeliveryFailure():
	pass

@dataclass
class SendFailure():
	pass
def send(to=None, cc=None, bcc=None, from_address="no-reply", from_name=None, subject=None, text=None, html=None, attachments=None, inline_attachments=None):
    """Send an email"""
    pass
