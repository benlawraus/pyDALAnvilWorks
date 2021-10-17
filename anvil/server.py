def func_decor1(func1=None):
    return func1


def func_decor2(func1=None):
    def inner(func2):
        return func2
    print(func1)
    # def inner(*args, **kwargs):
    return inner  # (*args, **kwargs)


def class_decor(_class):
    """https://notebook.community/justanr/notebooks/decorator_day"""
    return _class


call = func_decor1
portable_class = class_decor
callable = func_decor2
