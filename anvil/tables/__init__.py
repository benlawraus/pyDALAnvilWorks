import pydal.helpers.classes
from .anvilTables import *

from tests import pydal_def as mydal
from anvil.tables.query import *

from .AppTables import app_tables
from .basefunction import order_by


def get_id(self):
    return self['id']


def delete_row(self):
    # Row object
    self.delete_record()
    mydal.db.commit()
    return


def delete_ref(self):
    # Reference object
    mydal.db[self._table](self).delete_record()
    mydal.db.commit()
    return


def update_row(self, **kwargs):
    t_name = self.update_record.tablename
    mydal.db(mydal.db[t_name]._id == self.id).update(**kwargs)
    mydal.db.commit()
    for key in kwargs:
        if key in self.__dict__:
            self[key] = kwargs[key]
    return


def update_ref(self, **kwargs):
    mydal.db(mydal.db[self._table]._id == self).update(**kwargs)
    mydal.db.commit()
    for key in kwargs:
        self[key] = kwargs[key]
    return


pydal.objects.Row.get_id = get_id
pydal.helpers.classes.Reference.get_id = get_id
pydal.objects.Row.delete = delete_row
pydal.helpers.classes.Reference.delete = delete_ref
pydal.objects.Row.update = update_row
pydal.helpers.classes.Reference.update = update_ref
