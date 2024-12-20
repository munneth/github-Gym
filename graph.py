import webscraper
import matplotlib.pyplot as plt
import app


def newPlot():
    fig, ax = plt.subplots()

    time = app.timeData.keys()
    occupants = app.timeData.values()
    bar_colors = []
    for times in time:
        bar_colors.append('tab:blue')
    ax.set_ylabel('occupants')
    ax.set_title('ARC Occupancy')

    plt.show()




