from anvil import *
from _anvil_designer.common_structures import binding_property

databindings = [
]

class ItemTemplate1Template(ColumnPanel):
    def __init__(self, **properties):
        super(ItemTemplate1Template, self).__init__()
        self.__bindings = databindings
        if len(self.__bindings) >0:
            self.item = binding_property('item')
        if properties.get('item', None):
            self.item = properties['item']
    
    def init_components(self, **properties):
        ItemTemplate1Template.__init__(self, **properties)
