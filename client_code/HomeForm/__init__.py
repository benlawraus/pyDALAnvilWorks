from ._anvil_designer import HomeFormTemplate
import anvil.users
import anvil.server
from anvil_extras import navigation
from ..ContactListForm import ContactListForm

menu = [
  {"text": "Add Contact", "target": "addcontact"},
  {"text": "Display Emails", "target": "displayemails"},
]


class HomeForm(HomeFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
          
        self.advanced_mode = False
        navigation.build_menu(self.menu_panel, menu)
        self.init_components(**properties)
        user = anvil.users.get_user(allow_remembered=True)
        if user is None:
          self.link_login_click()
        self.contact_form = ContactListForm()
  
        self.content_panel.add_component(self.contact_form,full_width_row=True)
        if len(self.contact_form.contacts)==0:
          self.contact_form.repeating_panel_2.items = [{'name':'hello, you have no contacts.',
                           'uid':6, 
                           'phone':''}]




    def link_signin_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.users.signup_with_form(allow_cancel=True)
        pass

    def link_login_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.users.login_with_form(allow_cancel=True,show_signup_option=True)
        pass
