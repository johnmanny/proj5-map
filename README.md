# Project 5:  Booze Maps

This map will center on the user's position (if geolocation is enabled,
otherwise will center on Eugene, Or), and will display a marker with a small circle
 showing their approximate location. Markers are then placed in select liquor/alcohol stores
 in the Eugene area. The names and addresses are stored on a file on the server, 
read into the flask application, which handles an ajax request and returns json to 
the clientin order to place the markers on their map. Clicking on any other portion
of the map will output an address that is obtained through reverse geolocation of
the clicked latitude and longitude values.

## Assignment Information:

***Author***:
John Nemeth

***Class***: CIS322 17F

***Sources***:
 Heavy reference from prior projects (proj2, 3, and 4), class material (CIS322),
leaflet tutorial webpages and examples, esri geolocation examples, and other specific
sources listed in file headers. Some files (makefile, start and stop shell scripts) 
essentially recycled with minor modifications for compatibility.
