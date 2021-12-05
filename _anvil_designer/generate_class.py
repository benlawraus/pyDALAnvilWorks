import pathlib
from dataclasses import dataclass
from typing import Tuple, List, Dict
import strictyaml as sy

from string import Template


@dataclass
class Class_Bookkeeping:
    dict_str = \
        """
class GenericTemplate:
    def init_components(self, **kwargs):
        super().__init__()        
        pass
"""
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


def validate(value):
    for key in value['properties']:
        if value['properties'][key].text in {'true', 'false'}:
            value['properties'][key].revalidate(sy.Bool())
        elif value['properties'][key].text in {'null'}:
            value['properties'][key].revalidate(sy.NullNone())
        elif value['properties'][key].text in {''}:
            value['properties'][key].revalidate(sy.Str())
        elif set(value['properties'][key].text) <= set('0123456789.'):
            value['properties'][key].revalidate(sy.Float())
    return


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


def write_a_class(dict_name: str, of_dict: Dict, dict_list: List[str], base_class=''):
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
    return f"""
class {class_name}({base_class}):
{kwargs_string}
"""


def write_a_child_class(dict_name: str, of_dict: Dict, dict_list: List[str], base_class=''):
    if dict_name[0].islower():
        class_name = to_camel_case(dict_name)
    else:
        class_name = dict_name

    kwargs_template = Template("    $key=$value")
    kwargs_string = ""
    for key, value in of_dict.items():
        write_this_to_base_class = False
        if isinstance(value, str):
            if len(value) > 0 and value in dict_list:
                value = value + f"()"
            else:
                value = f"'{value}'"
        elif isinstance(value, dict) or value in dict_list:
            value = to_camel_case(key) + "()"
            write_this_to_base_class = True
        else:
            pass
        if write_this_to_base_class:
            if len(base_class) > 0:
                base_class += ', '
            base_class += value.replace("()", "")
        else:
            if len(kwargs_string) > 0:
                kwargs_string += "\n"
            kwargs_string += kwargs_template.substitute(key=key, value=value)
    return f"""
class {class_name}({base_class}):
{kwargs_string}
"""


def derive_dict(value: sy.YAML, bookkeeping: Class_Bookkeeping):
    if 'components' not in value:
        if value['type'].text == "TextBox":
            attrs = TextBox
        else:
            validate(value)
            attrs = value['properties'].data
        bookkeeping.dict_str += write_a_class(value['name'].text, attrs, bookkeeping.dict_list)
        # add to list
        bookkeeping.dict_list.append(to_camel_case(value['name'].text))
        return attrs, dict()
    else:
        instance_dict = dict()
        str_dict = dict()
        for _y in value['components']:
            inst_dict,s_dict = derive_dict(_y, bookkeeping)
            instance_dict[_y['name'].text] = inst_dict
            str_dict[_y['name'].text] = to_camel_case(_y['name'].text)
            if len(s_dict)>0:
                str_dict.update(s_dict)
        if value['type'].text == "ColumnPanel":
            instance_dict[value['name'].text] = ColumnPanel
            bookkeeping.dict_str += write_a_class(value['name'].text, ColumnPanel, bookkeeping.dict_list)
        else:
            # TODO
            raise(UserWarning("Haven't done this yet!"))
        str_dict[value['name'].text] = to_camel_case(value['name'].text)
        bookkeeping.dict_list.append(to_camel_case(value['name'].text))
        return instance_dict,str_dict


def convert_yaml_file_to_dict(form_name: str, bookkeeping: Class_Bookkeeping):
    file_name = 'form_template.yaml'
    folder = pathlib.Path(__file__).parent.parent / 'client_code' / form_name
    parsed = yaml_from_file(file_name, folder)
    value = parsed['components']
    all_comp = dict()
    if len(parsed['components']) == 1:
        if parsed['components'][0]['name'] == "content_panel":
            value = parsed['components'][0]['components']
            all_comp["content_panel"] = ColumnPanel
    bookkeeping.dict_str += write_a_class("content_panel", ColumnPanel, bookkeeping.dict_list)
    for p in value:
        _dict,_str_dict = derive_dict(p, bookkeeping)
        all_comp[p['name'].text] = to_camel_case(p['name'].text)  # _dict
        if len(_str_dict)>0:
            all_comp.update(_str_dict)
    return all_comp
