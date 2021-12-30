import pathlib

from _anvil_designer.definitions import ANVIL_TYPES
from _anvil_designer.generate_class import yaml_from_file

def get_tables(parsed):
    table_dict = dict()
    for table_yaml in parsed['db_schema']:
        table_dict[table_yaml.text]={}
        for column in parsed['db_schema'][table_yaml]['columns']:  # for later, not needed here
            table_dict[table_yaml.text].update({column['name'] : ANVIL_TYPES[column['type']]})
    return table_dict

def table_dict2string(table_dict):
    file_str = """from anvil.tables.basefunction import BaseFunction


class AppTables:
    def __init__(self):
"""
    tab1 = "    "
    for table_name in table_dict.keys():
        table_str = f"{tab1}{tab1}self.{table_name} = BaseFunction('{table_name}')\n"
        file_str += table_str

    file_str += """

app_tables = AppTables()
"""
    return file_str

def string2AppTables(file_str, main_dir):
    filep = pathlib.Path(main_dir / 'anvil'/'tables' / 'AppTables.py')
    filep.write_text(file_str)



def yaml2apptable():
    main_dir = pathlib.Path(__file__).parent.parent

    parsed = yaml_from_file('anvil.yaml', main_dir)
    table_dict = get_tables(parsed)
    file_str = table_dict2string(table_dict)
    string2AppTables(file_str, main_dir)

    return False

if __name__ == '__main__':
    yaml2apptable()
