from flask import Flask, render_template, jsonify
import webscraper
from datetime import datetime
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dictionary to store occupancy data and last update time
timeData = {}
#lastUpdateTime = 0


# Directory to save generated plots
STATIC_DIR = os.path.join(app.root_path, 'static', 'images')
os.makedirs(STATIC_DIR, exist_ok=True)  # Create directory if it doesn't exist


def fetchData():
    """
    Fetch data from webscraper and update timeData dictionary every 30 minutes.
    """
    #global lastUpdateTime
    #lastUpdateTime = 0
    now = datetime.now()

    if now.minute in [0, 30]:
        print(f"Fetching new data at fixed interval: {now.strftime('%H:%M:%S')}")
        occupancy = webscraper.getOccupancy()
        formattedTime = webscraper.getTime()
        timeData[formattedTime] = occupancy
        #lastUpdateTime = time.time()  # Update the last update timestamp

def generate_plot():
    fig, ax = plt.subplots(figsize=(10, 10))
    print(timeData)
    time = list(timeData.keys())
    #for str in time:
        #str = int(str)
    
    stringOccupants = list(timeData.values())
    intOccupants = []
    for number in stringOccupants:
        number = int(number[2:5])
        intOccupants.append(number)

    bar_colors = ['#FFD100'] * len(time)
    ax.bar(time, intOccupants, color=bar_colors)
    ax.set_xlabel('Time')
    ax.set_ylabel('Occupancy')
    ax.set_title('Generated Plot')
    ax.set_facecolor("#002855")
    
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability

    # Save plot as a static file
    plot_path = os.path.join(STATIC_DIR, 'plot.png')
    plt.savefig(plot_path)
    plt.close()  # Close the figure to free memory

scheduler = BackgroundScheduler()
scheduler.add_job(fetchData, 'interval', minutes=1)
scheduler.add_job(generate_plot, 'interval', minutes=1)
scheduler.start()

def findBestTime():
    """
    Find the best time to visit based on occupancy data.
    """
    # Convert timeData to a list of tuples (time, occupancy)
    occupancy_list = [(time, int(occupancy[2:5])) for time, occupancy in timeData.items()]
    # Sort by occupancy
    occupancy_list.sort(key=lambda x: x[1])
    # Return the time with the lowest occupancy
    return occupancy_list[0] if occupancy_list else None

@app.route('/')
def arc():
    occupancyOnRefresh = webscraper.getOccupancy()
    fetchData()  # Ensure the data is updated
    generate_plot()  # Generate and save the plot
    webscraper.getOccupancy()
    # Render the template with occupancy data

    return render_template('arc.html', timeData=timeData, occupancyOnRefresh = occupancyOnRefresh, time = webscraper.getTime())

@app.route("/api/info")
def send_info():
    occupancyOnRefresh = webscraper.getOccupancy()
    fetchData()  # Ensure the data is updated
    generate_plot()  # Generate and save the plot
    webscraper.getOccupancy()
    findBestTime()
    # Render the template with occupancy data
    return jsonify({
            'occupancy': occupancyOnRefresh.strip("[]'"),
            'timeData': timeData,
            'time': webscraper.getTime(),
            'best time': findBestTime()
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

