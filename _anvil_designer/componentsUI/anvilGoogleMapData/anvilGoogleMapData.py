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
class Feature():
	def to_geo_json(self):
		"""Exports this feature as a GeoJSON object.		"""
		pass
	pass

@dataclass
class Geometry():
	def get_type(self):
		"""Returns the type of the geometry object.		"""
		pass
	pass

@dataclass
class GeometryCollection(Geometry):
	def get_array(self):
		"""Returns an array of the contained Geometries. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained Geometry.		"""
		pass
	def get_length(self):
		"""Returns the number of contained Geometries.		"""
		pass
	pass

@dataclass
class LinearRing(Geometry):
	def get_array(self):
		"""Returns an array of the contained LatLngs. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained LatLng.		"""
		pass
	def get_length(self):
		"""Returns the number of contained LatLngs.		"""
		pass
	pass

@dataclass
class LineString(Geometry):
	def get_array(self):
		"""Returns an array of the contained LatLngs. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained LatLng.		"""
		pass
	def get_length(self):
		"""Returns the number of contained LatLngs.		"""
		pass
	pass

@dataclass
class MultiLineString(Geometry):
	def get_array(self):
		"""Returns an array of the contained Data.LineStrings. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained Data.LineString.		"""
		pass
	def get_length(self):
		"""Returns the number of contained Data.LineStrings.		"""
		pass
	pass

@dataclass
class MultiPoint(Geometry):
	def get_array(self):
		"""Returns an array of the contained LatLngs. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained LatLng.		"""
		pass
	def get_length(self):
		"""Returns the number of contained LatLngs.		"""
		pass
	pass

@dataclass
class MultiPolygon(Geometry):
	def get_array(self):
		"""Returns an array of the contained Polygons. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained Polygon.		"""
		pass
	def get_length(self):
		"""Returns the number of contained Polygons.		"""
		pass
	pass

@dataclass
class Point(Geometry):
	def get(self):
		"""Returns the contained LatLng.		"""
		pass
	pass

@dataclass
class Polygon(Geometry):
	def get_array(self):
		"""Returns an array of the contained LinearRings. A new array is returned each time get_array() is called.		"""
		pass
	def get_at(self, n):
		"""Returns the n-th contained LinearRing.		"""
		pass
	def get_length(self):
		"""Returns the number of contained LinearRings.		"""
		pass
	pass

@dataclass
class StyleOptions():
	pass
