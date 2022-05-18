from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

repeating_panel_2 = dict(
    role='null',
    tooltip='',
    border='',
    foreground='',
    items='null',
    visible='true',
    spacing_above='none',
    spacing_below='none',
    item_template='ContactDisplayForm',
    background='',
    parent=Container(),
)
data_grid_1 = dict(
    role='null',
    columns=[{'id': 'IZKCYB', 'title': 'Name', 'data_key': 'name'}, {'id': 'VBCVHP', 'title': 'Phone', 'data_key': 'phone'}],
    auto_header='true',
    tooltip='',
    border='',
    foreground='',
    rows_per_page='20',
    visible='true',
    wrap_on='never',
    show_page_controls='true',
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
