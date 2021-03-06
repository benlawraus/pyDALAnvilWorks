from tests import pydal_def as mydal
from _anvil_designer.set_up_user import new_user_in_db
import anvil.users
from tests.test_app_table import insert_get_contact_row_ref


def user_login():
    mydal.define_tables_of_db()
    user_ref = new_user_in_db()
    anvil.users.force_login(user_ref)
    user = anvil.users.get_user()
    assert user
    yield user
    anvil.users.logout()


from client_code.HomeForm import HomeForm
class TestHomeForm:
    def test_init(self):
        for user in user_login():
            contact_row, contact_ref = insert_get_contact_row_ref(user)
            home_form=HomeForm()
            home_form.contact_form.repeating_panel_2.raise_event("x-contact_name", uid=contact_ref)

    def test_login_with_form(self):
        mydal.define_tables_of_db()
        home_form = HomeForm()
        home_form.link_login_click()
        user = anvil.users.get_user()
        assert user
        anvil.users.logout(user)
        user = anvil.users.get_user()
        assert user is None