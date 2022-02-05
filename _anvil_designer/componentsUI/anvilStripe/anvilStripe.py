from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from ...common_structures import ClassDict


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
Items = list
Datagridcolumns = list
Pixels = int
Uri = str
Html = str
Icon = str
Form = object
def get_customer(customer_id):
    """Retrieve a Stripe Customer record by its ID"""
    pass
def new_customer(email_address, token):
    """Create a new Stripe Customer record"""
    pass
