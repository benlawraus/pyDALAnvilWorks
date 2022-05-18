from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

label_email = dict(
    role='null',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible='true',
    text='Email',
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
text_box_email = dict(
)
button_1 = dict(
    role='null',
    align='center',
    tooltip='',
    border='',
    enabled='true',
    foreground='',
    visible='false',
    text='',
    font_size='null',
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic='false',
    background='',
    bold='false',
    underline='false',
    icon='fa:plus',
    parent=Container(),
)
radio_btn_work = dict(
    role='null',
    selected='false',
    align='left',
    tooltip='',
    border='',
    enabled='true',
    foreground='',
    value='1',
    visible='true',
    text='Work ',
    font_size='null',
    font='',
    spacing_above='small',
    spacing_below='small',
    italic='false',
    background='',
    bold='false',
    group_name='radioGroup1',
    underline='false',
    parent=Container(),
)
radio_button_2 = dict(
    role='null',
    selected='false',
    align='left',
    tooltip='',
    border='',
    enabled='true',
    foreground='',
    value='2',
    visible='true',
    text='Home',
    font_size='null',
    font='',
    spacing_above='small',
    spacing_below='small',
    italic='false',
    background='',
    bold='false',
    group_name='radioGroup1',
    underline='false',
    parent=Container(),
)
radio_button_3 = dict(
    role='null',
    selected='false',
    align='left',
    tooltip='',
    border='',
    enabled='true',
    foreground='',
    value='4',
    visible='true',
    text='Other',
    font_size='null',
    font='',
    spacing_above='small',
    spacing_below='small',
    italic='false',
    background='',
    bold='false',
    group_name='radioGroup1',
    underline='false',
    parent=Container(),
)
column_panel_1 = dict(
    col_widths='{}',
    parent=Container(),
)


@dataclass
class EmailItemFormTemplate(ColumnPanel):
    label_email: Label = field(default_factory=lambda: Label(**label_email))
    text_box_email: TextBox = field(default_factory=lambda: TextBox(**text_box_email))
    button_1: Button = field(default_factory=lambda: Button(**button_1))
    radio_btn_work: RadioButton = field(default_factory=lambda: RadioButton(**radio_btn_work))
    radio_button_2: RadioButton = field(default_factory=lambda: RadioButton(**radio_button_2))
    radio_button_3: RadioButton = field(default_factory=lambda: RadioButton(**radio_button_3))
    column_panel_1: ColumnPanel = field(default_factory=lambda: ColumnPanel(**column_panel_1))

    def init_components(self, **kwargs):
        EmailItemFormTemplate.__init__(self)
