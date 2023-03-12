# Importing pandas  & matplotlib library
import pandas as pd
import matplotlib.pyplot as plt

# Reading data from csv files to create dataframe
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

# Filtering data by team  & eventname
T1 = df1[(df1['teamid'] == 724) & (df1["eventname"] == "shot")]
T2 = df1[(df1['teamid'] == 596) & (df1["eventname"] == "shot")]

# Consolidating individual team data to create a master data
Data = [[T1[['xcoord']], T1[['ycoord']], T1[['goal']].values.tolist()],
        [T2[['xcoord']], T2[['ycoord']], T2[['goal']].values.tolist()]]


def scatterPlot(x, y, z, TeamNum=None, **kwargs):
    """ This function when passed with x, y cordinates along with z value will construct a 2D scatter plot"""

    # Define colors to highlight goaled shots with red
    colors = ["red" if i[0] == 1 else "green" for i in z]

    # Create scatter plot
    plt.scatter(x, y, color=colors)

    # Adding labels and scatter plot title
    plt.xlabel("X-axis label")
    plt.ylabel("Y-axis label")
    plt.title("Team {} Scatter Plot".format(TeamNum))

    # Display plot
    plt.show()


def comments():
    """ Comments on scatter plot"""

    print('Team 596 has made 4 goals as indicated by red dots. The graph design implies that except one '
          'outlier goal shot, all the shots were present on the positive x coordinates')

    print('Team 724 has made just 1 goal as indicated by red dot. The graph design implies that their shots were '
          'evently distributed over the field.')


# Calling function to draw plot for the individual teams

scatterPlot(x=Data[0][0], y=Data[0][1], z=Data[0][2], TeamNum=724)
scatterPlot(x=Data[1][0], y=Data[1][1], z=Data[1][2], TeamNum=596)
comments()
