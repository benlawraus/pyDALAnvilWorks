from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

def default_val(val):
    return lambda: val
String = str
Number = float
Integer = int
Color = str
Boolean = bool
Themerole = str
Object = object
Seconds = float
Items = List[Dict]
Datagridcolumns = List[str]
Pixels = int
Uri = str
Html = str
Icon = str
Form = object

@dataclass
class SecretError():
	pass
def decrypt_with_key(key_name, value):
    """Decrypt a string with a cryptographic key derived from the named secret"""
    pass
def encrypt_with_key(key_name, value):
    """Encrypt a string with a cryptographic key derived from the named secret"""
    pass
def get_secret(secret_name):
    """Retrieve the named secret"""
    pass
