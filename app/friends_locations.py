'''
This module make get request to api.twitter.
'''
import requests
import json


def get_locations_of_friends(nickname, bearer_token):
    '''
    Return list with names and locations of user's followers.
    '''
    base_url = 'https://api.twitter.com/'
    search_url = '{}1.1/friends/list.json'.format(base_url)

    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }
    search_params = {
        'screen_name': nickname,
        'count': 30
    }

    response = requests.get(
        search_url, headers=search_headers, params=search_params)
    json_response = response.json()

    locations_of_friends_list = []
    for user in json_response['users']:
        locations_of_friends_list.append([user['name'], user['location']])

    return locations_of_friends_list
