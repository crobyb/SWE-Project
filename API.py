# CS_KSU
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyDsXXZgg7G1hz39Bfb-j5WiUXwxlY_aPQo')

# Get your current location
current_location = gmaps.geolocate()

# Define the search parameters
search_params = {
    'location': f"{current_location['lat']},{current_location['lng']}",
    # Search within 5 km
    'radius': 5000, 
    'type': 'movie_theater'
}

# Perform the search
theatres = gmaps.places_nearby(**search_params)

# Print the results
for theatre in theatres['results']:
    print(theatre['name'], theatre['vicinity'])
