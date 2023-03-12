import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

T1 = df1[df1['teamid'] == 724]
T2 = df1[df1['teamid'] == 596]

np.random.seed(19680801)

Data = [(T1[['xcoord', 'ycoord', 'goal']]), (T2[['xcoord', 'ycoord', 'goal']])]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
marker = ['^', 'o']
color = ['red', 'blue']

for i in range(len(Data)):
    x = Data[i].iloc[:, 0:1].values.tolist()
    y = Data[i].iloc[:, 1:2].values.tolist()
    z = Data[i].iloc[:, 2:3].values.tolist()
    ax.scatter(x, y, z, marker=marker[i], c=color[i])

ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_zlabel('Goal')


plt.show()
