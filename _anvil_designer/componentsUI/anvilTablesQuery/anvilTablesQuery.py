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
def all_of(*query_expressions):
    """Match all query parameters given as arguments and keyword arguments"""
    pass
def any_of(*query_expressions):
    """Match any query parameters given as arguments and keyword arguments"""
    pass
def between(min, max, min_inclusive=True, max_inclusive=False):
    """Match values between the provided min and max, optionally inclusive."""
    pass
def full_text_match(query, raw=False):
    """Match values that match the provided full-text search query."""
    pass
def greater_than(value):
    """Match values greater than the provided value."""
    pass
def greater_than_or_equal_to(value):
    """Match values greater than or equal to the provided value."""
    pass
def ilike(pattern):
    """Match values using a case-insensitive ILIKE query, using the % wildcard character."""
    pass
def less_than(value):
    """Match values less than the provided value."""
    pass
def less_than_or_equal_to(value):
    """Match values less than or equal to the provided value."""
    pass
def like(pattern):
    """Match values using a case-sensitive LIKE query, using the % wildcard character."""
    pass
def none_of(*query_expressions):
    """Match none of the query parameters given as arguments and keyword arguments"""
    pass
def not_(*query_expressions):
    """Match none of the query parameters given as arguments and keyword arguments"""
    pass
