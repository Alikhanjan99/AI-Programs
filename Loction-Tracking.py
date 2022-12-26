from geopy.geocoders import Nominatim
import pygmaps

def track_location(address):
  geolocator = Nominatim(user_agent="my-location-tracker")
  location = geolocator.geocode(address)
  latitude = location.latitude
  longitude = location.longitude
  
  # create a map centered at the location
  mymap = pygmaps.maps(latitude, longitude, 16)
  
  # add a point at the location
  mymap.addpoint(latitude, longitude)
  
  # generate the HTML file for the map
  mymap.draw('./map.html')

# track the location of the White House
track_location("1600 Pennsylvania Ave NW, Washington, DC 20500")
