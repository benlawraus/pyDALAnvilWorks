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
def get_user_attributes():
    """Get the user attributes of the currently-logged-in SAML user.The exact attributes available will depend on your SAML Identity Provider."""
    pass
def get_user_email():
    """Get the email address of the currently-logged-in SAML user.To log in with SAML, call anvil.saml.auth.login() from form code."""
    pass
def login():
    """Prompt the user to log in via SAML"""
    pass
