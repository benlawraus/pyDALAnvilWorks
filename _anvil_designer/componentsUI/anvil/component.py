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
class Component():
	def add_event_handler(self, event_name, handler_func):
		"""Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.		"""
		pass
	def get_event_handlers(self, event_name):
		"""Get the current event_handlers for a given event_name		"""
		pass
	def raise_event(self, event_name, **event_args):
		"""Trigger the event on this component. Any keyword arguments are passed to the handler function.		"""
		pass
	def remove_event_handler(self, event_name, handler_func):
		"""Remove a specific event handler function for a given event. Calling remove_event_handler with just the event name will remove all the handlers for this event		"""
		pass
	def remove_from_parent(self):
		"""Remove this component from its parent container.		"""
		pass
	def scroll_into_view(self, smooth=False):
		"""Scroll the window to make sure this component is in view.		"""
		pass
	def set_event_handler(self, event_name, handler_func):
		"""Set a function to call when the ‘event_name’ event happens on this component. Using set_event_hanlder removes all other handlers. Seting the handler function to None removes all handlers.		"""
		pass
	pass

@dataclass
class Container(Component):
	def add_component(self, component):
		"""Add a component to this container.		"""
		pass
	def clear(self):
		"""Remove all components from this container		"""
		pass
	def get_components(self):
		"""Get a list of components in this container		"""
		pass
	def raise_event_on_children(self, event_name, **event_args):
		"""Trigger the ‘event_name’ event on all children of this component. Any keyword arguments are passed to the handler function.		"""
		pass
	pass

@dataclass
class Media():
	def get_bytes(self):
		"""Get a binary string of the data represented by this Media object		"""
		pass
	pass
def alert(content, title="", buttons=None, large=False, dismissible=True, role=None):
    """Pop up an alert box. By default, it will have a single “OK” button which will return True when clicked."""
    pass
def confirm(content, title="", buttons=None, large=False, dismissible=False, role=None):
    """Pop up a confirmation box. By default, it will have “Yes” and “No” buttons which will return True and False respectively when clicked."""
    pass
def download(media):
    """Download the given Media Object immediately in the user’s browser."""
    pass
def get_focused_component():
    """Get the currently focused Anvil component, or None if focus is not in a component."""
    pass
def get_open_form():
    """Returns the form most recently opened with open_form()."""
    pass
def get_url_hash():
    """Get the decoded hash (the part after the ‘#’ character) of the URL used to open this app. If the first character of the hash is a question mark (eg ‘#?a=foo&b=bar’), it will be interpreted as query-string-type parameters and returned as a dictionary (eg {‘a’: ‘foo’, ‘b’: ‘bar’})."""
    pass
def open_form(form, *args, **kwargs):
    """Open the specified form as a new page.If ‘form’ is a string, a new form will be created (extra arguments will be passed to its constructor).If ‘form’ is a Form object, it will be opened directly."""
    pass
def set_default_error_handling(handler_fn):
    """Set a function to be called when an uncaught exception occurs. If set to None, a pop-up will appear letting the user know that an error has occurred."""
    pass

def set_url_hash(*args, **kwargs):
    """This is added for `anvil_extras`. for some reason it is not in the anvil documentation."""
    pass
