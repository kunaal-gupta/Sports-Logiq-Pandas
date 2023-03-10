import pandas as pd

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def parta():
    a = df1.groupby(['teamid'], as_index=False)['goal'].sum()
    print(a.loc[a['goal'].idxmax()], end='\n\n')


def partb():
    a = df2.groupby(['teamid'], as_index=False)['xg'].mean()
    print(a)

parta()
partb()
