import time
import requests
from bs4 import BeautifulSoup
import csv

def getOccupancy():
    # Gathering current arc occupancy
    r = requests.get('https://rec.ucdavis.edu/facilityoccupancy')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='occupancy-details')
    occupancy_elements = s.find_all('strong')
    # Extract the text from the second <strong> element and strip any extra whitespace
    occupancy_value = occupancy_elements[1].text.strip()
    return occupancy_value

def getTime():
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
    return time.time()

def main():
    timeData = {}
    printableTimeData = {}

    while getTime() != "00:01":
        adjTime = getTime()[3:5]
        if adjTime == "00" or adjTime == "30":
            timeData[getTime()] = getOccupancy()
            printableTimeData['time'] = getTime()
            printableTimeData['occupancy'] = getOccupancy()
            print(timeData)
            continue
        else:
            continue

    # Open and add header to csv
    with open("data.csv", "a") as f:
        header = ["Time", "Occupancy(Max 2500)"]
        f.write(",".join(header) + "\n")
        # Traverse the dictionary and add to csv file
        for key, value in timeData.items():
            f.write(key + "," + value + "\n")
    return timeData

# Uncomment to run main if needed
# print(getOccupancy())
