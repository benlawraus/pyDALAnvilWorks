from dataclasses import dataclass, field


@dataclass
class DeliveryFailure():
    pass


@dataclass
class SendFailure():
    pass


def send(to=None, cc=None, bcc=None, from_address="no-reply", from_name=None, subject=None, text=None, html=None,
         attachments=None, inline_attachments=None):
    """Send an email"""
    pass
