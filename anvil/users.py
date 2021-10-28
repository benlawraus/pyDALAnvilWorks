from datetime import datetime

import pydal.objects
import pickle
import tests.pydal_def as mydal


def add_row(**kwargs):
    row_ref = mydal.db['users'].insert(**kwargs)
    mydal.db.commit()
    return row_ref




def get_by_id(id):
    return mydal.db.users(id)


def get_user() -> pydal.helpers.classes.Reference:
    """Retrieves the last user added to the database."""
    # First see if a user is in mydal.db
    row = mydal.db().select(mydal.db.users.ALL, orderby=~mydal.db.users.id).first()
    # turn it into a reference
    if row is None:
        # create a user
        return add_row(name="Rex Eagle")
    # turn into reference
    dict_of = {'id':row['id']}
    for key in row.as_dict():
        if key != 'id':
            dict_of.update({key:row[key]})
    row.delete_record()
    mydal.db.commit()
    ref = mydal.db.users.insert(**dict_of)
    mydal.db.commit()
    return ref
