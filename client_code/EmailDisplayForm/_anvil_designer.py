from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

label_1 = dict(
    role='headline',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible='true',
    text='Emails',
    font_size='null',
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic='false',
    background='',
    bold='false',
    underline='false',
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
    role='null',
    columns=[{'id': 'TFKBUP', 'title': 'Address', 'data_key': 'address'}, {'id': 'ZBSADL', 'title': 'Place', 'data_key': 'place'}, {'id': 'QJRUIN', 'title': 'Created', 'data_key': 'created_on'}],
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
class EmailDisplayFormTemplate(ColumnPanel):
    label_1: Label = field(default_factory=lambda: Label(**label_1))
    repeating_panel_1: RepeatingPanel = field(default_factory=lambda: RepeatingPanel(**repeating_panel_1))
    data_grid_1: DataGrid = field(default_factory=lambda: DataGrid(**data_grid_1))

    def init_components(self, **kwargs):
        EmailDisplayFormTemplate.__init__(self)
