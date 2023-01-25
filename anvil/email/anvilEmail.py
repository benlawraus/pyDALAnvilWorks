from typing import List, Dict, Union, Optional
from unittest.mock import Mock

from anvil import Media

# classes
DeliveryFailure = Mock()
SendFailure = Mock()


def handle_message(func=lambda f: f):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def send(to:Union[str,List[str]]=None, cc:Union[str,List[str]]=None, bcc:Union[str,List[str]]=None, from_address="no-reply", from_name:Optional[str]=None, subject=None, text=None, html=None,
         attachments:List[Media]=None, inline_attachments=Dict[str,Media]):
    """Send an email.
    For testing purposes the email is the return."""
    return dict(to=to, cc=cc, bcc=bcc, from_address=from_address, from_name=from_name, subject=subject,
                text=text, html=html, attachments=attachments, inline_attachments=inline_attachments)
