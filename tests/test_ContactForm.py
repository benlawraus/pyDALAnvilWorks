import anvil.users
from anvil import tables
from anvil.tables import app_tables
import anvil.tables.query as q
import tests.pydal_def as mydal
from client_code.ContactForm import ContactForm
from client_code.client_code_functions import generate_contact
from tests.common import generate_contact_instance


class TestContactForm:
    def test_save_contact(self):
        # generate demo user
        mydal.define_tables_of_db()
        user = anvil.users.get_user()

        # generate a demo contact
        contact = generate_contact_instance(user=user)
        # generate form
        c_form = ContactForm(contact=contact)
        # The contact should be manifesting in the form, at moment cannot test data-binding so items
        assert contact['name'] == c_form.text_box_name.text
        assert contact['phone']['number'] == c_form.text_box_phone.text
        assert len(contact['email_list']) == len(c_form.repeating_panel_email.items)
        assert contact['email_list'][0]['address'] == c_form.repeating_panel_email.items[0]['email']
        # lets test the save contact
        c_form.button_save_click()
        # get last contact
        contact_row = app_tables.contact.get(name=contact['name'])
        assert contact_row is not None
        assert c_form.text_box_name.text == contact_row['name']
        # get email record
        email_row = app_tables.email.get(address=contact['email_list'][0]['address'])
        assert c_form.repeating_panel_email.items[0]['email']==email_row['address']