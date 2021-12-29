from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

from _anvil_designer.componentsUI.GoogleMap import GoogleMap
from _anvil_designer.componentsUI.anvil import Component,Container,Media
from math import pi as PI


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
class BlobMedia(Media):
	pass

@dataclass
class Button(Component):
	align:String=None		#  The position of this button in the available space.
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	icon:Icon=None		#  The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.
	icon_align:String=None		#  The alignment of the icon on this component. Set to ‘top’ for a centred icon on a component with no text.
	italic:Boolean=None		#  Display this component’s text in italics
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Button, or “default” to have the width set by the container.
	pass

@dataclass
class Canvas(Component):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	fill_style:String=None		#  The color or gradient to use when filling shapes and paths.
	font:String=None		#  The font to use when drawing text on this canvas.
	foreground:Color=None		#  The foreground colour of this component.
	global_alpha:Number=None		#  The global opacity to draw with, in the range 0-1.
	global_composite_operation:Number=None		#  The global composite operation to draw with. Defaults to ‘source-over’
	height:String=None		#  The height of this component.
	line_cap:String=None		#  The line cap to use when drawing lines on this canvas.
	line_join:String=None		#  The line join to use when connecting lines on this canvas.
	line_width:Number=None		#  The width of lines drawn on this canvas.
	miter_limit:Pixels=None		#  The limit of line join miters, in pixels.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	shadow_blur:Pixels=None		#  The required shadow blur, in pixels.
	shadow_color:String=None		#  The color to use for shadows.
	shadow_offset_x:Pixels=None		#  The horizontal shadow offset, in pixels.
	shadow_offset_y:Pixels=None		#  The vertical shadow offset, in pixels.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	stroke_style:String=None		#  The color or gradient to use when drawing outlines.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text_align:String=None		#  Text alignment, relative to the drawing point.
	text_baseline:String=None		#  Text baseline, relative to the drawing point.
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Canvas, or “default” to have the width set by the container.
	def arc(self, x, y, radius, start_angle=0, end_angle=PI*2, anticlockwise=False):
		"""Adds an arc to the end of the current path with specified center and radius.		"""
		pass
	def begin_path(self):
		"""Begin a path on the canvas.		"""
		pass
	def bezier_curve_to(self, cp1x, cp1y, cp2x, cp2y, x, y):
		"""Adds a Bezier curve at the end of the current path to (x,y) with control points (cp1x,cp1y) and (cp2x,cp2y).		"""
		pass
	def clear_rect(self, x, y, width, height):
		"""Clear the specified rectangle with the background color of the canvas.		"""
		pass
	def clip(self):
		"""Turn the current path into the clipping region of the canvas.		"""
		pass
	def close_path(self):
		"""Close the current path with a straight line back to the start point.		"""
		pass
	def create_linear_gradient(self, x0, y0, x1, y1):
		"""Returns a gradient object representing a linear gradient from (x0,y0) to (x1,y1).		"""
		pass
	def create_radial_gradient(self, x0, y0, x1, y1):
		"""Returns a gradient object representing a radial gradient from (x0,y0) with radius r0 to (x1,y1) with radius r1.		"""
		pass
	def draw_image(self, media, x, y, width, height):
		"""Draw an image (from a Media object) onto the canvas at the specified coordinates (optionally scaling to the specified width and height)		"""
		pass
	def draw_image_part(self, media, sx, sy, s_width, s_height, dx, dy, d_width, d_height):
		"""Draw a subset of an image (from a Media object) onto the canvas.sx, sy, s_width and s_height specify which pixels within the source image of the source image to draw. dx and dy (and optionally d_width and d_height) specify where (and optionally what dimensions) on the canvas to draw the image.		"""
		pass
	def fill(self):
		"""Fill the current path with the current fill style of the canvas.		"""
		pass
	def fill_rect(self, x, y, width, height):
		"""Fill the specified rectangle with the current fill style of the canvas.		"""
		pass
	def fill_text(self, text, x, y):
		"""Draw the specified text at the required position.		"""
		pass
	def get_height(self):
		"""Get the pixel height of this canvas.		"""
		pass
	def get_image(self):
		"""Take a snapshot of the canvas and return an image as a Media object.		"""
		pass
	def get_width(self):
		"""Get the pixel width of this canvas.		"""
		pass
	def line_to(self, x, y):
		"""Adds a straight line segment at the end of the current path to the specified position.		"""
		pass
	def measure_text(self, text):
		"""Get the size of the specified text in the current font.		"""
		pass
	def move_to(self, x, y):
		"""Moves the current path position to the specified point without drawing.		"""
		pass
	def quadratic_curve_to(self, cpx, cpy, x, y):
		"""Adds a quadratic curve at the end of the current path to (x,y) with control point (cpx, cpy).		"""
		pass
	def reset_context(self):
		"""Reset the drawing context for this canvas. Called automatically after a window resize.		"""
		pass
	def reset_transform(self):
		"""Reset the current transform to the identity matrix.		"""
		pass
	def restore(self):
		"""Restores a drawing transform saved by the ‘save()’ function		"""
		pass
	def rotate(self, angle):
		"""Rotate all subsequent drawing by ‘angle’ radians.		"""
		pass
	def save(self):
		"""Saves the current drawing transform, which can be restored by calling ‘restore()’		"""
		pass
	def scale(self, x, y):
		"""Scale all subsequent drawing operations by ‘x’ horizontally and ‘y’ vertically.		"""
		pass
	def set_transform(self):
		"""Set the current transform matrix to the specified values.		"""
		pass
	def stroke(self):
		"""Draw the current path with the current stroke style of the canvas.		"""
		pass
	def stroke_rect(self, x, y, width, height):
		"""Outline the specified rectangle with the current stroke style of the canvas.		"""
		pass
	def stroke_text(self, text, x, y):
		"""Draw the outline of the specified text at the required position.		"""
		pass
	def transform(self, a, b, c, d, e, f):
		"""Multiply the current transform matrix by the specified matrix.		"""
		pass
	def translate(self, x, y):
		"""Translate all subsequent drawing by ‘x’ pixels across and ‘y’ pixels down.		"""
		pass
	pass

@dataclass
class CheckBox(Component):
	align:String=None		#  Align this component’s text
	allow_indeterminate:Boolean=None		#  Support an indeterminate state. The indeterminate state can only be set in code by setting checked=None.
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	checked:Boolean=None		#  The status of the checkbox
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	italic:Boolean=None		#  Display this component’s text in italics
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this CheckBox, or “default” to have the width set by the container.
	def focus(self):
		"""Set the keyboard focus to this component		"""
		pass
	pass

@dataclass
class ColumnPanel(Container):
	background:Color="#ff0000"		#  The background colour of this component.
	border:String="1px solid #888888"		#  The border of this component. Can take any valid CSS border value.
	col_spacing:String="medium"		#  Space between columns
	col_widths:String=""		#  Custom column widths in this panel
	foreground:Color="#ff0000"		#  The foreground colour of this component.
	parent:Container=Container()		#  
	role:Themerole="default"		#  Choose how this component can appear, based on your app’s visual theme.
	row_spacing:Pixels=None		#  The spacing between rows of components in this container, in pixels.
	spacing_above:String="small"		#  The vertical space above this component.
	spacing_below:String="small"		#  The vertical space below this component.
	tag=""		#  Use this property to store any extra information about this component
	tooltip:String=""		#  Text to display when you hover the mouse over this component
	visible:Boolean=True		#  Should this component be displayed?
	width:String=None		#  The width of this ColumnPanel, or “default” to have the width set by the container.
	wrap_on:String="mobile"		#  The largest display on which to wrap columns in this panel
	def add_component(self, component, full_width_row=False, **layout_props):
		"""Add a component to the bottom of this ColumnPanel. Useful layout properties:full_width_row = True|False row_background = [colour]		"""
		pass
	pass

@dataclass
class DataGrid(Container):
	auto_header:Boolean=None		#  Whether to display an automatic header at the top of this Data Grid.
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	columns:Datagridcolumns=None		#  A list of columns to display in this Data Grid.
	foreground:Color=None		#  The foreground colour of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	row_spacing:Pixels=None		#  The spacing between rows of components in this container, in pixels.
	rows_per_page:Integer=None		#  The maximum number of rows to display at one time.
	show_page_controls:Boolean=None		#  Whether to display the next/previous page buttons.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this DataGrid, or “default” to have the width set by the container.
	wrap_on:String=None		#  The largest display on which to wrap columns in this DataGrid
	def add_component(self, component, index=None, pinned=False):
		"""Add a component to this DataGrid, in the ‘index’th position. If ‘index’ is not specified, adds to the bottom.		"""
		pass
	def get_page(self):
		"""Get the current page number of this DataGrid		"""
		pass
	def jump_to_first_page(self):
		"""Jump to the first page of this DataGrid		"""
		pass
	def jump_to_last_page(self):
		"""Jump to the last page of this DataGrid		"""
		pass
	def next_page(self):
		"""Jump to the next page of this DataGrid		"""
		pass
	def previous_page(self):
		"""Jump to the previous page of this DataGrid		"""
		pass
	def set_page(self):
		"""Set the page number of this DataGrid. The page number must be positive.		"""
		pass
	pass

@dataclass
class DataRowPanel(Container):
	align:String=None		#  Align this component’s text
	auto_display_data:Boolean=None		#  Whether to automatically display data in this row.
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	italic:Boolean=None		#  Display this component’s text in italics
	item=defaultdict(default_val(None))		#  The data to display in this row by default.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	row_spacing:Pixels=None		#  The spacing between rows of components in this container, in pixels.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this DataRowPanel, or “default” to have the width set by the container.
	def add_component(self, component, column=None):
		"""Add a component to the specified column of this DataRowPanel. TODO: If ‘column’ is not specified, adds the component full-width.		"""
		pass
	pass

@dataclass
class DatePicker(Component):
	align:String=None		#  Align this component’s text
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	date:String=None		#  The date selected on this component.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	format:String=None		#  The format in which to display the selected date.
	italic:Boolean=None		#  Display this component’s text in italics
	max_date:String=None		#  The maximum date the user can select.
	min_date:String=None		#  The minimum date the user can select.
	parent:Container=Container()		#  
	pick_time:Boolean=None		#  Whether the user should be able to select a time as well as a date
	placeholder:String=None		#  A string to display when the DatePicker is empty.
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this DatePicker, or “default” to have the width set by the container.
	pass

@dataclass
class DropDown(Component):
	align:String=None		#  The position of this dropdown in the available space.
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	include_placeholder:Boolean=None		#  Whether to add a placeholder item to the list with value None
	italic:Boolean=None		#  Display this component’s text in italics
	items:Items=None		#  The items to display in this dropdown.
	parent:Container=Container()		#  
	placeholder:String=None		#  The text to be displayed when the selected_value is None.
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	selected_value:Object=None		#  The value of the currently selected item. Can only be set at runtime.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this DropDown, or “default” to have the width set by the container.
	def focus(self):
		"""Set the keyboard focus to this component		"""
		pass
	pass

@dataclass
class FileLoader(Component):
	align:String=None		#  Align this component’s text
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	file:Media=None		#  The currently selected file (or the first, if multiple files are selected). This is a Media object.
	file_types:String=None		#  Specify what type of file to upload. Can accept a MIME type (eg “image/png” or “image/*“), or an extension (eg “.png”), or a comma-separated set of them (eg “.png,.jpg,.jpeg”)
	files:List[Media]=None		#  A list of currently selected files. Each file is a Media object.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	icon:Icon=None		#  The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.
	icon_align:String=None		#  The alignment of the icon on this component. Set to ‘top’ for a centred icon on a component with no text.
	italic:Boolean=None		#  Display this component’s text in italics
	multiple:Boolean=None		#  If True, this FileLoader can load multiple files at the same time
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	show_state:Boolean=None		#  If True, display a message describing selected files.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this FileLoader, or “default” to have the width set by the container.
	def clear(self):
		"""Clear any selected files from this FileLoader		"""
		pass
	def focus(self):
		"""Set the keyboard focus to this FileLoader		"""
		pass
	pass

@dataclass
class FlowPanel(Container):
	align:String=None		#  Align this component’s content
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing:String=None		#  Space between components
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this FlowPanel, or “default” to have the width set by the container.
	def add_component(self, component, index=None, width=None, expand=None):
		"""Add a component to this panel. Optionally specify the position in the panel to add it, or the width to apply to components that can’t self-size width-wise.		"""
		pass
	pass

@dataclass
class GoogleMap(Container):
	background_color:String=None		#  Color used for the background of the Map div. This color will be visible when tiles have not yet loaded as the user pans.
	center:GoogleMap.LatLng=None		#  The Map center.
	clickable_icons:Boolean=None		#  When false, map icons are not clickable. A map icon represents a point of interest
	disable_default_ui:Boolean=None		#  Enables/disables all default UI.
	disable_double_click_zoom:Boolean=None		#  Enables/disables zoom and center on double click.
	draggable:Boolean=None		#  If false, prevents the map from being dragged.
	draggable_cursor:String=None		#  The name or url of the cursor to display when mousing over a draggable map.
	dragging_cursor:String=None		#  The name or url of the cursor to display when the map is being dragged.
	fullscreen_control:Boolean=None		#  The enabled/disabled state of the Fullscreen control.
	fullscreen_control_options:GoogleMap.FullscreenControlOptions=None		#  The display options for the Fullscreen control.
	gesture_handling:String=None		#  This setting controls how gestures on the map are handled.
	heading:Number=None		#  The heading for aerial imagery in degrees measured clockwise from cardinal direction North.
	height:String=None		#  The height of this component.
	keyboard_shortcuts:Boolean=None		#  If false, prevents the map from being controlled by the keyboard.
	map_data:GoogleMap.Data=None		#  Map data
	map_type_control:Boolean=None		#  The enabled/disabled state of the Map type control.
	map_type_control_options:GoogleMap.MapTypeControlOptions=None		#  The display options for the Map type control.
	map_type_id:GoogleMap.MapTypeId=None		#  The map type ID. Defaults to MapTypeId.ROADMAP
	max_zoom:Number=None		#  The maximum zoom level which will be displayed on the map.
	min_zoom:Number=None		#  The minimum zoom level which will be displayed on the map.
	parent:Container=Container()		#  
	rotate_control:Boolean=None		#  The enabled/disabled state of the rotate control.
	rotate_control_options:GoogleMap.RotateControlOptions=None		#  The display options for the rotate control.
	scale_control:Boolean=None		#  The enabled/disabled state of the scale control.
	scale_control_options:GoogleMap.ScaleControlOptions=None		#  The display options for the scale control.
	scroll_wheel:Boolean=None		#  If false, disables scrollwheel zooming on the map.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	street_view_control:Boolean=None		#  The enabled/disabled state of the street view control.
	street_view_control_options:GoogleMap.StreetViewControlOptions=None		#  The display options for the street view control.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this GoogleMap, or “default” to have the width set by the container.
	zoom:Number=None		#  The map zoom level.
	zoom_control:Boolean=None		#  The enabled/disabled state of the zoom control.
	zoom_control_options:GoogleMap.ZoomControlOptions=None		#  The display options for the zoom control.
	def close(self):
		"""Closes this InfoWindow.		"""
		pass
	def open(self, map, anchor):
		"""Opens this InfoWindow on the given map. Optionally, an InfoWindow can be associated with an anchor.		"""
		pass
	pass

@dataclass
class GridPanel(Container):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	row_spacing:Pixels=None		#  The spacing between rows of components in this container, in pixels.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this GridPanel, or “default” to have the width set by the container.
	def add_component(self, component, row=None, col_xs=None, width_xs=None):
		"""Add a component to this GridPanel		"""
		pass
	pass

@dataclass
class HtmlTemplate(Container):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	html:Html=None		#  The HTML from which this panel is defined
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	def add_component(self, component, slot="default"):
		"""Add a component to the named slot of this HTML templated panel. If no slot is specified, the ‘default’ slot will be used.		"""
		pass
	def call_js(self, js_function_name, *args):
		"""Call a Javascript function		"""
		pass
	def clear(self, slot="default"):
		"""clear the HTML template of all components or clear a specific slot of components.		"""
		pass
	pass

@dataclass
class Image(Component):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	display_mode:String=None		#  Determines how the image’s size should be adjusted to fit the size of this Image component
	foreground:Color=None		#  The foreground colour of this component.
	height:String=None		#  The height of this component.
	horizontal_align:String=None		#  Position the image horizontally within this component
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	source:Uri=None		#  The image source - set a string for a URL or a Media object in code
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	vertical_align:String=None		#  Position the image vertically within this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Image, or “default” to have the width set by the container.
	pass

@dataclass
class Label(Component):
	align:String=None		#  Align this component’s text
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	icon:Icon=None		#  The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.
	icon_align:String=None		#  The alignment of the icon on this component. Set to ‘top’ for a centred icon on a component with no text.
	italic:Boolean=None		#  Display this component’s text in italics
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Label, or “default” to have the width set by the container.
	pass

@dataclass
class LinearPanel(Container):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	row_spacing:Pixels=None		#  The spacing between rows of components in this container, in pixels.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this LinearPanel, or “default” to have the width set by the container.
	def add_component(self, component, index=None):
		"""Add a component to this LinearPanel, in the ‘index’th position. If ‘index’ is not specified, adds to the bottom.		"""
		pass
	pass

@dataclass
class Link(ColumnPanel):
	align:String="left"		#  Align this component’s text
	bold:Boolean=False		#  Display this component’s text in bold
	font:String="Arial"		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	icon:Icon=""		#  The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.
	icon_align:String="left"		#  The alignment of the icon on this component. Set to ‘top’ for a centred icon on a component with no text.
	italic:Boolean=False		#  Display this component’s text in italics
	parent:Container=Container()		#  
	tag=None		#  Use this property to store any extra information about this component
	text:String=""		#  The text displayed on this component
	tooltip:String=""		#  Text to display when you hover the mouse over this component
	underline:Boolean=False		#  Display this component’s text underlined
	url:String=""		#  The target URL of the link. Can be set to a URL string or to a Media object.
	pass

@dataclass
class Notification():
	def __enter__(self):
		"""Show the notification when entering a ‘with’ block		"""
		pass
	def __exit__(self):
		"""Hide the notification when exiting a ‘with’ block		"""
		pass
	def hide(self):
		"""Hides the notification immediately		"""
		pass
	def show(self):
		"""Shows the notification		"""
		pass
	pass

@dataclass
class Plot(Component):
	config:Dict=None		#  Plot config
	data:Object=None		#  Plot traces
	figure:Dict=None		#  The Plotly figure to display. Specifies layout and data.
	height:String=None		#  The height of this component.
	interactive:Boolean=None		#  Whether this plot should be interactive
	layout:Object=None		#  Plot layout
	parent:Container=Container()		#  
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Plot, or “default” to have the width set by the container.
	def extend_traces(self, data, traces):
		"""Adds data to an existing trace.		"""
		pass
	def prepend_traces(self, data, traces):
		"""Prepends data to an existing trace.		"""
		pass
	def redraw(self):
		"""Redraws the chart. Call this function if you have updated data or layout properties.		"""
		pass
	def relayout(self, update):
		"""A more efficient means of updating just the layout in a graphDiv. The call signature and arguments for relayout are similar (but simpler) to restyle.		"""
		pass
	def restyle(self, update, traces):
		"""A more efficient means of changing attributes in the data array. When restyling, you may choose to have the specified changes effect as many traces as desired.		"""
		pass
	def to_image(self, options):
		"""Returns a Media object containing a snapshot of this plot. The argument is a dictionary specifying image options.		"""
		pass
	pass

@dataclass
class RadioButton(Component):
	align:String=None		#  Align this component’s text
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	group_name:String=None		#  The name of the group this radio button belongs to.
	italic:Boolean=None		#  Display this component’s text in italics
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	selected:Boolean=None		#  The status of the radio button
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	value:String=None		#  The value of the group when this radio button is selected
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this RadioButton, or “default” to have the width set by the container.
	def get_group_value(self):
		"""returns the value of the button in the group which is pressed.		"""
		pass
	pass

@dataclass
class RepeatingPanel(Component):
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	item_template:Form=None		#  The name of the form to repeat for every item
	items:Items=None		#  A list of items for which the ‘item_template’ will be instantiated.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this RepeatingPanel, or “default” to have the width set by the container.
	def get_components(self):
		"""Get the list of components created by this Repeating Panel. Each will be an instance of ‘item_template’, one for each item in ‘items’.		"""
		pass
	def raise_event_on_children(self, event_name, **event_args):
		"""Trigger the ‘event_name’ event on all children of this component. Any keyword arguments are passed to the handler function.		"""
		pass
	pass

@dataclass
class RichText(Container):
	align:String=None		#  Align this component’s text
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	content:String=None		#  The content to render in this component, in the format specified by the ‘format’ property
	data:Object=None		#  A dict of data or Components to populate the named content {slots}.
	enable_slots:Boolean=None		#  If true {braces} in content define slots. If false, braces in content display normally.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	format:String=None		#  The format of the content of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this RichText, or “default” to have the width set by the container.
	def add_component(self, component, slot):
		"""Add a component to this panel, in the specified slot		"""
		pass
	def clear(self, slot="slot_name"):
		"""clear the Rich Text Component of all components or clear a specific slot of components.		"""
		pass
	pass

@dataclass
class Spacer(Component):
	height:String=None		#  The height of this component.
	parent:Container=Container()		#  
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this Spacer, or “default” to have the width set by the container.
	pass

@dataclass
class TextArea(Component):
	align:String=None		#  Align this component’s text
	auto_expand:Boolean=None		#  If true, the text area will expand vertically to fit its contents
	background:Color=None		#  The background colour of this component.
	bold:Boolean=None		#  Display this component’s text in bold
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=None		#  True if this component should allow user interaction.
	font:String=None		#  The font to use for this component.
	font_size:Pixels=None		#  The height of text displayed on this component in pixels
	foreground:Color=None		#  The foreground colour of this component.
	height:String=None		#  The height of this component.
	italic:Boolean=None		#  Display this component’s text in italics
	parent:Container=Container()		#  
	placeholder:String=None		#  The text to be displayed when the component is empty.
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	text:String=None		#  The text displayed on this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	underline:Boolean=None		#  Display this component’s text underlined
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this TextArea, or “default” to have the width set by the container.
	def focus(self):
		"""Set the keyboard focus to this TextArea		"""
		pass
	def select(self):
		"""Select all the text in this TextArea		"""
		pass
	pass

@dataclass
class TextBox(Component):
	align:String="left"		#  Align this component’s text
	background:Color="#ff0000"		#  The background colour of this component.
	bold:Boolean=False		#  Display this component’s text in bold
	border:String="1px solid #888888"		#  The border of this component. Can take any valid CSS border value.
	enabled:Boolean=True		#  True if this component should allow user interaction.
	font:String="Arial"		#  The font to use for this component.
	font_size:Pixels=16		#  The height of text displayed on this component in pixels
	foreground:Color="#ff0000"		#  The foreground colour of this component.
	hide_text:Boolean=False		#  Display stars instead of the text in this box
	italic:Boolean=False		#  Display this component’s text in italics
	parent:Container=Container()		#  
	placeholder:String="Enter text here"		#  The text to be displayed when the component is empty.
	role:Themerole="default"		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String="small"		#  The vertical space above this component.
	spacing_below:String="small"		#  The vertical space below this component.
	tag=""		#  Use this property to store any extra information about this component
	text:String=""		#  The text displayed on this component
	tooltip:String=""		#  Text to display when you hover the mouse over this component
	type:String="text"		#  What type of data will be entered into this box?
	underline:Boolean=False		#  Display this component’s text underlined
	visible:Boolean=True		#  Should this component be displayed?
	width:String=None		#  The width of this TextBox, or “default” to have the width set by the container.
	def focus(self):
		"""Set the keyboard focus to this TextBox		"""
		pass
	def select(self):
		"""Select the text in this TextBox		"""
		pass
	pass

@dataclass
class Timer(Component):
	interval:Seconds=None		#  The number of seconds between each tick. 0 switches the timer off.
	parent:Container=Container()		#  
	pass

@dataclass
class URLMedia(Media):
	pass

@dataclass
class XYPanel(Container):
	align:String=None		#  Align this component’s content
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	foreground:Color=None		#  The foreground colour of this component.
	height:String=None		#  The height of this component.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	tooltip:String=None		#  Text to display when you hover the mouse over this component
	visible:Boolean=None		#  Should this component be displayed?
	width:String=None		#  The width of this XYPanel, or “default” to have the width set by the container.
	def add_component(self, component, x=0, y=0, width=None):
		"""Add a component to this XYPanel, at the specified coordinates. If the component’s width is not specified, uses the component’s default width.		"""
		pass
	def get_width(self):
		"""Get the width of this XYPanel, in pixels.		"""
		pass
	pass

@dataclass
class YouTubeVideo(Component):
	autoplay:Boolean=None		#  Set to true to play this video immediately
	background:Color=None		#  The background colour of this component.
	border:String=None		#  The border of this component. Can take any valid CSS border value.
	current_time:Seconds=None		#  Get or set the current playback position, in seconds.
	duration:Seconds=None		#  Get the duration of the video in seconds.
	foreground:Color=None		#  The foreground colour of this component.
	height:String=None		#  The height of this component.
	loop:Boolean=None		#  Set to true to play this video repeatedly
	mute:Boolean=None		#  Set whether the video is muted or not.
	parent:Container=Container()		#  
	role:Themerole=None		#  Choose how this component can appear, based on your app’s visual theme.
	spacing_above:String=None		#  The vertical space above this component.
	spacing_below:String=None		#  The vertical space below this component.
	state:Object=None		#  Get the current playback state of the video as a string. E.g. PLAYING
	tag=defaultdict(default_val(None))		#  Use this property to store any extra information about this component
	visible:Boolean=None		#  Should this component be displayed?
	volume:Object=None		#  Get or set the current volume, from 0 - 100.
	width:String=None		#  The width of this YouTubeVideo, or “default” to have the width set by the container.
	youtube_id:String=None		#  The ID of the YouTube video to play
	def pause(self):
		"""Pause this YouTube video		"""
		pass
	def play(self):
		"""Start playing this YouTube video		"""
		pass
	def stop(self):
		"""Stop playing this YouTube video		"""
		pass
	pass
