from p1_maps import maps, getLatLng
from p1_out import steps, latLong, totalTime
from p1_out import totalDistance, elevation

def main():


    #user enters number of locations
    numOfLocations = int(input("Enter number of locations: "))
    print("They can be cities, home addresses, as long as they are drivable locations.")
    #inputs the addresses into our dictionary
    addresses = []
    for key in range(numOfLocations):
        userInput = str(input())
        addresses.append(userInput)

    #calls maps(), returning .json()
    jsonDump = maps(addresses)


    #   checking for errors (although we assume the user
    #   correctly knows how to use the program)

    if jsonDump["route"]["routeError"]['errorCode'] != -400:
        print("\nNO ROUTE FOUND")
    elif jsonDump['info']['statuscode'] != 0:
       print('\nMAPQUEST ERROR')
    else:
        finalLatLng = getLatLng(jsonDump, numOfLocations)
    if finalLatLng == "39.78N 100.45W":
        print("\nNO ROUTE FOUND")


    ##  if no errors were found, we continue with the program.
    else:
        #similar to before, user enters num of outputs they want
        numOfOutputs = int(input())

        #append the things they want into a list.
        listOfOutputs = []
        for key in range(numOfOutputs):
            methods = str(input())
            listOfOutputs.append(methods)


        #if what the user entered is what we want, then we create our objects.
        #   no switch cases in Python
        #   1. check if i == the desired input
        #   2. print Title
        #   3. create object
        #   4. print result

        for i in listOfOutputs:
            if i == "STEPS":
                print("\nDIRECTIONS")
                s = steps(jsonDump)
                for item in s.output():
                    print(item)

            if i == "LATLONG":
                print("\nLATLONGS")
                s = latLong(jsonDump)
                for item in s.output():
                    print(item)

            if i == "ELEVATION":
                print("\nELEVATION")
                s = elevation(jsonDump)
                for item in s.output():
                    print(item)

            if i == "TOTALTIME":
                s = totalTime(jsonDump)
                print("\nTOTAL TIME: " + str(next(s.output())) + " minutes")

            if i == "TOTALDISTANCE":
                s = totalDistance(jsonDump)
                print("\nTOTAL DISTANCE: " + str(round(next(s.output(),2))) + " miles")



    print("\n\n\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMapContributors")

main()
