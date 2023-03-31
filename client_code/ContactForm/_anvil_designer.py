from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict
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
databindings = [
]

class ContactFormTemplate(HtmlTemplate):
    def __init__(self, **properties):
        super(ContactFormTemplate, self).__init__()
        self.label_name = Label(**label_name)
        self.text_box_name = TextBox(**text_box_name)
        self.label_phone = Label(**label_phone)
        self.text_box_phone = TextBox(**text_box_phone)
        self.column_panel_1 = ColumnPanel(**column_panel_1)
        self.repeating_panel_email = RepeatingPanel(**repeating_panel_email)
        self.button_save = Button(**button_save)
        self.email_display_form = EmailDisplayForm(**email_display_form)
        self.column_panel_email_lists = ColumnPanel(**column_panel_email_lists)
        self.content_panel = ColumnPanel(**content_panel)
        self._bindings = databindings
        self._item = ClassDict()

        if properties.get('item', None) is not None:
            self.item = properties['item']

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        ContactFormTemplate.__init__(self, **properties)
