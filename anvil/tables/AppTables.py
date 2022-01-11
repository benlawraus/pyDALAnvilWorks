from anvil.tables.basefunction import BaseFunction

TABLES = dict(
    users=dict(
        email='string',
        enabled='bool',
        signed_up='datetime',
        password_hash='string',
        confirmed_email='bool',
        email_confirmation_key='string',
        n_password_failures='number',
        last_login='datetime',
        remembered_logins='simpleObject',
    ),
    email=dict(
        address='string',
        created_by='link_single',
        created_on='datetime',
        place='number',
    ),
    phone=dict(
        number='string',
        created_by='link_single',
        created_on='datetime',
    ),
    contact=dict(
        name='string',
        phone='link_single',
        email_list='link_multiple',
        age='number',
        created_by='link_single',
        created_on='datetime',
        family='simpleObject',
        uid='number',
        father='link_single',
    ),
)


class AppTables:
    def __init__(self):
        self.users = BaseFunction('users', TABLES['users'])
        self.email = BaseFunction('email', TABLES['email'])
        self.phone = BaseFunction('phone', TABLES['phone'])
        self.contact = BaseFunction('contact', TABLES['contact'])


app_tables = AppTables()
