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
class Transaction():
	def __enter__(self):
		"""Begin the transaction		"""
		pass
	def __exit__(self):
		"""End the transaction		"""
		pass
	def abort(self):
		"""Abort this transaction. When it ends, all write operations performed during it will be cancelled		"""
		pass
	pass
def get_connection_string(via_host=None, via_port=None):
    """Get a Postgres connection string for accessing this app’s Data Tables via SQL.The returned string includes temporary login credentials and sets the search path to a schema representing this app’s Data Table environment.You can override the host and port for the database connection to connect via a secure tunnel.(Available on the Dedicated Plan only.)"""
    pass
def in_transaction(function, server_function):
    """When applied to a function (as a decorator), the whole function will run in a data tables transaction. If it conflicts with another transaction, it will retry up to five times."""
    pass
def order_by(column_name, ascending):
    """Sort the results of this table search by a particular column. Default to ascending order."""
    pass
