# CS_KSU
import json
import googlemaps
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path = '/temp2\stat2', static_folder= "temp2\stat2")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SWE-Project/test', methods=['POST'])
def search():
    location = request.get_json()

gmaps = googlemaps.Client(key='AIzaSyDsXXZgg7G1hz39Bfb-j5WiUXwxlY_aPQo')

# Get the user's location 
#address = input("Enter an address:") 

# Geocode the address to get its latitude and longitude
geocode_result = gmaps.geocode(address)
location = geocode_result[0]['geometry']['location']

# Define the search parameters
search_params = {
    'location': f"{location['lat']},{location['lng']}",
    'radius': 5000,
    'type': 'movie_theater'
}

# Perform the search
theatres = gmaps.places_nearby(**search_params)

# Print the results
for theatre in theatres['results']:
    print(theatre['name'], theatre['vicinity'])
