from unittest.mock import Mock

# classes
DeliveryFailure = Mock()
SendFailure = Mock()


def handle_message(func=lambda f: f):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def send(to=None, cc=None, bcc=None, from_address="no-reply", from_name=None, subject=None, text=None, html=None,
         attachments=None, inline_attachments=None):
    """Send an email.
    For testing purposes the email is the return."""
    return dict(to=to, cc=cc, bcc=bcc, from_address=from_address, from_name=from_name, subject=subject,
                text=text, html=html, attachments=attachments, inline_attachments=inline_attachments)
