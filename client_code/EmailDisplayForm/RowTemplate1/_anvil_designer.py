from _anvil_designer.componentsUI.anvil import *

class RowTemplate1Template(DataRowPanel):

    # not sure why, but item is not in the official api docs so must add here
    item = dict()

    def init_components(self, **kwargs):
        super().__init__()        
        pass
