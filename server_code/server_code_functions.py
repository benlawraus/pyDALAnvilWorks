"""Used for pyDALAnvilWorks tests only. Delete."""
import anvil.server
from anvil.tables import app_tables


@anvil.server.callable
def example_1() -> str:
    return "Returned string from function example_1."


@anvil.server.callable
def save_contact(contact_dict):
    phone_row = app_tables.phone.add_row(**contact_dict['phone'])
    email_row = app_tables.email.add_row(**contact_dict['email_list'][0])
    contact_dict['phone'] = phone_row
    contact_dict['email_list'] = [email_row]
    contact_row = app_tables.contact.add_row(**contact_dict)
    return contact_row.get_id()
