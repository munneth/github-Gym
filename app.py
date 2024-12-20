from flask import Flask, render_template
import webscraper
from datetime import datetime
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Dictionary to store occupancy data and last update time
timeData = {}
lastUpdateTime = 0

# Directory to save generated plots
STATIC_DIR = os.path.join(app.root_path, 'static', 'images')
os.makedirs(STATIC_DIR, exist_ok=True)  # Create directory if it doesn't exist


def fetchData():
    """
    Fetch data from webscraper and update timeData dictionary every 30 minutes.
    """
    global lastUpdateTime
    lastUpdateTime = 0
    now = datetime.now()

    if now.minute in [0, 30]:
        print(f"Fetching new data at fixed interval: {now.strftime('%H:%M:%S')}")
        occupancy = webscraper.getOccupancy()
        formattedTime = webscraper.getTime()
        timeData[formattedTime] = occupancy
        lastUpdateTime = time.time()  # Update the last update timestamp

def generate_plot():
    fig, ax = plt.subplots(figsize=(10, 10))
    #print(timeData)
    time = list(timeData.keys())
    #for str in time:
        #str = int(str)
    
    stringOccupants = list(timeData.values())
    intOccupants = []
    for number in stringOccupants:
        number = int(number[2:5])
        intOccupants.append(number)

    

    bar_colors = ['tab:blue'] * len(time)
    ax.bar(time, intOccupants, color=bar_colors)
    ax.set_xlabel('Time')
    ax.set_ylabel('Occupancy')
    ax.set_title('Generated Plot')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability

    # Save plot as a static file
    plot_path = os.path.join(STATIC_DIR, 'plot.png')
    plt.savefig(plot_path)
    plt.close()  # Close the figure to free memory

scheduler = BackgroundScheduler()
scheduler.add_job(fetchData, 'interval', minutes=1)  # Run fetchData every minute
scheduler.add_job(generate_plot, 'interval', minutes=1)
scheduler.start()

@app.route('/')
def arc():
    
    fetchData()  # Ensure the data is updated
    generate_plot()  # Generate and save the plot

    # Render the template with occupancy data
    return render_template('arc.html', timeData=timeData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
