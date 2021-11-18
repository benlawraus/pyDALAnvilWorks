"""Used for pyDALAnvilWorks tests only. Delete."""
import anvil.server
from datetime import datetime


def example_A():
    text = anvil.server.call("example_1")
    return text


def generate_contact(user=None):
    right_now = datetime.now().replace(microsecond=0)
    phone_dict = dict(number="(510) 666-8888",
                      created_by=user,
                      created_on=right_now)
    email_dict = dict(address="rex@exopotamia.com",
                      created_by=user,
                      created_on=right_now)
    contact_dict = dict(
        name="Rex Eagle",
        phone=phone_dict,
        email_list=[email_dict],
        age=6,
        created_by=user,
        created_on=right_now)
    return contact_dict


def save_contact():
    user = anvil.users.get_user()
    contact_dict = generate_contact(user)
    contact_dict['id'] = anvil.server.call("save_contact", contact_dict)
    return user, contact_dict['id']
