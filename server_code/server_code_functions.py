import anvil.users
"""Used for pyDALAnvilWorks tests only. Delete."""
from _datetime import datetime, timezone
from itertools import chain

import anvil
import anvil.server
from anvil.tables import app_tables


@anvil.server.callable
def example_1() -> str:
    return "Returned string from function example_1."


@anvil.server.callable
def save_contact(contact_dict):
    # add user and time to contact, email and phone records
    user = anvil.users.get_user()
    now_time = datetime.now(tz=timezone.utc)
    for var in chain.from_iterable(((contact_dict, contact_dict['phone']), contact_dict['email_list'])):
        var['created_by'] = user
        var['created_on'] = now_time

    phone_row = app_tables.phone.add_row(**contact_dict['phone'])
    email_rows = []
    for em in contact_dict['email_list']:
        email_rows.append(app_tables.email.add_row(**em))
    contact_dict['phone'] = phone_row
    contact_dict['email_list'] = email_rows

    contact_row = app_tables.contact.add_row(**contact_dict)
    return contact_row.get_id()

@anvil.server.callable
def get_emails():
  user= anvil.users.get_user()
  email_rows = app_tables.email.search(created_by=user)
  return email_rows