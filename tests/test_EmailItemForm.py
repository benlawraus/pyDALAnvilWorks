import _anvil_designer.componentsUI.users
from client_code.EmailItemForm import EmailItemForm
import anvil.users

class TestEmailDisplayForm:
    def test_init(self):
        # generate demo user
        form_under_test = EmailItemForm()
        form_under_test.item = {'text':'hello!'}
        form_under_test.parent = 4
        form_under_test.button_1_click()
        form_under_test.raise_event(event_name="boo")

    def test_UI(self):

        anvil.users.get_user()
        anvil.users.login_with_email(email='f',password='r')
        anvil.users.signup_with_google(additional_scopes='g')

