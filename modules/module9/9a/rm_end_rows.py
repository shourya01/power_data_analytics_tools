import fileinput
import sys
import os


def remove_lines(filename, del_lines):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i in range(0, len(del_lines) - 1):
        del lines[del_lines[i]]

    del lines[25]

    file = open(filename, "w+")
    for line in lines:
        file.write(line)
    file.close()


del_lines = [25, 26, 27]
del_lines.sort(reverse=True)

# num_lines = sum(1 for line in open('test.txt'))
# if(num_lines > 26):
#     remove_lines("test.txt", del_lines)

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        num_lines = sum(1 for line in open("Data\\" + filename))
        if(num_lines > 26):
            remove_lines("Data\\" + filename, del_lines)
        print("...Done")
