#in Python3.3, you need to import urllib.request
import urllib.request
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # open a connection to a URL using urllib2
    before = datetime.datetime.now()


    webUrl = urllib.request.urlopen("http://joemarini.com")
    print ("Result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print (data)

    after  = datetime.datetime.now()

    td = after - before

    # Calculate how long the connection took
    print ("Connection time: " + str(td.total_seconds()) + " seconds")



    pass

if __name__ == "__main__":
    main()

