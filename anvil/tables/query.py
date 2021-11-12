def all_of(*args, **kwargs):
    pass


def any_of(*args, **kwargs):
    pass


def ilike(*args):
    pass


def like(*args):
    pass


class not_:
    def __init__(self, *args):
        self.arg = args[0]


class less_than:
    def __init__(self, *args):
        self.arg = args[0]


class less_than_or_equal_to:
    def __init__(self, *args):
        self.arg = args[0]


class greater_than:
    def __init__(self, *args):
        self.arg = args[0]


class greater_than_or_equal_to:
    def __init__(self, *args):
        self.arg = args[0]
