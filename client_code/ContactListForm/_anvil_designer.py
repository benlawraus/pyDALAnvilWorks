from anvil import *
from _anvil_designer.common_structures import binding_property

repeating_panel_2 = dict(
    role=None,
    tooltip='',
    border='',
    foreground='',
    items=None,
    visible=True,
    spacing_above='none',
    spacing_below='none',
    item_template='ContactDisplayForm',
    background='',
    parent=Container(),
)
data_grid_1 = dict(
    role=None,
    columns=[{'id': 'IZKCYB', 'title': 'Name', 'data_key': 'name'}, {'id': 'VBCVHP', 'title': 'Phone', 'data_key': 'phone'}],
    auto_header=True,
    tooltip='',
    border='',
    foreground='',
    rows_per_page=20.0,
    visible=True,
    wrap_on='never',
    show_page_controls=True,
    spacing_above='small',
    spacing_below='small',
    background='',
    parent=Container(),
)
databindings = [
]

class ContactListFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(ContactListFormTemplate, self).__init__()
        self.repeating_panel_2 = RepeatingPanel(**repeating_panel_2)
        self.data_grid_1 = DataGrid(**data_grid_1)
        self.__bindings = databindings@property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        ContactListFormTemplate.__init__(self, **properties)
