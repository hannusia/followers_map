import folium
import json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from get_followers import get_followers


def get_locations(path: str) -> dict:
    """
    Get dictionary with followers and their locations.
    """
    locations = {}
    with open(path) as json_file:
        data = json.load(json_file)
    followers = data['data']
    for follower in followers:
        if 'location' in follower:
            locations[follower['username']] = follower['location']
    return locations


def generate_map(locations: dict):
    """
    Generate map with markers on followers locations.
    """
    followers_map = folium.Map(zoom_start=12)
    geolocator = Nominatim(user_agent='movie_map')
    for follower in locations:
        try:
            loc = geolocator.geocode(locations[follower])
            if loc is not None:
                caption = '<strong>' + follower + '</strong>'
                folium.Marker([loc.latitude, loc.longitude],
                              popup=caption,
                              icon=folium.Icon(color='cadetblue')).add_to(followers_map)
        except GeocoderUnavailable:
            pass
    followers_map.save('templates/followers_map.html')


def main(user: str, bearer_token: str):
    """
    Main function which combine 
    """
    get_followers(user, bearer_token)
    generate_map(get_locations('followers_loc.json'))
