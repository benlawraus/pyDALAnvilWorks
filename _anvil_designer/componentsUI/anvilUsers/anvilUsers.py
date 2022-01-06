from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from ..anvil import component as anvil

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
class AccountIsNotEnabled():
	pass

@dataclass
class AuthenticationFailed():
	pass

@dataclass
class EmailNotConfirmed():
	pass

@dataclass
class MFARequired():
	pass

@dataclass
class PasswordNotAcceptable():
	pass

@dataclass
class PasswordResetRequested():
	pass

@dataclass
class TooManyPasswordFailures():
	pass

@dataclass
class UserExists():
	pass
def change_password_with_form(require_old_password=True):
    """Display a form allowing the current user to reset their password."""
    pass
def configure_account_with_form():
    """Display a form allowing the current user to configure their account. The form contains links for password reset and two-factor authentication configuration."""
    pass
def force_login(user_row, remember=False):
    """Set the specified user object (a row from a Data Table) as the current logged-in user. It must be a row from the users table. By default, login status is not remembered between sessions."""
    pass
def get_user(allow_remembered=True):
    """Get the row from the users table that corresponds to the currently logged-in user. If allow_remembered is true (the default), the user may have logged in in a previous session. Returns None if no user is logged in."""
    pass
def login_with_email(email, password, remember=False):
    """Log in with the specified email address and password. Raises anvil.users.AuthenticationFailed exception if the login failed.By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def login_with_facebook(additional_scopes, remember=False):
    """Log in with a Facebook account. Prompts the user to authenticate with Facebook, then logs in with their Facebook email address (if that user exists). Returns None if the login was cancelled or we have no record of this user.additional_scopes: If supplied, these are passed on to anvil.facebook.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def login_with_form(show_signup_option=True, remember_by_default=True, allow_remembered=True, allow_cancel=False):
    """Display a login form and allow user to log in. Returns user object if logged in, or None if cancelled.show_signup_option: if True, the form will also show the option to sign up for a new account.remember_by_default: if True, the ‘remember me’ checkbox will be enabled by default.allow_remembered: if False, users with remembered login status will still be required to log in.allow_cancel: if True, the login form has a Cancel button that the user can use to dismiss the form."""
    pass
def login_with_google(additional_scopes, remember=False):
    """Log in with a Google account. Prompts the user to authenticate with Google, then logs in with their Google email address (if that user exists). Returns None if the login was cancelled or we have no record of this user.additional_scopes: If supplied, these are passed on to anvil.google.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def login_with_microsoft(additional_scopes, remember=False):
    """Log in with a Microsoft account. Prompts the user to authenticate with Microsoft, then logs in with their Microsoft email address (if that user exists). Returns None if the login was cancelled or we have no record of this user.additional_scopes: If supplied, these are passed on to anvil.microsoft.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def login_with_saml(remember=False):
    """Log in via a SAML Identity Provider. Prompts the user to authenticate with SAML, then logs in with their email address (if that user exists). Returns None if the login was cancelled or we have no record of this user.By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def logout():
    """Forget the current logged-in user"""
    pass
def reset_password(old_password, new_password):
    """Reset the password for the current user"""
    pass
def send_mfa_reset_email(email_address):
    """Send a two-factor authentication reset email to the specified user."""
    pass
def send_password_reset_email(email_address):
    """Send a password-reset email to the specified user"""
    pass
def send_token_login_email(email_address):
    """Send a login link email to the specified user"""
    pass
def signup_with_email(email, password, remember=False):
    """Sign up for a new account with the specified email address and password. Raises anvil.users.UserExists if an account is already registered with this email address.By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def signup_with_facebook(additional_scopes, remember=False):
    """Sign up for a new account with the email address associated with the user’s Facebook account. Prompts the user to authenticate with Facebook, then registers a new user with that email address. Raises anvil.users.UserExists if this email address is already registered; returns new user or None if cancelled.additional_scopes: If supplied, these are passed on to anvil.facebook.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def signup_with_form(remember_by_default=True, allow_cancel=False):
    """Display a sign-up form allowing a user to create a new account. Returns the new user object, or None if cancelled.remember_by_default: if True, the ‘remember me’ checkbox will be enabled by default.allow_cancel: if True, the signup form has a Cancel button that the user can use to dismiss the form."""
    pass
def signup_with_google(additional_scopes, remember=False):
    """Sign up for a new account with the email address associated with the user’s Google account. Prompts the user to authenticate with Google, then registers a new user with that email address. Raises anvil.users.UserExists if this email address is already registered; returns new user or None if cancelled.additional_scopes: If supplied, these are passed on to anvil.google.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def signup_with_microsoft(additional_scopes, remember=False):
    """Sign up for a new account with the email address associated with the user’s Microsoft account. Prompts the user to authenticate with Microsoft, then registers a new user with that email address. Raises anvil.users.UserExists if this email address is already registered; returns new user or None if cancelled.additional_scopes: If supplied, these are passed on to anvil.microsoft.auth.login().By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
def signup_with_saml(remember=False):
    """Sign up for a new account with the email address associated with the user’s SAML account. Prompts the user to authenticate via SAML, then registers a new user with that email address. Raises anvil.users.UserExists if this email address is already registered; returns new user or None if cancelled.By default, login status is not remembered between sessions; set remember=True to remember login status."""
    pass
