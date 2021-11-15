"""Thanks to https://realpython.com/primer-on-python-decorators/
"""
from functools import wraps
import anvil.users
import tests.pydal_def as mydal

PLUGINS = dict()


def callable(_func=None, *, require_user=None):
    """ Wraps the decorator of the function."""

    def decorator_callable(func):
        """Decorator of the function. """
        # register
        module = __import__(func.__module__)
        PLUGINS[func.__name__] = func.__qualname__

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
    """arg[0] = function name, arg[1:] are the arguments of function."""
    if len(args) == 1:
        return PLUGINS[args[0]['call']()]
    else:
        return PLUGINS[args[0]['call'](*args[1:])]


def func_decor1(func1=None, *args):
    return func1(*args)


def func_decor2(func1=None):
    def inner(func2):
        return func2

    print(func1)
    # def inner(*args, **kwargs):
    return inner  # (*args, **kwargs)


def class_decor(_class):
    """https://notebook.community/justanr/notebooks/decorator_day"""
    return _class


portable_class = class_decor
