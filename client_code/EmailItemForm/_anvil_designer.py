from _anvil_designer.componentsUI.anvil import *

LabelEmail = dict(
    role = None,
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Email',
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
TextBoxEmail = dict(
)
Button1 = dict(
    role = None,
    align = 'center',
    tooltip = '',
    border = '',
    enabled = True,
    foreground = '',
    visible = False,
    text = '',
    font_size = None,
    font = '',
    spacing_above = 'small',
    icon_align = 'left',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    underline = False,
    icon = 'fa:plus',
    parent = Container(),
)
RadioBtnWork = dict(
    role = None,
    selected = False,
    align = 'left',
    tooltip = '',
    border = '',
    enabled = True,
    foreground = '',
    value = 1.0,
    visible = True,
    text = 'Work ',
    font_size = None,
    font = '',
    spacing_above = 'small',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    group_name = 'radioGroup1',
    underline = False,
    parent = Container(),
)
RadioButton2 = dict(
    role = None,
    selected = False,
    align = 'left',
    tooltip = '',
    border = '',
    enabled = True,
    foreground = '',
    value = 2.0,
    visible = True,
    text = 'Home',
    font_size = None,
    font = '',
    spacing_above = 'small',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    group_name = 'radioGroup1',
    underline = False,
    parent = Container(),
)
RadioButton3 = dict(
    role = None,
    selected = False,
    align = 'left',
    tooltip = '',
    border = '',
    enabled = True,
    foreground = '',
    value = 4.0,
    visible = True,
    text = 'Other',
    font_size = None,
    font = '',
    spacing_above = 'small',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    group_name = 'radioGroup1',
    underline = False,
    parent = Container(),
)
ColumnPanel1 = dict(
    col_widths = '{}',
    parent = Container(),
)
class EmailItemFormTemplate(ColumnPanel):
    label_email = Label(**LabelEmail)
    text_box_email = TextBox(**TextBoxEmail)
    button_1 = Button(**Button1)
    radio_btn_work = RadioButton(**RadioBtnWork)
    radio_button_2 = RadioButton(**RadioButton2)
    radio_button_3 = RadioButton(**RadioButton3)
    column_panel_1 = ColumnPanel(**ColumnPanel1)

    def init_components(self, **kwargs):
        super().__init__()        
        pass
