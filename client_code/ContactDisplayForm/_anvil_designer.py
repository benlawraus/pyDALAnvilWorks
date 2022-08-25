from anvil import *
from _anvil_designer.common_structures import binding_property

link_name = dict(
    col_widths='{}',
    parent=Container(),
)
label_email = dict(
)
databindings = [
    dict( item='self.item["name"]', element='link_name.text', writeback=False,),
    dict( item='self.item["phone"]', element='label_email.text', writeback=False,),
]

class ContactDisplayFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(ContactDisplayFormTemplate, self).__init__()
        self.link_name = Link(**link_name)
        self.label_email = Label(**label_email)
        self.__bindings = databindings
        if len(self.__bindings) >0:
            self.item = binding_property('item')
        if properties.get('item', None):
            self.item = properties['item']
    
    def init_components(self, **properties):
        ContactDisplayFormTemplate.__init__(self, **properties)
