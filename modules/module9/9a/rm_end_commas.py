import re
import os


def rm_commas(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        i = 0
        for line in data:
            data[i] = data[i][:-2] + "\n"
            i += 1

    with open(filename, 'w') as file:
        file.writelines(data)


#rm_commas("test.txt")

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        rm_commas("Data\\" + filename)
        print("...Done")
