def connect(key, init_session=None, quiet=False):
    """Connect your uplink script to your anvil app."""
    pass


def disconnect():
    """Disconnect your uplink script from your anvil app. Your script is then free to call anvil.server.connect()
    with the same uplink key or a new uplink key. """
    pass


def wait_forever():
    """A useful shortcut to keep your Python script running. This allows your app to anvil.server.call functions
    inside your Python script. You can use any other way to keep the process alive in place of this function. """
    pass
