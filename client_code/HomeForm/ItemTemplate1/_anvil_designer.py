from anvil import *
from _anvil_designer.common_structures import binding_property

databindings = [
]

class ItemTemplate1Template(ColumnPanel):
    def __init__(self, **properties):
        super(ItemTemplate1Template, self).__init__()
        self.__bindings = databindings@property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        ItemTemplate1Template.__init__(self, **properties)
