import numpy as np
import pandas as pd

df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

global successful_pass, successful_reception, shot_attempt
successful_pass, successful_reception, shot_attempt = 0, 0, 0

PID_to_ShortAssistCount = {}
Sorted_df1_data = df1.sort_values(by=['possessionid'], ascending=True)
tempPid = next(Sorted_df1_data.iterrows())[1][8]

for index, row in Sorted_df1_data.iterrows():
    Pid = row['possessionid']

    if tempPid == Pid:

        if row['outcome'] == 'successful':
            if row['eventname'] == 'pass':
                successful_pass += 1
                # print('sp', successful_pass)
            elif row['eventname'] == 'reception':
                successful_reception += 1
        if row['eventname'] == 'shot':
            shot_attempt += 1

    else:

        # ShotAssist_Array[tempPid] = [successful_pass, successful_reception, shot_attempt]
        PID_to_ShortAssistCount[tempPid] = min(successful_pass, successful_reception, shot_attempt)
        # print(Pid, [successful_pass, successful_reception, shot_attempt], min(successful_pass, successful_reception, shot_attempt) )

        successful_pass, successful_reception, shot_attempt = 0, 0, 0

        Pid = row['possessionid']
        tempPid = Pid

        if row['outcome'] == 'successful':
            if row['eventname'] == 'pass':
                successful_pass += 1
            elif row['eventname'] == 'reception':
                successful_reception += 1
        if row['eventname'] == 'shot':
            shot_attempt += 1

# Sorting the dictionary in the descending order of Assist Count
PID_to_ShortAssistCount = sorted(PID_to_ShortAssistCount.items(), key=lambda x: x[1], reverse=True)
PID_to_ShortAssistCount = dict(PID_to_ShortAssistCount)

# Storing the number of the highest assist count
higestAssistCount = PID_to_ShortAssistCount[list(PID_to_ShortAssistCount.keys())[0]]

# Array of Possession ids with the highest assist count
maxPID_Array = [i for i in PID_to_ShortAssistCount if PID_to_ShortAssistCount[i] >=higestAssistCount ]

# Array to store playerids with max number of assist shots
PlayersList = []

for i in maxPID_Array:
    PlayersList.extend(df1[(df1['possessionid'] == i)]['playerid'].tolist())

print('The below list of players ids have the most number of assisted shots with the number being {}'.format(higestAssistCount))
print(PlayersList)
