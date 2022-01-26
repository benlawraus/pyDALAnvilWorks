from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container

link_name = dict(
    col_widths='{}',
    parent=Container(),
)
label_email = dict(
)


class ContactDisplayFormTemplate(ColumnPanel):
    link_name = Link(**link_name)
    label_email = Label(**label_email)

    def init_components(self, **kwargs):
        pass
