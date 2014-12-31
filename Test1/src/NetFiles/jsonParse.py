import urllib.request # instead of urllib2 like in Python 2.7
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print (theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print (str(count) + " events recorded")

    # for each event, print the place where it occured
    for i in theJSON["features"]:
        print (i["properties"]["place"])

    # print the events that only have magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

    # print only the events where at least 1 person reported feeling "something"
    print ("\nEvents that were felt: ")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0 ):
                print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")



def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"


    webUrl = urllib.request.urlopen(urlData)

    code = webUrl.getcode()
    print ("Website Response : " + str(code))

    if (code == 200) :
        data = webUrl.read()
        data = data.decode("utf-8")
        printResults(data)

    else:
        print ("Error fetching JSON data from server. Response code : " + str(webUrl.getcode()))


if __name__ == "__main__":
    main()
