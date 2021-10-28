from typing import Optional
import pydal.helpers.classes

import tests.pydal_def as mydal


def order_by(*args, **kwargs):
    return {**{'orderby': '|'.join(args)}, **kwargs}


class BaseFunction:
    """Saving rows and getting rows to/from the database"""

    def __init__(self, table_name):
        self.table_name = table_name

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

    def get_by_id(self, id)->Optional[pydal.objects.Row]:
        return mydal.db[self.table_name](id)

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
        query = []
        for key in kwargs:
            query.append(mydal.db[self.table_name][key] == kwargs[key])
        return mydal.db(*query).select(**orderby)

    def get(self, **kwargs) -> Optional[pydal.objects.Row]:
        return mydal.db[self.table_name](**kwargs)


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
    mydal.db.commit()
    return


def update_ref(self, **kwargs):
    mydal.db(mydal.db[self._table].id == self).update(**kwargs)
    mydal.db.commit()
    return


pydal.objects.Row.get_id = get_id
pydal.helpers.classes.Reference.get_id = get_id
pydal.objects.Row.delete = delete_row
pydal.helpers.classes.Reference.delete = delete_ref
pydal.objects.Row.update = update_row
pydal.helpers.classes.Reference.update = update_ref
