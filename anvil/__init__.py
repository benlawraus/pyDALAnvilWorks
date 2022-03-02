from collections import UserDict

import pydal.helpers.classes

from _anvil_designer.componentsUI.anvil import *
from _anvil_designer.componentsUI.anvilUsers import *

class dict(UserDict):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], pydal.helpers.classes.Reference):
            args_ix = []
            for attr in args[0]._table._fields:
                args_ix.append((attr, args[0][attr]))
            return super().__init__(args_ix)
        else:
            return super().__init__(*args, **kwargs)
