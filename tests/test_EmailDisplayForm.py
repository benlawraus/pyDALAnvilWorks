import tests.pydal_def as mydal
from client_code.EmailDisplayForm import EmailDisplayForm
from tests.test_ContactForm import TestContactForm


class TestEmailDisplayForm:
    def test_init(self):
        # generate demo user
        mydal.define_tables_of_db()

        # generate some contacts
        tests = TestContactForm()
        user, contact_row = tests.test_save_contact()
        # display emails
        form_under_test = EmailDisplayForm()
        form_under_test.user = user
        assert form_under_test.repeating_panel_1.items
        # make sure the contact created here is in this list
        for contact in form_under_test.repeating_panel_1.items:
            if contact_row.address == contact['address']:
                assert contact_row.created_by == contact['created_by']

