from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

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


@dataclass
class ContactListFormTemplate(ColumnPanel):
    repeating_panel_2: RepeatingPanel = field(default_factory=lambda: RepeatingPanel(**repeating_panel_2))
    data_grid_1: DataGrid = field(default_factory=lambda: DataGrid(**data_grid_1))

    def init_components(self, **kwargs):
        ContactListFormTemplate.__init__(self)
