from dataclasses import dataclass, field
from unittest.mock import Mock
from typing import Optional, Dict, List


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
class Component:
    _events: dict = field(default_factory=dict)

    def add_event_handler(self, event_name, handler_func):
        """Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.		"""
        ev = self._events.get(event_name, [])
        ev.append(handler_func)
        self._events.update({event_name: ev})

    def get_event_handlers(self, event_name):
        """Get the current event_handlers for a given event_name		"""
        return self._events.get(event_name, [])

    def raise_event(self, event_name, **event_args):
        """Trigger the event on this component. Any keyword arguments are passed to the handler function.		"""
        for ev in self._events.get(event_name, []):
            ev(**event_args)

    def remove_event_handler(self, event_name, handler_func=None):
        """Remove a specific event handler function for a given event. Calling remove_event_handler with just the event name will remove all the handlers for this event		"""
        if handler_func is None:
            self._events.pop(event_name, None)
        else:
            self._events[event_name].remove(handler_func)

    def remove_from_parent(self):
        """Remove this component from its parent container.		"""
        pass

    def scroll_into_view(self, smooth=False):
        """Scroll the window to make sure this component is in view.		"""
        pass

    def set_event_handler(self, event_name, handler_func):
        """Set a function to call when the ‘event_name’ event happens on this component. Using set_event_handler removes all other handlers. Setting the handler function to None removes all handlers.		"""
        self._events[event_name] = [handler_func]


@dataclass
class Container(Component):
    _components: list = field(default_factory=list)

    def add_component(self, component, **kwargs):
        """Add a component to this container.		"""
        if kwargs.get('index', None):
            self._components.insert(kwargs["index"],component)
        else:
            self._components.append(component)
        pass

    def clear(self):
        """Remove all components from this container		"""
        self._components = []

    def get_components(self):
        """Get a list of components in this container		"""
        return self._components

    def raise_event_on_children(self, event_name, **event_args):
        """Trigger the ‘event_name’ event on all children of this component. Any keyword arguments are passed to the handler function.		"""
        pass

    def refresh_data_bindings(self):
        """All bound properties for a particular Form are updated whenever:
            self.refresh_data_bindings() is called, or
            self.init_components(**properties) is called, or
            the self.item for the Form is set."""
        pass

# @dataclass
class Media:
    """Media object subclassed by BlobMedia and UrlMedia.

    Attributes
    ----------
    content_type : str
        the MIME type of this media. This is a string with values like "text/plain" or "image/png".
    content : bytes
        a binary string of the image or file
    name : str
        optional filename
    length:
        length in bytes of `content`
    url:
        Gives an URL where this media can be downloaded, if this Media is “permanent” (e.g. if it is stored in
        Data Tables, or a Google Drive file). If a Media object is not permanent (e.g. it is an anonymous
        BlobMedia object), its url property will be None. However, you can still download non-permanent Media
        objects using Link components, or display them with Image components.

    Methods
    -------
    get_bytes
        returns the content as a string
    """
    # url:Optional[str]=None
    # content_type:Optional[str] = None
    # content:bytes = b''
    # name:str = ''
    def __init__(self, url:str=None, content_type:str=None, content:bytes=None, name:str=None):
        self.url = url
        self.content_type = content_type
        self.content = content
        self.name = name
    @property
    def length(self):
        """length in bytes of `content`"""
        return len(self.content)

    def get_bytes(self)->str:
        """Get a binary string of the data represented by this Media object		"""
        return self.content.decode()



def alert(content, title="", buttons=None, large=False, dismissible=True, role=None):
    """Pop up an alert box. By default, it will have a single “OK” button which will return True when clicked."""
    if buttons:
        return buttons[0][1]
    return True


def confirm(content, title="", buttons=None, large=False, dismissible=False, role=None):
    """Pop up a confirmation box. By default, it will have “Yes” and “No” buttons which will return True and False
    respectively when clicked."""
    return True


def download(media:Media):
    """Download the given Media Object immediately in the user’s browser."""
    return Mock()


def get_focused_component():
    """Get the currently focused Anvil component, or None if focus is not in a component."""
    return Mock()


def get_open_form():
    """Returns the form most recently opened with open_form()."""
    return Mock()


def get_url_hash():
    """Get the decoded hash (the part after the ‘#’ character) of the URL used to open this app. If the first character of the hash is a question mark (eg ‘#?a=foo&b=bar’), it will be interpreted as query-string-type parameters and returned as a dictionary (eg {‘a’: ‘foo’, ‘b’: ‘bar’})."""
    return Mock()


def open_form(form, *args, **kwargs):
    """Open the specified form as a new page.If ‘form’ is a string, a new form will be created (extra arguments will be passed to its constructor).If ‘form’ is a Form object, it will be opened directly."""
    return Mock()


def set_default_error_handling(handler_fn):
    """Set a function to be called when an uncaught exception occurs. If set to None, a pop-up will appear letting the user know that an error has occurred."""
    return Mock()


def set_url_hash(*args, **kwargs):
    """This is added for `anvil_extras`. for some reason it is not in the anvil documentation."""
    return Mock()
