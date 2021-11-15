"""Used for pyDALAnvilWorks tests only. Delete."""
import anvil.server


@anvil.server.callable
def example_1() -> str:
    return "Returned string from function example_1."
