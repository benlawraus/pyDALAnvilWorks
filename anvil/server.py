"""Thanks to https://realpython.com/primer-on-python-decorators/
"""
import importlib
from functools import wraps
import anvil.users
import tests.pydal_def as mydal

PLUGINS = dict()


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


def call(*args):
    # register
    """arg[0] = function name, arg[1:] are the arguments of function."""
    if PLUGINS is None:
        importlib.import_module("server_code.server_code_functions")
    if len(args) == 1:
        return PLUGINS[args[0]]()
    else:
        return PLUGINS[args[0]](*args[1:])



def class_decor(_class):
    """https://notebook.community/justanr/notebooks/decorator_day"""
    return _class


portable_class = class_decor
