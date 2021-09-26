import fileinput
import sys
import os


def remove_lines(filename, del_lines):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i in range(0, len(del_lines) - 1):
        del lines[del_lines[i]]

    del lines[0]

    file = open(filename, "w+")
    for line in lines:
        file.write(line)
    file.close()


del_lines = [25, 26, 27, 28]
del_lines.sort(reverse=True)

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        remove_lines("Data\\" + filename, del_lines)
        print("...Done")
