from datetime import datetime
import tests.pydal_def as mydal


def add_row(**kwargs):
    row_id = mydal.db['users'].insert(**kwargs)
    mydal.db.commit()
    return row_id


def select_user():
    row = mydal.db().select(mydal.db.users.ALL, orderby=mydal.db.users.id).last()
    return row

def get_by_id(id):
    return mydal.db.users(id)

def get_user():
    # First see if a user is in mydal.db
    row = select_user()
    if row is None:
        # create a user
        add_row(name="Rex Eagle")
        row = select_user()
    return row
