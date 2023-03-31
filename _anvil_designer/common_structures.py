import warnings
from collections.abc import Mapping


class ClassDict(Mapping):
    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        if key not in self.__dict__.keys():
            warnings.warn(f"Key {key} not found in {self.__dict__.keys()}. Need to assign a default value.")
            return None
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


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


def get_item_key_from_string(s: str):
    """Returns xxxx from string self.item["xxxx"]"""
    start_index = s.find('["') + 2
    end_index = s.find('"]')
    if start_index != -1 and end_index != -1:
        return s[start_index:end_index]
    raise ValueError(f"Invalid string: {s}")


def attr_getter(instance, attr_name='item'):
    """Associate the UI with the item dictionary attribute of the form using the private attribute _item.

    :param instance: the form instance of the form class
    :param attr_name: the name of the attribute to be returned (item)
    :return: the (item) dictionary attribute of the form
    """
    private_attr = '_' + attr_name
    # getattr(instance, private_item) is **self._item**
    # and so is instance.__dict__[private_item]
    attr = instance.__dict__.get(private_attr, None)
    if attr is None:
        raise AttributeError(f"The attribute {private_attr} is not defined.")
    # if self.item = "i am something but not a dict"
    if hasattr(attr, '_private'):
        return attr['_private']
    # if self.item is a dict
    for binding in getattr(instance, '_bindings', []):  # binding is one of the data-bindings in the list
        # get the item key from the data-binding
        attr_member = binding['element'].split('.')
        ui_component = getattr(instance, attr_member[0])
        # setting the item value to the attribute's property
        item_key = get_item_key_from_string(binding['item'])
        if binding['writeback']:
            attr[item_key] = getattr(ui_component, attr_member[1], None)
    return attr


def attr_setter(instance, some_dict, attr_name='item'):
    """
    :param instance: the form instance of the form class
    :param attr_name: the name of the attribute that is assigned (item)
    :param some_dict: the Dict that will become instance.attr_name
    :return: None
    """
    private_item = '_' + attr_name
    if not isinstance(some_dict, Mapping):
        # this is for the case where self.item = "i am something but not a dict"
        # getattr(instance, private_item) is **self._item**
        # and so is instance.__dict__[private_item]. Which is better?
        setattr(getattr(instance, private_item), '_private', some_dict)
        return
    for key in some_dict:
        # this is for the case where self.item = {"name": "John", "age": 30}
        instance.__dict__[private_item][key] = some_dict[key]
        for binding in getattr(instance, '_bindings', []):
            item_key = get_item_key_from_string(binding['item'])
            # self.item has gone back to being a dict
            if hasattr(instance.__dict__[private_item], '_private'):
                delattr(instance.__dict__[private_item], '_private')
            # if the key in the dict matches the key in the data-binding
            if key == item_key:
                # get the item key from the data-binding
                attr_member = binding['element'].split('.')
                ui_component = getattr(instance, attr_member[0])
                setattr(ui_component, attr_member[1], some_dict[key])
    return
