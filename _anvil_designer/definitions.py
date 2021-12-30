from typing import Dict

ANVIL_TYPES: Dict[str, str] = {'string': '""',
                 'datetime': 'datetime()',
                 'date': 'date()',
                 'number': '0',
                 'bool': 'True',
                 'link_single': '""',
                 'simpleObject': '{}',
                 'link_multiple': '[]',
                 }