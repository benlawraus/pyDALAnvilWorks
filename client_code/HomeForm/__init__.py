from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ContactForm import ContactForm


class HomeForm(HomeFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        contact = dict(name="Rex Eagle")
        self.add_component(ContactForm(contact=contact))

    def link_signin_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def link_login_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass
