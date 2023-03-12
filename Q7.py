import pandas as pd

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

Goal_Data = df1[(df1['goal'] == 1)]['compiledgametime'].tolist()

xg_Array = list()
for i in Goal_Data:
    xg_Array.append(df2[(df2['compiledgametime'] == i)]['xg'].tolist()[0])

print('The highest xg among the goals that were scored is {}'.format(max(xg_Array)))