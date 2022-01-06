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
class Capability():
	def narrow(self, additional_scope):
		"""Return a new capability that is narrower than this one, by appending additional scope element(s) to it.		"""
		pass
	def send_update(self, update):
		"""Send an update to the update handler for this capability, in this interpreter and also in any calling environment (eg browser code) that passed this capability into the current server function.		"""
		pass
	def set_update_handler(self, apply_update, get_update):
		"""Set a handler for what happens when an update is sent to this capability.Optionally provide a function for aggregating updates (default behaviour is to merge them, if they are all dictionaries, or to return only the most recent update otherwise.)		"""
		pass
	pass

@dataclass
class HttpRequest():
	pass

@dataclass
class HttpResponse():
	pass
def get_api_origin(environment):
    """Returns the root URL of the API for the current app.By default, this function returns the URL for the current environment, which might be private or temporary (for example, if you are running your app in the Anvil Editor). If you want the URL for the published branch, pass ‘published’ as an argument."""
    pass
def get_app_origin(environment):
    """Returns the root URL for the current app.By default, this function returns the URL for the current environment, which might be private or temporary (for example, if you are running your app in the Anvil Editor). If you want the URL for the published branch, pass ‘published’ as an argument."""
    pass
def is_app_online():
    """Returns True if this app is online and False otherwise.If anvil.server.is_app_online() returns False we expect anvil.server.call() to throw an anvil.server.AppOfflineError"""
    pass
def reset_session():
    """Reset the current session to prevent further SessionExpiredErrors."""
    pass
def unwrap_capability(capability, scope_pattern):
    """Checks that its first argument is a valid Capability, and that its scope matches the supplied pattern.To match, the scope must: - Be at least as broad as the pattern (ie the same length or shorter)- Contain the same values in the same position as the pattern - unless that position in the pattern is Capability.ANY, which matches any valueReturns a list of matched scope elements, of the same length as the pattern. (If the scope was broader than required, missing elements are set to None.)"""
    pass
