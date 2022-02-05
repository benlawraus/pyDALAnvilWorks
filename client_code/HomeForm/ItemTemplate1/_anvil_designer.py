from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvil import Container
from dataclasses import dataclass, field



@dataclass
class ItemTemplate1Template(ColumnPanel):

    def init_components(self, **kwargs):
        ItemTemplate1Template.__init__(self)
