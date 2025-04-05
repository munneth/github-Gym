import time
import requests
from bs4 import BeautifulSoup
import csv

#r = requests.get('https://rec.ucdavis.edu/facilityoccupancy')

#print(r)

#soup = BeautifulSoup(r.content, 'html.parser')

def getOccupancy():
    #gathering current arc occupancy
    r = requests.get('https://rec.ucdavis.edu/facilityoccupancy')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_ = 'occupancy-details')
    occupancy = s.find_all('strong')
    occupancy = str(list(occupancy[1]))#see what this does
    print(type(occupancy))
    return occupancy

def getTime(): ####
    # Getting current time in 24-hour format
    currentTime = time.localtime()
    hour = currentTime.tm_hour
    minute = currentTime.tm_min

    # Convert to 12-hour format with AM/PM
    am_pm = "AM" if hour < 12 else "PM"
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12  # 0 becomes 12 in 12-hour format

    formattedTime = f"{hour_12}:{minute:02d} {am_pm}"
    return formattedTime


def lastUpdateTime():
    lastUpdate = time()
    return lastUpdate

def main():
    timeData = {}
    printableTimeData = {}

    while getTime() != "00:01":
        adjTime = getTime()[3:5]
        #print(adjTime)
        #print(getTime())
        if adjTime == "00" or adjTime == "30":
            timeData[getTime()] = getOccupancy()
            printableTimeData['time'] = getTime()
            printableTimeData['occupancy'] = getOccupancy()
            print(timeData)
            continue
        else:
            continue

    #open and add header to csv
    f = open("data.csv", "a")
    header = ["Time", "Occupancy(Max 2500)"]
    for head in header:
        f.write(head + ",")
    f.write("\n")

    #traverse the dictionary and add to csv file
    for key, value in timeData.items():
        f.write(key + "," + value + "\n")
    f.close()

    return timeData

#print(getOccupancy())