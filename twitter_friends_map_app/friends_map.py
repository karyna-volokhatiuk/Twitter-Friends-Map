'''
This module creates a map with locations
of user's friends in Twitter.
'''
import folium

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable


def find_coordinates(location_of_friend: str) -> tuple:
    '''
    Return latitude and longitude of location_of_friend.
    '''
    try:
        geolocator = Nominatim(user_agent="Twitter friends")
        location = geolocator.geocode(location_of_friend)
        if location:
            return location.latitude, location.longitude
    except GeocoderUnavailable:
        pass


def add_coordinates_to_list(locations_of_friends_list: list) -> list:
    '''
    Return list with info from locations_of_friends_list and
    coordinates of locations from it.
    '''
    coordinates_of_friends_list = []
    for friend in locations_of_friends_list:
        if find_coordinates(friend[1]):
            coordinates_of_friends_list.append(
                friend+[find_coordinates(friend[1])])
    return coordinates_of_friends_list


def generate_map(coordinates_of_friends_list: list) -> None:
    '''
    Generate map with locations from
    coordinates_of_friends_list.
    '''
    friends_map = folium.Map()
    fg_markers = folium.FeatureGroup(name='Friends locations')
    for friend in coordinates_of_friends_list:
        fg_markers.add_child(folium.Marker(location=friend[2],
                                           popup=friend[0] + '🌍' + friend[1],
                                           icon=folium.Icon(color='darkpurple', icon_color='white')))

    friends_map.add_child(fg_markers)

    friends_map.save('templates/twitter_friends_map.html')
