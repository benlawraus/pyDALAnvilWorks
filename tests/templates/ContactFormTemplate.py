
class GenericTemplate:
    def init_components(self, **kwargs):
        super().__init__()        
        pass

class ContentPanel():
    visible=True
    wrap_on='mobile'
    background='#ff0000'
    bold=False
    border='1px solid #888888'
    col_spacing='medium'
    col_widths=''
    foreground='#ff0000'
    role='default'
    spacing_above='small'
    spacing_below='small'
    tag=''
    tooltip=''

class LabelName():
    role=None
    align='left'
    tooltip=''
    border=''
    foreground=''
    visible=True
    text='Name'
    font_size=None
    font=''
    spacing_above='small'
    icon_align='left'
    spacing_below='small'
    italic=False
    background=''
    bold=False
    underline=False
    icon=''

class TextBoxName():
    enabled=True
    text=''
    visible=True
    align='left'
    background='#ff0000'
    bold=False
    border='1px solid #888888'
    font='Arial'
    font_size=16
    foreground='#ff0000'
    hide_text=False
    italic=False
    placeholder='Enter text here'
    role='default'
    spacing_above='small'
    spacing_below='small'
    tag=''
    tooltip=''
    type='text'
    underline=False

class LabelPhone():
    role=None
    align='left'
    tooltip=''
    border=''
    foreground=''
    visible=True
    text='Telephone Number'
    font_size=None
    font=''
    spacing_above='small'
    icon_align='left'
    spacing_below='small'
    italic=False
    background=''
    bold=False
    underline=False
    icon=''

class TextBoxPhone():
    enabled=True
    text=''
    visible=True
    align='left'
    background='#ff0000'
    bold=False
    border='1px solid #888888'
    font='Arial'
    font_size=16
    foreground='#ff0000'
    hide_text=False
    italic=False
    placeholder='Enter text here'
    role='default'
    spacing_above='small'
    spacing_below='small'
    tag=''
    tooltip=''
    type='text'
    underline=False

class ColumnPanel1():
    visible=True
    wrap_on='mobile'
    background='#ff0000'
    bold=False
    border='1px solid #888888'
    col_spacing='medium'
    col_widths=''
    foreground='#ff0000'
    role='default'
    spacing_above='small'
    spacing_below='small'
    tag=''
    tooltip=''

class RepeatingPanelEmail():
    role=None
    tooltip=''
    border=''
    foreground=''
    items=None
    visible=True
    spacing_above='small'
    spacing_below='small'
    item_template='EmailItemForm'
    background=''

class ButtonSave():
    role='primary-color'
    align='center'
    tooltip=''
    border=''
    enabled=True
    foreground=''
    visible=True
    text='Save Contact'
    font_size=None
    font=''
    spacing_above='small'
    icon_align='left'
    spacing_below='small'
    italic=False
    background=''
    bold=False
    underline=False
    icon=''

class ContactFormTemplate(GenericTemplate):
    content_panel=ContentPanel()
    column_panel_1=ColumnPanel1()
    label_name=LabelName()
    text_box_name=TextBoxName()
    label_phone=LabelPhone()
    text_box_phone=TextBoxPhone()
    repeating_panel_email=RepeatingPanelEmail()
    button_save=ButtonSave()
