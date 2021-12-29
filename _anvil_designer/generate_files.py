import pathlib
from _anvil_designer.generate_class import yaml2definition, yaml_from_file, build_path


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
