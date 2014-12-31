from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print ("Today's date is ", today)

    print ("Date Components: ", today.day, today.month, today.year)

    wd = date.weekday(today)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print ("Today is day number : ", (wd+1))
    print ("Which is a " + days[wd])
