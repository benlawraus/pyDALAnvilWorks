import tests.pydal_def as mydal
from _anvil_designer.set_up_user import new_user_in_db
from client_code.EmailDisplayForm import EmailDisplayForm
from tests.common import generate_contact_instance
import anvil.users
from tests.test_app_table import insert_contact_record


class TestEmailDisplayForm:
    def test_init(self):
        # generate demo user
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)

        # generate some contacts
        contact_ref = insert_contact_record(**generate_contact_instance(user))
        # display emails
        form_under_test = EmailDisplayForm()
        form_under_test.user = user
        assert form_under_test.repeating_panel_1.items
        # make sure the contact created here is in this list
        form_email_list = [email['address'] for email in form_under_test.repeating_panel_1.items]
        for email in contact_ref['email_list']:
            assert email.address in form_email_list
