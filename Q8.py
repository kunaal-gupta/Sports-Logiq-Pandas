# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Reading the data from files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


def addingDistanceCol():
    # Fetching the x & y cordinates from dataframe df1
    x = np.array(df1[['xcoord']])
    y = np.array(df1[['ycoord']])

    # Adding a new column called distance which stores distance between centre and specified coordinates
    df1['distance'] = ((89 - x) ** 2 + y ** 2) ** 0.5  # pythagoras theorem to calc distance


def StatModel():
    addingDistanceCol()

    # Merging both the dataframes based on compiled game time
    df = pd.merge(df1, df2, on=["compiledgametime", 'playerid', 'teamid'])

    xg_shots = df[df['xg'] > 0.5]

    # Dependent variable and independent variables
    Y = xg_shots['xg']
    X = xg_shots[['distance']]

    # Defining the model
    model = sm.Logit(Y, X).fit()
    print(model.summary())

    print('\n\nModel: Used Logit Regression to show highest predictor of goal value which is the distance')
    print('Reason: coefficients, standard errors, p-values, confidence intervals of dependent variable show the '
          'direction and intensity of the link between each predictor variable and the independent variable.')


StatModel()
