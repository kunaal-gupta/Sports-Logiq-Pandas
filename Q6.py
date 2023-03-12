# Importing pandas library as pd
import pandas as pd

# Reading data from csv files
df1 = pd.read_csv('Tutorial22_df.csv')
df2 = pd.read_csv('Tutorial22_xG_df.csv')

# Defining global variables
global successful_pass, successful_reception, shot_attempt


def ShotAssist():
    """
    If a "Shot Assist" is defined as a sequence of events with the same possessionid where there is: 1) a
    successful pass followed by 2) a successful reception by a teammate and then without giving up the puck 3) the
    receiving player has a shot attempt, create a column flagging shots that have a Shot Assist. Which player(s) had
    the most assisted shots in the game and how many assisted shots did they have?

    """
    successful_pass, successful_reception, shot_attempt = 0, 0, 0

    # Dictionary to store count of Short Assist. Key: PossessionId, Value: number of triplet variables
    PID_to_ShortAssistCount = {}

    # Sorting the data by possession id in ascending order
    Sorted_df1_data = df1.sort_values(by=['possessionid'], ascending=True)

    # Assigning temporary Possession Id
    tempPid = next(Sorted_df1_data.iterrows())[1][8]

    # Iterating through data row-by-row
    for index, row in Sorted_df1_data.iterrows():

        # Fetching possesion Id
        Pid = row['possessionid']

        # If possession id same as of previous iteration
        if tempPid == Pid:

            # Making counts for successful pass, successful reception & attempted shot
            if row['outcome'] == 'successful':
                if row['eventname'] == 'pass':
                    successful_pass += 1
                elif row['eventname'] == 'reception':
                    successful_reception += 1
            if row['eventname'] == 'shot':
                shot_attempt += 1

        # If possession id has changed compared to previous iteration
        else:
            # Storing the count of Shot assist in dictionary against the possession id
            PID_to_ShortAssistCount[tempPid] = min(successful_pass, successful_reception, shot_attempt)

            # Reinitialize the variables value for the next id
            successful_pass, successful_reception, shot_attempt = 0, 0, 0

            # Updating Possesion Id
            Pid = row['possessionid']
            tempPid = Pid

            # Making counts for successful pass, successful reception & attempted shot
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
    maxPID_Array = [i for i in PID_to_ShortAssistCount if PID_to_ShortAssistCount[i] >= higestAssistCount]

    # Array to store playerids with max number of assist shots
    PlayersList = []

    for i in maxPID_Array:
        PlayersList.extend(df1[(df1['possessionid'] == i)]['playerid'].tolist())

    print('The below list of players ids have the most number of assisted shots with the number being {}'.format(
        higestAssistCount))
    print(PlayersList)


ShotAssist()
