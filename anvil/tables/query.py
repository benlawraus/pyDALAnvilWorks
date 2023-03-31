def between(min, max, min_inclusive=True, max_inclusive=False):
    """Match values between the provided min and max, optionally inclusive."""
    pass


def full_text_match(query, raw=False):
    """Match values that match the provided full-text search query."""
    pass


def ilike(*args):
    """Match values using a case-insensitive ILIKE query, using the % wildcard character."""
    pass


def like(*args):
    """Match values using a case-sensitive LIKE query, using the % wildcard character."""
    pass


def none_of(*query_expressions):
    """Match none of the query parameters given as arguments and keyword arguments"""
    pass


class not_:
    """Match none of the query parameters given as arguments and keyword arguments"""
    def __init__(self, *args):
        self.arg = args[0]


class less_than:
    """Match values less than the provided value."""
    def __init__(self, *args):
        self.arg = args[0]


class less_than_or_equal_to:
    """Match values less than or equal to the provided value."""
    def __init__(self, *args):
        self.arg = args[0]


class greater_than:
    """Match values greater than the provided value."""
    def __init__(self, *args):
        self.arg = args[0]


class greater_than_or_equal_to:
    """Match values greater than or equal to the provided value."""
    def __init__(self, *args):
        self.arg = args[0]


class all_of:
    """Match all query parameters given as arguments and keyword arguments"""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class any_of:
    """Match any query parameters given as arguments and keyword arguments"""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class fetch_only:
    def __init__(self, *args):
        self.args = args
