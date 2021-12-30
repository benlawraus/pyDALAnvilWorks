from anvil.tables.basefunction import BaseFunction


class AppTables:
    def __init__(self):
        self.users = BaseFunction('users')
        self.email = BaseFunction('email')
        self.phone = BaseFunction('phone')
        self.contact = BaseFunction('contact')


app_tables = AppTables()
