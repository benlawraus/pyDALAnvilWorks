from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container

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


class ContactListFormTemplate(ColumnPanel):
    repeating_panel_2 = RepeatingPanel(**repeating_panel_2)
    data_grid_1 = DataGrid(**data_grid_1)

    def init_components(self, **kwargs):
        pass
