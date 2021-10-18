import tests.pydal_def as mydal

print("From tables:")


def order_by(*args, **kwargs):
    print("From order_by:")
    return {**{'orderby': '|'.join(args)}, **kwargs}


class BaseFunction:
    """Saving rows and getting rows to/from the database"""

    def __init__(self, table_name):
        self.table_name = table_name

    def get(self, **kwargs):
        pass

    def add_row(self, **kwargs):
        if self.table_name not in mydal.db.tables:
            raise AttributeError("Table not in database.")
        row_id = mydal.db[self.table_name].insert(**kwargs)
        mydal.db.commit()
        return row_id

    def get_by_id(self, id):
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


class AppTables:
    def __getattr__(self, item):
        if item not in self.__dict__:
            instance = BaseFunction(item)
            setattr(self, item, instance)
        return self.__dict__[item]


app_tables = AppTables()
