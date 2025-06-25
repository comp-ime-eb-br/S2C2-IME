import pandas as pd
import matplotlib.pyplot as plt
from math import pi


def radarChart(array1, array2):
    #Fonte: https://python-graph-gallery.com/390-basic-radar-chart/

    df = pd.DataFrame(columns=['group', 'Timeliness', 'Public Availability', 'Normal and Attack Trafic', 'Metadata', 'Anonymity',
               'Complete Network', 'Labeld', 'Findable', 'Accessible', 'Interoperable', 'Reusable'])
    array3 = ['A'] + array1 + array2
    df.loc[len(df)] = array3

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ["0", "0.2", "0.4", "0.6", "0.8", "1"], color="grey", size=7)
    plt.ylim(0, 1)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # Show the graph
    plt.show()

array1 = [0.8, 0.6, 0.7, 0.9, 0.4, 0.6]
array2 = [0.7, 0.8, 0.6, 0.5, 0.6]

radarChart(array1, array2)