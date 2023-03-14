from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter

label_1 = dict(
    role='headline',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Emails',
    font_size=None,
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
repeating_panel_1 = dict(
    spacing_above='none',
    spacing_below='none',
    item_template='EmailDisplayForm.RowTemplate1',
    parent=Container(),
)
data_grid_1 = dict(
    role=None,
    columns=[{'id': 'TFKBUP', 'title': 'Address', 'data_key': 'address'}, {'id': 'ZBSADL', 'title': 'Place', 'data_key': 'place'}, {'id': 'QJRUIN', 'title': 'Created', 'data_key': 'created_on'}],
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

class EmailDisplayFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(EmailDisplayFormTemplate, self).__init__()
        self.label_1 = Label(**label_1)
        self.repeating_panel_1 = RepeatingPanel(**repeating_panel_1)
        self.data_grid_1 = DataGrid(**data_grid_1)
        self._bindings = databindings
        self._item = {}

        self._item = {}

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        EmailDisplayFormTemplate.__init__(self, **properties)
