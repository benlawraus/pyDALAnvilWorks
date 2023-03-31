import pathlib
import string
from collections import OrderedDict, namedtuple
from dataclasses import dataclass
from string import Template
from typing import Dict, List, Tuple, Union

import strictyaml as sy

# from _anvil_designer.generate_files import MODULE_PATH

# from collections import defaultdict


CLIENT_CODE_PATH = pathlib.Path(__file__).parent.parent / 'client_code'
TOP_LEVEL_NAME = "container"
TAB = ' ' * 4


def module_tree(client_code) -> Dict[str, pathlib.Path]:
    module_path = {}
    for init_file in client_code.rglob('__init__.py'):
        form_path = init_file.parent.relative_to(client_code)
        module_path[form_path.name] = form_path
    return module_path


MODULE_PATH: Dict[str, pathlib.Path] = module_tree(CLIENT_CODE_PATH)


def anvil_yaml_schema() -> sy.MapPattern:
    """
    Generates a strictyaml schema

    Returns
    -------
        Schema object
    """
    # schema used by strictyaml to parse the text
    schema = sy.MapPattern(sy.Str(), sy.Any())
    return schema


def build_path(filename, directory) -> pathlib.Path:
    root = directory / filename
    return root


def readfile(filename: str, directory: pathlib.Path) -> Tuple[str, List[str]]:
    """Reads a file and outputs the text and an array of newline characters
    used at the end of each line.

    Parameters
    ----------
    filename : str
    directory : str, optional
        Directory of the file. The default is current directory.

    Returns
    -------
    text :
        File as a str
    n : TYPE
        List of strings that contain the types of new_line characters used in the file.
    """
    fn = build_path(filename, directory)
    n = []
    with fn.open("r") as f:
        lines = f.readlines()
        text = ''.join(lines)  # list(f))
        n.extend(f.newlines)
    return text, n


def yaml_from_file(input_yaml: str, folder: pathlib.Path) -> sy.YAML:
    # if there is anvil.yaml, converts to openapi.yaml
    anvil_yaml_str, newline_list = readfile(input_yaml, folder)
    return sy.dirty_load(yaml_string=anvil_yaml_str, schema=anvil_yaml_schema(), allow_flow_style=True)


def validate_text(value: sy.YAML) -> None:
    if value.text in {'true', 'false'}:
        value.revalidate(sy.Bool())
    elif value.text in {'null'}:
        value.revalidate(sy.NullNone())
    elif value.text in {''}:
        value.revalidate(sy.Str())
    elif set(value.text) <= set('0123456789.'):
        value.revalidate(sy.Float())
    return


def validate_yaml(value: sy.YAML, sequence_key: Union[str, int]) -> None:
    if value[sequence_key].is_mapping():
        if len(value[sequence_key]) == 0:
            value.revalidate(sy.EmptyDict())
        else:
            for key in value[sequence_key]:
                validate_yaml(value[sequence_key], key)
    elif value[sequence_key].is_sequence():
        if len(value[sequence_key]) == 0:
            try:
                value.revalidate(sy.EmptyList())
            except AttributeError:
                del value[sequence_key]
        else:
            for ix in range(len(value[sequence_key])):
                validate_yaml(value[sequence_key], ix)
    elif value[sequence_key].is_scalar():
        validate_text(value[sequence_key])
    else:
        raise TypeError(f"{value[sequence_key]} is not a sequence, mapping or a scalar.")
    return


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


def dict2string(of_dict: Dict) -> str:
    """Converts the ``of_dict`` into a string describing a default conditions for a class."""
    kwargs_template = Template("    $key=$value,\n")
    kwargs_string = ""
    for key, value in of_dict.items():
        if isinstance(value, str):
            value = value.replace('\n', ' ')
            if key != 'parent':
                value = f"'{value}'"
        kwargs_string += kwargs_template.substitute(key=key, value=value)
    return kwargs_string


def only_space(txt):
    clean_txt = []
    for _c in txt:
        if _c in string.whitespace and _c != ' ':
            _c = ' '
        clean_txt.append(_c)
    return ''.join(clean_txt)


def add_properties(value: sy.YAML, parent: str) -> Dict:
    """Adds the YAML 'properties' to `attrs` as key:value pairs."""
    attrs = dict()  # getattr(defaults, value['type'].text, dict())
    if len(value.get('properties', [])) == 0:
        return attrs
    # If validate_yaml is commented out,
    # then there is no check on the correctness of the yaml and other errors can occur.
    validate_yaml(value, 'properties')
    properties_data = value['properties'].data
    try:
        # check that there are no newlines in the text
        txt = properties_data.get("text", None)
        if txt:
            properties_data["text"] = only_space(txt)
        attrs.update(properties_data)
    except AttributeError:
        # if it is a list, the parent is probably a custom component
        for p in properties_data:
            attrs.update(p)
    # add parent class
    attrs.update({'parent': 'Container()'})  # Container(**{parent}) ?
    return attrs


@dataclass
class DataBinding:
    item: str  # usually in the form of `item['font']`
    element: str  # usually in the form of `rich_text1.text`
    writeback: bool


@dataclass
class CatalogCard:
    name: str
    of_type: str
    parent: str
    as_string: str
    data_bindings: List[Dict]


def format_import_list(of_type: str, form_name: str) -> str:
    modules = of_type.split('.')
    # print(len(MODULE_PATH[parent].parts), len(modules))
    nr_dots = '.' * (len(MODULE_PATH[form_name].parts) + 1)
    return f"from {nr_dots}{of_type} import {modules[-1]}"


# def format_import_list(of_type: str, parent:str) -> str:
#     if of_type == 'ActionForm':
#         print(of_type)
#         exit(0)
#     modules = of_type.split('.')
#     return f"from {of_type} import {modules[-1]}"


def add_databindings(value: sy.YAML) -> List[Dict]:
    """    An example of output is :
    `self.__bindings = [{'item': "item['text']", 'element': "text_area.text", 'writeback': True}]`
    """
    return [DataBinding(db['code'].text,
                        value['name'].text + "." + db['property'].text,
                        db.get('writeback', None) is not None).__dict__
            for db in value.get('data_bindings', [])]


def lowest_level_component(value: sy.YAML,
                           parent: str,
                           import_list: List[str],
                           form_name: str) -> CatalogCard:
    """Derives dict from `value`. `value` has to have `type`

    Parameters
    ----------
    value :
    parent :
    import_list :
    """
    name = value['name'].text
    of_type: str = value['type'].text  # raise attribute error if no `type`
    if "form:" in of_type:
        of_type = of_type.replace("form:", '')
        # add to list of imports
        import_list.append(format_import_list(of_type, form_name))
    attrs = add_properties(value, parent)
    attrs_as_string = dict2string(attrs)
    databindings = add_databindings(value)
    # db_as_string = "".join([dict2string(databinding)+",\n" for databinding in databindings])
    return CatalogCard(name=name, of_type=of_type, parent=parent, as_string=attrs_as_string, data_bindings=databindings)


def derive_dict(value: sy.YAML,
                catalog: OrderedDict[str, CatalogCard],
                parent: str,
                import_list: List[str],
                form_name: str) -> None:
    """Organizes the YAML into a nested dict where the keys are the names of the components
    and the YAML 'properties' are attributes.

    Example
    Before:
    dict('components':list({'type':ColumnPanel,'name':'column_panel1',properties:{'role':'blah','text':'My Form'} etc)
    After:
    {'column_panel1':{'type':ColumnPanel, 'role':'blah', 'text':'My Form' etc}

    :param value: The YAML from the `form_template.yaml` file
    :param catalog: This is this function's return. It is a parameter because this function is recursive.
    :param parent:
    :param import_list: Contains the import statement at beginning of file.
    :return: None   (`catalog` is changed)
    """
    top_level = False
    try:
        name = value['name'].text
    except KeyError:
        # add top form name to the catalog too
        name = parent
        top_level = True
    if 'components' in value:
        # go down into the hierarchy
        parent = name
        for component in value['components']:
            # create a dict from each in the component list
            derive_dict(component, catalog, parent, import_list, form_name)
    if top_level:
        # check for properties
        if 'properties' in value:
            for prop in value['properties']:
                cat_card = lowest_level_component(prop, parent, import_list, form_name)
                cat_card.of_type = cat_card.of_type.capitalize()
                catalog[cat_card.name] = cat_card
        value = value.get('container')
        value['name'] = sy.load(TOP_LEVEL_NAME, sy.Str())
    catalog[name] = lowest_level_component(value, parent, import_list, form_name)
    return


def databindings_as_string(databindings) -> str:
    as_str = 'databindings = [\n'
    for d in databindings:
        as_str += f'{TAB}dict(' + dict2string(d).replace('\n', '').replace(TAB, ' ').replace("['", '["').replace("']",
                                                                                                                 '"]') + '),\n'
    as_str += ']'
    return as_str


ItemGetterSetter = namedtuple('ItemGetterSetter', ['defs', 'imports'])
item_getter_setter = ItemGetterSetter("""
    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return
""", "from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict")

def add_properties_to_item() -> str:
    return f"""
{TAB}{TAB}if properties.get('item', None) is not None:
{TAB}{TAB}{TAB}self.item = properties['item']
"""


def form_the__init__str(catalog: OrderedDict[str, CatalogCard], form_name: str) -> Tuple[str, str]:
    """Derives the def __init__() part of the class definition from catalog."""
    attr_string = f"{TAB}def __init__(self, **properties):\n{TAB}{TAB}super({form_name}Template, self).__init__()\n"
    default_string = ""
    databindings = []
    for key, item in catalog.items():
        if key == form_name or len(item.name.split()) == 0:
            continue
        default_string += f"{item.name} = dict(\n{item.as_string})\n"
        _class = item.of_type.split('.')[-1]
        attr_string += f"{TAB}{TAB}self.{key} = {_class}(**{item.name})\n"
        databindings.extend(item.data_bindings)
    # add databindings
    databindings_as_str = databindings_as_string(databindings)
    default_string += databindings_as_str
    attr_string += f"{TAB}{TAB}self._bindings = databindings\n"
    attr_string += f"{TAB}{TAB}self._item = ClassDict()\n"
    attr_string += add_properties_to_item()
    attr_string += item_getter_setter.defs
    return attr_string, default_string


def yaml2definition(parsed: sy.YAML, form_name):
    """Converts the YAML into a string that contains the class definition."""
    import_list = ["from anvil import *",
                   # "from dataclasses import dataclass, field",
                   item_getter_setter.imports
                   ]
    catalog = OrderedDict()
    derive_dict(parsed, catalog, form_name, import_list, form_name)
    attr_string, default_string = form_the__init__str(catalog, form_name)
    class_string = '\n'.join(import_list) + '\n\n' + \
                   default_string + '\n\n' + \
                   f"class {form_name}Template({catalog[form_name].of_type}):\n" + \
                   attr_string
    class_string += f"""
    def init_components(self, **properties):
        {form_name}Template.__init__(self, **properties)
"""
    return class_string
