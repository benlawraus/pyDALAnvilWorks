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
def alias(new_user_id, previous_id, options):
    """Combines two previously unassociated user identities. (previous_id defaults to the current user)"""
    pass
def group(group_id, traits, options):
    """Identify this user as a member of a group"""
    pass
def identify(user_id, traits, options):
    """Identify a user to associate subsequent actions to a recognisable user ID and traits"""
    pass
def page(category, name, options):
    """Register a virtual page change"""
    pass
def track(event, properties, options):
    """Track an action performed by the current user"""
    pass
