from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field
from ..EmailDisplayForm import EmailDisplayForm

label_name = dict(
    role=None,
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Name',
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
text_box_name = dict(
)
label_phone = dict(
    role=None,
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Telephone Number',
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
text_box_phone = dict(
)
column_panel_1 = dict(
    col_widths='{"NWGMBY":15,"VPHMVV":45,"MDNMFP":15,"LOBHDT":45}',
    parent=Container(),
)
repeating_panel_email = dict(
    role=None,
    tooltip='',
    border='',
    foreground='',
    items=None,
    visible=True,
    spacing_above='small',
    spacing_below='small',
    item_template='EmailItemForm',
    background='',
    parent=Container(),
)
button_save = dict(
    role='primary-color',
    align='center',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    visible=True,
    text='Save Contact',
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
email_display_form = dict(
)
column_panel_email_lists = dict(
    col_widths='{}',
    parent=Container(),
)
content_panel = dict(
    col_widths='{}',
    parent=Container(),
)


@dataclass
class ContactFormTemplate(HtmlTemplate):
    label_name: Label = field(default_factory=lambda: Label(**label_name))
    text_box_name: TextBox = field(default_factory=lambda: TextBox(**text_box_name))
    label_phone: Label = field(default_factory=lambda: Label(**label_phone))
    text_box_phone: TextBox = field(default_factory=lambda: TextBox(**text_box_phone))
    column_panel_1: ColumnPanel = field(default_factory=lambda: ColumnPanel(**column_panel_1))
    repeating_panel_email: RepeatingPanel = field(default_factory=lambda: RepeatingPanel(**repeating_panel_email))
    button_save: Button = field(default_factory=lambda: Button(**button_save))
    email_display_form: EmailDisplayForm = field(default_factory=lambda: EmailDisplayForm(**email_display_form))
    column_panel_email_lists: ColumnPanel = field(default_factory=lambda: ColumnPanel(**column_panel_email_lists))
    content_panel: ColumnPanel = field(default_factory=lambda: ColumnPanel(**content_panel))

    def init_components(self, **kwargs):
        ContactFormTemplate.__init__(self)
