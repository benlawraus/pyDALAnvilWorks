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
    """Get the Facebook access token of the currently-logged-in Facebook user.To log in with Facebook, call facebook.auth.login() from form code."""
    pass
def get_user_email():
    """Get the email address of the currently-logged-in Facebook user.To log in with Facebook, call facebook.auth.login() from form code."""
    pass
def get_user_id():
    """Get the Facebook user ID of the currently-logged-in Facebook user.To log in with Facebook, call facebook.auth.login() from form code."""
    pass
def login():
    """Prompt the user to log in with their Facebook account"""
    pass
