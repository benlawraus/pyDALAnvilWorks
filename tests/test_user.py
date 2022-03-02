# Example test.
from tests import pydal_def as mydal
from _anvil_designer.set_up_user import new_user_in_db

import anvil.users

class TestUser:
    def test_get_user(self):
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        assert anvil.users.get_user()
        anvil.users.logout()
