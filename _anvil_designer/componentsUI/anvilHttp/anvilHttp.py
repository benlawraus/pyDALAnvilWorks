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
class HttpError():
	pass

@dataclass
class UrlEncodingError():
	pass
def request(url, method="GET", data=None, json=False, headers=None, username=None, password=None, timeout=None):
    """Make an HTTP request to the specified URL.If json=True, the response is parsed into Python objects (dicts/lists/etc), and ‘data’ is JSON-encoded before sending.‘headers’ can be a dict of strings to set HTTP headers.If specified, ‘username’ and ‘password’ will be used to perform HTTP Basic authentication."""
    pass
def url_decode(string_to_encode):
    """URL-decode a string. Raises UrlEncodingError on failure."""
    pass
def url_encode(string_to_encode):
    """URL-encode a string"""
    pass
