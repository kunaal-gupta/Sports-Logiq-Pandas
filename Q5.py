import numpy as np
import pandas as pd


df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def parta():
    x = np.array(df1[['xcoord']])
    y = np.array(df1[['ycoord']])

    df1['distance'] = ((89-x)**2 + y**2)**0.5

    Farthest_Goal_Data = df1.loc[df1['distance'].idxmax()]
    print('Distance of the furthest goal scored in the game is {}'.format(Farthest_Goal_Data[['distance']].tolist()[0]))
    return Farthest_Goal_Data

def partb(Farthest_Goal_Data):

    compiledgametime = float(Farthest_Goal_Data[['compiledgametime']].tolist()[0])

    xg_value = (df2[df2['xg'] == compiledgametime])
    if len(xg_value) == 0:
        print('No corresponding xg value found')
    else:
        print('The corresponding xg value for the maximum distance calculated is {}'.format(compiledgametime))


Farthest_Goal_Data = parta()
print()
partb(Farthest_Goal_Data)