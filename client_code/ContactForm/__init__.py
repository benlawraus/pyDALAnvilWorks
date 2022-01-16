import anvil.users
from ._anvil_designer import ContactFormTemplate

import anvil.server
from anvil_extras import navigation


@navigation.register(name="addcontact")
class ContactForm(ContactFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.contact = properties.get('contact', dict())
        if self.contact.get('email_list', None) is None:
            self.contact['email_list'] = [dict(address='', place=1)]
        self.convert_to_items()
        # Any code you write here will run when the form opens.


    def convert_to_items(self):
        self.text_box_name.text = self.contact.get('name', None)
        em_items = []  # type: list[dict]
        for em in self.contact.get('email_list', []):  # type: dict
            em_items.append({'email': em['address'], 'place': em['place']})
        self.repeating_panel_email.items = em_items
        self.text_box_phone.text = self.contact.get('phone', dict()).get('number', None)

    def convert_from_items(self):
        self.contact['name'] = self.text_box_name.text
        em_list = []  # type: list[dict]
        for em in self.repeating_panel_email.items:
            em_list.append({'address': em['email'], 'place': em['place']})
        self.contact['email_list'] = em_list
        self.contact['phone'] = {'number': self.text_box_phone.text}

    def button_save_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.convert_from_items()
        contact_id = anvil.server.call('save_contact', self.contact)
