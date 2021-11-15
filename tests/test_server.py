import anvil.server
from server_code.server_code_functions import example_1
from client_code.client_code_functions import example_A

class TestServer:
    def test_callable(self):
        assert "Returned string from function example_1." == example_1()

    def test_call(self):
        assert "Returned string from function example_1." == example_A()
