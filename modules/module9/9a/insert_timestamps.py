import pandas as pd
import os


def edit_timestaps(filepath, filename):
    df = pd.read_csv(filepath)
    for hour in df.Timestamp:
        index = hour - 1
        df.Timestamp = df.Timestamp.astype("str")
        df.at[index, "Timestamp"] = filename[:4] + '.' + filename[4:6] + '.' + filename[6:8] + '.' + str("{:02d}".format(hour))

    return df


#df = edit_timestaps("20180601_DailyRenewables.csv")
#df.to_csv("20180601_DailyRenewables.csv", sep=',', index=False)

for filename in os.listdir("Data"):
    if filename.endswith(".csv"):
        df = edit_timestaps("Data\\" + filename, filename)
        df.to_csv("Data\\" + filename, sep=',', index=False)
        print("...Done: " + filename)
