from collections import UserDict


class ClassDict(UserDict):
    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value
    #
    # def __setitem__(self, key, value):
    #     self.__dict__[key] = value
    #
    # def __getitem__(self, item):
    #     if item not in self.__dict__.keys():
    #         return f"Unassigned. key={item} (Databindings not implemented yet.)"
    #     return self.__dict__[item]
    pass


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


def attr_getter(instance, attr_name='item'):
    """
    :param instance: the form instance of the form class
    :param attr_name: the name of the attribute to be returned (item)
    :return: the (item) dictionary attribute of the form
    """
    for key in instance.__dict__['_' + attr_name]:  # key='font' in item['font']
        for binding in getattr(instance, '_bindings', []):  # binding is one of the data-bindings in the list
            item_attr = binding['item'].split('[')
            if binding['writeback'] and attr_name == item_attr[0].replace('self.', ''):
                if key in item_attr[1]:
                    attr_member = binding['element'].split('.')
                    ui_component = getattr(instance, attr_member[0])
                    # setting the item value to the attribute's property
                    instance.__dict__['_' + attr_name][key] = getattr(ui_component, attr_member[1], None)
    return instance.__dict__['_' + attr_name]


def attr_setter(instance, some_dict, attr_name='item'):
    """
    :param instance: the form instance of the form class
    :param attr_name: the name of the attribute that is assigned (item)
    :param some_dict: the Dict that will become instance.attr_name
    :return: None
    """
    for key in some_dict:
        instance.__dict__['_' + attr_name][key] = some_dict[key]
        for binding in getattr(instance, '_bindings', []):
            item_attr = binding['item'].split('[')
            if attr_name == item_attr[0].replace('self.', '') and key in item_attr[1]:
                attr_mem = binding['element'].split('.')
                attr = getattr(instance, attr_mem[0])
                setattr(attr, attr_mem[1], some_dict[key])
    return


# def binding_property(attr_name):
#     """Assigns data-bindings to `self.item`
#     An example of self.__bindings is :
#     `self.__bindings = [{'item': "item['text']", 'element': "text_area.text", 'writeback': True}]`"""
#     return property(attr_getter, attr_setter)
