import os

#os.rename("test.txt", "test.csv")

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        os.rename("Data\\" + filename, "Data\\" + filename[:-4] + ".csv")
        print("...Done")
