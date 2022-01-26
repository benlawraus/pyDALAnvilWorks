from ._anvil_designer import ContactDisplayFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ContactDisplayForm(ContactDisplayFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run when the form opens.

  def link_name_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.parent.raise_event("x-contact_name",uid=self.item['uid'])
    pass

