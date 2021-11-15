from typing import Optional, Dict, List
import pydal.helpers.classes

import tests.pydal_def as mydal
from anvil.tables.query import *


class order_by:
    def __init__(self, *args, **kwargs):
        self.order = '|'.join(args)
        self.kwargs = kwargs


class BaseFunction:
    """Saving rows and getting rows to/from the database"""

    def __init__(self, table_name):
        self.query: List = []  # list of pydal.objects.Query
        self.table_name: str = table_name

    def add_row(self, **kwargs) -> pydal.helpers.classes.Reference:
        if self.table_name not in mydal.db.tables:
            raise AttributeError("Table not in database.")
        try:
            reference = mydal.db[self.table_name].insert(**kwargs)
        except TypeError:
            msg = f"\n{self.table_name}:\n fields:\n {kwargs}"
            raise TypeError(msg)
        mydal.db.commit()
        return reference

    def get_by_id(self, uid) -> Optional[pydal.objects.Row]:
        return mydal.db[self.table_name](uid)

    def _pick_apart(self, key, val, _q):
        if len(val.args) > 0:
            for arg in val.args:
                # there must be a key
                _q.append(self.add_to_query(key,arg))
        for _key in val.kwargs:
            # there must be no key
            _q.append(self.add_to_query(_key, val.kwargs[_key]))
        return

    def add_to_query(self, key, val):
        if isinstance(val, all_of):
            _q = []
            self._pick_apart(key, val, _q)
            _query = _q[0]
            if len(_q) > 1:
                for ix in range(1, len(_q)):
                    _query &= (_q[ix])
            return _query
        elif isinstance(val, any_of):
            _q = []
            self._pick_apart(key, val, _q)
            _query = _q[0]
            if len(_q) > 1:
                for ix in range(1, len(_q)):
                    _query |= (_q[ix])
            return _query
        elif isinstance(val, not_):
            return mydal.db[self.table_name][key] != val.arg
        elif isinstance(val, less_than):
            return mydal.db[self.table_name][key] < val.arg
        elif isinstance(val, greater_than):
            return mydal.db[self.table_name][key] > val.arg
        elif isinstance(val, greater_than_or_equal_to):
            return mydal.db[self.table_name][key] >= val.arg
        elif isinstance(val, less_than_or_equal_to):
            return mydal.db[self.table_name][key] <= val.arg
        elif key is not None:
            return mydal.db[self.table_name][key] == val
        else:
            return val

    def search(self, *args, **kwargs):
        orderby = {}
        self.query = None
        if len(args) > 0:
            for arg in args:
                if isinstance(arg, order_by):
                    ord_for = arg.order.split('|')
                    _o = mydal.db[self.table_name][ord_for[0]]
                    if len(ord_for) > 1:
                        for f in ord_for[1:]:
                            _o |= mydal.db[self.table_name][f]
                    if 'ascending' in arg.kwargs:
                        if not arg.kwargs['ascending']:
                            _o = ~_o
                    orderby = {'orderby': _o}
                else:
                    self.query = self.add_to_query(None, arg)
        # can only be one kwarg
        for key in kwargs:
            self.query = self.add_to_query(key, kwargs[key])
        return mydal.db(self.query).select(**orderby)

    def get(self, **kwargs) -> Optional[pydal.objects.Row]:
        return mydal.db[self.table_name](**kwargs)

    def list_columns(self) -> List[Dict[str, str]]:
        field_list = []
        for field in mydal.db[self.table_name].fields:
            if field == 'id':
                continue
            field_list.append({'name': field, 'type': mydal.db[self.table_name][field].type})
        return field_list


class AppTables:
    def __getattr__(self, item):
        if item not in self.__dict__:
            instance = BaseFunction(item)
            setattr(self, item, instance)
        return self.__dict__[item]


app_tables = AppTables()


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
    mydal.db(mydal.db[t_name].id == self.id).update(**kwargs)
    for key in kwargs:
        if key in self.__dict__:
            self[key] = kwargs[key]
    mydal.db.commit()
    return


def update_ref(self, **kwargs):
    mydal.db(mydal.db[self._table].id == self).update(**kwargs)
    for key in kwargs:
        self[key] = kwargs[key]
    mydal.db.commit()
    return


pydal.objects.Row.get_id = get_id
pydal.helpers.classes.Reference.get_id = get_id
pydal.objects.Row.delete = delete_row
pydal.helpers.classes.Reference.delete = delete_ref
pydal.objects.Row.update = update_row
pydal.helpers.classes.Reference.update = update_ref
