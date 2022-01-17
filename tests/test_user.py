# Example test.
from _anvil_designer.set_up_user import new_user_in_db
import anvil.users

class TestUser:
    def test_get_user(self):
        user = new_user_in_db()
        anvil.users.force_login(user)
        assert anvil.users.get_user()
        anvil.users.logout()
