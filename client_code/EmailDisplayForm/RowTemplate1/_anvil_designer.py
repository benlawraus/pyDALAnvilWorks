from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

databindings = [
]

class RowTemplate1Template(DataRowPanel):
    def __init__(self, **properties):
        super(RowTemplate1Template, self).__init__()
        self._bindings = databindings
        self._item = ClassDict()

        if properties.get('item', None) is not None:
            self.item = properties['item']

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        RowTemplate1Template.__init__(self, **properties)
