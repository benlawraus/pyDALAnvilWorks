from _anvil_designer.generate_class import CLIENT_CODE_PATH, build_path, yaml2definition, yaml_from_file


class ModuleDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self:
            super().__setitem__(key, value)
        else:
            pass


def yaml2classes():
    for yaml_file in CLIENT_CODE_PATH.rglob('*.yaml'):
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
