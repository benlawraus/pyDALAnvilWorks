from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from _anvil_designer.common_structures import ClassDict


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
