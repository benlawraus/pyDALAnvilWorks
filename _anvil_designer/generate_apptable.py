import pathlib
from typing import Dict

from _anvil_designer.generate_class import yaml_from_file


def get_tables(parsed):
    table_dict = dict()
    for table_yaml in parsed['db_schema']:
        table_dict[table_yaml.text] = {}
        for column in parsed['db_schema'][table_yaml]['columns']:  # for later, not needed here
            if column['type'] == 'link_single':
                column_type = 'liveObject'
            elif column['type'] == 'link_multiple':
                column_type = 'liveObjectArray'
            else:
                column_type = column['type']
            table_dict[table_yaml.text].update({column['name']: column_type})
    return table_dict


IMPORTS = "from anvil.tables.basefunction import BaseFunction\n\n"


def table_dict2string(table_dict):
    file_str = """class AppTables:
    def __init__(self):
"""
    tab1 = "    "
    for table_name in table_dict.keys():
        table_str = f"{tab1}{tab1}self.{table_name} = BaseFunction('{table_name}', TABLES['{table_name}'])\n"
        file_str += table_str

    file_str += """

app_tables = AppTables()
"""
    return file_str


def list_columns(table_dict: Dict[str, Dict[str, str]]):
    """Outputs dictionaries of the column names and types. To be used in the app_tables.tbl.list_columns() function."""
    tab1 = "    "
    dicts_str = "TABLES = dict(\n"
    for table_name in table_dict.keys():  # type: str
        dict_str = f"{tab1}{table_name}=dict(\n"
        for field_name in table_dict[table_name].keys():
            dict_str += f"{tab1}{tab1}{field_name}='{table_dict[table_name][field_name]}',\n"
        dict_str += f'{tab1}),\n'
        dicts_str += dict_str
    dicts_str += ')\n'
    return dicts_str


def string2AppTables(file_str, main_dir):
    filep = pathlib.Path(main_dir / 'anvil' / 'tables' / 'AppTables.py')
    filep.write_text(file_str)


def yaml2apptable():
    main_dir = pathlib.Path(__file__).parent.parent

    parsed = yaml_from_file('anvil.yaml', main_dir)
    table_dict = get_tables(parsed)
    file_str = table_dict2string(table_dict)
    dicts_str = list_columns(table_dict)
    string2AppTables(IMPORTS + dicts_str + '\n\n' + file_str, main_dir)
    return False


if __name__ == '__main__':
    yaml2apptable()
    if yaml2apptable():
        exit(1)
    exit(0)
