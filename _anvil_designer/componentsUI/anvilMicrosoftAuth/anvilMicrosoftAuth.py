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
    """Get the secret access token of the currently-logged-in Microsoft user, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret."""
    pass
def get_user_email():
    """Get the email address of the currently-logged-in Microsoft user.To log in with Microsoft, call anvil_microsoft.auth.login() from form code."""
    pass
def get_user_refresh_token():
    """Get the secret refresh token of the currently-logged-in Microsoft user, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret."""
    pass
def login():
    """Prompt the user to log in with their Microsoft account"""
    pass
def refresh_access_token(refresh_token):
    """Get a new access token from a refresh token you have saved, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret."""
    pass
