import pathlib
from collections import OrderedDict
from dataclasses import dataclass
from typing import Tuple, List, Dict, Union
import strictyaml as sy

from string import Template

GENERIC_COMPONENT = """
class GenericComponent:
    def scroll_into_view(self):
        return

    def add_event_handler(*args,**kwargs):
        return
"""

GENERIC_PANEL = """
class GenericDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key)
                
class GenericPanel:
    item = GenericDict()
    
    def add_component(self, *args, **kwargs):
        return
        
    def clear(self):
        return
        
    def add_event_handler(self, *args,**kwargs):
        return

    def set_event_handler(self, *args,**kwargs):
        return

    def get_event_handlers(self, *args,**kwargs):
        return
    
    def parent(self, *args,**kwargs):
        return
"""

GENERIC_TEMPLATE = """
class GenericTemplate:
    def init_components(self, **kwargs):
        super().__init__()        
        pass
"""

TOP_LEVEL_NAME = "container"


@dataclass
class Class_Bookkeeping:
    dict_str = \
        f"""{GENERIC_COMPONENT}

{GENERIC_PANEL}
        
{GENERIC_TEMPLATE}"""
    dict_list = []


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
    root = pathlib.Path.cwd() / directory / filename
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


Link = dict(
    url='',
    text='',
    align='left',
    font_size=None,
    font='Arial',
    bold=False,
    italic=False,
    underline=False,
    icon='',
    icon_align='left',
    tooltip='',
    tag=None
)

TextBox = dict(
    enabled=True,
    text="",
    visible=True,
    align="left",
    background="#ff0000",
    bold=False,
    border="1px solid #888888",
    font="Arial",
    font_size=16,
    foreground="#ff0000",
    hide_text=False,
    italic=False,
    placeholder="Enter text here",
    role="default",
    spacing_above="small",
    spacing_below="small",
    tag='',
    tooltip="",
    type="text",
    underline=False)

ColumnPanel = dict(
    visible=True,
    wrap_on="mobile",
    background="#ff0000",
    bold=False,
    border="1px solid #888888",
    col_spacing="medium",
    col_widths='',
    foreground="#ff0000",
    role="default",
    spacing_above="small",
    spacing_below="small",
    tag="",
    tooltip=""
)

HtmlTemplate = ColumnPanel
DataRowPanel = ColumnPanel
DataGrid = ColumnPanel


# FUNCTIONS = {"add_component"}


def validate_text(value: sy.YAML) -> None:
    if value.text in {'true', 'false'}:
        value.revalidate(sy.Bool())
    elif value.text in {'null'}:
        value.revalidate(sy.NullNone())
    elif value.text in {''}:
        value.revalidate(sy.Str())
    # elif value.text in FUNCTIONS:
    #     value.revalidate(sy.ScalarValidator)
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


def write_a_class(dict_name: str, of_dict: Dict, dict_list: List[str], base_class='') -> str:
    """Converts the ``of_dict`` into a string describing a class."""
    if dict_name[0].islower():
        class_name = to_camel_case(dict_name)
    else:
        class_name = dict_name

    kwargs_template = Template("    $key=$value")
    kwargs_string = ""
    for key, value in of_dict.items():
        if len(kwargs_string) > 0:
            kwargs_string += "\n"
        if isinstance(value, str):
            if len(value) > 0 and value in dict_list:
                value = value + f"()"
            else:
                value = f"'{value}'"
        elif isinstance(value, dict) or value in dict_list:
            value = to_camel_case(key) + f"()"
        else:
            pass
        kwargs_string += kwargs_template.substitute(key=key, value=value)
    if kwargs_string == "":
        kwargs_string="    pass"
    return f"""
class {class_name}({base_class}):
{kwargs_string}
"""


def lowest_level_component(value: sy.YAML, bookkeeping: Class_Bookkeeping):
    if value['type'].text == "TextBox":
        attrs = TextBox
        if 'properties' in value and len(value['properties']) > 0:
            validate_yaml(value, 'properties')
            attrs.update(value['properties'].data)
        bookkeeping.dict_str += write_a_class(value['name'].text, attrs, bookkeeping.dict_list,
                                              base_class="GenericComponent")
    elif value['type'].text in ("ColumnPanel", "HtmlTemplate", "Link", "DataGrid", "DataRowPanel"):
        attrs = globals().get(value['type'].text)
        if 'properties' in value and len(value['properties']) > 0:
            validate_yaml(value, 'properties')
            attrs.update(value['properties'].data)
        if 'name' not in value:
            value['name'] = sy.load(TOP_LEVEL_NAME, sy.Str())
        bookkeeping.dict_str += write_a_class(value['name'].text, attrs, bookkeeping.dict_list,
                                              base_class="GenericPanel")
    else:
        if 'properties' in value and len(value['properties']) > 0:
            validate_yaml(value, 'properties')
            attrs = value['properties'].data
        else:
            attrs = OrderedDict()
        bookkeeping.dict_str += write_a_class(value['name'].text, attrs, bookkeeping.dict_list,
                                              base_class="GenericComponent")
    # add to list
    bookkeeping.dict_list.append(to_camel_case(value['name'].text))
    return attrs, dict()


def derive_dict(value: sy.YAML, bookkeeping: Class_Bookkeeping):
    if 'components' not in value:
        if 'type' in value:
            return lowest_level_component(value, bookkeeping)
        if 'container' in value:
            return lowest_level_component(value['container'], bookkeeping)
    else:
        # go down into the hierarchy
        instance_dict = dict()
        str_dict = dict()
        for _y in value['components']:
            # create a dict from each in the component list
            inst_dict, s_dict = derive_dict(_y, bookkeeping)
            # instead of making a list of these dicts, make a dict of dict
            instance_dict[_y['name'].text] = inst_dict
            str_dict[_y['name'].text] = to_camel_case(_y['name'].text)
            if len(s_dict) > 0:
                str_dict.update(s_dict)
        value.__delitem__('components')
        attrs, _ = lowest_level_component(value, bookkeeping)
        instance_dict[value['name'].text] = attrs
        str_dict[value['name'].text] = to_camel_case(value['name'].text)
        return instance_dict, str_dict


def convert_yaml_file_to_dict(parsed: sy.YAML, bookkeeping: Class_Bookkeeping):
    value = parsed['components']
    all_comp = dict()
    for p in value:
        _dict, _str_dict = derive_dict(p, bookkeeping)
        all_comp[p['name'].text] = to_camel_case(p['name'].text)  # _dict
        if len(_str_dict) > 0:
            all_comp.update(_str_dict)
    # container without its components
    parsed.__delitem__('components')
    _dict, _str_dict = derive_dict(parsed, bookkeeping)
    all_comp['top_level'] = to_camel_case(TOP_LEVEL_NAME)
    if len(_str_dict) > 0:
        all_comp.update(_str_dict)
    return all_comp
