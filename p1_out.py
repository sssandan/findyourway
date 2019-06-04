# Sandan, Ryan
# Professor Nadia
# Project 1
# May 9, 2019

from p1_maps import maps
import requests

class steps:
    def __init__(self, jsonDump):
        self.__dic = jsonDump

    def output(self):
        num = len(self.__dic["route"]["locationSequence"]) - 1
        for item in range(num):
            for x in self.__dic["route"]["legs"][item]["maneuvers"]:
                yield x["narrative"]

class totalDistance:
    def __init__(self, jsonDump):
        self.__dic = jsonDump

    def output(self):
        dist = self.__dic['route']['distance']
        yield(round(dist))


class totalTime:
    def __init__(self, jsonDump):
        self.__dic = jsonDump

    def output(self):
        time = self.__dic['route']['formattedTime']
        timeList = time.split(":")
        minutes = int(timeList[0]) * 60 + int(timeList[1])
        yield(minutes)




class latLong:
    def __init__(self, jsonDump):
        self.__dic = jsonDump

    def output(self):
        for i in range(len(self.__dic) + 1):
            lng = str(round(self.__dic['route']['locations'][i]['latLng']['lng'], 2))
            lat = str(round(self.__dic['route']['locations'][i]['latLng']['lat'], 2))
            if lng[0] == '-':
               lng = lng[1:] + 'W'
            else:
               lng = lng + 'E'
            if lat[0] == '-':
               lat = lat[1:] + 'S'
            else:
               lat = lat + 'N'
            finalLatLng = lat + " " + lng
            yield finalLatLng


class elevation:
    def __init__(self, jsonDump):
        self.__dic = jsonDump

    def output(self):

        url = ("http://open.mapquestapi.com/elevation/v1/profile" +
        "?key=A8RmTl27mFnA8Q2h8h7HNQqUCTu5APBH&shapeFormat=raw&latLngCollection=")

        for i in range(len(self.__dic['route']['locationSequence'])):
            latlng = (str(self.__dic['route']['locations'][i]['latLng']['lat']) + ","
            + str(self.__dic['route']['locations'][i]['latLng']['lng']) + ",")

            latlng = latlng.rstrip(",")
            newUrl = url + latlng
            newUrl = newUrl.rstrip()
            newOutput = (requests.post(newUrl)).json()
            elevationValue = newOutput['elevationProfile'][0]['height']

            yield(elevationValue)