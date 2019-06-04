# Sandan, Ryan
# Professor Nadia
# Project 1
# May 9, 2019

'''
 building URLS
 making HTTP requests
 parsing JSON responses

'''

import requests

def maps(locations):
    #replace any spaces in the locations list with a "+"
    for x in range(1, len(locations)):
        locations[x].replace(' ', '+')

    locations = [x.strip(',') for x in locations]
    payload = {"key" : "A8RmTl27mFnA8Q2h8h7HNQqUCTu5APBH", "to" : locations[1:], "from" : locations[0]}
    r = requests.get('http://open.mapquestapi.com/directions/v2/route', params = payload)
    output = (requests.post(r.url)).json()

    return output





def getLatLng(jsonDump, numOfLocations):
    for i in range(numOfLocations):
        lng = str(round(jsonDump['route']['locations'][i]['latLng']['lng'], 2))
        lat = str(round(jsonDump['route']['locations'][i]['latLng']['lat'], 2))
        if lng[0] == '-':
            lng = lng[1:] + 'W'
        else:
            lng = lng + 'E'
        if lat[0] == '-':
            lat = lat[1:] + 'S'
        else:
            lat = lat + 'N'
        finalLatLng = lat + " " + lng
        return finalLatLng

