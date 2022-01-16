from _anvil_designer.componentsUI.anvil import *

LinkSignin = dict(
    role = None,
    url = '',
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Sign In',
    font_size = None,
    wrap_on = 'mobile',
    font = '',
    col_spacing = 'medium',
    spacing_above = 'small',
    icon_align = 'left',
    col_widths = '',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    underline = False,
    icon = '',
    parent = Container(),
)
LinkLogin = dict(
    role = None,
    url = '',
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'Log In',
    font_size = None,
    wrap_on = 'mobile',
    font = '',
    col_spacing = 'medium',
    spacing_above = 'small',
    icon_align = 'left',
    col_widths = '',
    spacing_below = 'small',
    italic = False,
    background = '',
    bold = False,
    underline = False,
    icon = '',
    parent = Container(),
)
NavbarLinks = dict(
)
LabelTitle = dict(
    role = None,
    align = 'left',
    tooltip = '',
    border = '',
    foreground = '',
    visible = True,
    text = 'pyDAL anvil.works',
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
RichText1 = dict(
    role = None,
    align = 'left',
    tooltip = '',
    enable_slots = True,
    border = '',
    foreground = '',
    visible = True,
    font_size = None,
    content = 'Welcome to the test app. This is the companion app to the GitHub repo [pyDALAnvilWorks](https://github.com/benlawraus/pyDALAnvilWorks).',
    font = '',
    spacing_above = 'small',
    spacing_below = 'small',
    data = None,
    background = '',
    format = 'markdown',
    parent = Container(),
)
ContentPanel = dict(
    col_widths = '{}',
    parent = Container(),
)
MenuPanel = dict(
)
class HomeFormTemplate(HtmlTemplate):
    link_signin = Link(**LinkSignin)
    link_login = Link(**LinkLogin)
    navbar_links = FlowPanel(**NavbarLinks)
    label_title = Label(**LabelTitle)
    rich_text_1 = RichText(**RichText1)
    content_panel = ColumnPanel(**ContentPanel)
    menu_panel = ColumnPanel(**MenuPanel)

    # not sure why, but item is not in the official api docs so must add here
    item = dict()

    def init_components(self, **kwargs):
        super().__init__()        
        pass
