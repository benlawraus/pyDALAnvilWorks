from _anvil_designer.componentsUI.anvil import *

Label1 = dict(
    role = 'headline',
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Emails',
    font_size = None,
    font = '',
    spacing_above = 'small',
    icon_align = 'left',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    underline = False,
    icon = '',
    parent = Container(),
)
RepeatingPanel1 = dict(
    spacing_above = 'none',
    spacing_below = 'none',
    item_template = 'EmailDisplayForm.RowTemplate1',
    parent = Container(),
)
DataGrid1 = dict(
    role = None,
    columns = [{'id': 'TFKBUP', 'title': 'Address', 'data_key': 'address'}, {'id': 'ZBSADL', 'title': 'Place', 'data_key': 'place'}, {'id': 'QJRUIN', 'title': 'Created', 'data_key': 'created_on'}],
    auto_header = True,
    tooltip = '',
    border = '',
    foreground = '',
    rows_per_page = 20.0,
    visible = True,
    wrap_on = 'never',
    show_page_controls = True,
    spacing_above = 'small',
    spacing_below = 'small',
    background = '',
    parent = Container(),
)
class EmailDisplayFormTemplate(ColumnPanel):
    label_1 = Label(**Label1)
    repeating_panel_1 = RepeatingPanel(**RepeatingPanel1)
    data_grid_1 = DataGrid(**DataGrid1)

    def init_components(self, **kwargs):
        super().__init__()        
        pass