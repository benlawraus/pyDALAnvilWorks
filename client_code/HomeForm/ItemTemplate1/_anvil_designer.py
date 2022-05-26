from anvil import *
from dataclasses import dataclass, field



@dataclass
class ItemTemplate1Template(ColumnPanel):

    def init_components(self, **kwargs):
        ItemTemplate1Template.__init__(self)
