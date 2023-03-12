# Importing pandas library as pd
import pandas as pd

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def higestXG_count():
    """ What is highest xg among the goals that were scored and why do you think it was this high? """

    # Fetching the compiled game time data from the successful goaled shots
    Goal_Data = df1[(df1['goal'] == 1)]['compiledgametime'].tolist()

    # Array to store xg values for goaled shots
    xg_Array = list()

    # Storing xg values in the array
    for i in Goal_Data:
        xg_Array.append(df2[(df2['compiledgametime'] == i)]['xg'].tolist()[0])

    print('The highest xg among the goals that were scored is {}'.format(max(xg_Array)))
    print('I believe being outside type player and making a successful shot from the offensive zone could be a '
          'deciding factor ')


def comments():
    """ Did this goal have a shot assist? """

    print('\nComments: This goal doesn''\'t have a Shot Assist primary becuase it is the only record for its '
          'possession id = 555, and doesn''\'t have successful pass & successful reception as required')


higestXG_count()
comments()
