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
    #getting current time
    currentTime = time.localtime()
    formattedTime = time.strftime("%H:%M", currentTime)
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