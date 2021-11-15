import anvil.server
from server_code.server_code_functions import example_1
class TestServer:
    def test_callable(self):
        assert "Returned string from function example_1."==example_1()
