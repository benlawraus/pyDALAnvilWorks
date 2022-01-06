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
def add_mfa_method(password, mfa_method, clear_existing=False):
    """Add an MFA method to the current user by passing the user’s password and the mfa method, optionally clearing all existing methods."""
    pass
def configure_mfa_with_form(allow_cancel=False):
    """Display a form for the user to configure 2-factor authentication.allow_cancel: if True, the signup form has a Cancel button that the user can use to dismiss the form."""
    pass
def create_fido_mfa_method(email_address):
    """Generate a WebAuthn challenge that can be used to register a new hardware token for two-factor authentication."""
    pass
def generate_totp_secret(email_address):
    """Generate a TOTP secret that can be added as two-factor authentication for the current user."""
    pass
def get_available_mfa_types(email_address, password):
    """Get the available MFA types for the given user by passing their email and password."""
    pass
def get_fido_mfa_login(email_address, password):
    """Generate a WebAuthn challenge that the given user can use to log in with a previously registered hardware token."""
    pass
def get_totp_mfa_login(code):
    """Get an MFA login object representing a TOTP login code. This can be passed to the login_with_email function as the mfa argument."""
    pass
def mfa_login_with_form(email_address, password):
    """Display a form to collect two-factor authentication credentials from the user currently logging in by passing the function their email and password."""
    pass
def validate_totp_code(mfa_method, code):
    """Validate the given TOTP code against the given MFA method from a User row."""
    pass
