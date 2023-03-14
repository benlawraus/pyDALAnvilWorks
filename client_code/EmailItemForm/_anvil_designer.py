from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter

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
databindings = [
    dict( item='self.item["email"]', element='text_box_email.text', writeback=True,),
]

class EmailItemFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(EmailItemFormTemplate, self).__init__()
        self.label_email = Label(**label_email)
        self.text_box_email = TextBox(**text_box_email)
        self.button_1 = Button(**button_1)
        self.radio_btn_work = RadioButton(**radio_btn_work)
        self.radio_button_2 = RadioButton(**radio_button_2)
        self.radio_button_3 = RadioButton(**radio_button_3)
        self.column_panel_1 = ColumnPanel(**column_panel_1)
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
        EmailItemFormTemplate.__init__(self, **properties)
