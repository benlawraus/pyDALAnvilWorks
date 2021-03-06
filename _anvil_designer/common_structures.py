class ClassDict:
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        if item not in self.__dict__.keys():
            return "Unassigned. (Databindings not implemented yet.)"
        return self.__dict__[item]


def make_no_None_kwargs(**kwargs):
    _kwargs = []
    for key in kwargs:
        if kwargs[key] is not None:
            _kwargs.append(kwargs[key])
    return _kwargs

def default_val(val):
    return lambda: val


String = str
Number = float
Integer = int
Color = str
Boolean = bool
Themerole = str
Object = object
Seconds = float
Items = list
Datagridcolumns = list
Pixels = int
Uri = str
Html = str
Icon = str
Form = object
