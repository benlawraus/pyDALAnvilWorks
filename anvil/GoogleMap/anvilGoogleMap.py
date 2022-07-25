from dataclasses import dataclass, field
from typing import List, Dict

from ..component import *
from _anvil_designer.common_structures import *


@dataclass
class Icon:
    pass


@dataclass
class LatLng:
    def lat(self):
        """Returns the latitude in degrees.		"""
        pass

    def lng(self):
        """Returns the longitude in degrees.		"""
        pass

    pass


@dataclass
class StrokePosition():
    pass


@dataclass
class Size():
    pass


@dataclass
class Animation():
    pass


@dataclass
class Symbol():
    pass


@dataclass
class MarkerLabel():
    pass


@dataclass
class LatLngBounds():
    def contains(self, point):
        """Returns True if the given lat/lng is in this bounds.		"""
        pass

    def equals(self, other):
        """Returns True if this bounds approximately equals the given bounds.		"""
        pass

    def extend(self, point):
        """Extends this bounds to contain the given point.		"""
        pass

    def get_center(self):
        """Computes the center of this LatLngBounds		"""
        pass

    def get_north_east(self):
        """Returns the north-east corner of this bounds.		"""
        pass

    def get_south_west(self):
        """Returns the south-west corner of this bounds.		"""
        pass

    def intersects(self, other):
        """Returns True if this bounds shares any points with the other bounds.		"""
        pass

    def is_empty(self):
        """Returns True if the bounds are empty.		"""
        pass

    def to_json(self):
        """Converts to JSON representation.		"""
        pass

    def to_span(self):
        """Converts the given map bounds to a lat/lng span.		"""
        pass

    def to_url_value(self, precision=6):
        """Returns a string of the form ‘lat_lo,lng_lo,lat_hi,lng_hi’ for this bounds.		"""
        pass

    def union(self, other):
        """Extends this bounds to contain the union of this and the given bounds.		"""
        pass

    pass


@dataclass
class AbstractOverlay(Component):
    clickable: Boolean = field(default_factory=Boolean)  # True if this overlay raises mouse events.
    draggable: Boolean = field(default_factory=Boolean)  # True if this overlay can be dragged.
    parent: Container = field(default_factory=Container)  #
    visible: Boolean = field(default_factory=Boolean)  # True if this overlay should be displayed.
    z_index: Number = field(default_factory=Number)  # The z-index compared to other overlays.

    def add_component(self, map_component):
        """Add a map component to this GoogleMap		"""
        pass

    def fit_bounds(self, lat_lng_bounds, padding):
        """Sets the viewport to contain the given bounds. Adds some padding around the bounds by default - set
        padding to 0 to match the bounds exactly. """
        pass

    def get_bounds(self):
        """Returns the lat/lng bounds of the current viewport.		"""
        pass

    def pan_by(self, dx, dy):
        """Changes the center of the map by the given distance in pixels.		"""
        pass

    def pan_to(self, position):
        """Changes the center of the map to the given LatLng position.		"""
        pass

    def pan_to_bounds(self, lat_lng_bounds, padding):
        """Pans the map by the minimum amount necessary to contain the given LatLngBounds. Adds some padding around
        the bounds by default - set padding to 0 to match the bounds exactly. """
        pass

    pass


@dataclass
class Circle(AbstractOverlay):
    center: LatLng = field(default_factory=LatLng)  # The center of the Circle.
    editable: Boolean = field(default_factory=Boolean)  # True if this overlay can be edited by the user.
    fill_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    fill_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    parent: Container = field(default_factory=Container)  #
    radius: Number = field(default_factory=Number)  # The radius of the Circle.
    stroke_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    stroke_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    stroke_position: StrokePosition = field(default_factory=StrokePosition)  # The stroke position. Defaults to CENTER.
    stroke_weight: Number = field(default_factory=Number)  # The weight of the overlay outline
    pass


@dataclass
class ControlPosition():
    pass


@dataclass
class Data():
    def add(self, feature, geometry, id, properties):
        """Adds a feature to the collection, and returns the added feature.		"""
        pass

    def add_geo_json(self, geo_json, id_property_name=id):
        """Adds GeoJSON features to the collection. Give this method a parsed JSON. The imported features are
        returned. """
        pass

    def contains(self, feature):
        """Checks whether the given feature is in the collection.		"""
        pass

    def get_feature_by_id(self, id):
        """Returns the feature with the given ID, if it exists in the collection.		"""
        pass

    def load_geo_json(self, url, id_property_name=id):
        """Loads GeoJSON from a URL, and adds the features to the collection.		"""
        pass

    def override_style(self, feature, clickable, cursor, draggable, editable, fillColor, fillOpacity, icon, shape,
                       strokeColor, strokeOpacity, strokeWeight, title, visible, zIndex):
        """Sets the style for all features in the collection. Styles specified on a per-feature basis via
        override_style() continue to apply. """
        pass

    def remove(self, feature):
        """Removes a feature from the collection.		"""
        pass

    def revert_style(self, feature):
        """Removes the effect of previous override_style() calls. The style of the given feature reverts to the style
        specified by set_style(). """
        pass

    def to_geo_json(self):
        """Exports the features in the collection to a GeoJSON object.		"""
        pass

    pass


@dataclass
class FullscreenControlOptions():
    pass


@dataclass
class GeocoderAddressComponent():
    pass


@dataclass
class GeocoderGeometry():
    pass


@dataclass
class GeocoderLocationType():
    pass


@dataclass
class GeocoderResult():
    pass


@dataclass
class IconSequence():
    pass


@dataclass
class InfoWindow(Component):
    """
    GoogleMap.InfoWindow

    Display a popup on the map at a particular position.

    Properties

    position: GoogleMap.LatLng - Specifies the position of the popup. Not required if this popup is anchored to a component (see the open method, below).
    content: anvil.Component | string - The content of the popup. Can be a string, or an Anvil Component.
    """
    content: Component = field(default_factory=Component)  # Content to display in the InfoWindow.
    disable_auto_pan: Boolean = field(default_factory=Boolean)  # Disable auto-pan on open.
    max_width: Number = field(default_factory=Number)  # Maximum width of the infowindow, regardless of content’s width.
    parent: Container = field(default_factory=Container)  #
    pixel_offset: Size = field(
        default_factory=Size)  # The offset, in pixels, of the tip of the info window from the point on the map at whose geographical coordinates the info window is anchored.
    position: LatLng = field(default_factory=LatLng)  # The LatLng at which to display this InfoWindow.
    z_index: Number = field(
        default_factory=Number)  # All InfoWindows are displayed on the map in order of their zIndex, with higher values displaying in front of InfoWindows with lower values.

    def open(self, map, anchor=None):
        """ Display this InfoWindow on the specified map. If anchor is specified, the InfoWindow does not need to have its own position property set."""
        pass

    def close(self):
        """ Hide this InfoWindow. The user can also cause this to happen by clicking the close button in the top-right of the popup."""
        pass


@dataclass
class LatLngBoundsLiteral():
    pass


@dataclass
class LatLngLiteral():
    pass


@dataclass
class MapTypeControlOptions():
    pass


@dataclass
class MapTypeControlStyle():
    pass


@dataclass
class MapTypeId():
    pass


@dataclass
class Marker(AbstractOverlay):
    animation: Animation = field(default_factory=Animation)  # The animation of this Marker.
    cursor: String = field(default_factory=String)  # The cursor to display over this Marker.
    icon: Symbol = field(default_factory=Symbol)  # The icon to display at the position of this Marker.
    label: MarkerLabel = field(default_factory=MarkerLabel)  # The label to display on this Marker.
    opacity: Number = field(default_factory=Number)  # The opacity of this Marker.
    parent: Container = field(default_factory=Container)  #
    position: LatLng = field(default_factory=LatLng)  # The LatLng position of this Marker
    title: String = field(default_factory=String)  # The tooltip text for this Marker.
    pass


@dataclass
class MotionTrackingControlOptions():
    pass


@dataclass
class Point():
    pass


@dataclass
class Polygon(AbstractOverlay):
    editable: Boolean = field(default_factory=Boolean)  # True if this overlay can be edited by the user.
    fill_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    fill_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    geodesic: Boolean = field(
        default_factory=Boolean)  # When true, edges of the polygon are interpreted as geodesic and will follow the curvature of the Earth.
    parent: Container = field(default_factory=Container)  #
    path: List[LatLng] = field(
        default_factory=List[LatLng])  # The ordered sequence of LatLng coordinates of the Polygon.
    stroke_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    stroke_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    stroke_position: StrokePosition = field(default_factory=StrokePosition)  # The stroke position. Defaults to CENTER.
    stroke_weight: Number = field(default_factory=Number)  # The weight of the overlay outline
    pass


@dataclass
class Polyline(AbstractOverlay):
    editable: Boolean = field(default_factory=Boolean)  # True if this overlay can be edited by the user.
    geodesic: Boolean = field(
        default_factory=Boolean)  # When true, edges of the polygon are interpreted as geodesic and will follow the curvature of the Earth.
    icons: String = field(default_factory=String)  # The icons to be rendered along the polyline.
    parent: Container = field(default_factory=Container)  #
    path: List[LatLng] = field(
        default_factory=List[LatLng])  # The ordered sequence of LatLng coordinates of the Polyline.
    stroke_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    stroke_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    stroke_weight: Number = field(default_factory=Number)  # The weight of the overlay outline
    pass


@dataclass
class Rectangle(AbstractOverlay):
    bounds: LatLngBounds = field(default_factory=LatLngBounds)  # The bounds of the Rectangle.
    editable: Boolean = field(default_factory=Boolean)  # True if this overlay can be edited by the user.
    fill_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    fill_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    parent: Container = field(default_factory=Container)  #
    stroke_color: String = field(default_factory=String)  # The color to draw the overlay outline.
    stroke_opacity: Number = field(default_factory=Number)  # The opacity of the overlay outline.
    stroke_position: StrokePosition = field(default_factory=StrokePosition)  # The stroke position. Defaults to CENTER.
    stroke_weight: Number = field(default_factory=Number)  # The weight of the overlay outline
    pass


@dataclass
class RotateControlOptions():
    pass


@dataclass
class ScaleControlOptions():
    pass


@dataclass
class StreetViewControlOptions():
    pass


@dataclass
class SymbolPath():
    pass


@dataclass
class ZoomControlOptions():
    pass
