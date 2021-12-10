
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

class Label1():
    role='headline'
    align='left'
    tooltip=''
    border=''
    foreground=''
    visible=True
    text='Emails'
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

class RepeatingPanel1():
    spacing_above='none'
    spacing_below='none'
    item_template='EmailDisplayForm.RowTemplate1'

class DataGrid1():
    role=None
    columns=[{'id': 'TFKBUP', 'title': 'Address', 'data_key': 'address'}, {'id': 'ZBSADL', 'title': 'Place', 'data_key': 'place'}, {'id': 'QJRUIN', 'title': 'Created', 'data_key': 'created_on'}]
    auto_header=True
    tooltip=''
    border=''
    foreground=''
    rows_per_page=20.0
    visible=True
    wrap_on='never'
    show_page_controls=True
    spacing_above='small'
    spacing_below='small'
    background=''

class EmailDisplayFormTemplate(GenericTemplate):
    label_1=Label1()
    data_grid_1=DataGrid1()
    repeating_panel_1=RepeatingPanel1()
