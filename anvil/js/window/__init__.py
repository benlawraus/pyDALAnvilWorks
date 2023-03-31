from unittest.mock import Mock


def Function(*args, **kwargs):
    return Mock()


class Promise:
    def __init__(self, *args, **kwargs):
        # this is for the case in anvil_extras.storage.py:
        # _window.Promise(lambda res, rej: self._store.removeItem(key))
        if callable(args[0]):
            args[0](1,2)  # res, rej
        return

    def all(self, *args, **kwargs):
        return Mock()


document = Mock()
document.body = Mock()

jQuery = Mock()
jQuery.appendTo = Mock()


def addEventListener(*args, **kwargs):
    return Mock()


def removeEventListener(*args, **kwargs):
    return Mock()


class Object(Mock):
    pass
