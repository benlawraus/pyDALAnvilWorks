from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field

link_name = dict(
    col_widths='{}',
    parent=Container(),
)
label_email = dict(
)


@dataclass
class ContactDisplayFormTemplate(ColumnPanel):
    link_name: Link = field(default_factory=lambda: Link(**link_name))
    label_email: Label = field(default_factory=lambda: Label(**label_email))

    def init_components(self, **kwargs):
        ContactDisplayFormTemplate.__init__(self)
