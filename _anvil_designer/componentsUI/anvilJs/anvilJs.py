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
def await_promise(js_promise):
    """Await the result of a Javascript Promise in Python. This function will block until the promise resolves or rejects. If the promise resolves, it will return the resolved value. If the promise rejects, it will raise the rejected value as an exception"""
    pass
def call(js_function_or_name, *args):
    """Call a global Javascript function by name, translating arguments and return values from Python to Javascript."""
    pass
def get_dom_node(component):
    """Returns the Javascript DOM node for an Anvil component. If a DOM node is passed to the function it will be returned. Anything else throws a TypeError"""
    pass
def import_from(url):
    """use anvil.js.import_from(url) to dynamically import a Javascript Module. Accessing the attributes of a Javascript Module vary depending on the Module. See the documentation for examples"""
    pass
def new(js_class, *args):
    """Given a Javascript class (aka function object) that’s been passed into Python, construct a new instance of it."""
    pass
def report_exceptions(wrapped_function):
    """Use @anvil.js.report_exceptions as a decorator for any function used as a javascript callback. Error handling may be suppressed by an external javascript libary. This decorator makes sure that errors in your python code are reported."""
    pass
def to_media(blob, content_type="", name=None):
    """Convert a javascript Blob, ArrayBuffer, Uint8Array or an Array of these types to an anvil BlobMedia object. If a Blob, or Array of Blobs, is passed the content_type will be inferred."""
    pass
