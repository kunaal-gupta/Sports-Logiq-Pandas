import pandas as pd

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def parta():
    a = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')]
    a = a.groupby(['possessionid'], as_index=False)['eventname'].count()
    a = a.iloc[a['eventname'].idxmax()]
    array = a.tolist()

    print('Possession Id - {}, had the highest total successful passes'.format((array[0])))



def partb():
    a = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')].count()
    a = a['outcome']

    print('Total Number of successful passes were {}'.format((a)))


parta()
partb()