from .anvilServer import *

"""Thanks to https://realpython.com/primer-on-python-decorators/
"""
import pickle
from functools import wraps
from types import NoneType

import anvil.users
from tests import pydal_def as mydal
import pathlib


class Context:
    type = 'laptop'


PLUGINS = dict()
context = Context()

no_loading_indicator = NoLoadingIndicator()


def callable(_func=None, *, require_user=None):
    """ Wraps the decorator of the function."""

    def decorator_callable(func):
        """Decorator of the function. """
        # register
        PLUGINS[func.__name__] = func

        @wraps(func)
        def wrapper(*args, **kwargs):
            if require_user:
                mydal.define_tables_of_db()
                user = anvil.users.get_user()
                if isinstance(require_user, bool):
                    if user is None:
                        raise PermissionError()
                elif not require_user(user):
                    raise PermissionError()
            return_value = func(*args, **kwargs)
            # after function
            return return_value

        return wrapper

    if _func is None:
        return decorator_callable
    else:
        return decorator_callable(_func)


def import_source_file(file_path, module_name):
    """From https://docs.python.org/3/library/importlib.html#importing-programmatically"""
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if not isinstance(spec, NoneType):
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    return


def call(*args):
    """Simulates the call from the anvil client to the anvil server."""
    # register
    """arg[0] = function name, arg[1:] are the arguments of function."""
    if args[0] not in PLUGINS:
        pth = pathlib.Path(__file__).parent.parent.parent / 'server_code'
        for p in pth.iterdir():
            if p.is_file():
                import_source_file(p, p.stem)
    if len(args) == 1:
        return PLUGINS[args[0]]()
    else:
        """Need to pickle as a way to copy so that not sending reference."""
        new_args = []
        for arg in args[1:]:
            temp = pickle.dumps(arg)
            new_args.append(pickle.loads(temp))
        return PLUGINS[args[0]](*new_args)


def class_decor(_class):
    """https://notebook.community/justanr/notebooks/decorator_day"""
    return _class


portable_class = class_decor

