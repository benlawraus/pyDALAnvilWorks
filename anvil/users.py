"""Functions here over-write functions defined in _anvil_designer/componentsUI/users/Users.py"""
import os
from datetime import datetime
from warnings import warn

import pydal.objects
import tests.pydal_def as mydal
from pydal import Field
from _anvil_designer.componentsUI.users import *


def add_row(**kwargs):
    row_ref = mydal.db['users'].insert(**kwargs)
    mydal.db.commit()
    return row_ref


def get_by_id(id):
    return mydal.db.users(id)


def logout():
    """Forget the current logged-in user"""
    query = (mydal.db.logged_in_users.pid == os.getpid()) \
            & (mydal.db.logged_in_users.pytest ==os.environ["PYTEST_CURRENT_TEST"])
    mydal.db(query).delete()
    return


def force_login(user_row, remember=False):
    """Set the specified user object (a row from a Data Table) as the current logged-in user. It must be a row from the users table. By default, login status is not remembered between sessions."""
    if 'logged_in_users' not in mydal.db.tables:
        mydal.db.define_table('logged_in_users', Field('user_ref', type='reference users'),
                              Field('pid', type='integer'),
                              Field('pytest','string'))
    new_log = mydal.db.logged_in_users.insert(user_ref=user_row,
                                              pid=os.getpid(),
                                              pytest=os.environ["PYTEST_CURRENT_TEST"])
    mydal.db.commit()
    return new_log.user_ref


def get_user(allow_remembered=True) -> pydal.helpers.classes.Reference:
    """Get the row from the users table that corresponds to the currently logged-in user. If allow_remembered is true (the default), the user may have logged in in a previous session. Returns None if no user is logged in."""
    pass
    """Retrieves the user in database corresponding to pid

    Why is there an extra table ``logged_in_users`` ?!?

    So that the returned user is a reference and not a row (pyDAL). Also logged_in_users contains the pid of the test.
    Tests can run in parallel, so the correct user is important."""

    def get_user_with_pid():
        query = (mydal.db.logged_in_users.pid == os.getpid()) \
                & (mydal.db.logged_in_users.pytest == os.environ["PYTEST_CURRENT_TEST"])
        rows = mydal.db(query).select()
        if len(rows) == 1:
            return rows[0]
        elif len(rows) == 0:
            warn(UserWarning("No user logged in. Use 'force_login(user)'."))
            return None
        else:
            raise ValueError("More than one user is logged in for the same pid.")

    if mydal.db is None:
        raise ConnectionError("Database not connected")
    logged_in_user = get_user_with_pid()
    if logged_in_user:
        return logged_in_user.user_ref
    return None
