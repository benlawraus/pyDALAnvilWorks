try:
  from ._anvil_designer import EmailDisplayFormTemplate
except ImportError:
  from _anvil_designer import EmailDisplayFormTemplate

import anvil.server
import anvil.users
from anvil_extras import navigation


@navigation.register(name="displayemails")
class EmailDisplayForm(EmailDisplayFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    emails=anvil.server.call('get_emails')
    self.repeating_panel_1.items = emails
    # Any code you write here will run when the form opens.
    