from _anvil_designer.generate_class import yaml_from_file, build_path, convert_yaml_file_to_dict, write_a_class, \
    Class_Bookkeeping
import pathlib
import importlib
import importlib.util

__all__ = dict()


def __getattr__(name: str):
    if True:
        bookkeeping = Class_Bookkeeping()

        # get the yaml
        # using yaml create a class
        # read in the yaml
        form_name = name.split('Template')[0]
        all_components = convert_yaml_file_to_dict(form_name, bookkeeping)
        bookkeeping.dict_str += write_a_class(
            name,
            all_components,
            bookkeeping.dict_list,
            base_class="GenericTemplate, GenericPanel")
        # write the models out to the local folder.
        _anvil_designer_path = build_path('_anvil_designer.py', pathlib.Path(__file__).parent.parent / 'client_code' / form_name)
        _anvil_designer_path.write_text(bookkeeping.dict_str)
        # add the class to __all__
        module_obj = importlib.import_module(f"client_code.{form_name}._anvil_designer")
        __all__.update({name: getattr(module_obj, name)})
        # return the class
    if name in __all__:
        return __all__[name]
    raise AttributeError(name)
