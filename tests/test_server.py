from server_code.server_code_functions import example_1
from tests.client_code_functions import example_A, save_contact, generate_contact
import tests.pydal_def as mydal

class TestServer:
    def test_callable(self):
        assert "Returned string from function example_1." == example_1()

    def test_call(self):
        assert "Returned string from function example_1." == example_A()

    def test_client_save_contact(self):
        mydal.define_tables_of_db()
        user, contact_id = save_contact()
        # get from database
        contact_row = mydal.db.contact(contact_id)
        assert contact_row
        # get initial dict
        contact_dict = generate_contact(user)
        for attr in {'name', 'age', 'created_on', 'created_by'}:
            assert contact_dict[attr] == contact_row[attr]
        for attr in {'number', 'created_on', 'created_by'}:
            assert contact_dict['phone'][attr] == contact_row.phone[attr]
        for attr in {'address', 'created_on', 'created_by'}:
            assert contact_dict['email_list'][0][attr] == contact_row.email_list[0][attr]


