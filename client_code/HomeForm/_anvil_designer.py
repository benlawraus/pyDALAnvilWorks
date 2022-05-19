from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

link_signin = dict(
    role=None,
    url='',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Sign In',
    font_size=None,
    wrap_on='mobile',
    font='',
    col_spacing='medium',
    spacing_above='small',
    icon_align='left',
    col_widths='',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
link_login = dict(
    role=None,
    url='',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Log In',
    font_size=None,
    wrap_on='mobile',
    font='',
    col_spacing='medium',
    spacing_above='small',
    icon_align='left',
    col_widths='',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
navbar_links = dict(
)
label_title = dict(
    role=None,
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='pyDAL anvil.works',
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
rich_text_1 = dict(
    role=None,
    align='left',
    tooltip='',
    enable_slots=True,
    border='',
    foreground='',
    visible=True,
    font_size=None,
    content='Welcome to the test app. This is the companion app to the GitHub repo [pyDALAnvilWorks](https://github.com/benlawraus/pyDALAnvilWorks).',
    font='',
    spacing_above='small',
    spacing_below='small',
    data=None,
    background='',
    format='markdown',
    parent=Container(),
)
content_panel = dict(
    col_widths='{}',
    parent=Container(),
)
menu_panel = dict(
)


@dataclass
class HomeFormTemplate(HtmlTemplate):
    link_signin: Link = field(default_factory=lambda: Link(**link_signin))
    link_login: Link = field(default_factory=lambda: Link(**link_login))
    navbar_links: FlowPanel = field(default_factory=lambda: FlowPanel(**navbar_links))
    label_title: Label = field(default_factory=lambda: Label(**label_title))
    rich_text_1: RichText = field(default_factory=lambda: RichText(**rich_text_1))
    content_panel: ColumnPanel = field(default_factory=lambda: ColumnPanel(**content_panel))
    menu_panel: ColumnPanel = field(default_factory=lambda: ColumnPanel(**menu_panel))

    def init_components(self, **kwargs):
        HomeFormTemplate.__init__(self)
