# Importing pandas library as pd
import pandas as pd

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')


def part_a():
    """ Using the event data provided along with x/y coordinate columns, can you identify the likely xCoord of each
    blueline?"""

    # Filtering the dataset by specific zones & grouping them by possession ID
    dZone = df1[df1["zone"] == "dz"].groupby("possessionid")
    oZone = df1[df1["zone"] == "oz"].groupby("possessionid")

    # Calculating the mean of x-coordinates of each zones
    oZone_xCoord = oZone["xcoord"].mean()
    dZone_xCoord = dZone["xcoord"].mean()

    print("Likely xCoord of Offensive blue line : ", oZone_xCoord.mean())
    print("Likely xCoord of Defensive blue line : ", dZone_xCoord.mean())


part_a()
