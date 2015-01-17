import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print("Outputting Information to file")

# Print the name of the OS
string = "\nOS Type: " + os.name

# Check for item existence and type
string += "\nItem exists: " + str(path.exists("textfile.txt"))
string += "\nItem is a file: " + str(path.isfile("textfile.txt"))
string += "\nItem is a directory: " + str(path.isdir("textfile.txt"))


# Work with file paths
string += "\nItem's path: " + str(path.realpath("textfile.txt"))
string += "\nItem's path and name: " + str(path.split(path.realpath("textfile.txt")))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
string += "\n" + t
#string += "\n" + datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

# Calculate how long ago the item was modified
td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
string += "\nIt has been " + str(td) + "\nThe file was modified"
string += "\nTotal time: " + str(td.total_seconds()) + " seconds"


string += "\nLet us modify the file again"
t = time.ctime(path.getmtime("textfile.txt"))
file = open("textfile.txt", "w+")
file.write(string)
file.write("\nLast modification: " + t)
file.close()



y = open("textfile.txt", "r")

if (y.mode == 'r'):
    inFile = "\nFile import"
    fl = y.readlines()
    for x in fl:
        inFile += x
    print(inFile)

y.close()
