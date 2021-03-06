from ._anvil_designer import ContactListFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ContactForm import ContactForm

class ContactListForm(ContactListFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_2.add_event_handler("x-contact_name",self.goto_contact)
    self.contacts = anvil.server.call('get_contacts')
    self.contact_items = [{'name':contact['name'],
                           'uid':contact.get_id(), 
                           'phone':contact['phone']['number']}
                     for contact in self.contacts]
    self.repeating_panel_2.items = self.contact_items
    for c in self.contact_items:
      print(c['name'],c['phone'])


  def goto_contact(self, **event_args):
    uid = event_args.get("uid",None)
    contact_one = [cont for cont in self.contacts if cont.get_id()==uid]
    # convert row into dict
    contact = dict(contact_one[0])
    em_list = contact.get('email_list',[])
    contact['email_list'] = []
    if len(em_list)>0:
      for em in em_list:
        contact['email_list'].append(dict(em))
    contact['phone'] = dict(contact['phone'])
    if uid:
      contact_form = ContactForm(contact=contact)
      self.parent.add_component(contact_form)
      
      
