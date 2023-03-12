# Importing pandas library as pd
import pandas as pd

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

Team = None


def part_a():
    """  Who won the game & what was the score? """

    global Team  # Declaring global variable for later usage

    # Calculating total goal of each team by grouping
    ds = df1.groupby(['teamid'], as_index=False)['goal'].sum()

    # Storing Team name & its score
    Team = ds.loc[ds['goal'].idxmax()].tolist()[0]
    Score = ds.loc[ds['goal'].idxmax()].tolist()[1]

    print('Team {} won the game, and their score was {}.'.format(Team, Score) + '\n')


def part_b():
    """ Who won the Expected Goals (xg) battle & what was each team's total xg? """

    # Calculating the expected goal value of each team by calculating the mean of xg value of each team
    ds = df2.groupby(['teamid'], sort=True, as_index=False)['xg'].mean()

    # Storing the winner team of Expected goal battle
    Winner = ds.loc[ds['xg'].idxmax()].tolist()[0]

    print('Team {} has won the Expected goal battle'.format(Winner))
    print('Each team''\' total expected goal \n', ds)


def part_c():
    """ More info about performance"""

    print('\n Comparing expected goal value & score of the teams, team {} performed better'.format(Team))


part_a()
part_b()
part_c()
