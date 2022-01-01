from _anvil_designer.set_up_user import new_user_in_db
import anvil.users
from server_code.server_code_functions import example_1
from client_code.client_code_functions import example_A, save_contact_from_client
import tests.pydal_def as mydal


class TestServer:
    def test_callable(self):
        assert "Returned string from function example_1." == example_1()

    def test_call(self):
        assert "Returned string from function example_1." == example_A()

    def test_client_save_contact(self):
        mydal.define_tables_of_db()
        # create user
        user = new_user_in_db()
        user = anvil.users.force_login(user)
        user, contact_dict = save_contact_from_client()
        # get from database
        contact_row = mydal.db.contact(contact_dict['id'])
        assert contact_row
        # get initial dict
        # contact_dict = generate_contact(user)
        for attr in {'name', 'age', 'created_by'}:
            assert contact_dict[attr] == contact_row[attr]
        for attr in {'number', 'created_by'}:
            assert contact_dict['phone'][attr] == contact_row.phone[attr]
        for attr in {'address', 'created_by'}:
            assert contact_dict['email_list'][0][attr] == contact_row.email_list[0][attr]
        anvil.users.logout()

    def test_context(self):
        """This test is for pycharm's type checking feature using
        Python 2 style comments.  Here, the context object is used to
        ascertain whether code is running on laptop or not."""
        mydal.define_tables_of_db()
        user = new_user_in_db()
        user = anvil.users.force_login(user)

        from client_code.EmailDisplayForm import EmailDisplayForm
        test_import_ok = EmailDisplayForm()
        anvil.users.logout()
