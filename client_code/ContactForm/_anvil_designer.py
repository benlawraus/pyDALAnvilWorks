from _anvil_designer.componentsUI.anvil import *

LabelName = dict(
    role = None,
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Name',
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
TextBoxName = dict(
)
LabelPhone = dict(
    role = None,
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Telephone Number',
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
TextBoxPhone = dict(
)
ColumnPanel1 = dict(
    col_widths = '{"NWGMBY":15,"VPHMVV":45,"MDNMFP":15,"LOBHDT":45}',
    parent = Container(),
)
RepeatingPanelEmail = dict(
    role = None,
    tooltip = '',
    border = '',
    foreground = '',
    items = None,
    visible = True,
    spacing_above = 'small',
    spacing_below = 'small',
    item_template = 'EmailItemForm',
    background = '',
    parent = Container(),
)
ButtonSave = dict(
    role = 'primary-color',
    align = 'center',
    tooltip = '',
    border = '',
    enabled = True,
    foreground = '',
    visible = True,
    text = 'Save Contact',
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
ContentPanel = dict(
    col_widths = '{}',
    parent = Container(),
)
class ContactFormTemplate(HtmlTemplate):
    label_name = Label(**LabelName)
    text_box_name = TextBox(**TextBoxName)
    label_phone = Label(**LabelPhone)
    text_box_phone = TextBox(**TextBoxPhone)
    column_panel_1 = ColumnPanel(**ColumnPanel1)
    repeating_panel_email = RepeatingPanel(**RepeatingPanelEmail)
    button_save = Button(**ButtonSave)
    content_panel = ColumnPanel(**ContentPanel)

    # not sure why, but item is not in the official api docs so must add here
    item = dict()

    def init_components(self, **kwargs):
        super().__init__()        
        pass
