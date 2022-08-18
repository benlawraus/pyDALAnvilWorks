import pathlib
import pickle
from dataclasses import dataclass
from functools import wraps
from types import NoneType
from unittest.mock import Mock


@dataclass
class Capability():
    def narrow(self, additional_scope):
        """Return a new capability that is narrower than this one, by appending additional scope element(s) to it.		"""
        return Capability()

    def send_update(self, update):
        """Send an update to the update handler for this capability, in this interpreter and also in any calling
        environment (eg browser code) that passed this capability into the current server function. """
        pass

    def set_update_handler(self, apply_update, get_update):
        """Set a handler for what happens when an update is sent to this capability.Optionally provide a function for
        aggregating updates (default behaviour is to merge them, if they are all dictionaries, or to return only the
        most recent update otherwise.) """
        pass

    pass


@dataclass
class HttpRequest():
    pass


@dataclass
class HttpResponse():
    pass


def get_api_origin(environment):
    """Returns the root URL of the API for the current app.By default, this function returns the URL for the current
    environment, which might be private or temporary (for example, if you are running your app in the Anvil Editor).
    If you want the URL for the published branch, pass ‘published’ as an argument. """
    return Mock()


def get_app_origin(environment):
    """Returns the root URL for the current app.By default, this function returns the URL for the current
    environment, which might be private or temporary (for example, if you are running your app in the Anvil Editor).
    If you want the URL for the published branch, pass ‘published’ as an argument. """
    return Mock()


def is_app_online():
    """Returns True if this app is online and False otherwise.If anvil.server.is_app_online() returns False we expect
    anvil.server.call() to throw an anvil.server.AppOfflineError """
    return True


def reset_session():
    """Reset the current session to prevent further SessionExpiredErrors."""
    pass


def unwrap_capability(capability, scope_pattern):
    """Checks that its first argument is a valid Capability, and that its scope matches the supplied pattern.To
    match, the scope must:
    - Be at least as broad as the pattern (ie the same length or shorter)
    - Contain the same
    values in the same position as the pattern
    - unless that position in the pattern is Capability.ANY, which matches
    any valueReturns a list of matched scope elements, of the same length as the pattern. (If the scope was broader
    than required, missing elements are set to None.) """
    pass


def list_background_tasks(all_environments=False):
    """Return a list of Background Task objects.

    Running this function from the published version of your app will return only those Background Tasks that
    were started from the published version, and running from the development version (i.e. by clicking “Run” in
    the designer) will only return tasks started in that environment. To return all tasks regardless of environment,
    set the all_environments keyword argument to True.

    This function can only be run from the server side."""
    return Mock()


BACKGROUND_FUNCTIONS = dict()


def background_task(_func=None):
    """ Wraps the decorator of the function. Similar to anvil.server.callable"""

    def decorator_callable(func):
        """Decorator of the function. """
        # register
        BACKGROUND_FUNCTIONS[func.__name__] = func

        @wraps(func)
        def wrapper(*args, **kwargs):
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


def launch_background_task(*args):
    """Runs a background task.  (similar to anvil.server.call)
    arg[0] = function name, arg[1:] are the arguments of function."""
    if args[0] not in BACKGROUND_FUNCTIONS:
        pth = pathlib.Path(__file__).parent.parent.parent / 'server_code'
        for p in pth.iterdir():
            if p.is_file():
                import_source_file(p, p.stem)
    if len(args) == 1:
        return BACKGROUND_FUNCTIONS[args[0]]()
    else:
        """Need to pickle as a way to copy so that not sending reference."""
        new_args = []
        for arg in args[1:]:
            temp = pickle.dumps(arg)
            new_args.append(pickle.loads(temp))
        return BACKGROUND_FUNCTIONS[args[0]](*new_args)


class NoLoadingIndicator:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

