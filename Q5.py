# Importing pandas  & numpy library
import pandas as pd
import numpy as np

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def part_a():
    """
    If the centre of the net that teams shoot at is located at xCoord=89, yCoord=0, create a column for the
    distance from each shot to this point. What is the distance of the furthest goal scored in the game?
    """

    # Fetching the x & y cordinates from dataframe df1
    x = np.array(df1[['xcoord']])
    y = np.array(df1[['ycoord']])

    # Adding a new column called distance which stores distance between centre and specified coordinates
    df1['distance'] = ((89 - x) ** 2 + y ** 2) ** 0.5   # pythagoras theorem to calc distance

    # Goal data furthest from centre of the net
    Farthest_Goal_Data = df1.loc[df1['distance'].idxmax()]

    print('Distance of the furthest goal scored in the game is {}'.format(Farthest_Goal_Data[['distance']].tolist()[0]))
    return Farthest_Goal_Data


def part_b(Farthest_Goal_Data):
    """
    What is the expected goals (xg) value of this furthest goal and what do you think contributed to this xg
    value?
    """
    # Connecting both the tables with compilegametime as a foreign key to pull out xg value of the farthest goal shot
    compiledgametime = float(Farthest_Goal_Data[['compiledgametime']].tolist()[0])

    # Storing xg value
    xg_value = (df2[df2['xg'] == compiledgametime])

    # Checking if xg value exists for that goal
    if len(xg_value) == 0:
        print('No corresponding xg value found!')
    else:
        print('The corresponding xg value for the maximum distance calculated is {}'.format(compiledgametime))


Farthest_Goal_Data = part_a()
part_b(Farthest_Goal_Data)
