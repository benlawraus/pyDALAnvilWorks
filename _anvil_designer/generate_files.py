from _anvil_designer.generate_class import build_path, convert_yaml_file_to_dict, write_a_class, \
    Class_Bookkeeping, yaml_from_file
import pathlib


def yaml2class():
    """Derives `_anvil_designer.py` from the corresponding `form_template.yaml`

    Called only when import fails."""
    bookkeeping = Class_Bookkeeping()

    # get the yaml
    # using yaml create a class
    # read in the yaml
    client_code = pathlib.Path(__file__).parent.parent / 'client_code'
    for yaml_file in client_code.rglob('*.yaml'):
        # if build_path('_anvil_designer.py', yaml_file.parent).exists():
        #     continue
        form_name = yaml_file.parent.name
        parsed = yaml_from_file('form_template.yaml', yaml_file.parent)
        all_components = convert_yaml_file_to_dict(parsed, bookkeeping)
        container_class = all_components.pop('top_level')
        bookkeeping.dict_str += write_a_class(
            form_name+"Template",
            all_components,
            bookkeeping.dict_list,
            base_class=f"{container_class}, GenericTemplate")
        # write the models out to the local folder.
        _anvil_designer_path = build_path('_anvil_designer.py',
                                          yaml_file.parent)
        _anvil_designer_path.write_text(bookkeeping.dict_str)
    return

if __name__ == '__main__':
    yaml2class()