
"""interacts with Open MapQuest APIs; build URLs, make HTTP requests,
    parse JSON responses"""

import json
import pprint
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'GTNe648FwGZwAlnDxNIMiMZlaIhpFUQa'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def build_search_url(address_list: list) -> str:
    '''creates a url for mapquest using my api key'''
    query_parameters = [
        ('key', MAPQUEST_API_KEY)
        ]
    
    for new_param in address_list:
        if new_param == address_list[0]:
            query_parameters.append(('from', new_param))
        else:
            query_parameters.append(('to', new_param))

    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def url_to_json(url: str) -> 'json':
    '''turns a url into a json'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()




def distance_parse(json_result: 'json') -> int:
    '''separates the distance out of the json result'''
    distance = json_result['route']['distance']
    return distance


def time_parse(json_result: 'json') -> int:
    '''separates the time out of the json result'''
    time = json_result['route']['time']
    return time


def steps_parse(json_result: 'json') -> [str]:
    '''separates all the navigation steps out of the json result'''
    steps_list = []
    for item in json_result['route']['legs']:
        for thing in item.get('maneuvers'):
            steps_list.append(thing.get('narrative'))
    return steps_list


def latlongs_parse(json_result: 'json') -> [tuple]:
    '''separates the latitude and longtitude for each location out of the json result'''
    latlongs = []
    latlongs_tuple = []
    for item in json_result['route']['locations']:
        latlongs.append(item.get('displayLatLng'))
    for x in latlongs:
        latlongs_tuple.append((x.get('lat'),x.get('lng')))
    return latlongs_tuple

def elevation_url(latlongs_tuple: list) -> str:
    '''returns the url created for elevation'''
    url_list = []
    for x in latlongs_tuple:
        lat_str = ''
        lat_str += str(x[0]) + ',' + str(x[1]) + ','
        lat_str = lat_str[:-1]
        elev_param = [
        ('key', MAPQUEST_API_KEY), ('latLngCollection', lat_str)
        ]
        url_list.append(MAPQUEST_ELEVATION_URL + urllib.parse.urlencode(elev_param))
    return url_list


def elevations_parse(elev_json: 'json') -> list:
    '''separates the elevation out of the json result of the elevation url'''
    heights = []
    for elevation in elev_json['elevationProfile']:
        heights.append(elevation['height'])
    return heights

