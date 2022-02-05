from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

label_email = dict(
    role=None,
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Email',
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
text_box_email = dict(
)
button_1 = dict(
    role=None,
    align='center',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    visible=False,
    text='',
    font_size=None,
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='fa:plus',
    parent=Container(),
)
radio_btn_work = dict(
    role=None,
    selected=False,
    align='left',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    value=1.0,
    visible=True,
    text='Work ',
    font_size=None,
    font='',
    spacing_above='small',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    group_name='radioGroup1',
    underline=False,
    parent=Container(),
)
radio_button_2 = dict(
    role=None,
    selected=False,
    align='left',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    value=2.0,
    visible=True,
    text='Home',
    font_size=None,
    font='',
    spacing_above='small',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    group_name='radioGroup1',
    underline=False,
    parent=Container(),
)
radio_button_3 = dict(
    role=None,
    selected=False,
    align='left',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    value=4.0,
    visible=True,
    text='Other',
    font_size=None,
    font='',
    spacing_above='small',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    group_name='radioGroup1',
    underline=False,
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
