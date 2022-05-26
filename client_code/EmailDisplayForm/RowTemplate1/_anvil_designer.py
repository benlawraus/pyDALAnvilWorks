from anvil import *
from dataclasses import dataclass, field



@dataclass
class RowTemplate1Template(DataRowPanel):

    def init_components(self, **kwargs):
        RowTemplate1Template.__init__(self)
