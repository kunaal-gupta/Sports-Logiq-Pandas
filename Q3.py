import pandas as pd
"""" filter the data by possession zone. The offensive blue line will have a possession zone of "oz" and the 
defensive blue line will have a possession zone of "dz". Here's the updated code:


code filters the data by possession zone and groups the data by possession ID. Then, it calculates the mean xCoord 
for each possession in each zone and prints the results. The offensive blue line xCoord is the mean xCoord for 
possessions in the offensive zone, and the defensive blue line xCoord is the mean xCoord for possessions in the 
defensive zone.

"""
# load the data
df = pd.read_csv("Tutorial22_df.csv")

# filter by possession zone and group by possession ID
offensive_zone = df[df["zone"] == "oz"].groupby("possessionid")
defensive_zone = df[df["zone"] == "dz"].groupby("possessionid")

# calculate the mean xCoord for each possession in each zone
offensive_xCoord = offensive_zone["xcoord"].mean()
defensive_xCoord = defensive_zone["xcoord"].mean()

# print the results
print("Offensive blue line xCoord: ", offensive_xCoord.mean())
print("Defensive blue line xCoord: ", defensive_xCoord.mean())