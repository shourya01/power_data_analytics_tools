import re
import os


def copy_data(filename):
    data_append = []
    file = open(filename, "r")
    data = file.readlines()
    data_append = data[25:]
    file.close()

    del_data(filename, data)

    return data_append


def del_data(filename, data):
    for i in reversed(range(25, 50)):
        del data[i]

    file = open(filename, "w+")
    for line in data:
        file.write(line)
    file.close()


def add_data(filename, data_append):
    with open(filename, 'r') as file:
        data = file.readlines()
        i = 0
        for line in data:
            line_append = data_append[i]
            line = data[i].replace("\n", "")
            data[i] = line + line_append
            data[i] = re.sub("[\t ]{2,}", "\t", data[i])
            i += 1

    with open(filename, 'w') as file:
        file.writelines(data)


for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        data_append = copy_data("Data\\" + filename)
        add_data("Data\\" + filename, data_append)
        print("...Done")
