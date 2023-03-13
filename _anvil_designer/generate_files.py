import pathlib
from typing import Dict

from _anvil_designer.generate_class import yaml2definition, yaml_from_file, build_path

class ModuleDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self:
            super().__setitem__(key, value)
        else:
            pass

def module_tree(client_code)->Dict[str:pathlib.Path]:
    """Forms a dictionary of all the modules {module_name:module_hierarchy, ..} where
    module_hierarchy is the path relative to the dir 'client_code'"""
    module_path = {}
    for init_file in client_code.rglob('__init__.py'):
        form_path = init_file.parent.relative_to(client_code)
        module_path[form_path.name] = form_path
    return module_path

def yaml2classes():
    client_code = pathlib.Path(__file__).parent.parent / 'client_code'
    for yaml_file in client_code.rglob('*.yaml'):
        form_name = yaml_file.parent.name
        parsed = yaml_from_file('form_template.yaml', yaml_file.parent)
        file_string = yaml2definition(parsed, form_name)
        # write the models out to the local folder.
        _anvil_designer_path = build_path('_anvil_designer.py',
                                          yaml_file.parent)
        _anvil_designer_path.write_text(file_string)
    return False


if __name__ == '__main__':
    if yaml2classes():
        exit(1)
    exit(0)
