from typing import Optional, Dict, List
import pydal.helpers.classes

import tests.pydal_def as mydal
from anvil.tables.query import *


def order_by(*args, **kwargs):
    return {**{'orderby': '|'.join(args)}, **kwargs}


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

    def add_to_query(self, key, val):
        if isinstance(val, not_):
            self.query.append(mydal.db[self.table_name][key] != val.arg)
        elif isinstance(val, less_than):
            self.query.append(mydal.db[self.table_name][key] < val.arg)
        elif isinstance(val, greater_than):
            self.query.append(mydal.db[self.table_name][key] > val.arg)
        elif isinstance(val, greater_than_or_equal_to):
            self.query.append(mydal.db[self.table_name][key] >= val.arg)
        elif isinstance(val, less_than_or_equal_to):
            self.query.append(mydal.db[self.table_name][key] <= val.arg)
        else:
            self.query.append(mydal.db[self.table_name][key] == val)

    def search(self, *args, **kwargs):
        orderby = {}
        if len(args) > 0:
            ord_for = args[0]['orderby'].split('|')
            _o = mydal.db[self.table_name][ord_for[0]]
            if len(ord_for) > 1:
                for f in ord_for[1:]:
                    _o |= mydal.db[self.table_name][f]
            if 'ascending' in args[0]:
                if not args[0]['ascending']:
                    _o = ~_o
            orderby = {'orderby': _o}
        self.query = []
        for key in kwargs:
            self.add_to_query(key, kwargs[key])
        return mydal.db(*self.query).select(**orderby)

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
