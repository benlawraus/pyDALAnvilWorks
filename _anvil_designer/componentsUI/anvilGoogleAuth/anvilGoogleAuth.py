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
def get_user_access_token():
    """Get the secret access token of the currently-logged-in Google user, for use with the Google REST API. Requires this app to have its own Google client ID and secret."""
    pass
def get_user_email():
    """Get the email address of the currently-logged-in Google user.To log in with Google, call anvil.google.auth.login() from form code."""
    pass
def get_user_refresh_token():
    """Get the secret refresh token of the currently-logged-in Google user, for use with the Google REST API. Requires this app to have its own Google client ID and secret."""
    pass
def login(additional_scopes):
    """Prompt the user to log in with their Google account.If you have specified your own client ID in the Google Service configuration, you can specify additional OAuth scopes for use with the Google REST API."""
    pass
def refresh_access_token(refresh_token):
    """Get a new access token from a refresh token you have saved, for use with the Google REST API. Requires this app to have its own Google client ID and secret."""
    pass
