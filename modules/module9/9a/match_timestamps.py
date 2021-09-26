import pandas as pd
import os


count = 0


def edit_timestamps(filepath, filename):
    df = pd.read_csv(filepath)
    global count
    hour = df.Timestamp[count]
    timestamp = filename[:4] + '.' + filename[4:6] + '.' + filename[6:8]
    if(hour[:10] != timestamp):
        print(timestamp) # not included
        count -= 24 # reset count

    return df


for filename in os.listdir("Data_Original"):
    if filename.endswith(".txt"):
        df = edit_timestamps("power_generation.csv", filename)
        print("...Done: " + filename)
        count += 24
