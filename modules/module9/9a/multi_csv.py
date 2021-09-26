import re
import os


def add_commas(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        i = 0
        for line in data:
            line = line.lstrip("\t")
            line = line.rstrip("\t")
            data[i] = re.sub("[\t ]+", ',', line)
            i += 1

    with open(filename, 'w') as file:
        file.writelines(data)


#add_commas("test.txt")

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        add_commas("Data\\" + filename)
        print("...Done")
