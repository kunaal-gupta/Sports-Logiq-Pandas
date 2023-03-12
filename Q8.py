import pandas as pd
import statsmodels.api as sm

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')


high_xg_shots = df2[df2['xg'] > 0.45]
print(high_xg_shots)


# Define the dependent variable and independent variables
y = high_xg_shots['xg']
X = high_xg_shots[['playerid', 'teamid']]

# Add an intercept term to the independent variables
X = sm.add_constant(X)

# Fit the logistic regression model
model = sm.Logit(y, X).fit()

# Print the model summary
print(model.summary())