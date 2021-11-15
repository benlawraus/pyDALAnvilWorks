"""Used for pyDALAnvilWorks tests only. Delete."""
import anvil.server


def example_A():
    text = anvil.server.call("example_1")
    return text
