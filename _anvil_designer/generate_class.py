import pathlib
import string
from collections import OrderedDict
from dataclasses import dataclass
from typing import Tuple, List, Dict, Union
import strictyaml as sy
from string import Template

# from collections import defaultdict

TOP_LEVEL_NAME = "container"


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
            value.revalidate(sy.EmptyList())
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
            if key != 'parent':
                value = f"'{value}'"
        kwargs_string += kwargs_template.substitute(key=key, value=value)
    return kwargs_string


def only_space(txt):
    clean_txt = []
    for _c in txt:
        if _c in string.whitespace and _c != ' ':
            continue
        clean_txt.append(_c)
    return ''.join(clean_txt)


def add_properties(value: sy.YAML, parent: str) -> Dict:
    """Adds the YAML 'properties' to `attrs` as key:value pairs."""
    attrs = dict()  # getattr(defaults, value['type'].text, dict())
    if len(value.get('properties', [])) == 0:
        return attrs
    validate_yaml(value, 'properties')
    properties_as_dict = value['properties'].data
    # check that there are no newlines in the text
    txt = properties_as_dict.get("text", None)
    if txt:
        properties_as_dict["text"] = only_space(txt)
    attrs.update(value['properties'].data)
    # add parent class
    attrs.update({'parent': 'Container()'})  # Container(**{parent}) ?
    return attrs


@dataclass
class CatalogCard:
    name: str
    of_type: str
    parent: str
    as_string: str


def lowest_level_component(value: sy.YAML, parent: str, import_list: List[str]) -> CatalogCard:
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
        import_list.append(f"from client_code.{of_type} import {of_type}")
    attrs = add_properties(value, parent)
    attrs_as_string = dict2string(attrs)
    return CatalogCard(name=name, of_type=of_type, parent=parent, as_string=attrs_as_string)


def derive_dict(value: sy.YAML, catalog: OrderedDict, parent: str, import_list: List[str]):
    """

    Parameters
    ----------
    value :
    catalog :
    parent :
    import_list :

    Returns
    -------

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
            derive_dict(component, catalog, parent, import_list)
    if top_level:
        value = value.get('container')
        value['name'] = sy.load(TOP_LEVEL_NAME, sy.Str())
    catalog[name] = lowest_level_component(value, parent, import_list)
    return


def yaml2definition(parsed: sy.YAML, form_name):
    """Organizes the YAML into a nested dict where the keys are the names of the components
    and the YAML 'properties' are attributes.

    Example
    Before:
    dict('components':list({'type':ColumnPanel,'name':'column_panel1',properties:{'role':'blah','text':'My Form'} etc)
    After:
    {'column_panel1':{'type':ColumnPanel, 'role':'blah', 'text':'My Form' etc}
"""
    import_list = ["from _anvil_designer.componentsUI.anvil import *",
                   "from _anvil_designer.componentsUI.anvil import Container",
                   "from dataclasses import dataclass, field"]

    catalog = OrderedDict()
    TAB = '    '
    derive_dict(parsed, catalog, form_name, import_list)
    # create form class
    attr_string = ""
    default_string = ""
    for key, item in catalog.items():
        if key == form_name:
            continue
        default_string += f"{item.name} = dict(\n{item.as_string})\n"
        attr_string += f"{TAB}{key}: {item.of_type} = field(default_factory=lambda: {item.of_type}(**{item.name}))\n"
    class_string = '\n'.join(import_list) + '\n\n' + \
                   default_string + '\n\n' + \
                   f"@dataclass\nclass {form_name}Template({catalog[form_name].of_type}):\n" + \
                   attr_string
    class_string += f"""
    def init_components(self, **kwargs):
        {form_name}Template.__init__(self)
"""
    return class_string
