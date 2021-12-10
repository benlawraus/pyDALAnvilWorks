import anvil.users
"""Used for pyDALAnvilWorks tests only. Delete."""
import random
import string

import anvil.server
from datetime import datetime

from tests.common import phone_generator, email_generator, name_generator


def example_A():
    text = anvil.server.call("example_1")
    return text


def generate_contact(user=None):
    right_now = datetime.now().replace(microsecond=0)
    phone_dict = dict(number=phone_generator(),
                      created_by=user,
                      created_on=right_now)
    email_dict = dict(address=email_generator(),
                      place=1,
                      created_by=user,
                      created_on=right_now)
    contact_dict = dict(
        name=name_generator(),
        phone=phone_dict,
        email_list=[email_dict],
        age=6,
        created_by=user,
        created_on=right_now)
    return contact_dict


def save_contact_from_client():
    user = anvil.users.get_user()
    contact_dict_client = generate_contact(user)
    contact_dict_client['id'] = anvil.server.call("save_contact", contact_dict_client)
    return user, contact_dict_client

