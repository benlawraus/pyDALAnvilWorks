import pathlib
import sys

path_name = pathlib.Path(__file__).parent.parent / 'client_code'

if str(path_name) not in sys.path:
    sys.path.append(str(path_name))

path_name = pathlib.Path(__file__).parent.parent / 'server_code'

if str(path_name) not in sys.path:
    sys.path.append(str(path_name))

path_name = pathlib.Path(__file__).parent.parent
print(path_name)
if str(path_name) not in sys.path:
    sys.path.append(str(path_name))
