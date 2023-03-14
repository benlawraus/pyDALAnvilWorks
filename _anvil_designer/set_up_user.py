import random

from tests import pydal_def as mydal

try:
    from tests.common import user_generator
except ImportError:
    def user_generator():
        random_str = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)])
        return dict(email=f"{random_str} see {__file__}",
                    password_hash=random_str)


def new_user_in_db():
    """Creates a new user in the database"""
    try:
        user_ref = mydal.db.users.insert(**user_generator())
    except AttributeError:
        raise AttributeError("'User' table or Database not defined. Either no 'user' table or did not run 'mydal.define_tables_of_db()'?")
    mydal.db.commit()
    return user_ref  # gets last inserted user
