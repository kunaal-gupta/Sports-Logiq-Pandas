# Importing pandas library as pd
import pandas as pd

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def part_a():
    """ Which possessionid had the highest total successful passes? """

    # Filtering the data frame having successful passes
    ds = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')]

    # Grouping the filtered data by possessionid
    ds = ds.groupby(['possessionid'], as_index=False)['eventname'].count()

    # Storing the possession id having the max number of successful passes
    P_ID = ds.iloc[ds['eventname'].idxmax()].tolist()[0]

    print('Possession Id - {}, had the highest total successful passes'.format(P_ID) + '\n')



def part_b():
    """ How many successful passes were there and why do you think this specific possession had so many? """

    # Fetching the count of dataset having successful passes
    ds = df1[(df1['eventname'] == 'pass') & (df1['outcome'] == 'successful')].count()

    # Storing the count of such passes
    NumOfSuccesPasses = ds['outcome']

    print('Total Number of successful passes were {}. '.format(NumOfSuccesPasses))
    print('There could be many arguments for this, but I believe it will keep the opponent team busy in maintaining the'
          'defensive mode until your team keeps the possession of puck')

part_a()
part_b()