from datetime import datetime

import pydal.objects
import tests.pydal_def as mydal
from pydal import Field

def add_row(**kwargs):
    row_ref = mydal.db['users'].insert(**kwargs)
    mydal.db.commit()
    return row_ref




def get_by_id(id):
    return mydal.db.users(id)


def get_user() -> pydal.helpers.classes.Reference:
    """Retrieves the last user added to the database.

    Why is there an extra table ``logged_in_users`` ?!?

    So that the returned user is a reference and not a row (pyDAL). Sorry!"""
    if mydal.db is None:
        raise ConnectionError("Database not connected")
    if 'logged_in_users' not in mydal.db.tables:
        mydal.db.define_table('logged_in_users', Field('user_ref', 'reference users'))
    rows = mydal.db().select(mydal.db.users.ALL, orderby=~mydal.db.users.id)
    if len(rows) == 0:
        ref = mydal.db.users.insert(name="Rex Eagle")
        new_log = mydal.db.logged_in_users.insert(user_ref=ref)
    else:
        new_log = mydal.db.logged_in_users.insert(user_ref=rows[0])
    mydal.db.commit()
    mydal.logged_in_user = new_log.user_ref
    return mydal.logged_in_user


def signup_with_form(allow_cancel=False):
    return None


def login_with_form(allow_cancel=False, show_signup_option=False):
    return None